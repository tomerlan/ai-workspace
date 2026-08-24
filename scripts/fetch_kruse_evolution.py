#!/usr/bin/env python3
"""
Fetch optimalklubs.com blog posts about cancer through the lens of evolution and
life-history theory, then write a raw JSON dump + formatted Markdown.

The WP REST API returns full post HTML in content.rendered; we strip tags to get
plain text for downstream digest use — no PDFs or intermediate steps needed.

Usage:
    python3 scripts/fetch_kruse_evolution.py --cookies cookies.txt
    python3 scripts/fetch_kruse_evolution.py --cookies cookies.txt --out outputs/evolution
    python3 scripts/fetch_kruse_evolution.py --cookies cookies.txt --min-score 2

Getting cookies.txt:
    1. Log in to optimalklubs.com in Chrome/Firefox
    2. Install Cookie-Editor → Export → Netscape format → save as cookies.txt
"""

import argparse
import http.cookiejar
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

BASE_URL = "https://optimalklubs.com"
WP_API   = f"{BASE_URL}/wp-json/wp/v2/posts"

# Search terms that surface evolution / life-history / atavism cancer content.
DEFAULT_QUERIES = [
    "cancer evolution",
    "atavism cancer",
    "life history cancer",
    "Warburg evolution",
    "mitochondria cancer evolution",
    "cancer entropy",
    "oncogenesis quantum",
    "cancer epigenetics evolution",
    "cancer environment mismatch",
    "cancer redox evolution",
]

# Keywords used to score post relevance after fetching full text.
RELEVANCE_KEYWORDS = re.compile(
    r"\batavism\b|\batavistic\b|\blife.?history\b|\bwarburg\b|\boncogenesis\b|"
    r"\bevolution(?:ary)?\b|\bphylogen\b|\bnatural selection\b|\bfitness\b|"
    r"\br.?strategy\b|\bk.?strategy\b|\bmitochondri\b|\bredox\b|\bentropy\b|"
    r"\bepigenetic\b|\bsomatic evolution\b|\bcancer stem\b|\boncology\b",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# HTML stripping
# ---------------------------------------------------------------------------

class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._parts = []
        self._skip = 0
        self._skip_tags = {"script", "style", "noscript"}

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self._skip_tags and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self._parts.append(data)

    def get_text(self):
        return re.sub(r" {2,}", " ", re.sub(r"\n{3,}", "\n\n", "".join(self._parts))).strip()


def strip_html(html: str) -> str:
    p = _TextExtractor()
    try:
        p.feed(html)
        return p.get_text()
    except Exception:
        return re.sub(r"<[^>]+>", " ", html)


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def build_opener(cookies_file=None):
    jar = http.cookiejar.MozillaCookieJar()
    if cookies_file:
        # Handle #HttpOnly_ prefix added by Cookie-Editor
        raw = Path(cookies_file).read_text()
        fixed = re.sub(r"^#HttpOnly_", "", raw, flags=re.MULTILINE)
        import tempfile
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tmp:
            tmp.write(fixed)
            tmp_path = tmp.name
        jar.load(tmp_path, ignore_discard=True, ignore_expires=True)
        Path(tmp_path).unlink()

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [
        ("User-Agent",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
        ("Accept", "application/json, text/html;q=0.9"),
    ]
    return opener


def api_get(opener, url, retries=3, delay=2.0):
    for attempt in range(retries):
        try:
            resp = opener.open(url, timeout=30)
            return json.loads(resp.read()), dict(resp.headers)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f"    Rate-limited — waiting {wait}s ...")
                time.sleep(wait)
            elif e.code in (401, 403):
                print(f"    {e.code} — check cookies")
                return None, {}
            else:
                print(f"    HTTP {e.code} at {url}")
                if attempt == retries - 1:
                    return None, {}
                time.sleep(delay)
        except Exception as e:
            print(f"    Error: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return None, {}
    return None, {}


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def fetch_posts_for_query(opener, query, page_size=50, delay=1.5) -> list[dict]:
    """Return all posts matching query via WP REST API, with full HTML content."""
    posts = []
    page = 1
    while True:
        params = urllib.parse.urlencode({
            "search":   query,
            "per_page": page_size,
            "page":     page,
            "_fields":  "id,title,link,slug,date,content",
        })
        url = f"{WP_API}?{params}"
        batch, headers = api_get(opener, url)
        if not batch:
            break
        total = headers.get("X-WP-Total", "?")
        print(f"    Page {page}: {len(batch)} posts  (server total: {total})")
        posts.extend(batch)
        if len(batch) < page_size:
            break
        page += 1
        time.sleep(delay)
    return posts


def score_post(text: str) -> int:
    """Count distinct relevance keyword matches in the text."""
    return len(RELEVANCE_KEYWORDS.findall(text))


def collect_posts(opener, queries, delay=2.0) -> list[dict]:
    """Run all queries, deduplicate by post ID, strip HTML, score."""
    seen: dict[int, dict] = {}

    for query in queries:
        print(f"\n  Searching: '{query}' ...")
        raw_posts = fetch_posts_for_query(opener, query, delay=delay)
        for p in raw_posts:
            pid = p["id"]
            if pid in seen:
                seen[pid]["matched_queries"].append(query)
                continue
            title = strip_html(p.get("title", {}).get("rendered", ""))
            html  = p.get("content", {}).get("rendered", "")
            text  = strip_html(html)
            seen[pid] = {
                "post_id":        pid,
                "title":          title,
                "url":            p.get("link", ""),
                "date":           p.get("date", "")[:10],
                "text":           text,
                "matched_queries": [query],
                "relevance_score": score_post(f"{title} {text}"),
            }
        time.sleep(delay)

    posts = sorted(seen.values(), key=lambda x: x["relevance_score"], reverse=True)
    print(f"\nUnique posts found: {len(posts)}")
    return posts


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def _raw_dir(out_dir: Path) -> Path:
    """Raw scrape artifacts live in <out_dir>/raw/; digests live in <out_dir>/."""
    d = Path(out_dir) / "raw"
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_json(posts, out_dir: Path):
    out = _raw_dir(out_dir) / "kruse_evolution_raw.json"
    out.write_text(json.dumps(posts, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"JSON:     {out}")


def write_markdown(posts, out_dir: Path, min_score: int = 1):
    out = _raw_dir(out_dir) / "kruse_evolution_posts.md"
    qualifying = [p for p in posts if p["relevance_score"] >= min_score]

    with open(out, "w", encoding="utf-8") as f:
        f.write("# Jack Kruse — Cancer Through Evolution & Life History\n\n")
        f.write(f"*Retrieved: {datetime.now().strftime('%Y-%m-%d')}*\n\n")
        f.write(f"**Posts qualifying (score ≥ {min_score}):** {len(qualifying)} / {len(posts)} total\n\n")
        f.write("---\n\n")

        for p in qualifying:
            f.write(f"## [{p['title']}]({p['url']})\n\n")
            f.write(f"*Date: {p['date']} | Relevance score: {p['relevance_score']} | "
                    f"Queries: {', '.join(p['matched_queries'])}*\n\n")
            # Truncate very long posts in the markdown for readability
            text = p["text"]
            if len(text) > 6000:
                text = text[:6000] + "\n\n[… truncated — see JSON for full text …]"
            f.write(text)
            f.write("\n\n---\n\n")

    print(f"Markdown: {out}")
    return out


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Fetch Jack Kruse blog posts about cancer, evolution, and life history."
    )
    parser.add_argument("--cookies",   default="cookies.txt",
                        help="Netscape cookies.txt (default: cookies.txt)")
    parser.add_argument("--queries",   default=None,
                        help="Comma-separated search terms (default: built-in list)")
    parser.add_argument("--out",       default="outputs/evolution")
    parser.add_argument("--delay",     type=float, default=2.0)
    parser.add_argument("--min-score", type=int,   default=1,
                        help="Minimum relevance score to include in Markdown (default: 1)")
    args = parser.parse_args()

    cookies_path = Path(args.cookies)
    if not cookies_path.exists():
        print(f"ERROR: cookies file not found: {cookies_path}")
        raise SystemExit(1)

    queries = [q.strip() for q in args.queries.split(",")] if args.queries else DEFAULT_QUERIES
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    opener = build_opener(str(cookies_path))

    # Quick auth check
    try:
        resp = opener.open(f"{BASE_URL}/wp-json/wp/v2/users/me", timeout=10)
        me = json.loads(resp.read())
        print(f"Authenticated as: {me.get('name', '?')}\n")
    except Exception:
        print("WARNING: could not verify auth — check cookies\n")

    posts = collect_posts(opener, queries, delay=args.delay)

    write_json(posts, out_dir)
    write_markdown(posts, out_dir, min_score=args.min_score)
    print(f"\nDone. Output: {out_dir}/")


if __name__ == "__main__":
    main()
