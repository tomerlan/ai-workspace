#!/usr/bin/env python3
"""
Fetch all optimalklubs.com blog posts matching a search term and download them as PDFs.

The site uses the dk-pdf WordPress plugin; PDFs are generated via:
    https://optimalklubs.com/?pdf=<post_id>

Usage:
    python3 scripts/fetch_kruse_melanin.py --cookies cookies.txt
    python3 scripts/fetch_kruse_melanin.py --cookies cookies.txt --search "quantum biology"
    python3 scripts/fetch_kruse_melanin.py --cookies cookies.txt --out data/kruse_pdfs

Getting your cookies.txt:
    1. Log in to optimalklubs.com in Chrome/Firefox
    2. Install the "Cookie-Editor" browser extension
    3. While on optimalklubs.com, click the extension → Export → "Netscape" format
    4. Save as cookies.txt in the project root
"""

import argparse
import http.cookiejar
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


BASE_URL = "https://optimalklubs.com"
WP_API   = f"{BASE_URL}/wp-json/wp/v2/posts"


def build_opener(cookies_file=None):
    jar = http.cookiejar.MozillaCookieJar()
    if cookies_file:
        jar.load(cookies_file, ignore_discard=True, ignore_expires=True)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (compatible; KruseFetcher/1.0)")]
    return opener


def fetch_post_list(opener, search, page_size=100):
    """Return all posts matching `search` via the WP REST API."""
    posts = []
    page = 1
    while True:
        params = urllib.parse.urlencode({
            "search":   search,
            "per_page": page_size,
            "page":     page,
            "_fields":  "id,title,link,slug",
        })
        url = f"{WP_API}?{params}"
        try:
            resp  = opener.open(url)
            total = resp.headers.get("X-WP-Total", "?")
            batch = json.loads(resp.read())
            if not batch:
                break
            posts.extend(batch)
            print(f"  Page {page}: {len(batch)} posts  (total on server: {total})")
            if len(batch) < page_size:
                break
            page += 1
        except urllib.error.HTTPError as e:
            print(f"API error on page {page}: {e}")
            break
    return posts


def download_pdf(opener, post, out_dir, delay=1.5):
    """Download the dk-pdf version of a post and save to out_dir."""
    post_id = post["id"]
    slug    = post["slug"]

    filename = out_dir / f"{slug}.pdf"
    if filename.exists():
        print(f"  [skip] {filename.name}")
        return filename

    pdf_url = f"{BASE_URL}/?pdf={post_id}"
    try:
        resp    = opener.open(pdf_url)
        content = resp.read()
        if content[:4] != b"%PDF":
            print(f"  [WARN] {slug} — not a PDF (paywall or redirect). Check cookies.")
            # save as html for debugging
            (out_dir / f"{slug}_error.html").write_bytes(content[:4000])
            return None
        filename.write_bytes(content)
        size_kb = len(content) // 1024
        print(f"  [ok]   {slug}.pdf  ({size_kb} KB)")
        time.sleep(delay)
        return filename
    except urllib.error.HTTPError as e:
        print(f"  [err]  {slug} — HTTP {e.code}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Download Jack Kruse / OptimalKlubs PDFs")
    parser.add_argument("--search",  default="melanin",         help="Search term (default: melanin)")
    parser.add_argument("--out",     default="data/kruse_pdfs", help="Output directory")
    parser.add_argument("--cookies", required=True,             help="Path to Netscape cookies.txt")
    parser.add_argument("--delay",   type=float, default=1.5,   help="Seconds between downloads")
    args = parser.parse_args()

    cookies_path = Path(args.cookies)
    if not cookies_path.exists():
        print(f"ERROR: cookies file not found: {cookies_path}")
        sys.exit(1)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    opener = build_opener(str(cookies_path))

    print(f"Searching '{args.search}' on optimalklubs.com ...\n")
    posts = fetch_post_list(opener, args.search)
    print(f"\nFound {len(posts)} posts total.\n")
    for p in posts:
        print(f"  • [{p['id']}] {p['title']['rendered'][:70]}")

    print(f"\nDownloading PDFs to '{out_dir}/' ...\n")
    ok, fail = 0, 0
    for post in posts:
        result = download_pdf(opener, post, out_dir, delay=args.delay)
        if result:
            ok += 1
        else:
            fail += 1

    print(f"\nDone. {ok} downloaded, {fail} failed/skipped.")
    if fail:
        print("Tip: if you see WARN messages, your cookies may be expired — re-export from browser.")


if __name__ == "__main__":
    main()
