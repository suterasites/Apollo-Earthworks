#!/usr/bin/env python3
"""
clean_url_links.py - point every internal reference at the URL the host actually
serves, instead of the one that 308-redirects to it.

WHY. On 2026-09-15 Google Search Console still reported 12 of Apollo's 26 pages as
not in Google. /basements and /capability-statement were two of them, and neither
had a single link to its clean URL anywhere on the site: basements.html was linked
25 times and capability-statement.html 12 times, and the host 308s `.html` to the
extension-less URL. The 09-09 pass counted those as "linked from indexed pages",
which was true and did not help - Google's only path in was a redirect, and the
URL the canonical and the sitemap both nominate was linked from nowhere. Same
cause as TJM Detailing on 2026-09-03 (its .build/clean_url_links.py).

Apollo differs from TJM in one way: the 14 landing pages live in folders
(/site-cuts-melbourne/index.html) and link up with `../services.html`, so the
rewrite has to take a `../` prefix and emit a root-relative path.

WHAT IT REWRITES, and nothing else:

    href="page.html"        -> href="/page"      (index.html -> "/")
    href="../page.html"     -> href="/page"
    https://www.apolloearthworks.com.au/page.html -> .../page   (og:url, JSON-LD, #@id kept)

Left alone on purpose: invoice/ (Kosta's working invoice tool, noindex and
robots-disallowed), the googletagmanager ns.html iframe, and the tailwind content
globs. Every clean target was checked live at 200 with no redirect before this ran.

Idempotent - a second run finds nothing to do. Dry run by default, --apply writes.
"""

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://www.apolloearthworks.com.au"
SKIP_DIRS = ("invoice",)

# href="slug.html", "./slug.html", "../slug.html" or "/slug.html" -> href="/slug", fragment kept
HREF = re.compile(r'(href\s*=\s*")(?:\./|\.\./)?/?([A-Za-z0-9_-]+)\.html(#[^"]*)?(")')
# Absolute self-referencing URLs inside content="", JSON-LD "url"/"item"/"@id".
ABS = re.compile(r'(' + re.escape(DOMAIN) + r'/)([A-Za-z0-9_-]+)\.html\b')


def clean_href(m):
    slug = m.group(2)
    return m.group(1) + ("/" if slug == "index" else "/" + slug) + (m.group(3) or "") + m.group(4)


def clean_abs(m):
    slug = m.group(2)
    return m.group(1) + ("" if slug == "index" else slug)


def pages():
    out = sorted(glob.glob(os.path.join(ROOT, "*.html")))
    for path in sorted(glob.glob(os.path.join(ROOT, "*", "index.html"))):
        if os.path.basename(os.path.dirname(path)) not in SKIP_DIRS:
            out.append(path)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    total = 0
    touched = 0
    for path in pages():
        txt = open(path, encoding="utf-8").read()
        new, n1 = HREF.subn(clean_href, txt)
        new, n2 = ABS.subn(clean_abs, new)
        n = n1 + n2
        if not n:
            continue
        touched += 1
        total += n
        print("  %-46s %4d  (%d href, %d absolute)"
              % (os.path.relpath(path, ROOT), n, n1, n2))
        if args.apply:
            open(path, "w", encoding="utf-8").write(new)

    print("\n%d reference(s) across %d file(s)%s"
          % (total, touched, "" if args.apply else "  [dry run - use --apply]"))

    if args.apply:
        # Nothing may name a .html URL afterwards. A leftover means a form this
        # script does not understand, and a silent partial sweep is worse than none.
        left = []
        for path in pages():
            txt = open(path, encoding="utf-8").read()
            for m in re.finditer(r'(?:href\s*=\s*"[^"]*|' + re.escape(DOMAIN)
                                 + r'/[^"\s]*)\.html\b', txt):
                left.append("%s: %s" % (os.path.relpath(path, ROOT), m.group(0)[:70]))
        if left:
            print("\nFAIL - %d reference(s) survived the sweep:" % len(left))
            for line in left[:20]:
                print("  " + line)
            return 1
        print("verified: no internal reference names a .html URL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
