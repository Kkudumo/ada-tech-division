# ADA Tech Division website

Public site for tech.andreasdigitalagency.com. Plain HTML, one stylesheet,
small scripts, no build step on Vercel.

## How the pages are made

Every public page is generated from the Python files in `build/` and the
generated HTML is committed. To change wording, prices or layout:

```
# edit the content in build/pages_*.py, or the layout in build/layout.py
python3 build/build.py        # regenerates every page, sitemap.xml and the search index
python3 build/serve.py 8771   # local preview at http://127.0.0.1:8771
```

Do not edit the generated `.html` files by hand: the next build overwrites them.

| File | What it holds |
| --- | --- |
| `build/layout.py` | Header, footer, contact details, icons, shared components, structured data |
| `build/pages_home.py` | Home page, including the fault finder |
| `build/pages_problems.py` | Problems hub and the twelve problem pages (`PROBLEMS`) |
| `build/pages_services.py` | Services hub and the nine service pages (`SERVICES`) |
| `build/pages_plans.py` | Pricing, ADA First Aid and Managed IT. **All prices live here** |
| `build/pages_company.py` | How we work, case files, reviews, support, contact, FAQ, Rundu, who we help, client desk, service record |
| `build/pages_guides.py` | Guides hub and articles |
| `build/pages_news.py` | News, updates and notices. Add an item to `NEWS` and rebuild |
| `build/pages_search.py` | Search page, search keywords and the search index |
| `build/pages_system.py` | List of all pages and the 404 page |
| `assets/css/ada.css` | All public styles. Brand colours match the main ADA site; the last section is the Tech workshop look |
| `assets/js/ada.js` | Menu, search bar, scroll reveal, fault finder filter, home-page starting-point helper |
| `assets/js/search.js` | Site search, reading `assets/search-index.json` |

## Prices

Prices are written in `build/pages_plans.py` (`PRICES`, `PACKAGES`,
`FIRST_AID`, `MANAGED`), with the diagnostic fee as `DIAG` in
`build/layout.py`. Service and problem pages quote some of them in their own
text, so after changing a price search the `build/` folder for the old amount,
then rebuild. Also check the amounts quoted in the home-page helper in
`assets/js/ada.js`.

## Pages that talk to the service database

Case files, reviews, client tickets and Service Records are read from and
written to the `tech-public-api` function. The scripts are in `assets/js/`:

| Page | Script | Element ids it relies on |
| --- | --- | --- |
| `/work`, and the home page | `work.js` | `caseGrid` (`data-limit` shows only the newest few) |
| `/reviews` | `reviews.js` | `reviewGrid`, `refreshNote`, `reviewForm`, `serviceVerified`, `jobReference`, `reviewMsg` |
| `/client-desk` | `client-desk.js` | `ticketForm`, `ticketResult`, `trackForm`, `trackResult`, `trackCode`, `trackToken`, `jobRef`, `deviceSystem` |
| `/service-record` | `service-record.js` | `recordView`, `lookupForm` |
| `/support` | `support.js` | `supportForm` (opens WhatsApp; nothing is stored) |

`assets/js/tech-api.js` holds the API address and shared helpers. Form field
`name` attributes are what the API receives, so keep them when editing forms.

## Not generated (left as they were)

- `tech-publisher.html` and `styles.css` — the staff tool for publishing case
  files. `styles.css` is now used only by that page.
- `sentinel-assets/` and `api/` — not linked from the public site.

## Rules the content follows

- No invented results, clients or testimonials. Case files and reviews come
  only from the service database.
- Prices are the published ADA Tech prices. Parts and licences are always
  described as separate.
- Each problem and service page opens with a short plain answer, and problem
  pages list only checks that are safe for a non-technical person.
- Guides link their sources and carry a review date (`REVIEWED` in
  `build/layout.py`).
- Old addresses are redirected in `vercel.json`.
