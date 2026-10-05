"""News, updates and notices.

To publish an item, add it to NEWS below (newest first) and run
`python3 build/build.py`.

Each item: slug, date (YYYY-MM-DD, used for sorting), label (how the date is
shown), kind ("News", "Update", "Announcement" or "Notice"), title, summary,
body (HTML), and related links.
"""
from layout import page, hero, sec, head_block, related, e, url, SITE, MAIN, WEB

N = ("news", "News")

NEWS = [
    {
        "slug": "rebuilt-website-fault-finder-and-guides",
        "date": "2026-10-05", "label": "5 October 2026", "kind": "Announcement",
        "title": "ADA Tech's rebuilt website is live, with a fault finder and guides",
        "summary": "The ADA Tech website has been rebuilt around the faults people bring to us. It has a fault "
                   "finder, twelve problem pages, four guides and a site search. Prices are unchanged.",
        "body": """
<p>The ADA Tech Division website has been rebuilt. It is organised around what goes wrong with computers and
networks, so you can start from the symptom and not from a list of technical terms.</p>
<h2>What is new</h2>
<ul>
<li><strong>Fault finder.</strong> On the <a href="/">home page</a>, type what the device is doing, such as
“slow” or “blue screen”, and go straight to the page for it.</li>
<li><strong>Twelve problem pages.</strong> Each one says what the symptom usually means, what you can check
yourself at no cost, when to stop, and what a repair costs. Four are new: battery, printer, virus warnings and
liquid spills. <a href="/problems">See all problems</a>.</li>
<li><strong>Service sheets.</strong> Every <a href="/services">service page</a> now opens with a short sheet:
the price, where the work is done and what is not included.</li>
<li><strong>Guides.</strong> Four plain guides, starting with
<a href="/guides/windows-10-end-of-support">what to do now Windows 10 support has ended</a>.</li>
<li><strong>Search.</strong> Use the Search button at the top of any page.</li>
</ul>
<h2>What has not changed</h2>
<p>The prices, the seven-step way of working, the case files, the client reviews, the Existing Client Desk and
Service Records all work as before. Old page addresses redirect to the new pages.</p>
""",
        "links": [("/problems", "Problems", "Start from the symptom."),
                  ("/pricing", "Pricing", "Every published price."),
                  ("/guides", "Guides", "Plain answers before you spend money.")],
    },
    {
        "slug": "diagnostic-fee-n99-deducted-from-repair",
        "date": "2026-10-05", "label": "5 October 2026", "kind": "Update",
        "title": "The diagnostic fee is now N$99 and always comes off the repair",
        "summary": "The standard device diagnostic costs N$99. If you go ahead with the repair, the full amount "
                   "is deducted from the repair cost, whatever the size of the repair.",
        "body": """
<p>The standard diagnostic for a laptop or desktop now costs <strong>N$99</strong>.</p>
<h2>What changed</h2>
<ul>
<li>Before: the diagnostic was N$120, and it was waived only when the repair that followed cost N$350 or more.</li>
<li>Now: the diagnostic is N$99, and it is deducted from the repair cost whenever you go ahead, whatever the
repair costs.</li>
</ul>
<p>If you decide not to repair, the fee is not refunded, because the inspection and diagnosis have been done.
This matches Andreas Digital Agency's
<a href="https://www.andreasdigitalagency.com/payment-refund-cancellation">payment, refund and cancellation
policy</a>.</p>
<p>The full price list is on the <a href="/pricing">pricing page</a>.</p>
""",
        "links": [("/pricing", "Pricing", "Every published price."),
                  ("/services/computer-repair", "Computer and laptop repair", "What the diagnostic covers."),
                  ("/about", "How we work", "The seven steps, and what you approve.")],
    },
    {
        "slug": "windows-10-security-updates-extended-to-2027",
        "date": "2026-10-05", "label": "5 October 2026", "kind": "Notice",
        "title": "Windows 10: security updates for home PCs now run to October 2027",
        "summary": "Microsoft has moved the end of Extended Security Updates for home Windows 10 PCs from "
                   "October 2026 to 12 October 2027. A PC must be enrolled to receive them.",
        "body": """
<p>If your computer still runs Windows 10, this affects you. Microsoft ended normal support for Windows 10 on
14 October 2025. Home PCs could keep receiving security fixes through a programme called Extended Security
Updates, which was due to end in October 2026.</p>
<p>Microsoft has since moved that date. Its own page now says the programme for home PCs ends on
<strong>12 October 2027</strong>.</p>
<h2>What to do</h2>
<ul>
<li>Open <em>Settings</em>, <em>Update &amp; Security</em>, <em>Windows Update</em> on the Windows 10 PC and
look for the enrolment link. A PC is not covered until it is enrolled.</li>
<li>Check whether the PC can run Windows 11. If it can, the upgrade is free.</li>
<li>If it cannot, use the extra year to plan a replacement.</li>
</ul>
<p>Our guide sets out the dates, the requirements and the options:
<a href="/guides/windows-10-end-of-support">Windows 10 support has ended: what to do with your PC</a>.</p>
<p>Source: <a href="https://www.microsoft.com/en-us/windows/extended-security-updates" rel="noopener">Microsoft,
Windows 10 Extended Security Updates</a>, checked 5 October 2026.</p>
""",
        "links": [("/guides/windows-10-end-of-support", "Windows 10 guide", "Dates, requirements and options."),
                  ("/services/windows-setup", "Windows and software setup", "Upgrade or clean installation."),
                  ("/problems/windows-update-not-working", "Windows Update fails", "If updates will not install.")],
    },
    {
        "slug": "ada-tech-moves-to-its-own-address",
        "date": "2026-10-05", "label": "5 October 2026", "kind": "Update",
        "title": "ADA Tech has moved to its own web address",
        "summary": "Andreas Digital Agency has moved to its own domain. The Tech division is at "
                   "tech.andreasdigitalagency.com, and the old addresses redirect.",
        "body": f"""
<p>Andreas Digital Agency now runs on its own domain name. Each part of the company has an address under it:</p>
<ul>
<li><a href="{MAIN}/">www.andreasdigitalagency.com</a> for the main company site</li>
<li><a href="/">tech.andreasdigitalagency.com</a> for the Tech division, which is this site</li>
<li><a href="{WEB}/">web.andreasdigitalagency.com</a> for the Web division</li>
<li><a href="https://marketing.andreasdigitalagency.com/">marketing.andreasdigitalagency.com</a> for the Marketing division</li>
</ul>
<h2>Do you need to do anything?</h2>
<p>No. The previous addresses redirect to the new ones, so old links and bookmarks still lead to the right page.
Private Service Record and ticket links that ADA Tech has already sent you continue to work.</p>
<p>Our phone number, WhatsApp number and email address are unchanged. They are on the
<a href="/contact">contact page</a>.</p>
""",
        "links": [("/contact", "Contact", "Phone, WhatsApp and email."),
                  ("/client-desk", "Existing Client Desk", "Follow up on previous work."),
                  ("/about", "How we work", "The seven-step standard.")],
    },
]


def news_card(item):
    return (f'<a class="card card--link news-card" href="/news/{item["slug"]}" data-date="{item["date"]}">'
            f'<span class="tag">{e(item["kind"])}</span><time datetime="{item["date"]}">{e(item["label"])}</time>'
            f'<h3 class="h3">{e(item["title"])}</h3><p>{e(item["summary"])}</p>'
            f'<span class="more">Read more</span></a>')


def latest(n=3):
    """Cards for the newest items, used on the home page."""
    return '<div class="grid g3 swipe">' + "".join(news_card(i) for i in NEWS[:n]) + "</div>"


def build():
    body = hero(
        "News, updates and notices",
        "Changes to our services and prices, and notices about things that affect your computer, such as "
        "the end of Windows 10 support.",
        [N], [("/guides", "Looking for guides?", "line")], code=("Bulletin", f"{len(NEWS)} items"))
    body += sec('<h2 class="vh">All items</h2><div class="grid g2" id="newsGrid">'
                + "".join(news_card(i) for i in NEWS) + "</div>")
    body += sec(head_block(
        "Company-wide news",
        'News about Andreas Digital Agency as a whole, including events and careers, is on the main site: '
        f'<a href="{MAIN}/news">andreasdigitalagency.com/news</a>.', label="ADA"),
        "sec--light sec--tight")
    page("news", "News, Updates and Notices | ADA Tech Division",
         "Service and price changes from ADA Tech Division in Rundu, Namibia, and notices about things that "
         "affect your computer.",
         body, active="/news", crumbs=[N])

    for item in NEWS:
        path = "news/" + item["slug"]
        crumbs = [N, (path, item["title"])]
        b = hero(e(item["title"]), e(item["summary"]), crumbs, None, code=(item["kind"], item["label"]))
        b += sec(f'<article class="prose"><p class="byline">{e(item["kind"])} / {e(item["label"])} / ADA Tech Division</p>'
                 f'{item["body"]}<p class="mt3"><a class="more" href="/news">All news</a></p></article>')
        b += related(item["links"], "Related")
        schema = [{
            "@type": "NewsArticle", "headline": item["title"], "description": item["summary"], "url": url(path),
            "datePublished": item["date"], "dateModified": item["date"], "inLanguage": "en",
            "author": {"@id": SITE + "/#organization"}, "publisher": {"@id": SITE + "/#organization"},
            "mainEntityOfPage": url(path), "image": SITE + "/assets/img/og-ada-tech.png",
        }]
        page(path, item["title"] + " | ADA Tech", item["summary"], b, active="/news", crumbs=crumbs,
             schema=schema, og_type="article", lastmod=item["date"])
