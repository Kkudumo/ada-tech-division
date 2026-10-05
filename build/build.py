#!/usr/bin/env python3
"""Regenerate every public page:  python3 build/build.py"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layout  # noqa: E402

MODULES = ["pages_home", "pages_problems", "pages_services", "pages_plans", "pages_company",
           "pages_guides", "pages_news", "pages_search", "pages_system"]


def main():
    for name in MODULES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError as err:
            if err.name != name:
                raise
            print("skip", name)
            continue
        mod.build()
    write_sitemap()
    import pages_search
    count, size = pages_search.build_index()
    print(f"built {len(layout.PAGES)} pages; search index: {count} pages, {size // 1024} KB")


def write_sitemap():
    rows = []
    for path, lastmod, indexable in layout.PAGES:
        if indexable:
            rows.append(f"  <url><loc>{layout.url(path)}</loc><lastmod>{lastmod}</lastmod></url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(layout.ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


if __name__ == "__main__":
    main()
