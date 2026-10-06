"""The list of all pages and the not-found page."""
from layout import page, hero, sec, head_block, cards, MAIN, WEB, buttons, e
import pages_problems
import pages_services
import pages_guides
import pages_news


def lst(items):
    return '<ul class="signs">' + "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in items) + "</ul>"


def directory():
    c = [("directory", "All pages")]
    body = hero("All pages", "Every public page on the ADA Tech site, in one list.", c, None,
                code=("Site index", "ADA Tech"))
    groups = [
        ("Problems", [("/problems", "All problems")] + [("/problems/" + p["slug"], p["short"]) for p in pages_problems.PROBLEMS]),
        ("Services", [("/services", "All services")] + [("/services/" + s["slug"], s["name"]) for s in pages_services.SERVICES]),
        ("Prices and plans", [("/pricing", "Pricing"), ("/first-aid", "ADA First Aid"), ("/managed-it", "Managed IT"),
                              ("/solutions", "Who we help"), ("/locations/rundu", "IT support in Rundu")]),
        ("Guides and news", [("/guides", "All guides")] + [("/" + g[0], g[1]) for g in pages_guides.GUIDES]
         + [("/news", "All news")] + [("/news/" + n["slug"], n["title"]) for n in pages_news.NEWS]),
        ("Proof and how we work", [("/work", "Case files"), ("/reviews", "Client reviews"), ("/about", "How we work"),
                                   ("/faq", "Questions and answers")]),
        ("Clients and contact", [("/support", "Get support"), ("/client-desk", "Existing Client Desk"),
                                 ("/service-record", "Open a Service Record"), ("/contact", "Contact"),
                                 ("/search", "Search this site"), (MAIN + "/", "Andreas Digital Agency"),
                                 (WEB + "/", "ADA Web Division")]),
    ]
    inner = '<div class="grid g3">' + "".join(
        f'<div><h2 class="h3">{name}</h2>{lst(items)}</div>' for name, items in groups) + "</div>"
    body += sec(inner)
    page("directory", "All Pages | ADA Tech Division",
         "A list of every public page on the ADA Tech Division website: problems, services, prices, guides, "
         "news, case files and client pages.", body, crumbs=c)

WA_BROKEN = "https://wa.me/264818032641?text=Hello%20ADA%20Tech%2C%20a%20link%20on%20your%20website%20led%20to%20a%20page%20that%20does%20not%20exist%3A%20"


def not_found_page(site_name, chips, h1, lead, placeholder, actions, steps_, popular, plain_chips=False):
    """The designed 404 page. Vercel serves 404.html for any address that does not exist."""
    if plain_chips:
        k = '<span class="where">' + " · ".join(e(x) for x in chips) + "</span>"
    else:
        k = '<p class="code-line">' + "".join(f"<span>{e(x)}</span>" for x in chips) + "</p>"
    body = f"""<section class="hero hero-page on-dark nf"><p class="nf-num" aria-hidden="true">4<b>0</b>4</p><div class="wrap">
{k}<h1>{e(h1)}</h1>
<p class="lead">{e(lead)}</p>
<form class="nf-search" action="/search" method="get" role="search">
<label class="vh" for="nf-q">Search this site</label>
<input id="nf-q" name="q" type="search" placeholder="{e(placeholder)}" autocomplete="off" required>
<button class="btn" type="submit">Search</button>
</form>
<p class="nf-url" id="nfUrl" hidden>You asked for <code></code></p>
{buttons(*actions)}
</div></section>"""
    lis = "".join(f"<li><h3>{e(t)}</h3><p>{d}</p></li>" for t, d in steps_)
    body += sec(head_block("Three ways back", label="What to do now") + f'<ol class="nf-steps">{lis}</ol>')
    body += sec(head_block("Where most people were heading", label="Popular pages") + cards(popular, swipe=True)
                + f'<p class="note mt2"><strong>Followed a link on this site that led here?</strong> '
                  f'<a href="{WA_BROKEN}" target="_blank" rel="noopener">Tell us on WhatsApp</a> and we will fix it.</p>',
                "sec--light")
    page("404", f"Page Not Found | {site_name}", "The page you were looking for does not exist.",
         body, noindex=True, cta=False)


def not_found():
    not_found_page(
        'ADA Tech Division', ('Fault F-404', 'Page not found'),
        'This page will not start.',
        'Diagnosis: the address is mistyped, or the page moved when the site was rebuilt. Nothing is wrong with your device.',
        'Search: blue screen, prices, Wi-Fi…',
        [("/", "Go to the home page"), ("/problems", "Open the fault list", "line")],
        [
        ('Check the address', 'One wrong letter is enough. Look at the end of the address at the top of your screen.'),
        ('Search the site', 'Type the fault or the service, such as slow laptop or Windows 11.'),
        ('Start from the symptom', 'The <a href="/problems">fault list</a> covers the most common faults, each with checks you can do yourself.'),
    ],
        [
        ("/problems", "Problems", "Start from the symptom.", "Find the fault"),
        ("/services", "Services", "What we repair and set up.", "See services"),
        ("/pricing", "Pricing", "Every published price.", "See prices"),
        ("/work", "Case files", "Real jobs, written up.", "See work"),
        ("/guides", "Guides", "Plain answers before you spend.", "Read guides"),
        ("/support", "Get support", "Describe what is going wrong.", "Start"),
    ])


def build():
    directory()
    not_found()
