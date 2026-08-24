#!/usr/bin/env python3
"""
Scrape forum.jackkruse.com for El Salvador / mito-gathering content.

Searches for El Salvador, Shalpa, mito meetups, etc., then fetches full
thread posts and identifies active community members/contacts.

Usage:
    python3 scripts/fetch_kruse_elsalvador.py --cookies forum_cookies.txt
    python3 scripts/fetch_kruse_elsalvador.py  # auto-loads from .env

Output:
    outputs/kruse_elsalvador/el_salvador_results.md
    outputs/kruse_elsalvador/el_salvador_raw.json
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
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime


BASE_URL = "https://forum.jackkruse.com"

ES_QUERIES = [
    "El Salvador",
    "Shalpa",
    "El Salvador mito",
    "El Salvador gathering",
    "El Salvador meetup",
    "El Salvador beach",
    "El Salvador retreat",
    "living in El Salvador",
    "move to El Salvador",
    "moved to El Salvador",
    "ES mito",
]

# Threads we already know are relevant (from prior scrape)
KNOWN_THREADS = [
    "/threads/headed-to-el-salvador-in-3-days.28445",
    "/threads/gynecologist-in-el-salvador.28455",
    "/threads/jack-foster-oj-history-of-brain-tumor-and-hydrocephalus.30099",
    "/threads/first-update-after-being-in-es-for-41-2-months.31053",
    "/threads/chases-optimal-journal.31640",
    "/threads/jack-lehmans-optimal-journal.31892",
    "/threads/paiges-optimal-journal.31150",
    "/threads/joys-optimal-journal.31416",
    "/threads/sunhunters-journal-to-happiness.28072",
]

# Patterns that indicate El Salvador / gathering context
ES_SIGNALS = re.compile(
    r"\bel salvador\b|\bsalvador\b|\bshalpa\b|\bmito gather\b|\b"
    r"gather.*mito\b|\bmito.*meetup\b|\bmeetup.*mito\b|\bretreat.*el\b|"
    r"\bES beach\b|\bbeach.*ES\b|\bEl Salvador.*mito\b|\bmito.*El Salvador\b|"
    r"\bIndia\b.*\bEl Salvador\b|\bEl Salvador\b.*\bIndia\b",
    re.IGNORECASE,
)

OPERATION_SIGNALS = re.compile(
    r"\boperation\b|\bfacility\b|\bclinic\b|\bcenter\b|\bcentre\b|"
    r"\bprogram\b|\btreatment center\b|\bhealing center\b|\bcommunity\b|"
    r"\bshalpa\b|\bIndia\b|\bhost\b|\bguide\b|\bcoordinator\b",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

class TextExtractor(HTMLParser):
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


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def load_env_file():
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip())


def load_cookies(cookies_file):
    raw = Path(cookies_file).read_text()
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
        ("Accept", "text/html,application/xhtml+xml,*/*;q=0.8"),
        ("Accept-Language", "en-US,en;q=0.9"),
    ]
    return opener


def fetch_url(opener, url, post_data=None, retries=3, delay=2.0):
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
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f"    Rate limited — waiting {wait}s ...")
                time.sleep(wait)
            elif e.code in (403, 401):
                print(f"    {e.code} at {url}")
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


def get_page_csrf(opener):
    html, _ = fetch_url(opener, f"{BASE_URL}/search/")
    if not html:
        raise RuntimeError("Could not fetch search page")
    m = re.search(r'data-csrf=["\']([^"\']+)["\']', html)
    if not m:
        raise RuntimeError("data-csrf not found on search page")
    return m.group(1)


# ---------------------------------------------------------------------------
# XenForo search
# ---------------------------------------------------------------------------

def xf_search(opener, query, csrf_token, page=1):
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
# Thread / post fetching — with improved author extraction
# ---------------------------------------------------------------------------

def extract_author_from_block(block):
    """
    Try multiple XenForo HTML patterns to extract the post author.

    Scoped to the opening article tag + user-cell section to avoid
    picking up the logged-in user's links from nav/sidebar.
    """
    # Pattern 1: data-author on the <article> opening tag (first 400 chars)
    article_tag = block[:400]
    m = re.search(r'data-author=["\']([^"\']+)["\']', article_tag)
    if m:
        return m.group(1).strip()

    # Extract just the user-info cell to avoid nav links
    user_cell_m = re.search(
        r'class=["\'][^"\']*message-cell--user[^"\']*["\'][^>]*>(.*?)</(?:div|aside)\b',
        block, re.DOTALL | re.IGNORECASE
    )
    scope = user_cell_m.group(1) if user_cell_m else block[:2000]

    # Pattern 2: member profile link  /members/slug.NNN/  scoped to user cell
    m = re.search(
        r'href=["\'][^"\']*?/members/([^/"\'\.]+)\.\d+/?["\']',
        scope, re.IGNORECASE
    )
    if m:
        return m.group(1).strip()

    # Pattern 3: class="username" scoped
    m = re.search(
        r'class=["\'][^"\']*\busername\b[^"\']*["\'][^>]*>\s*([^<]{2,60})\s*<',
        scope, re.IGNORECASE
    )
    if m:
        return strip_html(m.group(1)).strip()

    # Pattern 4: itemprop="name"
    m = re.search(r'itemprop=["\']name["\'][^>]*>\s*([^<]{2,60})\s*<', scope)
    if m:
        return strip_html(m.group(1)).strip()

    return "?"


def fetch_thread_posts(opener, thread_url, max_pages=8):
    """Fetch posts from a thread. Returns (list_of_posts, thread_title)."""
    posts = []
    page = 1
    while page <= max_pages:
        url = thread_url if page == 1 else f"{thread_url}/page-{page}"
        html, _ = fetch_url(opener, url)
        if not html:
            break

        # Thread title
        title_m = re.search(
            r'class=["\']p-title-value["\'][^>]*>(.*?)</h1',
            html, re.DOTALL | re.IGNORECASE
        )
        thread_title = strip_html(title_m.group(1)) if title_m else ""

        # Split into per-post blocks on <article> tags
        post_blocks = re.split(
            r'(?=<article\b[^>]*class=["\'][^"\']*\bmessage\b)',
            html
        )

        found_posts = 0
        for block in post_blocks:
            if not re.search(r'<article\b[^>]*class=["\'][^"\']*\bmessage\b', block):
                continue

            author = extract_author_from_block(block)

            pid_m = re.search(r'data-content=["\']post-(\d+)["\']', block)
            post_id = pid_m.group(1) if pid_m else "?"

            date_m = re.search(r'<time\b[^>]*datetime=["\']([^"\']+)["\']', block)
            date = date_m.group(1)[:10] if date_m else ""

            # Body text — try bbWrapper first, then message-body
            body_m = re.search(
                r'class=["\'][^"\']*bbWrapper[^"\']*["\'][^>]*>(.*?)</div>',
                block, re.DOTALL | re.IGNORECASE
            )
            if not body_m:
                body_m = re.search(
                    r'class=["\'][^"\']*message-body[^"\']*["\'][^>]*>(.*?)</div>',
                    block, re.DOTALL | re.IGNORECASE
                )
            if not body_m:
                continue

            text = strip_html(body_m.group(1))[:4000]
            if len(text) < 20:
                continue

            posts.append({
                "post_id":           post_id,
                "thread_title":      thread_title,
                "thread_url":        thread_url,
                "author":            author,
                "date":              date,
                "text":              text,
                "es_signal":         bool(ES_SIGNALS.search(text)),
                "operation_signal":  bool(OPERATION_SIGNALS.search(text)),
            })
            found_posts += 1

        if found_posts == 0 or not re.search(r'rel=["\']next["\']', html, re.IGNORECASE):
            break
        page += 1
        time.sleep(1.5)

    return posts, thread_title


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run(opener, queries, csrf_token, delay=3.0):
    seen_threads = {}

    # Seed with known ES threads
    for path in KNOWN_THREADS:
        tid_m = re.search(r"\.(\d+)/?$", path)
        if tid_m:
            tid = tid_m.group(1)
            seen_threads[tid] = {
                "thread_id":       tid,
                "thread_url":      BASE_URL + path,
                "title":           "",
                "matched_queries": ["[known]"],
                "posts":           [],
            }

    # Search for new threads
    for query in queries:
        print(f"\n  Searching: '{query}' ...")
        for page in range(1, 4):
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
                        "posts":           [],
                    }
                elif query not in seen_threads[tid]["matched_queries"]:
                    seen_threads[tid]["matched_queries"].append(query)
            if len(results) < 5:
                break
            time.sleep(delay)
        time.sleep(delay)

    threads = list(seen_threads.values())
    print(f"\nUnique threads to fetch: {len(threads)}")

    print(f"\nFetching posts ...\n")
    for i, entry in enumerate(threads):
        print(f"  [{i+1}/{len(threads)}] {entry['thread_url']}")
        posts, title = fetch_thread_posts(opener, entry["thread_url"])
        entry["posts"] = posts
        if title:
            entry["thread_title"] = title
        n_es = sum(1 for p in posts if p["es_signal"])
        authors = {p["author"] for p in posts if p["author"] != "?"}
        print(f"    {len(posts)} posts | {n_es} ES-signal | authors: {authors or '(none extracted)'}")
        time.sleep(delay)

    return threads


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def build_contact_list(threads):
    """
    Build a ranked list of users to contact, prioritising those who posted
    in ES-signal threads and wrote about El Salvador themselves.
    """
    contact_scores = defaultdict(lambda: {"score": 0, "threads": [], "posts": []})

    for t in threads:
        for p in t["posts"]:
            author = p["author"]
            if author == "?" or not author:
                continue
            entry = contact_scores[author]
            if p["es_signal"]:
                entry["score"] += 3
            if p["operation_signal"] and p["es_signal"]:
                entry["score"] += 2
            turl = p["thread_url"]
            if turl not in entry["threads"]:
                entry["threads"].append(turl)
            if p["es_signal"] and len(entry["posts"]) < 3:
                entry["posts"].append({
                    "thread": p.get("thread_title") or turl,
                    "date":   p["date"],
                    "text":   p["text"][:400],
                })

    return sorted(
        [(name, data) for name, data in contact_scores.items() if data["score"] > 0],
        key=lambda x: -x[1]["score"]
    )


def write_markdown(threads, out_dir):
    contacts = build_contact_list(threads)
    out_file = out_dir / "el_salvador_results.md"

    total_posts = sum(len(t["posts"]) for t in threads)
    es_posts = sum(sum(1 for p in t["posts"] if p["es_signal"]) for t in threads)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# Jack Kruse Community — El Salvador / Mito Gatherings\n\n")
        f.write(f"*Retrieved: {datetime.now().strftime('%Y-%m-%d')}*\n\n")
        f.write(
            f"**Threads:** {len(threads)} | "
            f"**Posts fetched:** {total_posts} | "
            f"**El Salvador mentions:** {es_posts}\n\n"
        )
        f.write("---\n\n")

        # Contact list
        f.write("## Users to Contact\n\n")
        if contacts:
            f.write(
                "Ranked by activity in El Salvador / mito-gathering discussions "
                "(score = weighted engagement):\n\n"
            )
            for name, data in contacts:
                f.write(f"### @{name}  *(score: {data['score']})*\n\n")
                f.write(f"Active in {len(data['threads'])} relevant thread(s).\n\n")
                for post in data["posts"]:
                    f.write(f"**Thread:** {post['thread']}  \n")
                    f.write(f"**Date:** {post['date']}  \n")
                    f.write(f"> {post['text']}\n\n")
                f.write("---\n\n")
        else:
            f.write(
                "_No usernames could be extracted automatically. "
                "See threads below for manual identification._\n\n"
            )
            f.write("---\n\n")

        # El Salvador signal posts
        f.write("## El Salvador / Gathering Posts\n\n")
        for entry in threads:
            es_p = [p for p in entry["posts"] if p["es_signal"]]
            if not es_p:
                continue
            title = entry.get("thread_title") or entry["thread_url"]
            f.write(f"### [{title}]({entry['thread_url']})\n\n")
            f.write(f"*Queries: {', '.join(entry['matched_queries'])}*\n\n")
            for p in es_p:
                f.write(f"**@{p['author']}** ({p['date']}):\n\n")
                f.write(f"> {p['text'][:1500]}\n\n")
            f.write("---\n\n")

        # Operation / facility signals
        f.write("## Operation / Facility Mentions\n\n")
        for entry in threads:
            op_p = [p for p in entry["posts"] if p["operation_signal"] and p["es_signal"]]
            if not op_p:
                continue
            title = entry.get("thread_title") or entry["thread_url"]
            f.write(f"### [{title}]({entry['thread_url']})\n\n")
            for p in op_p:
                f.write(f"**@{p['author']}** ({p['date']}):\n\n")
                f.write(f"> {p['text'][:1500]}\n\n")
            f.write("---\n\n")

        # All threads index
        f.write("## All Threads Index\n\n")
        for entry in threads:
            title = entry.get("thread_title") or entry["thread_url"]
            n_es = sum(1 for p in entry["posts"] if p["es_signal"])
            f.write(f"- [{title}]({entry['thread_url']}) — {len(entry['posts'])} posts, {n_es} ES-signal\n")

    print(f"\nMarkdown: {out_file}")
    return out_file


def write_json(threads, out_dir):
    out_file = out_dir / "el_salvador_raw.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(threads, f, indent=2, ensure_ascii=False)
    print(f"JSON:     {out_file}")


def main():
    load_env_file()

    parser = argparse.ArgumentParser()
    parser.add_argument("--cookies", default="forum_cookies.txt",
                        help="Netscape cookies.txt (default: forum_cookies.txt)")
    parser.add_argument("--queries", default=None,
                        help="Comma-separated extra queries")
    parser.add_argument("--out", default="outputs/kruse_elsalvador")
    parser.add_argument("--delay", type=float, default=3.0)
    parser.add_argument("--no-search", action="store_true",
                        help="Skip searching, only fetch known threads")
    args = parser.parse_args()

    cookies_path = Path(args.cookies)
    if not cookies_path.exists():
        print(f"ERROR: {cookies_path} not found.")
        sys.exit(1)

    extra_queries = [q.strip() for q in args.queries.split(",")] if args.queries else []
    queries = [] if args.no_search else (ES_QUERIES + extra_queries)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    opener = build_opener(str(cookies_path))

    print("Fetching CSRF token ...")
    csrf_token = get_page_csrf(opener)
    print(f"  CSRF: {csrf_token[:16]}...\n")

    html, _ = fetch_url(opener, f"{BASE_URL}/search/")
    if html and 'data-logged-in="true"' in html:
        print("Authenticated ✓\n")
    else:
        print("WARNING: not authenticated — check cookies\n")

    threads = run(opener, queries, csrf_token, delay=args.delay)

    write_json(threads, out_dir)
    write_markdown(threads, out_dir)
    print(f"\nDone. Output: {out_dir}/")


if __name__ == "__main__":
    main()
