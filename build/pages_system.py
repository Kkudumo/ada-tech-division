"""The list of all pages and the not-found page."""
from layout import page, hero, sec, head_block, cards, MAIN, WEB
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


def not_found():
    body = hero(
        "That page does not exist",
        "The address may be mistyped, or the page may have moved when the site was rebuilt. These are the "
        "places most people are looking for.",
        None, [("/", "Go to the home page"), ("/support", "Get support", "line")], code=("Error 404", "Page not found"))
    body += sec('<h2 class="vh">Popular pages</h2>' + cards([
        ("/problems", "Problems", "Start from the symptom.", "Find the fault"),
        ("/services", "Services", "What we repair and set up.", "See services"),
        ("/pricing", "Pricing", "Every published price.", "See prices"),
        ("/work", "Case files", "Real jobs, written up.", "See work"),
        ("/guides", "Guides", "Plain answers before you spend.", "Read guides"),
        ("/search", "Search", "Look for a topic, such as prices.", "Search the site"),
    ]))
    page("404", "Page Not Found | ADA Tech Division", "The page you were looking for does not exist.",
         body, noindex=True, cta=False)


def build():
    directory()
    not_found()
