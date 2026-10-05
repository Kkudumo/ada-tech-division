"""Shared layout and components for the ADA Tech Division site.

The site is plain HTML. `python3 build/build.py` regenerates every public
page from the content files in this folder. There is no build step on
Vercel: the generated HTML is committed.
"""
import html
import json
import os
import re
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = "https://tech.andreasdigitalagency.com"
MAIN = "https://www.andreasdigitalagency.com"
WEB = "https://web.andreasdigitalagency.com"
FOUNDER_URL = "https://founder.andreasdigitalagency.com"
REVIEWED = "5 October 2026"
REVIEWED_ISO = "2026-10-05"

PHONE = "+264 81 803 2641"
PHONE_TEL = "+264818032641"
COMPANY_LINE = "+264 83 677 5783"
COMPANY_TEL = "+264836775783"
EMAIL = "hello.ada1@outlook.com"
PLACE = "Rundu, Kavango East, Namibia"
DIAG = "N$99"

NAV = [
    ("/problems", "Problems"),
    ("/services", "Services"),
    ("/pricing", "Pricing"),
    ("/first-aid", "First Aid"),
    ("/managed-it", "Managed IT"),
    ("/work", "Work"),
    ("/guides", "Guides"),
    ("/news", "News"),
    ("/about", "How we work"),
]

PAGES = []  # (path, lastmod, indexable) collected for the sitemap
HUB_FOLDERS = {"services", "problems", "guides", "news"}


def e(text):
    return html.escape(str(text), quote=True)


def url(path):
    return SITE + ("/" + path.strip("/") if path.strip("/") else "/")


def wa(text="Hello ADA Tech, I need help with: "):
    """A WhatsApp link with the opening line already typed."""
    return "https://wa.me/264818032641?text=" + quote(text, safe="")


WA = wa()

# ------------------------------------------------------------------ icons

ICONS = {
    "laptop": '<rect x="4" y="5" width="16" height="11"/><path d="M2 19h20"/>',
    "power": '<path d="M12 3v9"/><path d="M7 6.5a7 7 0 1 0 10 0"/>',
    "screen": '<rect x="3" y="4" width="18" height="13"/><path d="M9 21h6M12 17v4"/>',
    "alert": '<rect x="3" y="4" width="18" height="13"/><path d="M12 7.5v4.5M12 14.2v.3M9 21h6"/>',
    "gauge": '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-6"/><path d="M3 20h18"/>',
    "heat": '<path d="M10 4h4v10.5a4 4 0 1 1-4 0z"/><path d="M12 9v8"/>',
    "update": '<path d="M20 12a8 8 0 0 1-14.5 4.6M4 12a8 8 0 0 1 14.5-4.6"/><path d="M18.5 3.5v4h-4M5.5 20.5v-4h4"/>',
    "wifi": '<path d="M3 9.5a13 13 0 0 1 18 0M6 13a8.5 8.5 0 0 1 12 0M9 16.5a4.2 4.2 0 0 1 6 0"/><path d="M12 19.5v.5"/>',
    "chip": '<rect x="7" y="7" width="10" height="10"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>',
    "battery": '<rect x="3" y="8" width="16" height="9"/><path d="M21 11v3M7 11v3M10 11v3"/>',
    "printer": '<path d="M7 9V4h10v5"/><rect x="4" y="9" width="16" height="8"/><path d="M7 14h10v6H7z"/>',
    "threat": '<path d="M12 3l8 3v6c0 4.5-3.2 7.6-8 9-4.8-1.4-8-4.5-8-9V6z"/><path d="M12 8.5v4.5M12 15.5v.5"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.2 7.6-8 9-4.8-1.4-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "drop": '<path d="M12 3c3.5 4.5 6 7.6 6 11a6 6 0 0 1-12 0c0-3.4 2.5-6.5 6-11z"/>',
    "windows": '<path d="M4 5.5l7-1v7H4zM13 4.2l7-1v8.3h-7zM4 13h7v7l-7-1zM13 13h7v8.3l-7-1z"/>',
    "remote": '<rect x="3" y="4" width="18" height="12"/><path d="M8 20h8M8 10h7M12.5 7.5L15 10l-2.5 2.5"/>',
    "camera": '<path d="M3 8l13-3 2 6-13 3z"/><path d="M18 8.5l3 .8M7 13.5V19h5M4 19h3"/>',
    "server": '<rect x="4" y="4" width="16" height="6"/><rect x="4" y="14" width="16" height="6"/><path d="M7.5 7h.5M7.5 17h.5M12 7h5M12 17h5"/>',
    "office": '<rect x="3" y="4" width="8" height="6"/><rect x="13" y="4" width="8" height="6"/><rect x="8" y="14" width="8" height="6"/><path d="M7 10v2h10v-2M12 12v2"/>',
    "wrench": '<path d="M14.5 4a4.5 4.5 0 0 0-4.2 6.1L4 16.4V20h3.6l6.3-6.3A4.5 4.5 0 0 0 20 9.5l-3 3-2.5-.5-.5-2.5 3-3A4.5 4.5 0 0 0 14.5 4z"/>',
    "doc": '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 12h7M9 16h7"/>',
    "chat": '<path d="M4 5h16v11H10l-5 4v-4H4z"/>',
    "kit": '<rect x="3" y="7" width="18" height="13"/><path d="M9 7V4h6v3M12 10.5v6M9 13.5h6"/>',
    "pin": '<path d="M12 21s-6-6.2-6-11a6 6 0 0 1 12 0c0 4.8-6 11-6 11z"/><path d="M12 9.5v1"/>',
    "tag": '<path d="M3 4h8l10 10-7 7L4 11z"/><path d="M7.5 8v.5"/>',
    "key": '<path d="M14 4a6 6 0 1 0 0 12 6 6 0 0 0 0-12z" transform="translate(2 -1)"/><path d="M11.5 13.5L4 21M6.5 18.5L9 21"/>',
    "disk": '<rect x="4" y="4" width="16" height="16"/><path d="M8 4v6h8V4M8 20v-5h8v5"/>',
}


def icon(name):
    return (f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            f'{ICONS[name]}</svg>')


# ---------------------------------------------------------------- schema

ORG = {
    "@type": ["LocalBusiness", "ProfessionalService"],
    "@id": SITE + "/#organization",
    "name": "ADA Tech Division",
    "legalName": "Andreas Digital Agency",
    "alternateName": ["ADA Tech", "Andreas Digital Agency Tech Division"],
    "url": SITE + "/",
    "logo": SITE + "/assets/brand/lettermark-blue.png",
    "image": SITE + "/assets/img/og-ada-tech.png",
    "description": "ADA Tech Division repairs laptops and desktop computers, sets up Windows, fixes Wi-Fi and "
                   "office networks, installs CCTV and supports business IT. On site in Rundu, remote across Namibia.",
    "telephone": PHONE_TEL,
    "email": EMAIL,
    "priceRange": "N$99+",
    "currenciesAccepted": "NAD",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Rundu",
        "addressRegion": "Kavango East",
        "addressCountry": "NA",
    },
    "areaServed": [{"@type": "City", "name": "Rundu"}, {"@type": "Country", "name": "Namibia"}],
    "parentOrganization": {"@type": "Organization", "name": "Andreas Digital Agency", "url": MAIN + "/"},
    "knowsAbout": ["Computer repair", "Laptop repair", "Windows installation", "Wi-Fi and network setup",
                   "CCTV installation", "Remote IT support", "Managed IT services"],
}


def crumbs_schema(crumbs):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (path, name) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": name, "item": url(path)})
    return {"@type": "BreadcrumbList", "itemListElement": items}


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def faq_schema(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in items
        ],
    }


def service_schema(name, desc, path, price=None, unit=None):
    s = {"@type": "Service", "name": name, "description": desc, "url": url(path),
         "provider": {"@id": SITE + "/#organization"},
         "areaServed": [{"@type": "Country", "name": "Namibia"}]}
    if price:
        spec = {"@type": "PriceSpecification", "price": price, "priceCurrency": "NAD", "minPrice": price}
        if unit:
            spec["unitText"] = unit
        s["offers"] = {"@type": "Offer", "priceCurrency": "NAD", "price": price, "priceSpecification": spec,
                       "url": url("pricing")}
    return s


def howto_schema(name, desc, steps_):
    return {"@type": "HowTo", "name": name, "description": desc,
            "step": [{"@type": "HowToStep", "position": i, "name": t, "text": strip_tags(d)}
                     for i, (t, d) in enumerate(steps_, start=1)]}


# ------------------------------------------------------------ components

def buttons(*items):
    """items: (href, label, variant) — variant '', 'line' or 'blue'."""
    out = []
    for href, label, *rest in items:
        v = rest[0] if rest else ""
        cls = "btn" + (f" btn--{v}" if v else "")
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        out.append(f'<a class="{cls}" href="{e(href)}"{ext}>{e(label)}</a>')
    return '<div class="btn-row">' + "".join(out) + "</div>"


def hero(h1, lead, crumbs=None, actions=None, code=None, ico=None):
    """code: short strings shown as technical chips above the title,
    for example ("Fault F-03", "Windows")."""
    c = ""
    if crumbs:
        parts = ['<a href="/">Home</a>']
        for path, name in crumbs[:-1]:
            parts.append(f'<a href="/{e(path)}">{e(name)}</a>')
        parts.append(f"<span>{e(crumbs[-1][1])}</span>")
        c = '<nav class="crumbs" aria-label="Breadcrumb">' + '<span aria-hidden="true">/</span>'.join(parts) + "</nav>"
    k = ""
    if code:
        k = '<p class="code-line">' + "".join(f"<span>{e(x)}</span>" for x in code) + "</p>"
    a = buttons(*actions) if actions else ""
    big = ""
    if ico:
        big = (f'<svg class="hero-ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
               f'{ICONS[ico]}</svg>')
    return f"""<section class="hero hero-page on-dark">{big}<div class="wrap">
{c}{k}<h1>{h1}</h1>
<p class="lead">{lead}</p>
{a}</div></section>"""


def sec(inner, cls="", wrap_cls=""):
    c = "sec" + (f" {cls}" if cls else "")
    w = "wrap" + (f" {wrap_cls}" if wrap_cls else "")
    return f'<section class="{c}"><div class="{w}">\n{inner}\n</div></section>'


def head_block(h2, p="", label="", tag="h2"):
    lab = f'<span class="label">{e(label)}</span>' if label else ""
    para = f"<p>{p}</p>" if p else ""
    return f'<div class="sec-head">{lab}<{tag} class="h2">{h2}</{tag}>{para}</div>'


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def signs(items):
    return '<ul class="signs">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def steps(items, vertical=False, cls=""):
    c = "steps" + (" steps--v" if vertical else "") + (f" {cls}" if cls else "")
    return f'<ol class="{c}">' + "".join(
        f'<li><h3>{e(t)}</h3><p>{d}</p></li>' for t, d in items) + "</ol>"


def checks(items):
    """Numbered checks a person can do themselves. items: (title, html)."""
    return '<ol class="checks">' + "".join(
        f"<li><h3>{e(t)}</h3>{d if d.lstrip().startswith('<p') else '<p>' + d + '</p>'}</li>"
        for t, d in items) + "</ol>"


def rows(items):
    """items: (href, title, detail, right)"""
    return '<ul class="rows">' + "".join(
        f'<li><a href="{e(h)}"><strong>{e(t)}</strong><span>{d}</span><em>{e(r)}</em></a></li>'
        for h, t, d, r in items) + "</ul>"


def code_rows(items):
    """items: (href, icon, code, title, detail, right)"""
    return '<ul class="rows rows--code">' + "".join(
        f'<li><a href="{e(h)}">{icon(i)}<b>{e(c)}</b><strong>{e(t)}</strong><span>{d}</span><em>{e(r)}</em></a></li>'
        for h, i, c, t, d, r in items) + "</ul>"


def cards(items, cols=3, swipe=False):
    """items: (href, title, text, link_label[, tag[, icon]])."""
    out = []
    for h, t, d, l, *rest in items:
        tag = f'<span class="tag">{e(rest[0])}</span>' if rest and rest[0] else ""
        ic = icon(rest[1]) if len(rest) > 1 and rest[1] else ""
        ext = ' target="_blank" rel="noopener"' if h.startswith("http") else ""
        out.append(f'<a class="card card--link" href="{e(h)}"{ext}>{ic}{tag}<h3 class="h3">{e(t)}</h3><p>{d}</p>'
                   f'<span class="more">{e(l)}</span></a>')
    return f'<div class="grid g{cols}{" swipe" if swipe else ""}">' + "".join(out) + "</div>"


def info_cards(items, cols=3, swipe=False):
    """Cards that are not links. items: (tag, title, html[, icon])."""
    out = []
    for tag, t, d, *rest in items:
        ic = icon(rest[0]) if rest and rest[0] else ""
        tg = f'<span class="tag">{e(tag)}</span>' if tag else ""
        out.append(f'<div class="card">{ic}{tg}<h3 class="h3">{e(t)}</h3>'
                   f'{d if d.lstrip().startswith(("<p", "<ul")) else "<p>" + d + "</p>"}</div>')
    return f'<div class="grid g{cols}{" swipe" if swipe else ""}">' + "".join(out) + "</div>"


def faq(items):
    out = ['<div class="faq">']
    for q, a in items:
        out.append(f"<details><summary>{e(q)}</summary><div>{a}</div></details>")
    out.append("</div>")
    return "".join(out)


def table(headers, body_rows, caption="", first_th=True):
    th = "".join(f'<th scope="col">{e(h)}</th>' for h in headers)
    trs = []
    for r in body_rows:
        cells = []
        for i, c in enumerate(r):
            if i == 0 and first_th:
                cells.append(f'<th scope="row">{c}</th>')
            else:
                label = e(headers[i]) if i < len(headers) else ""
                cells.append(f'<td data-label="{label}"><span class="cell">{c}</span></td>')
        trs.append("<tr>" + "".join(cells) + "</tr>")
    cap = f"<caption>{caption}</caption>" if caption else ""
    return (f'<div class="tbl-wrap"><table class="stack">{cap}<thead><tr>{th}</tr></thead>'
            f'<tbody>{"".join(trs)}</tbody></table></div>')


def answer(text, label="In short"):
    return f'<div class="answer"><span class="tag">{e(label)}</span><p>{text}</p></div>'


def sheet(title, ref, items, action=None):
    """A job sheet: a titled box of label and value pairs.
    items: (label, html). action: (href, label)."""
    body = "".join(f"<div><dt>{e(k)}</dt><dd>{v}</dd></div>" for k, v in items)
    foot = ""
    if action:
        ext = ' target="_blank" rel="noopener"' if action[0].startswith("http") else ""
        foot = f'<div class="sheet-foot"><a class="btn" href="{e(action[0])}"{ext}>{e(action[1])}</a></div>'
    return (f'<aside class="sheet" aria-label="{e(title)}"><div class="sheet-head"><span>{e(title)}</span>'
            f'<span>{e(ref)}</span></div><dl>{body}</dl>{foot}</aside>')


def stop(items, title="Stop and get it looked at if", after=""):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="stop"><strong>{e(title)}</strong><ul>{lis}</ul>{after}</div>'


def photo(name, alt=""):
    return (f'<figure class="photo"><img src="/assets/img/{name}.webp" alt="{e(alt)}" width="1200" height="800" '
            f'loading="lazy"></figure>')


def plan(tag, name, price, per, who, items, action, main=False):
    """A priced package. action: (href, label)."""
    ext = ' target="_blank" rel="noopener"' if action[0].startswith("http") else ""
    return (f'<div class="plan{" plan--main" if main else ""}"><span class="tag">{e(tag)}</span>'
            f'<h3>{e(name)}</h3><p class="for">{who}</p>'
            f'<p class="price">{e(price)} <small>{e(per)}</small></p>{ticks(items)}'
            f'<a class="btn{"" if main else " btn--blue"}" href="{e(action[0])}"{ext}>{e(action[1])}</a></div>')


def cta_band(h2="Tell us what is going wrong.",
             p="You do not need to know the cause. Say what the device is, what it is doing and when it "
               f"started. A standard diagnostic costs {DIAG} and comes off the repair if you go ahead."):
    return f"""<section class="cta" aria-labelledby="cta-h"><div class="wrap">
<div><h2 class="h2" id="cta-h">{h2}</h2><p>{p}</p></div>
<ul class="ways">
<li><a href="{WA}" target="_blank" rel="noopener"><span>WhatsApp</span><strong>081 803 2641</strong></a></li>
<li><a href="tel:{PHONE_TEL}"><span>Call</span><strong>{PHONE}</strong></a></li>
<li><a href="/support"><span>Form</span><strong>Describe the problem</strong></a></li>
<li><a href="mailto:{EMAIL}"><span>Email</span><strong>{EMAIL}</strong></a></li>
</ul></div></section>"""


# ----------------------------------------------------------------- shell

def header(active):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return f"""<a class="skip" href="#main">Skip to main content</a>
<div class="util"><div class="wrap">
<span class="util-note">A division of <a href="{MAIN}/">Andreas Digital Agency</a>, Rundu, Namibia</span>
<span class="util-links"><a href="tel:{PHONE_TEL}">{PHONE}</a><a class="hide-s" href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="/client-desk">Existing clients</a><a class="hide-s" href="/contact">Contact</a></span>
</div></div>
<header class="head"><div class="wrap">
<a class="brand" href="/" aria-label="ADA Tech Division home"><img src="/assets/img/ada-mark-blue.png" alt="" width="320" height="147"><span><strong>ADA Tech Division</strong><span>Andreas Digital Agency</span></span></a>
<div class="head-tools">
<a class="search-btn" id="searchBtn" href="/search" aria-controls="searchBar" aria-expanded="false"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg><span>Search</span></a>
<button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
</div>
<nav class="nav" id="nav" aria-label="Main">{''.join(links)}<a class="btn" href="/support">Get support</a></nav>
</div>
<form class="searchbar" id="searchBar" action="/search" method="get" role="search" hidden><div class="wrap">
<label class="vh" for="q-head">Search this site</label>
<input id="q-head" name="q" type="search" placeholder="Search: blue screen, prices, Wi-Fi, Windows 11…" autocomplete="off" required>
<button class="btn btn--blue" type="submit">Search</button>
</div></form>
</header>"""


def footer():
    return f"""<footer class="foot"><div class="wrap">
<div class="foot-grid">
<div>
<img class="foot-logo" src="/assets/img/ada-logo-white.png" alt="Andreas Digital Agency" width="440" height="106" loading="lazy">
<p>ADA Tech Division is the computer repair and IT support division of Andreas Digital Agency.</p>
<dl>
<dt>Phone and WhatsApp</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd>
<dt>Company line</dt><dd><a href="tel:{COMPANY_TEL}">{COMPANY_LINE}</a></dd>
<dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Workshop</dt><dd>{PLACE}</dd>
<dt>Cover</dt><dd>On site in Rundu. Remote support across Namibia.</dd>
</dl>
</div>
<div><h2>Services</h2><ul>
<li><a href="/services/computer-repair">Computer and laptop repair</a></li>
<li><a href="/services/windows-setup">Windows and software setup</a></li>
<li><a href="/services/bios-firmware">BIOS and firmware</a></li>
<li><a href="/services/networking">Wi-Fi and networking</a></li>
<li><a href="/services/remote-support">Remote support</a></li>
<li><a href="/services/security">Security and backups</a></li>
<li><a href="/services/cctv">CCTV</a></li>
<li><a href="/services/server-infrastructure">Servers and infrastructure</a></li>
<li><a href="/services/business-it">Business IT setup</a></li>
</ul></div>
<div><h2>Common problems</h2><ul>
<li><a href="/problems/laptop-not-turning-on">Laptop will not turn on</a></li>
<li><a href="/problems/slow-laptop">Laptop is very slow</a></li>
<li><a href="/problems/windows-blue-screen">Blue screen errors</a></li>
<li><a href="/problems/windows-black-screen">Black screen</a></li>
<li><a href="/problems/laptop-overheating">Overheating</a></li>
<li><a href="/problems/wifi-keeps-disconnecting">Wi-Fi keeps dropping</a></li>
<li><a href="/problems/windows-update-not-working">Windows Update fails</a></li>
<li><a href="/problems/liquid-spilled-on-laptop">Liquid spilled on a laptop</a></li>
<li><a href="/problems">All problems</a></li>
</ul></div>
<div><h2>Prices and plans</h2><ul>
<li><a href="/pricing">Pricing</a></li>
<li><a href="/first-aid">ADA First Aid (monthly care)</a></li>
<li><a href="/managed-it">Managed IT for business</a></li>
<li><a href="/solutions">Who we help</a></li>
<li><a href="/locations/rundu">IT support in Rundu</a></li>
<li><a href="/guides">Guides</a></li>
<li><a href="/faq">Questions and answers</a></li>
<li><a href="/news">News and updates</a></li>
<li><a href="/search">Search this site</a></li>
</ul></div>
<div><h2>Clients</h2><ul>
<li><a href="/support">Get support</a></li>
<li><a href="/client-desk">Existing client desk</a></li>
<li><a href="/service-record">Open a service record</a></li>
<li><a href="/work">Case files</a></li>
<li><a href="/reviews">Client reviews</a></li>
<li><a href="/about">How we work</a></li>
<li><a href="/contact">Contact</a></li>
<li><a href="{MAIN}/">Andreas Digital Agency</a></li>
<li><a href="{WEB}/">ADA Web Division</a></li>
</ul></div>
</div>
<div class="foot-base">
<span>&copy; <span id="year">2026</span> Andreas Digital Agency. All rights reserved.</span>
<span><a href="{MAIN}/privacy">Privacy</a> &nbsp; <a href="{MAIN}/cookies">Cookies</a> &nbsp; <a href="{MAIN}/payment-refund-cancellation">Payments and refunds</a> &nbsp; <a href="/directory">All pages</a></span>
<span>Built in Namibia. Designed for Africa.</span>
</div>
</div></footer>
<div class="bar" aria-label="Quick contact"><a href="tel:{PHONE_TEL}">Call</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="/support">Get support</a></div>"""


def page(path, title, desc, body, *, active="", crumbs=None, schema=None, og_type="website",
         noindex=False, scripts=(), cta=True, lastmod=REVIEWED_ISO):
    """Write one page. `path` is the clean URL path ('' for the home page)."""
    canonical = url(path)
    graph = [ORG, {
        "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/",
        "name": "ADA Tech Division", "publisher": {"@id": SITE + "/#organization"}, "inLanguage": "en",
        "potentialAction": {"@type": "SearchAction",
                            "target": {"@type": "EntryPoint", "urlTemplate": SITE + "/search?q={search_term_string}"},
                            "query-input": "required name=search_term_string"},
    }, {
        "@type": "WebPage", "@id": canonical + "#webpage", "url": canonical, "name": title,
        "description": desc, "isPartOf": {"@id": SITE + "/#website"}, "dateModified": lastmod, "inLanguage": "en",
    }]
    if crumbs:
        graph.append(crumbs_schema(crumbs))
    for s in (schema or []):
        graph.append(s)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    # Never let the JSON-LD close its own script element.
    ld = ld.replace("</", "<\\/")
    robots = "noindex, follow" if noindex else "index, follow"
    extra = "".join(f'<script type="module" src="{s}"></script>' for s in scripts)
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#081b33">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="ADA Tech Division">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-ada-tech.png">
<meta property="og:locale" content="en_NA">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/css/ada.css">
<script src="/assets/js/ada.js"></script>
<script type="application/ld+json">{ld}</script>
</head>
<body>
{header(active)}
<main id="main">
{body}
{cta_band() if cta is True else (cta or '')}
</main>
{footer()}
{extra}
</body>
</html>
"""
    # A hub that also has child pages (/problems and /problems/...) is written
    # as <hub>/index.html so the folder and the page can never be confused.
    clean = path.strip("/")
    rel = (clean + "/index.html") if clean in HUB_FOLDERS else ((clean or "index") + ".html")
    out = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    PAGES.append((path.strip("/"), lastmod, not noindex))
    return out


# ------------------------------------------------------- page patterns

def split(label, h2, right_html, cls=""):
    """Heading on the left, content on the right."""
    lab = f'<span class="label">{e(label)}</span>' if label else ""
    return sec(f'<div class="split"><div>{lab}<h2 class="h2">{h2}</h2></div><div>{right_html}</div></div>', cls)


def block(label, h2, inner, intro="", cls=""):
    return sec(head_block(h2, intro, label=label) + inner, cls)


def related(items, h2="Related", cls="sec--light"):
    """items: (href, title, text)"""
    return sec(head_block(h2, label="See also") + cards(
        [(h, t, d, "Open") for h, t, d in items],
        cols=3 if len(items) % 3 == 0 or len(items) > 4 else 2, swipe=True), cls)
