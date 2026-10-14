"""ADA Tech prices, taken from ADA Core.

Pages never contain a price as typed text. They contain a placeholder such as
[[price:diag]], and layout.page() swaps it for the price when the page is
written, for example "N$99".

Where the prices come from:
  * During a build with ADA_API_KEY set (the Vercel build), from ADA Core's public
    API: GET https://api.andreasdigitalagency.com/api/public/services. Only
    published services with a current approved price are returned.
  * Otherwise, or if ADA Core cannot be reached, from SNAPSHOT below: the last
    known prices, so a build never fails or shows an empty price.

To change a price, change it in ADA Hub (Services). The next deployment of this
site picks it up. Update SNAPSHOT too when convenient, so local builds match.
"""
import json
import os
import re
import urllib.parse
import urllib.request

API = os.environ.get("ADA_API_URL", "https://api.andreasdigitalagency.com")

# placeholder name: (ADA Core service id, last known amount in NAD)
SNAPSHOT = {
    "diag":          ("ADA-SVC-2026-0015", 99),     # Standard device diagnostic
    "remote":        ("ADA-SVC-2026-0016", 149),    # Remote quick support, from
    "tuneup":        ("ADA-SVC-2026-0017", 249),    # PC tune-up and optimisation
    "driver":        ("ADA-SVC-2026-0018", 179),    # Driver or software fault, from
    "winupdate":     ("ADA-SVC-2026-0019", 249),    # Windows Update repair, from
    "bios_update":   ("ADA-SVC-2026-0020", 249),    # BIOS or UEFI update, from
    "bios_recovery": ("ADA-SVC-2026-0021", 449),    # BIOS recovery or boot fault, from
    "office":        ("ADA-SVC-2026-0022", 249),    # Microsoft Office setup, from
    "printer":       ("ADA-SVC-2026-0023", 179),    # Printer setup, from
    "ram":           ("ADA-SVC-2026-0024", 179),    # RAM or SSD fitting (labour), from
    "backup":        ("ADA-SVC-2026-0025", 249),    # Data backup or transfer, from
    "router":        ("ADA-SVC-2026-0026", 349),    # Router and Wi-Fi setup, from
    "win_ready":     ("ADA-SVC-2026-0012", 649),    # Windows Ready
    "win_office":    ("ADA-SVC-2026-0013", 849),    # Windows + Office Complete
    "refresh":       ("ADA-SVC-2026-0014", 1049),   # Complete Device Refresh
    "fa_essential":  ("ADA-SVC-2026-0031", 249),    # First Aid Essential, a month
    "fa_plus":       ("ADA-SVC-2026-0032", 399),    # First Aid Plus, a month
    "fa_family":     ("ADA-SVC-2026-0033", 699),    # First Aid Family, a month
    "micro_care":    ("ADA-SVC-2026-0034", 1249),   # Micro Business Care, a month
    "business_care": ("ADA-SVC-2026-0035", 2449),   # Business Care, a month
    "managed_it":    ("ADA-SVC-2026-0036", 3999),   # Managed IT, from, a month
}

TOKEN = re.compile(r"\[\[price:([a-z_]+)\]\]")
TOKEN_URL = re.compile(r"%5B%5Bprice%3A([a-z_]+)%5D%5D")


def money(amount):
    """1199.99 -> 'N$1,199.99'; 649 -> 'N$649'."""
    whole = float(amount).is_integer()
    return "N$" + (f"{amount:,.0f}" if whole else f"{amount:,.2f}")


def _from_ada_core():
    key = os.environ.get("ADA_API_KEY")
    if not key:
        return None, "ADA_API_KEY not set"
    req = urllib.request.Request(f"{API}/api/public/services", headers={"X-API-Key": key, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            rows = json.load(res)
    except Exception as err:  # network, HTTP or JSON error: fall back, never fail the build
        return None, f"ADA Core not reachable ({type(err).__name__})"
    found = {}
    for row in rows if isinstance(rows, list) else []:
        price = row.get("price") or {}
        if row.get("id") and price.get("amount") is not None and price.get("currency", "NAD") == "NAD":
            found[row["id"]] = float(price["amount"])
    return found, None


def _load():
    live, problem = _from_ada_core()
    prices, notes = {}, []
    for name, (service_id, last_known) in SNAPSHOT.items():
        if live and service_id in live:
            prices[name] = live[service_id]
            if live[service_id] != last_known:
                notes.append(f"{name}: ADA Core {money(live[service_id])} (snapshot {money(last_known)})")
        else:
            prices[name] = last_known
            if live is not None:
                notes.append(f"{name}: {service_id} has no published price in ADA Core; using snapshot")
    source = "ADA Core" if live is not None else f"snapshot ({problem})"
    print(f"prices: {source}" + "".join(f"\n  {n}" for n in notes))
    return prices


PRICES = _load()


def fill(text):
    """Replace every [[price:name]] placeholder. An unknown name stops the build."""
    def swap(m):
        name = m.group(1)
        if name not in PRICES:
            raise KeyError(f"unknown price placeholder [[price:{name}]]")
        return money(PRICES[name])
    text = TOKEN.sub(swap, text)
    # The same placeholder inside a link (for example a WhatsApp message text) arrives URL-encoded.
    return TOKEN_URL.sub(lambda m: urllib.parse.quote(swap(m), safe=""), text)


def number(value):
    """For structured data: a price name or [[price:name]] placeholder -> '649'; other text -> digits only."""
    m = TOKEN.search(value or "")
    name = m.group(1) if m else value
    if name in PRICES:
        amount = PRICES[name]
        return f"{amount:.0f}" if float(amount).is_integer() else f"{amount:.2f}"
    return (value or "").replace("From ", "").replace("N$", "").replace(",", "")
