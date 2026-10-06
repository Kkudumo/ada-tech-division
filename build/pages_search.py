"""Site search: the /search page and the index it reads.

The index is written to assets/search-index.json from the generated HTML,
so it always matches what is on the pages. KEYWORDS adds the words people
actually type (prices, cost, how much, slow, not working...) to the pages
that answer them.
"""
import html
import json
import os
import re

from layout import page, hero, sec, cards, ROOT, PAGES, HUB_FOLDERS
import pages_problems
import pages_services
import pages_guides

KEYWORDS = {
    "": "home ada tech division computer repair it support rundu namibia technician laptop fix it company it companies in namibia "
        "it companies in rundu computer repair rundu laptop repair rundu computer shop rundu",
    "pricing": "price prices pricing cost costs fee fees charge charges rate rates how much money budget cheap "
               "affordable package packages quote quotation payment pay diagnostic n$",
    "support": "support help request book booking fix repair problem fault whatsapp start get help",
    "contact": "contact phone number telephone call whatsapp email address location where office reach message",
    "about": "about how we work process steps standard method diagnose approve test document seven it company in rundu",
    "work": "work case files portfolio jobs examples proof repairs done previous",
    "reviews": "reviews testimonials feedback rating ratings clients customers stars",
    "faq": "faq questions answers help licence data files warranty complaint",
    "first-aid": "first aid monthly plan subscription care personal device home family student",
    "managed-it": "managed it monthly business plan support contract helpdesk help desk organisation office outsourced "
                  "it support for small businesses it company it companies in namibia",
    "solutions": "who we help individuals students households remote workers small business lodges schools",
    "locations/rundu": "rundu kavango east west local near me nkurenkuru divundu town computer repair rundu laptop repair rundu "
                       "it companies in rundu it company in rundu cctv installation rundu wifi installation rundu "
                       "computer shop rundu laptop repair near me",
    "services": "services what we do offer list",
    "problems": "problems issues faults trouble not working broken help symptom",
    "client-desk": "client desk existing client ticket track tracking follow up warranty rework complaint priority",
    "service-record": "service record handover job record token",
    "news": "news updates announcements notices latest",
    "directory": "all pages site map sitemap directory index",
}
KEYWORDS.update({"services/" + k: v for k, v in pages_services.KEYWORDS.items()})
KEYWORDS.update({"problems/" + k: v for k, v in pages_problems.KEYWORDS.items()})
KEYWORDS.update(pages_guides.KEYWORDS)

SKIP = {"404", "search"}


def kind_of(path):
    if path.startswith("problems"):
        return "Problem"
    if path.startswith("guides"):
        return "Guide"
    if path.startswith("news"):
        return "News"
    if path.startswith("services"):
        return "Service"
    if path in ("pricing", "first-aid", "managed-it"):
        return "Pricing"
    if path in ("work", "reviews"):
        return "Proof"
    if path in ("client-desk", "service-record"):
        return "Clients"
    return "Page"


def text_of(fragment):
    fragment = re.sub(r"<(script|style|svg|noscript)[\s\S]*?</\1>", " ", fragment)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(fragment)).strip()


def build_index():
    docs = []
    for path, _lastmod, _indexable in PAGES:
        if path in SKIP:
            continue
        rel = (path + "/index.html") if path in HUB_FOLDERS else ((path or "index") + ".html")
        src = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        main = re.search(r"<main[^>]*>([\s\S]*?)</main>", src).group(1)
        main = re.sub(r'<section class="cta"[\s\S]*?</section>', " ", main)
        main = re.sub(r'<nav class="(?:crumbs|finder)"[\s\S]*?</nav>', " ", main)
        main = re.sub(r'<form[\s\S]*?</form>', " ", main)
        h1 = text_of(re.search(r"<h1[^>]*>([\s\S]*?)</h1>", main).group(1))
        desc = html.unescape(re.search(r'name="description" content="([^"]*)"', src).group(1))
        heads = [text_of(m) for m in re.findall(r"<(?:h2|h3|summary)[^>]*>([\s\S]*?)</(?:h2|h3|summary)>", main)]
        body = text_of(main)
        docs.append({"u": "/" + path, "t": h1, "d": desc, "k": KEYWORDS.get(path, ""),
                     "h": " | ".join(heads)[:1500], "b": body[:7000], "c": kind_of(path)})
    out = os.path.join(ROOT, "assets", "search-index.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, separators=(",", ":"))
    return len(docs), os.path.getsize(out)


def build():
    body = hero(
        "Search this site",
        "Type what you are looking for, such as prices, blue screen, Wi-Fi or Windows 11.",
        [("search", "Search")], None, code=("Lookup", "All pages"))
    body += sec("""<form class="search-form" id="searchForm" action="/search" method="get" role="search">
<label class="vh" for="q">Search this site</label>
<input id="q" name="q" type="search" placeholder="What are you looking for?" autocomplete="off" autofocus>
<button class="btn btn--blue" type="submit">Search</button>
</form>
<p class="search-count" id="searchCount" role="status" aria-live="polite"></p>
<ol class="results" id="searchResults"></ol>
<noscript><p class="note mt2">Search needs JavaScript. You can also use the menu, or see the list of pages below.</p></noscript>
<div id="searchPopular" class="mt3"><h2 class="h3">Popular pages</h2>""" + cards([
        ("/pricing", "Prices", "Every published price.", "See prices"),
        ("/problems", "Problems", "Start from the symptom.", "Find the fault"),
        ("/services", "Services", "What we repair and set up.", "See services"),
        ("/support", "Get support", "Describe what is going wrong.", "Start"),
        ("/guides", "Guides", "Plain answers before you spend.", "Read guides"),
        ("/contact", "Contact", "Phone, WhatsApp and email.", "Contact us"),
    ]) + "</div>")
    page("search", "Search | ADA Tech Division", "Search the ADA Tech Division website for faults, services, prices, guides and news.",
         body, noindex=True, crumbs=[("search", "Search")], scripts=["/assets/js/search.js"], cta=False)
