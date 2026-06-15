#!/usr/bin/env python3
"""Regenerates airport + heliport datasets from OurAirports (public domain)."""

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
AIRPORT_TYPES = {"small_airport", "medium_airport", "large_airport", "seaplane_base"}
HELIPORT_TYPES = {"heliport"}


def fetch_airports_csv(local_path):
    if local_path:
        with open(local_path, "r", encoding="utf-8") as f:
            return f.read()
    if requests is None:
        raise SystemExit("Install requests (pip install requests) or pass --csv <path>.")
    resp = requests.get(AIRPORTS_CSV_URL, timeout=60)
    resp.raise_for_status()
    return resp.text


def build_records(csv_text):
    from timezonefinder import TimezoneFinder
    tf = TimezoneFinder()
    airports, heliports = [], []
    reader = csv.DictReader(io.StringIO(csv_text))
    for row in reader:
        rtype = (row.get("type") or "").strip()
        if rtype not in AIRPORT_TYPES and rtype not in HELIPORT_TYPES:
            continue
        try:
            lat = float(row["latitude_deg"])
            lon = float(row["longitude_deg"])
        except (KeyError, ValueError):
            continue
        iata = (row.get("iata_code") or "").strip()
        icao = (row.get("icao_code") or row.get("ident") or "").strip()
        if rtype in AIRPORT_TYPES and not (iata or icao):
            continue
        if rtype in HELIPORT_TYPES and not icao:
            continue
        tz = tf.timezone_at(lng=lon, lat=lat) or "UTC"
        record = {
            "iata": iata,
            "icao": icao,
            "name": (row.get("name") or "").strip(),
            "latitude": lat,
            "longitude": lon,
            "timezone": tz,
            "country": (row.get("iso_country") or "").strip(),
        }
        (heliports if rtype in HELIPORT_TYPES else airports).append(record)
    return airports, heliports


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--base-url", default="https://REPLACE-ME/data")
    ap.add_argument("--out", default="out")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    csv_text = fetch_airports_csv(args.csv)
    airports, heliports = build_records(csv_text)

    with open(os.path.join(args.out, "clean_airports.json"), "w", encoding="utf-8") as f:
        json.dump(airports, f, separators=(",", ":"))
    with open(os.path.join(args.out, "clean_heliports.json"), "w", encoding="utf-8") as f:
        json.dump(heliports, f, separators=(",", ":"))

    version = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    manifest = {
        "version": version,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": "OurAirports (public domain)",
        "airports":  {"url": f"{args.base_url}/clean_airports.json",  "count": len(airports)},
        "heliports": {"url": f"{args.base_url}/clean_heliports.json", "count": len(heliports)},
    }
    with open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"airports={len(airports)} heliports={len(heliports)} version={version}")


if __name__ == "__main__":
    main()
