"""Run:  python3 -m unittest build/test_prices.py   (or python3 build/test_prices.py)

Guards the link between this site and ADA Core: every service name the generator looks up must exist in build/prices.json,
and no catalogue price may be typed into a page file again."""
import json
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# The only price literals allowed in the generator: a dated news announcement (a historical record, not a live price).
ALLOWED_LITERALS = {"pages_news.py"}


def source(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return f.read()


def looked_up_names():
    names = set()
    call = re.compile(r'\b(?:m|fm|lc|st|raw)\(\s*"([^"]+)"')
    for fn in sorted(os.listdir(HERE)):
        if fn.startswith("pages_") or fn in ("layout.py", "build.py"):
            names.update(call.findall(source(fn)))
    for tok in re.findall(r"\{\{\w+:([^}]+)\}\}", source("ada.js.in")):
        names.update(tok.split("|"))
    import layout
    names.update(layout.PRICED)
    return names


class PriceNames(unittest.TestCase):
    def test_every_looked_up_name_is_in_the_snapshot(self):
        with open(os.path.join(HERE, "prices.json"), encoding="utf-8") as f:
            snap = {" ".join(s["name"].lower().split()): s for s in json.load(f)["services"]}
        names = looked_up_names()
        self.assertGreater(len(names), 20)
        for n in sorted(names):
            self.assertIn(" ".join(n.lower().split()), snap, f'"{n}" is not in build/prices.json (renamed in ADA Hub?)')
            self.assertIsNotNone(snap[" ".join(n.lower().split())].get("price"), f'"{n}" has no list price in the snapshot')

    def test_every_lookup_resolves(self):
        import layout
        for n in looked_up_names():
            self.assertTrue(layout.m(n).startswith("N$"))

    def test_no_price_literals_in_page_files(self):
        lit = re.compile(r"N\$\s?\d")
        for fn in sorted(os.listdir(HERE)):
            if not fn.endswith(".py") or fn in ALLOWED_LITERALS or fn.startswith("test_") or fn == "ada_prices.py":
                continue
            for i, line in enumerate(source(fn).splitlines(), 1):
                if lit.search(line) and not line.lstrip().startswith(('"""', "'")) and '"""' not in line:
                    self.assertFalse(lit.search(line), f"{fn}:{i} has a typed price: {line.strip()[:80]}")
        self.assertNotRegex(source("ada.js.in"), lit)


if __name__ == "__main__":
    unittest.main()
