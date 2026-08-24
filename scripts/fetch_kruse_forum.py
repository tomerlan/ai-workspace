#!/usr/bin/env python3
"""
Search forum.jackkruse.com (XenForo) for testimonials and melanin/UV/cancer content.

Logs in automatically with username + password — no manual cookie export needed.

Usage:
    python3 scripts/fetch_kruse_forum.py --user EMAIL --password PASS
    python3 scripts/fetch_kruse_forum.py  # reads KRUSE_FORUM_USER / KRUSE_FORUM_PASS from env
    python3 scripts/fetch_kruse_forum.py --queries "melanin cancer,UV tumor"

Credentials (pick one):
    - Pass --user / --password on the command line
    - Set env vars:  export KRUSE_FORUM_USER=you@email.com
                     export KRUSE_FORUM_PASS=yourpassword
    - Create .env in the project root with those two lines (loaded automatically)
"""

import argparse
import http.cookiejar
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime


BASE_URL = "https://forum.jackkruse.com"

DEFAULT_QUERIES = [
    "melanin cancer",
    "cancer remission",
    "tumor sunlight",
    "cancer recovery",
    "UV healing cancer",
    "melanin tumor",
    "cancer healed",
    "cancer cure sunlight",
]

TESTIMONIAL_SIGNALS = re.compile(
    r"\bmy cancer\b|\bmy tumor\b|\bi was diagnosed\b|\bremission\b|"
    r"\brecovery\b|\bcured\b|\bhealed\b|\bshrunk\b|\bno evidence of disease\b|"
    r"\bNED\b|\bi have cancer\b|\bi had cancer\b|\bmy diagnosis\b|"
    r"\bmy oncologist\b|\bmy chemo\b|\bmy treatment\b|\bcancer free\b",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# HTML parsing helpers
# ---------------------------------------------------------------------------

class TextExtractor(HTMLParser):
    """Strip tags, keep text."""
    def __init__(self):
        super().__init__()
        self._parts = []
        self._skip_tags = {"script", "style", "noscript"}
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self._skip_tags and self._skip > 0:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self._parts.append(data)

    def get_text(self):
        return re.sub(r"\s+", " ", "".join(self._parts)).strip()


def strip_html(html):
    p = TextExtractor()
    try:
        p.feed(html)
        return p.get_text()
    except Exception:
        return re.sub(r"<[^>]+>", " ", html)


def extract_attr(tag_html, attr):
    """Pull a single attribute value from a tag string."""
    m = re.search(rf'{attr}=["\']([^"\']*)["\']', tag_html, re.IGNORECASE)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def load_env_file():
    """Load .env file from project root if present."""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip())


def load_cookies(cookies_file):
    """
    Load a Netscape cookies.txt, handling the #HttpOnly_ prefix that
    Cookie-Editor adds to HttpOnly cookies. Python's MozillaCookieJar
    treats those lines as comments and silently drops them — which loses
    xf_session and xf_user, the two auth cookies.
    """
    raw = Path(cookies_file).read_text()
    # Strip the #HttpOnly_ prefix so the jar sees them as normal cookie lines
    fixed = re.sub(r"^#HttpOnly_", "", raw, flags=re.MULTILINE)

    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tmp:
        tmp.write(fixed)
        tmp_path = tmp.name

    jar = http.cookiejar.MozillaCookieJar()
    jar.load(tmp_path, ignore_discard=True, ignore_expires=True)
    Path(tmp_path).unlink()
    return jar


def build_opener(cookies_file=None):
    jar = load_cookies(cookies_file) if cookies_file else http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [
        ("User-Agent",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
        ("Accept", "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8"),
        ("Accept-Language", "en-US,en;q=0.9"),
    ]
    return opener


def get_page_csrf(opener):
    """Fetch the search page and extract the live data-csrf token from the HTML."""
    html, _ = fetch_url(opener, f"{BASE_URL}/search/")
    if not html:
        raise RuntimeError("Could not fetch search page for CSRF token")
    m = re.search(r'data-csrf=["\']([^"\']+)["\']', html)
    if not m:
        raise RuntimeError("data-csrf not found on search page")
    return m.group(1)


def fetch_url(opener, url, post_data=None, retries=3, delay=2.0):
    """GET or POST a URL, return (response_text, final_url). Returns (None, None) on error."""
    for attempt in range(retries):
        try:
            if post_data:
                data = urllib.parse.urlencode(post_data).encode()
                req = urllib.request.Request(url, data=data)
                req.add_header("Content-Type", "application/x-www-form-urlencoded")
            else:
                req = urllib.request.Request(url)
            resp = opener.open(req, timeout=20)
            return resp.read().decode("utf-8", errors="replace"), resp.geturl()
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f"    Rate limited — waiting {wait}s ...")
                time.sleep(wait)
            elif e.code in (403, 401):
                print(f"    {e.code} at {url} — may need fresh cookies")
                return None, None
            else:
                print(f"    HTTP {e.code} at {url}")
                if attempt == retries - 1:
                    return None, None
                time.sleep(delay)
        except Exception as e:
            print(f"    Error: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return None, None
    return None, None


# ---------------------------------------------------------------------------
# XenForo search
# ---------------------------------------------------------------------------

def xf_search(opener, query, csrf_token, page=1):
    """
    XenForo search is two steps:
      1. POST /search/search  →  JSON with {"redirect": "/search/<id>/?q=..."}
      2. GET that redirect URL  →  HTML page with thread links
    Returns list of {thread_id, thread_url, title} dicts.
    """
    # Step 1: submit the search
    post_data = {
        "keywords":        query,
        "users":           "",
        "date":            "",
        "child_nodes":     "1",
        "order":           "relevance",
        "_xfToken":        csrf_token,
        "_xfRequestUri":   "/search/",
        "_xfWithData":     "1",
        "_xfResponseType": "json",
    }
    if page > 1:
        post_data["page"] = page

    raw, _ = fetch_url(opener, f"{BASE_URL}/search/search", post_data=post_data)
    if not raw:
        return []

    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return []

    redirect = data.get("redirect")
    if not redirect:
        return []

    # Step 2: fetch the results page
    results_url = redirect if redirect.startswith("http") else BASE_URL + redirect
    if page > 1:
        results_url = re.sub(r"([?&])page=\d+", f"\\1page={page}", results_url)
        if "page=" not in results_url:
            sep = "&" if "?" in results_url else "?"
            results_url += f"{sep}page={page}"

    html, _ = fetch_url(opener, results_url)
    if not html:
        return []

    return _parse_thread_links(html)


def _parse_thread_links(html):
    """Extract unique thread links from a XenForo search results page."""
    thread_pattern = re.compile(
        r'href=["\'](?:' + re.escape(BASE_URL) + r')?(/threads/[^"\'#?]+)["\']',
        re.IGNORECASE
    )
    seen = set()
    results = []
    for m in thread_pattern.finditer(html):
        path = m.group(1)
        url_clean = re.sub(r"/page-\d+/?$", "", path.rstrip("/"))
        tid_m = re.search(r"\.(\d+)/?$", url_clean)
        if not tid_m:
            continue
        tid = tid_m.group(1)
        if tid in seen:
            continue
        seen.add(tid)
        results.append({
            "thread_id":  tid,
            "thread_url": BASE_URL + url_clean,
            "title":      "",
        })
    return results


# ---------------------------------------------------------------------------
# Thread fetching
# ---------------------------------------------------------------------------

def fetch_thread_posts(opener, thread_url, max_pages=5):
    """Fetch all posts from a XenForo thread. Returns list of post dicts."""
    posts = []
    page = 1
    while page <= max_pages:
        url = thread_url if page == 1 else f"{thread_url}/page-{page}"
        html, _ = fetch_url(opener, url)
        if not html:
            break

        # Extract thread title from <h1 class="p-title-value">
        title_m = re.search(
            r'class=["\']p-title-value["\'][^>]*>(.*?)</h1',
            html, re.DOTALL | re.IGNORECASE
        )
        thread_title = strip_html(title_m.group(1)) if title_m else ""

        # XenForo post structure: <article class="message message--post ...">
        # Each post has data-author and a .message-body
        post_blocks = re.split(
            r'<article\b[^>]*class=["\'][^"\']*message[^"\']*["\']',
            html
        )

        found_posts = 0
        for block in post_blocks[1:]:  # skip before first <article>
            # Author
            author_m = re.search(r'data-author=["\']([^"\']+)["\']', block)
            author = author_m.group(1) if author_m else "?"

            # Post ID
            pid_m = re.search(r'data-content=["\']post-(\d+)["\']', block)
            post_id = pid_m.group(1) if pid_m else "?"

            # Date/time
            date_m = re.search(r'<time\b[^>]*datetime=["\']([^"\']+)["\']', block)
            date = date_m.group(1)[:10] if date_m else ""

            # Body: .message-body .bbWrapper (or similar)
            body_m = re.search(
                r'class=["\'][^"\']*bbWrapper[^"\']*["\'][^>]*>(.*?)</div>',
                block, re.DOTALL | re.IGNORECASE
            )
            if not body_m:
                # Fallback: find the largest text block
                body_m = re.search(
                    r'class=["\'][^"\']*message-body[^"\']*["\'][^>]*>(.*?)</div>',
                    block, re.DOTALL | re.IGNORECASE
                )

            if not body_m:
                continue

            text = strip_html(body_m.group(1))[:3000]
            if len(text) < 20:
                continue

            posts.append({
                "post_id":      post_id,
                "thread_title": thread_title,
                "thread_url":   thread_url,
                "author":       author,
                "date":         date,
                "text":         text,
                "is_testimonial": bool(TESTIMONIAL_SIGNALS.search(text)),
            })
            found_posts += 1

        # Check if there's a next page
        if found_posts == 0 or not re.search(r'rel=["\']next["\']', html, re.IGNORECASE):
            break
        page += 1
        time.sleep(1.0)

    return posts, thread_title


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run(opener, queries, csrf_token, delay=2.5, fetch_posts=True):
    seen_threads = {}  # thread_id -> entry

    for query in queries:
        print(f"\n  Searching: '{query}' ...")
        for page in range(1, 4):  # up to 3 pages of search results
            results = xf_search(opener, query, csrf_token, page=page)
            if not results:
                print(f"    Page {page}: 0 results")
                break
            print(f"    Page {page}: {len(results)} threads")
            for r in results:
                tid = r["thread_id"]
                if tid not in seen_threads:
                    seen_threads[tid] = {
                        **r,
                        "matched_queries": [query],
                        "posts": [],
                    }
                elif query not in seen_threads[tid]["matched_queries"]:
                    seen_threads[tid]["matched_queries"].append(query)
            if len(results) < 5:
                break
            time.sleep(delay)
        time.sleep(delay)

    threads = list(seen_threads.values())
    print(f"\nUnique threads found: {len(threads)}")

    if fetch_posts:
        print(f"\nFetching posts for {len(threads)} threads ...\n")
        for i, entry in enumerate(threads):
            print(f"  [{i+1}/{len(threads)}] {entry['thread_url']}")
            posts, title = fetch_thread_posts(opener, entry["thread_url"])
            entry["posts"] = posts
            if title:
                entry["thread_title"] = title
            n_test = sum(1 for p in posts if p["is_testimonial"])
            print(f"    {len(posts)} posts, {n_test} with testimonial signal")
            time.sleep(delay)

    return threads


def _raw_dir(out_dir: Path) -> Path:
    """Raw scrape artifacts live in <out_dir>/raw/; digests live in <out_dir>/."""
    d = Path(out_dir) / "raw"
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_markdown(threads, out_dir):
    out_file = out_dir / "kruse_forum_results.md"
    total_posts = sum(len(t["posts"]) for t in threads)
    total_test = sum(sum(1 for p in t["posts"] if p["is_testimonial"]) for t in threads)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# Jack Kruse Forum — UV / Melanin / Cancer Testimonials\n\n")
        f.write(f"*Retrieved: {datetime.now().strftime('%Y-%m-%d')}*\n\n")
        f.write(f"**Threads:** {len(threads)} | **Posts fetched:** {total_posts} | **Testimonial signals:** {total_test}\n\n")
        f.write("---\n\n")

        # Testimonial posts first
        f.write("## Threads with Testimonial Signal\n\n")
        for entry in threads:
            testimonials = [p for p in entry["posts"] if p["is_testimonial"]]
            if not testimonials:
                continue
            title = entry.get("thread_title") or entry["thread_url"]
            f.write(f"### [{title}]({entry['thread_url']})\n\n")
            f.write(f"*Queries matched: {', '.join(entry['matched_queries'])}*\n\n")
            for p in testimonials:
                f.write(f"**@{p['author']}** ({p['date']}):\n\n")
                f.write(f"> {p['text'][:1200]}\n\n")
            f.write("---\n\n")

        # All other threads as a compact list
        f.write("## All Matched Threads (no testimonial signal)\n\n")
        for entry in threads:
            testimonials = [p for p in entry["posts"] if p["is_testimonial"]]
            if testimonials:
                continue
            title = entry.get("thread_title") or entry["thread_url"]
            f.write(f"- [{title}]({entry['thread_url']}) — *{', '.join(entry['matched_queries'])}*\n")

    print(f"\nMarkdown: {out_file}")
    return out_file


def write_json(threads, out_dir):
    out_file = _raw_dir(out_dir) / "kruse_forum_raw.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(threads, f, indent=2, ensure_ascii=False)
    print(f"JSON:     {out_file}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cookies", default="forum_cookies.txt",
                        help="Netscape cookies.txt from Cookie-Editor (default: forum_cookies.txt)")
    parser.add_argument("--queries", default=None,
                        help="Comma-separated search terms (default: built-in list)")
    parser.add_argument("--out",     default="outputs/forum")
    parser.add_argument("--delay",   type=float, default=2.5)
    parser.add_argument("--no-fetch-posts", action="store_true")
    args = parser.parse_args()

    cookies_path = Path(args.cookies)
    if not cookies_path.exists():
        print(f"ERROR: {cookies_path} not found.")
        sys.exit(1)

    queries = [q.strip() for q in args.queries.split(",")] if args.queries else DEFAULT_QUERIES
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    opener = build_opener(str(cookies_path))

    print("Fetching CSRF token from search page ...")
    csrf_token = get_page_csrf(opener)
    print(f"  CSRF: {csrf_token[:16]}...\n")

    # Confirm auth
    html, _ = fetch_url(opener, f"{BASE_URL}/search/")
    if html and 'data-logged-in="true"' in html:
        print("Authenticated ✓\n")
    else:
        print("WARNING: does not appear authenticated — check cookies\n")

    threads = run(opener, queries, csrf_token,
                  delay=args.delay,
                  fetch_posts=not args.no_fetch_posts)

    write_json(threads, out_dir)
    write_markdown(threads, out_dir)
    print(f"\nOutput: {out_dir}/")


if __name__ == "__main__":
    main()
