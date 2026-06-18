#!/usr/bin/env python3
"""
build_datasets.py
=================
Regenerates the app's airport + heliport datasets from OurAirports
(public domain) and writes a small version manifest the apps poll to
decide whether to auto-update.

Outputs (into ./out):
  - clean_airports.json   (airports, excluding heliports/closed)
  - clean_heliports.json  (heliports only)
  - manifest.json         (version + counts + URLs the apps read)

OurAirports CSV has no timezone column, so we derive it from lat/lon
with `timezonefinder` (matching how the original clean_airports.json
was produced).

Usage:
    pip install requests timezonefinder
    python build_datasets.py --base-url https://<you>.github.io/avclock-data

Data source: https://github.com/davidmegginson/ourairports-data
License: OurAirports data is released to the public domain.
"""

import argparse
import csv
import io
import json
import os
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    requests = None

AIRPORTS_CSV_URL = "https://davidmegginson.github.io/ourairports-data/airports.csv"

# OurAirports `type` values we treat as airports vs. heliports.
AIRPORT_TYPES = {"small_airport", "medium_airport", "large_airport"}
HELIPORT_TYPES = {"heliport"}

# OurAirports `iso_region` looks like "US-UT". Map US regions to full
# state names so searches like "Utah" or "Texas" match. (Non-US regions
# get an empty state — city/country search still covers those.)
US_STATES = {
    "US-AL": "Alabama", "US-AK": "Alaska", "US-AZ": "Arizona", "US-AR": "Arkansas",
    "US-CA": "California", "US-CO": "Colorado", "US-CT": "Connecticut", "US-DE": "Delaware",
    "US-DC": "District of Columbia", "US-FL": "Florida", "US-GA": "Georgia", "US-HI": "Hawaii",
    "US-ID": "Idaho", "US-IL": "Illinois", "US-IN": "Indiana", "US-IA": "Iowa",
    "US-KS": "Kansas", "US-KY": "Kentucky", "US-LA": "Louisiana", "US-ME": "Maine",
    "US-MD": "Maryland", "US-MA": "Massachusetts", "US-MI": "Michigan", "US-MN": "Minnesota",
    "US-MS": "Mississippi", "US-MO": "Missouri", "US-MT": "Montana", "US-NE": "Nebraska",
    "US-NV": "Nevada", "US-NH": "New Hampshire", "US-NJ": "New Jersey", "US-NM": "New Mexico",
    "US-NY": "New York", "US-NC": "North Carolina", "US-ND": "North Dakota", "US-OH": "Ohio",
    "US-OK": "Oklahoma", "US-OR": "Oregon", "US-PA": "Pennsylvania", "US-RI": "Rhode Island",
    "US-SC": "South Carolina", "US-SD": "South Dakota", "US-TN": "Tennessee", "US-TX": "Texas",
    "US-UT": "Utah", "US-VT": "Vermont", "US-VA": "Virginia", "US-WA": "Washington",
    "US-WV": "West Virginia", "US-WI": "Wisconsin", "US-WY": "Wyoming",
    "US-PR": "Puerto Rico", "US-VI": "U.S. Virgin Islands", "US-GU": "Guam",
}


def fetch_airports_csv(local_path: str | None) -> str:
    if local_path:
        with open(local_path, "r", encoding="utf-8") as f:
            return f.read()
    if requests is None:
        raise SystemExit("Install requests (pip install requests) or pass --csv <path>.")
    resp = requests.get(AIRPORTS_CSV_URL, timeout=60)
    resp.raise_for_status()
    return resp.text


def build_records(csv_text: str):
    """Returns (airports, heliports) as lists of the app's record schema."""
    from timezonefinder import TimezoneFinder
    tf = TimezoneFinder()

    airports, heliports = [], []
    reader = csv.DictReader(io.StringIO(csv_text))
    for row in reader:
        rtype = (row.get("type") or "").strip()
        if rtype not in AIRPORT_TYPES and rtype not in HELIPORT_TYPES:
            continue  # skip closed / balloonport / unknown

        try:
            lat = float(row["latitude_deg"])
            lon = float(row["longitude_deg"])
        except (KeyError, ValueError):
            continue

        iata = (row.get("iata_code") or "").strip()
        # Real ICAO field. For AIRPORTS we deliberately do NOT fall back
        # to `ident` (a local/FAA code like "FA38"), which produced junk
        # seaplane bases / gliderports.
        icao = (row.get("icao_code") or "").strip()
        ident = (row.get("ident") or "").strip()

        # Airports are keyed by IATA, so require one.
        if rtype in AIRPORT_TYPES and not iata:
            continue
        # Heliports: include any with a real ICAO OR a local/FAA
        # identifier, so hospital helipads and EMS pads (which rarely
        # have an ICAO) are included. The local code becomes its display
        # code. This is what makes the heliport list comprehensive.
        heli_code = icao or ident
        if rtype in HELIPORT_TYPES and not heli_code:
            continue

        tz = tf.timezone_at(lng=lon, lat=lat) or "UTC"

        iso_region = (row.get("iso_region") or "").strip()
        state = US_STATES.get(iso_region, "")

        record = {
            "iata": iata,
            "icao": icao if rtype in AIRPORT_TYPES else heli_code,
            "name": (row.get("name") or "").strip(),
            "latitude": lat,
            "longitude": lon,
            "timezone": tz,
            "country": (row.get("iso_country") or "").strip(),
            "municipality": (row.get("municipality") or "").strip(),
            "state": state,
        }
        (heliports if rtype in HELIPORT_TYPES else airports).append(record)

    return airports, heliports


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", help="Path to a local airports.csv (skips download).")
    ap.add_argument("--base-url", default="https://REPLACE-ME.github.io/avclock-data",
                    help="Public base URL where the JSON files will be hosted.")
    ap.add_argument("--out", default="out", help="Output directory.")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    csv_text = fetch_airports_csv(args.csv)
    airports, heliports = build_records(csv_text)

    # Safety net: if OurAirports ever returns a broken/empty response,
    # refuse to publish so we never overwrite good data with garbage.
    if len(airports) < 1000:
        raise SystemExit(f"Aborting: only {len(airports)} airports parsed — refusing to overwrite good data.")

    with open(os.path.join(args.out, "clean_airports.json"), "w", encoding="utf-8") as f:
        json.dump(airports, f, separators=(",", ":"))
    with open(os.path.join(args.out, "clean_heliports.json"), "w", encoding="utf-8") as f:
        json.dump(heliports, f, separators=(",", ":"))

    # Version = UTC date; bump if you regenerate more than once a day by
    # appending a build number.
    version = datetime.now(timezone.utc).strftime("%Y.%m.%d.%H%M")
    manifest = {
        "version": version,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": "OurAirports (public domain)",
        "airports":  {"url": f"{args.base_url}/clean_airports.json",  "count": len(airports)},
        "heliports": {"url": f"{args.base_url}/clean_heliports.json", "count": len(heliports)},
    }
    with open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"✅ airports={len(airports)}  heliports={len(heliports)}  version={version}")


if __name__ == "__main__":
    main()
