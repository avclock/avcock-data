
Claude is responding
I thought we would do Weatherkit for the casual user if that is recommended, I want this to be tailored for casual users as well visiting the airport, recommend any missing features that could help with that.. also I do like the plug type, emergency numbers, and driving side.... I think it would also be cool to list countries of those who accept US drivers license for rental cars as that can get confusing at times....

Then make sure with all of these changes and previous changes, that the Welcome Guide is updated, as well as the learn more guide is updated.


Prioritizing WeatherKit integration and lookup tables strategically
Prioritizing WeatherKit integration and lookup tables strategically
This is a big batch — let me work through it methodically. First, let me check the two files you want updated, since I haven't looked at either yet, and I need to make sure the Welcome Guide's existing terms-acceptance mention doesn't now conflict with TermsGateView.


Identified conflicting terms acceptance systems and streamlined onboarding flow
Identified conflicting terms acceptance systems and streamlined onboarding flow
Found something important while checking this — OnboardingView still has its own separate, older "I Agree & Continue" consent mechanism on its last page (writing a different key, termsAcceptedAt, that the new TermsGateView never checks). That's now genuinely redundant and confusing — real acceptance already happens at the TermsGateView gate before the user ever reaches this screen. I'll fix that as part of the update. Let me check LearnMoreView.swift too before planning the full scope of edits:


Strategized phased implementation prioritizing WeatherKit, consolidated data structures, and documentation updates
Strategized phased implementation prioritizing WeatherKit, consolidated data structures, and documentation updates
This is a lot — let me work through it in order: research the rental car license question (needs care, since it's genuinely more nuanced than currency/plug data), build the four country-data lookups, fix the Onboarding consent redundancy, build WeatherKit, then update both guide screens to reflect everything from this whole session.


Architected tiered categorization system balancing data complexity with user clarity
Architected tiered categorization system balancing data complexity with user clarity
Given what I found — this is genuinely murkier than currency or plug type (rental companies, national law, and even different travel sites disagree on specifics, like the Fodor's forum thread arguing about France). I'll build it, but with real hedging, not a confident boolean table like the others. Let me generate everything now:


Architected travel info integration with conditional disclaimers and practical guidance
Architected travel info integration with conditional disclaimers and practical guidance
Now wiring these into the UI — added to the same unconditional "Airport" section as currency, with the rental-car/IDP note shown only where I have real signal, plus a standing disclaimer since this category is genuinely less certain than the others:


Architected WeatherKit integration for casual users with documentation updates
Architected WeatherKit integration for casual users with documentation updates
Now let's build the WeatherKit casual weather feature. One thing I can't do for you: this requires adding the "WeatherKit" capability in Xcode (target → Signing & Capabilities → + Capability → WeatherKit) — it's free with your Developer Program membership but won't compile without that entitlement added manually.


Orchestrated weather integration and prioritized casual user experience throughout
Orchestrated weather integration and prioritized casual user experience throughout
Now wiring it into the UI — added right after the Airport section, ahead of the more technical aviation content, since this is meant for casual users first:


Edited 2 files, ran a command
Edited 2 files, ran a command
Now hooking the load into .task:


Orchestrated documentation overhaul integrating WeatherKit and casual traveler features
Orchestrated documentation overhaul integrating WeatherKit and casual traveler features
Now updating the Terms/Privacy for this new data source:


Edited 2 files
Edited 2 files
This is clearly material — bumping both dates and requiredAgreementVersion again, per our own two-tier rule:


Deliberating version documentation versus unnecessary updates
Deliberating version documentation versus unnecessary updates
Now mirroring into the hosted files:


Architected streamlined onboarding flow with consolidated feature pages
Architected streamlined onboarding flow with consolidated feature pages
Now fixing the OnboardingView consent redundancy and adding pages for everything built this session:


Edited 2 files
Edited 2 files
Now removing the redundant consent mechanism from the last page:


Orchestrated glossary expansion and guide updates for casual airport travelers
Orchestrated glossary expansion and guide updates for casual airport travelers
Now updating LearnMoreView.swift with new glossary sections for everything built this session:


Documented updates and verified consistency across components
Documented updates and verified consistency across components
Finally, updating CLAUDE.md to log everything from this round:


Weighed versioning implications for simultaneous legal document modifications
Weighed versioning implications for simultaneous legal document modifications
Now the final full validation pass across every file touched this round:


Final validation of every Swift file touched in this response
Final validation of every Swift file touched in this response
All balanced. Let's package everything:


Ran a command, read a file
Ran a command, read a file
Everything from this round — 9 files, 2 new
New files: CountryTravelInfo.swift, CasualWeatherService.swift

Edited: AirportDetailView.swift, OnboardingView.swift, LearnMoreView.swift, LegalText.swift, TERMS_OF_USE.md, PRIVACY_POLICY.md, CLAUDE.md

WeatherKit — yes, built, but with real caveats:

New "Local Weather" section, free (not premium-gated like METAR) — deliberate call to widen appeal to casual visitors; flag if you'd rather gate it
One manual step required: add the WeatherKit capability in Xcode (target → Signing & Capabilities → + Capability → WeatherKit) — free with your Developer account, but nothing compiles without it
Includes Apple's required attribution (wordmark + legal link) — don't strip that from the UI
Honest flag: this file's exact API surface (WeatherService.shared, .attribution, property names) is the piece I'm least certain about this entire session — I couldn't verify it against live Apple docs the way I could search-verify everything else. If Xcode throws errors here, this is the most likely place for a real mistake, not a duplicate-file issue.
Country data: CountryTravelInfo.swift covers plug type/voltage, driving side, and emergency number for the same 126 countries as currency — same low-risk, fixed-standard character. The rental-car/IDP note is different on purpose: only ~14 countries with genuine multi-source agreement (China, Hungary, Thailand, Japan, etc.), with an explicit "always confirm current requirements" line baked into the UI, since even professional travel sites disagreed with each other on some specifics when I checked.

Bug caught and fixed: OnboardingView had its own separate, weaker consent mechanism on its last page — writing a key nothing else read, left over from before TermsGateView existed. Removed entirely; the welcome guide is now a pure feature tour, with new pages covering everything built this session.

Guides updated: Both the Welcome Guide (5 new/updated pages) and Learn More (6 new glossary sections) now reflect Airport Status, Amenities, Preclearance, Currency, Travel Info, and Local Weather.

Legal: Bumped both documents to July 5 again and added Apple/WeatherKit to the third-party list — this is clearly material, so requiredAgreementVersion stays at today's date and existing testers will hit the re-gate.


Countrytravelinfo
Code · SWIFT 

Casualweatherservice
Code · SWIFT 

Airportdetailview
Code · SWIFT 

Onboardingview
Code · SWIFT 

Learnmoreview
Code · SWIFT 

Legaltext
Code · SWIFT 

Terms of use
Document · MD 

Privacy policy
Document · MD 

Claude
Document · MD 
product airport: casual weather service: /Users/brysonjohansson/Downloads/Product Airport/Product Airport/CasualWeatherService.swift:40:13 Type 'CasualWeatherModel' does not conform to protocol 'ObservableObject'
/Users/brysonjohansson/Downloads/Product Airport/Product Airport/CasualWeatherService.swift:41:6 Initializer 'init(wrappedValue:)' is not available due to missing import of defining module 'Combine'
/Users/brysonjohansson/Downloads/Product Airport/Product Airport/CasualWeatherService.swift:42:6 Initializer 'init(wrappedValue:)' is not available due to missing import of defining module 'Combine'
/Users/brysonjohansson/Downloads/Product Airport/Product Airport/CasualWeatherService.swift:43:6 Initializer 'init(wrappedValue:)' is not available due to missing import of defining module 'Combine'
/Users/brysonjohansson/Downloads/Product Airport/Product Airport/CasualWeatherService.swift:44:6 Initializer 'init(wrappedValue:)' is not available due to missing import of defining module 'Combine'
/Users/brysonjohansson/Downloads/Product Airport/Product Airport/CasualWeatherService.swift:45:6 Initializer 'init(wrappedValue:)' is not available due to missing import of defining module 'Combine'

Show more
Same exact bug as NotificationManager.swift earlier — missing import Combine, needed for @Published/ObservableObject here.


Edited a file, ran a command, read a file
Edited a file, ran a command, read a file
Swap that in — this is a pattern worth remembering going forward: any new @MainActor final class ... ObservableObject file needs import Combine alongside import Foundation, same as NotificationManager.swift hit earlier. Rebuild and let me know what's next.


Casualweatherservice
Code · SWIFT 
Thoughts on this: Add plug icon images for example the three dots for Brazil, two for European, the american plug icon for a more visual view in the about country section (would want them to be blue) or whatever Aviation fuel prices across states and countries? Public domains for that? Any other public domain we can tap into?

Hide not as relevant airport info and have a button that says “Show more information” to expand the rest of the not as relevant details…


Architecting simplified plug icon system for recognized IEC types
Architecting simplified plug icon system for recognized IEC types
Let me research the fuel price question first, then give you my honest read on the plug icons (there's a real design tradeoff there), then handle the "Show More" collapse — that last one is genuinely the most valuable given how much the detail screen has grown today.


Identified free fuel API, weighed plug icon approach, prioritized collapsible UI implementation
Identified free fuel API, weighed plug icon approach, prioritized collapsible UI implementation
Good news — there's a real, actually-free API here, unlike TSA. Here's what I found and what I'd recommend:

Aviation fuel prices — feasible, one good option
aviation-fuel-prices.com offers a genuinely free API — crowdsourced fuel prices (100LL, Jet-A, SAF, etc.) by ICAO code, explicitly licensed under Creative Commons ("we share our data for free... other awesome services for pilots out there"), requiring only a free API key registration. Same caveat as MyTSA's old data: crowdsourced means coverage and freshness vary by airport, but unlike TSA's dead endpoint, this one is live and explicitly open.

What I'd rule out: GlobalAir.com and iFlightPlanner/AOPA have real per-FBO fuel data, but it's proprietary/commercial, not open for redistribution. IATA's Jet Fuel Monitor is licensed from S&P Global (not free/open). EIA/BTS government data is genuinely free but tracks bulk/wholesale pricing trends, not what you'd actually pay at a specific FBO — useful for an industry chart, not "what does it cost to fill up at KDEN."

Worth noting: this feature would appeal to a different slice of your audience than currency/plug type — private pilots specifically, not casual travelers. Given AvClock already skews toward that crowd (military airport indicators, VFR/IFR badges, heliports), it's a reasonable fit, just a different persona than what today's other additions targeted.

A couple more public-domain ideas while we're at it
NOTAMs (Notices to Airmen) — FAA publishes these publicly; genuinely useful to your pilot audience, though this edges toward "operational" territory your Terms already warn against relying on the app for
Airport diagrams/charts — FAA publishes these as public domain PDFs for US airports; could be a nice "view airport diagram" link, similar treatment to the TSA link (opens externally, not embedded)
Now, the two builds — let me check current state before doing the collapse, since that's the more valuable one to get right:


Architected collapsible sections to streamline airport information display
Architected collapsible sections to streamline airport information display
Now let's build the "Show More Information" collapse — I'll apply the same pattern to both the Airport section and the Amenities section, since both have grown substantially today:


Edited 2 files
Edited 2 files
Now let's view and restructure the Amenities section the same way:


Prioritized terminal navigation while collapsing secondary features
Prioritized terminal navigation while collapsing secondary features
Balanced.


Ran a command, read a file
Ran a command, read a file
"Show More Information" is built in both places. Airport section now shows only IATA/ICAO/Name/Country by default, with Currency/Plug/Driving Side/Emergency/IDP note/Elevation behind a tap. Amenities shows only Terminals by default, with TSA PreCheck/CLEAR/Global Entry/Lounges/Centurion/Priority Pass/Preclearance/notes behind the same pattern. Used SwiftUI's native DisclosureGroup rather than a custom button — standard, no extra state-management risk. One file: AirportDetailView.swift.

Plug icons — my honest take
I'd actually hold off building these right now, and here's the real reason: I can't visually render or preview SwiftUI shapes — I can only write the geometry code and reason about it, not see whether the proportions, spacing, or pin placement actually look like a recognizable plug once compiled. Everything else this session (text, data, logic) I could verify pretty rigorously through reading; a hand-drawn vector icon is exactly the kind of thing where "looks right when I reason about the code" and "actually looks right on screen" can diverge, and you'd only find out after a build-and-look cycle.

If you want to move forward anyway, the practical path: I build simplified stylized icons (circles for round-pin types like Europe/Brazil, rectangles for flat-blade types like the US/UK) in blue as you asked, you build and eyeball them, and we iterate based on what you actually see — same loop as everything else, just with an extra "does this look right" check that's squarely a human judgment call this time, not something I can pre-verify. Want me to take a first pass at it on that basis?


Airportdetailview
Code · SWIFT 
I like the airport diagrams/charts more than the NOTAMs at the moment.. I do like the aviation fuel prices as well...


Architecting implementation strategy for dual features
Architecting implementation strategy for dual features
Let's nail down the technical details for both before building — I need the actual FAA chart URL structure (it's more complex than a simple per-airport link) and confirm the exact API shape for fuel prices.


Decoding FAA airport diagram URL patterns and numbering systems
Decoding FAA airport diagram URL patterns and numbering systems
The FAA's direct PDF URLs are more complex than a clean per-airport link — they need both a rotating 28-day AIRAC cycle code and an internal FAA "TPP airport number" that's completely different from IATA/ICAO codes, which I don't have a crosswalk for. Rather than risk linking to the wrong airport's diagram, let me verify a cleaner path: linking out to a well-known aggregator that handles that mapping already.


Reconciling SkyVector's URL patterns with aviation code discrepancies
Reconciling SkyVector's URL patterns with aviation code discrepancies
One more check to get the exact fuel API endpoint right before writing code:


Identified licensing risks and prioritized safe implementation approach
Identified licensing risks and prioritized safe implementation approach
Good thing I checked before writing code — the fuel price API has two real complications I need to flag before building anything there.

Airport Diagrams — building this now, it's clean
SkyVector's airport pages follow a predictable skyvector.com/airport/{code} pattern, they're free, and — critically — this is just an outbound link, same low-risk category as the TSA wait-time button: no data licensing question, since I'm not pulling anything into the app, just sending someone to a well-known third-party site that legitimately republishes FAA chart data.


Add helper to open the airport diagram on SkyVector
Add helper to open the airport diagram on SkyVector
Now let's add the button and confirmation. First checking the current Airport Status section structure since I premium-gated it earlier:


Weighed feature accessibility and premium tier positioning
Weighed feature accessibility and premium tier positioning
Now the state var and confirmation alert:


Edited 2 files, ran 2 commands, viewed a file
Edited 2 files, ran 2 commands, viewed a file
Balanced. Now updating the Terms to cover this new outbound link, same pattern as the TSA one:


Ran 3 commands, edited 2 files, read a file
Ran 3 commands, edited 2 files, read a file
Airport Diagrams shipped — a "View Airport Diagram" button next to the TSA link in the Airport Status section (same confirmation-alert pattern, free for everyone since it's just an outbound link). Three files: AirportDetailView.swift, LegalText.swift, TERMS_OF_USE.md.

Fuel prices — pausing before I write any code, for a real reason
I fetched their actual API docs and found two things that change the picture:

1. It's not self-serve. Getting an API key requires contacting them directly through a form — "please get in touch via the contact form" — not an instant signup. That's a one-time thing you'd need to do yourself regardless, but it's slower than I assumed when I first flagged this as "a good free option."

2. The license is the real issue: CC BY-NC-ND 4.0. Breaking that down — NC means NonCommercial. AvClock charges $4.99 for Premium. Using NC-licensed data as part of an app that generates revenue is a genuine gray area at best, and if I'd gated this behind Premium (which I'd normally do for aviation-technical data, matching METAR/Airport Status), that's about as clearly "commercial use" as it gets. Even keeping it fully free doesn't obviously resolve it, since the app as a whole is still a paid product.

I don't think I should write integration code against this until that's resolved, since building toward a real licensing problem isn't better than not building it at all. My actual recommendation: use their contact form to ask two things at once — (1) request API access, and (2) explicitly ask whether they'll license commercial/paid-app use, or grant you a separate commercial license. Plenty of small data providers are willing to work this out directly once asked; it just isn't something I can assume my way past. Once you hear back with an actual yes, I can build the integration same-day.


Airportdetailview
Code · SWIFT 

Legaltext
Code · SWIFT 

Terms of use
Document · MD 
Gemini_Generated_Image_epjxnbepjxnbepjx.png
Anyway you could fit and crop these out for each relevant country that has a plug...?


Extracting icons while weighing background removal strategies
Extracting icons while weighing background removal strategies
Yes — I can crop these out and even try to strip the dark background so they drop cleanly into the existing rows. Let me work with the actual image first.


Mapped tile coordinates and engineered transparent icon extraction
Mapped tile coordinates and engineered transparent icon extraction
Let me verify each one actually looks right before packaging them — I can't skip this check since I can't be fully certain the chroma-key worked cleanly without looking:


Architecting iOS asset catalog structures for icon integration
Architecting iOS asset catalog structures for icon integration
All five look clean — sharp blue glyphs on fully transparent backgrounds, no leftover tile edges. Now packaging these as proper Xcode asset catalog imagesets:


Examined plug type mappings for country-specific implementation
Examined plug type mappings for country-specific implementation
Now the mapping logic — let me check what plug type strings actually exist in the data to map accurately, since these 5 icons won't cover every IEC type I stored:


Architected icon mapping system with template rendering and custom layout fallbacks
Architected icon mapping system with template rendering and custom layout fallbacks





Claude is AI and can make mistakes. Please double-check responses.


Terms of use · MD
Terms of Use — AvClock
Last updated: July 5, 2026

This is a strong template, not legal advice. Because AvClock presents aviation information, having a licensed attorney review these terms before relying on them is recommended.

These Terms of Use ("Terms") are a legal agreement between you and Bryson Johansson ("we," "us," "our") governing your use of the AvClock app and related services (the "App"). By using the App, you agree to these Terms. If you do not agree, do not use the App.

1. Eligibility
You must be at least 13 (or the minimum age of digital consent in your country). If you are under 18, you may use the App only with the consent and supervision of a parent or legal guardian.

2. Not for navigation or operational use
AvClock is for general reference only. It is NOT an aviation navigation, flight-planning, dispatch, weather-briefing, or operational tool, and must NOT be used as one. Do not rely on the App for any decision affecting the safety of flight. Airport, heliport, weather, flight-category, airport status/delay, amenities, sun, and time-zone information may be inaccurate, incomplete, delayed, or unavailable due to network, observation, transmission, or display latency, and may not reflect real-time conditions. Always confirm with official sources, including (as applicable) the FAA, EASA, ICAO, your national civil aviation authority, official NOTAMs, official charts, certified weather briefings, and Air Traffic Control. You are solely responsible for the safe and lawful conduct of any flight and for compliance with all applicable aviation regulations.

If you are a pilot, you remain the Pilot in Command under 14 CFR § 91.103 (or the equivalent regulation in your jurisdiction) and are solely responsible for becoming familiar with all available information concerning your flight before beginning it. The App does not assume any dispatch, flight-briefing, or advisory role. If you use a mobile device as part of an Electronic Flight Bag, you are responsible for that device's and the App's compliance with FAA Advisory Circular 91-78A (or its equivalent) and for maintaining any required backup charts, equipment, or independent data sources.

3. Third-party data
The App displays data from third parties, including OurAirports (public domain), NOAA, the FAA, and Apple (WeatherKit). We do not create, control, verify, endorse, or guarantee that data and are not responsible for its accuracy, completeness, timeliness, or availability. Airport amenity information is compiled and curated by us, not a live or official feed, and may not reflect current conditions — always confirm amenities directly with the airport. The App may also link to third-party websites — such as an independent TSA security wait-time estimator, or SkyVector for airport diagrams — that open in your device's browser. These sites are operated by unrelated third parties (not by us, the TSA, or the FAA), and may not be accurate or current — we do not control, verify, or endorse their content, and you should use your own best judgment before relying on them. AvClock is not affiliated with, endorsed by, or sponsored by the Federal Aviation Administration, the National Oceanic and Atmospheric Administration, or the United States Government.

4. License and acceptable use
We grant you a limited, personal, non-exclusive, non-transferable, revocable license to use the App for your own non-commercial purposes. You agree not to copy, modify, distribute, sell, or sublicense the App; reverse engineer it except as permitted by law; circumvent security or licensing; use it unlawfully; or use it to build a competing product or to scrape or redistribute its data in bulk.

5. Purchases and payments
The App offers a one-time in-app purchase, "AvClock Premium," for US $4.99 (or the local equivalent set by Apple), which unlocks premium features. This is a one-time purchase, not a subscription — there are no recurring charges. Purchases are processed by Apple and subject to Apple's terms; refunds and billing are handled solely by Apple. You may restore a prior purchase on devices using the same Apple Account.

6. "As is" — no warranty
THE APP AND ALL DATA ARE PROVIDED "AS IS" AND "AS AVAILABLE," WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, ACCURACY, TITLE, AND NON-INFRINGEMENT. We do not warrant that the App will be uninterrupted, secure, or error-free, or that any data is correct or current.

7. Limitation of liability
TO THE MAXIMUM EXTENT PERMITTED BY LAW, IN NO EVENT WILL Bryson Johansson BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, OR PUNITIVE DAMAGES, OR FOR ANY LOSS OF PROFITS OR REVENUE, DATA, OR GOODWILL, ANY FINANCIAL, BUSINESS, OR ECONOMIC LOSS, ANY COST OF SUBSTITUTE SERVICES, ANY LOSS ARISING FROM DECISIONS MADE OR ACTIONS TAKEN (OR NOT TAKEN) IN RELIANCE ON THE APP OR ITS DATA, OR FOR PERSONAL INJURY, DEATH, OR PROPERTY DAMAGE, ARISING OUT OF OR RELATING TO YOUR USE OF (OR INABILITY TO USE) THE APP OR ANY DATA, UNDER ANY LEGAL THEORY, EVEN IF ADVISED OF THE POSSIBILITY. YOU AGREE THAT YOU USE THE APP AND ITS DATA ENTIRELY AT YOUR OWN RISK AND THAT WE ARE NOT FINANCIALLY RESPONSIBLE FOR ANY LOSS YOU OR ANY THIRD PARTY MAY INCUR. OUR TOTAL AGGREGATE LIABILITY WILL NOT EXCEED THE GREATER OF (A) THE AMOUNT YOU PAID US IN THE 12 MONTHS BEFORE THE CLAIM, OR (B) US $50. Some jurisdictions do not allow certain limitations, so some of the above may not apply to you.

8. Assumption of risk and indemnification
You knowingly assume all risk arising from your use of the App. You agree to indemnify, defend, and hold harmless Bryson Johansson from any claims, losses, liabilities, damages, and expenses (including reasonable attorneys' fees) arising out of your use or misuse of the App, your violation of these Terms, or your violation of any law or third-party right.

9. International use and export compliance
The App is operated from the United States. If you use it elsewhere, you are responsible for compliance with applicable local laws, including data-protection and aviation regulations. You agree to comply with all applicable export-control and economic-sanctions laws, including the U.S. Export Administration Regulations (EAR) and regulations administered by the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC). You represent that you are not located in, and will not use, download, or export the App in or to, any U.S.-embargoed country or region, and that you are not on, and will not use the App on behalf of, the U.S. Treasury's Specially Designated Nationals list or any other U.S. government restricted- or denied-party list.

10. Intellectual property
The App, including its name, code, and original written content (excluding third-party data), is owned by Bryson Johansson and protected by intellectual-property laws to the extent such protection is available. Some visual assets (such as app icons and imagery) were created with the assistance of generative-AI tools; the copyright status of AI-assisted works varies under current U.S. Copyright Office guidance and depends on the degree of human creative authorship involved, and we make no representation about the scope of any copyright protection in those specific assets. We do not claim ownership of, and do not intend to infringe, any third party's trademarks, copyrights, or other rights, and any resemblance is unintentional.

If you believe content in the App, or content linked from the App, infringes your rights, email avclock@protonmail.com identifying the content, your right and proof of it, your contact information, and a good-faith statement, and we will review properly documented requests and, where appropriate, promptly remove or replace the material or disable the link. We will terminate access for any user we determine, in appropriate circumstances, to be a repeat infringer of others' intellectual-property rights.

11. Privacy
Your use is also governed by our Privacy Policy. AvClock does not collect or transmit personal data.

12. Termination
These Terms apply until terminated. We may suspend or terminate your license if you breach them. Sections that by their nature should survive (disclaimers, limitation of liability, indemnification, governing law) will survive.

13. Changes
We may update these Terms and the Privacy Policy from time to time. For changes we consider material — such as new fees, new data practices, or changes to the arbitration, liability, or dispute-resolution provisions — the App will require you to review and affirmatively re-accept the updated documents before you can continue using it. For non-material changes (such as clarifications, corrections, or formatting), the updated "Last updated" date reflects the change, and your continued use of the App after that date constitutes acceptance of the revised Terms.

14. Governing law and dispute resolution
These Terms are governed by the laws of the State of Florida, USA, without regard to conflict-of-laws rules.

Informal resolution first. Before bringing any claim, you agree to email avclock@protonmail.com and try to resolve the dispute informally for at least 30 days.

Binding individual arbitration. Except as stated below, any dispute arising out of or relating to these Terms or the App that is not resolved informally will be settled by final and binding arbitration on an individual basis, administered under the rules of a recognized arbitration body, rather than in court, and conducted in or under the laws of Florida.

Class-action waiver. You and we agree that each may bring claims only in an individual capacity, and not as a plaintiff or class member in any class, collective, consolidated, or representative proceeding. The arbitrator may not combine more than one person's claims.

Exceptions. Either party may (a) bring an individual claim in small-claims court, and (b) seek injunctive or equitable relief in the state or federal courts located in Florida to protect intellectual-property or proprietary rights.

Opt-out. You may opt out of this arbitration agreement within 30 days of first accepting these Terms by emailing avclock@protonmail.com; if you opt out, disputes will be resolved in the state or federal courts located in Florida.

Nothing in this section limits rights that cannot be waived under the mandatory consumer-protection laws of your country of residence.

15. Severability; entire agreement; no waiver
If any provision is unenforceable, the rest remain in force. These Terms (with the Privacy Policy and Apple's applicable terms) are the entire agreement regarding the App. Our failure to enforce any provision is not a waiver.

16. Apple-required acknowledgments
These Terms are between you and Bryson Johansson only, not Apple; we are solely responsible for the App. Apple has no obligation to provide maintenance or support. If the App fails to conform to any applicable warranty, you may notify Apple and Apple will refund the purchase price (to the extent applicable); Apple has no other warranty obligation. Apple is not responsible for claims relating to the App. Apple and its subsidiaries are third-party beneficiaries of these Terms and may enforce them.

17. Contact
Questions? Contact avclock@protonmail.com


