# Prices come from ADA Core

No price is typed into `build/*.py` any more. The owner changes a price in ADA Hub; the next build of this site picks it up.

## How it works

- `build/ada_prices.py` (copied from `Andreas-Digital-Agency-Database/public-api/clients/python/`) is the client. `build/layout.py` creates one
  `P = Prices("tech", build/prices.json)` and exposes small helpers: `m(name)` -> `N$249`, `fm(name)` -> `From N$249` (or `N$249` when ADA Core says
  the price is fixed), `lc(name)` -> `from N$249` / `at N$249`, `st(name)` -> `starts from N$249` / `costs N$249`, `raw(name)` -> `249` (schema.org).
- Lookup is by the service **name in ADA Core**, for example `m("Windows Ready")`. The names are the `name` column of
  `supabase/seed_data/catalogue.csv` in the database repo (division `tech`).
- A section-level "from" (for example "Windows packages from N$649") is the cheapest of its services: `sfrom(*PKGS)` / `sfl(*PKGS)`. The groups
  (`PKGS`, `FIRST_AID_PLANS`, `BUSINESS_PLANS`, `BIOS_WORK`) are at the top of `build/layout.py`. `priceRange` in the structured data is the cheapest
  of all priced services.
- `assets/js/ada.js` is generated from `build/ada.js.in` (tokens such as `{{lc:Printer setup}}`); edit the `.in` file, not `ada.js`.

## At build time

- `ADA_API_URL` and `ADA_API_KEY` both set: the build asks ADA Core (`/api/public/services?division=tech`) and prints which prices differ from the snapshot.
- Not set, or the API is down, slow or answers badly: the build uses the committed `build/prices.json` and says so. It never fails because of the API.
- A name that is in neither the API nor the snapshot stops the build with a clear message (so a typo cannot publish "N$None").
- With no API configured the output is byte-identical to the committed HTML.

## Refresh the snapshot

The snapshot is the fallback, so refresh and commit it now and then (and after a price change you want in git history):

    ADA_API_URL=... ADA_API_KEY=... python3 build/ada_prices.py tech build/prices.json --refresh
    python3 build/build.py && python3 build/test_prices.py

## Renaming a service in ADA Hub

The site looks services up by name. If a service is renamed in ADA Hub, update the name in the build (search `build/` for the old name, including
`build/ada.js.in`) and in `build/prices.json`; `python3 build/test_prices.py` fails until they agree. Until then the build keeps the snapshot price for that service.

## Not driven by ADA Core

Quoted services (CCTV, servers, security, business IT, networks and cabling) have no list price. Parts, licences and example figures are not ours.
The news post "The diagnostic fee is now N$99..." in `build/pages_news.py` is a dated announcement and stays as written.

## Vercel

`vercel.json` runs `python3 build/build.py` and publishes the repository root. Set `ADA_API_URL` and `ADA_API_KEY` as environment variables on the
Vercel project (Production and Preview); ADA Hub should trigger a redeploy (deploy hook) after a price change.
