# Privacy Policy — AvClock

_Last updated: July 19, 2026_

AvClock ("the app") is designed to respect your privacy. **The app does not
collect, store, or share any personal information.** This policy explains what
that means in practice.

## Information we collect

**None.** AvClock does not have user accounts, does not include analytics or
advertising SDKs, and does not transmit any personal or device information to us
or to any third party.

## Location

If you choose to allow location access, the app uses your location **only on
your device** to find airports near you and to show your local time. Your
location is never sent to us or to any third party. It is stored only on your
device (and shared with the app's own Home Screen and Lock Screen widgets) so
those features can work. You can deny or revoke location permission at any time
in the iOS Settings app; the rest of the app continues to function.

## Weather data

When you view aviation weather for an airport (METAR/TAF, flight category), the
app requests publicly available data from the U.S. National Oceanic and
Atmospheric Administration (NOAA) at aviationweather.gov. The only information
sent in that request is the airport's public identifier code. No personal or
device information is included. NOAA's handling of requests is governed by its
own policies.

For the general "current conditions" weather shown for an airport (temperature,
feels-like, humidity, condition), the app uses Apple's WeatherKit, sending only
the airport's coordinates to Apple — never your own location — to fetch that
airport's forecast. WeatherKit requests are governed by Apple's own privacy
policy.

## Airport status data

When you view an airport's status, the app fetches the FAA's public National
Airspace System status feed. This request is not airport-specific — no airport
code or other information about you is sent. Airport amenity information is
bundled with the app / cached on-device and involves no network request at all.

## My Flights

My Flights lets you manually enter your own flight information (airline,
flight number, airports, date and time, notes). This is entirely local —
stored only on your device, never transmitted to us or anyone else. It is not
live flight tracking. If you choose to add a flight to your calendar, the app
requests calendar access and creates an event using Apple's EventKit
framework; this only happens for flights you explicitly choose to add, and
calendar access is governed by iOS's own permission system, which you can
revoke at any time in Settings.

## Currency conversion

When an airport's local currency differs from USD, the app requests a current
exchange rate from the Frankfurter API (rates published by the European Central
Bank). Only the currency codes being converted are sent — no personal or device
information, and no location. This request is only made if you view that part
of an airport's information.

## Third-party links

The app may link to third-party websites and apps (for example, an
independent TSA wait-time estimator, or Uber and Lyft for ride requests) that
open in your device's browser or in those apps directly, after you confirm
where applicable. We do not control these destinations, and once you leave
the app, your interaction with them is governed by their own privacy policy,
not this one.

## Purchases

AvClock Premium is a one-time in-app purchase sold through Apple's In-App
Purchase. All payment processing is handled by Apple; the app never sees or
stores your payment details. Purchases are governed by Apple's terms and
privacy policy.

## International users

Because AvClock does not collect, store, or transmit any personal data, it does
not process personal data under regulations such as the EU/UK GDPR or the
California Consumer Privacy Act (CCPA). There is no personal data to access,
correct, or delete. If you have questions, contact us below.

## Children

The app does not knowingly collect any information from anyone, including
children under 13.

## Changes to this policy

If this policy changes, the updated version will be posted at this URL with a
new "Last updated" date.

## Contact

Questions about this policy? Contact: **avclock@protonmail.com**

<!--
HOW TO USE THIS FILE:
1. Replace the contact email above if you'd prefer a different one.
2. Publish this page at a public URL (GitHub Pages, your website, a public
   Notion page, etc.).
3. Put that URL in:
     • Legal.swift  ->  Legal.privacyURL
     • App Store Connect  ->  App Privacy  ->  Privacy Policy URL
-->
