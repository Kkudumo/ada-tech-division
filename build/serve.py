#!/usr/bin/env python3
"""Local preview that mimics Vercel's cleanUrls:  python3 build/serve.py [port]"""
import http.server
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def translate_path(self, path):
        clean = path.split("?")[0].split("#")[0]
        full = super().translate_path(clean)
        if not os.path.exists(full) and os.path.exists(full + ".html"):
            return full + ".html"
        return full

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
