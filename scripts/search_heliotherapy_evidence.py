"""
Exhaustive search: UV / sunlight / vitamin D → cancer remission/healing.

SOURCES:
  1. PubMed (NCBI Entrez) — case reports & clinical studies
     Free. No key needed (rate-limited to ~3 req/sec).
     Key trick: use [ptyp] filter for "Case Reports", NOT hypercalcemia to cut noise.

  2. Europe PMC — broader than PubMed (includes preprints, books, older lit)
     Free. No key needed.

  3. Reddit — personal accounts
     NOTE: Reddit's public JSON search is severely rate-limited and returns <10 results.
     For exhaustive search you need either:
       a) Reddit official API (free, requires OAuth app at reddit.com/prefs/apps)
       b) Arctic Shift (community PushShift mirror): https://arctic-shift.photon-reddit.com
     This script uses the public endpoint; to upgrade, set REDDIT_CLIENT_ID/SECRET in env.

  4. OpenAlex — broad academic database (no key needed, polite rate limit)
     Good for finding review papers and finding who cites key case reports.

NOT INCLUDED (require keys you'd need to register for):
  - Google Custom Search API (100 free/day then $5/1000): best for forum posts, blogs, news
  - YouTube Data API v3 (free with Google account): for video testimonials
  - Semantic Scholar API (free key available): https://www.semanticscholar.org/product/api

Run:   python3 scripts/search_heliotherapy_evidence.py
Output: outputs/photomelanin/evidence_search_results.md
"""

import json, time, sys, textwrap, os
from urllib.parse import quote_plus, urlencode
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("pip3 install requests")

OUT = Path("outputs/photomelanin/evidence_search_results.md")
OUT.parent.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "heliotherapy-research/1.0 (research; contact: researcher)"}

# ─────────────────────────────────────────────────────────────────────────────
# PUBMED
# ─────────────────────────────────────────────────────────────────────────────

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# Each tuple: (label, PubMed query string)
# [ptyp] = publication type filter  |  NOT hypercalcemia cuts calcium-metabolism noise
PUBMED_QUERIES = [
    ("Vitamin D / calcitriol + cancer remission — case reports",
     '("vitamin D" OR calcitriol OR calcipotriol OR paricalcitol) AND '
     '(cancer OR carcinoma OR tumor OR leukemia OR lymphoma OR melanoma) AND '
     '(remission OR regression OR "complete response") AND '
     '"Case Reports"[ptyp] NOT hypercalcemia'),

    ("Vitamin D + cancer survival / outcome — clinical studies",
     '("vitamin D" OR "25-hydroxyvitamin D" OR cholecalciferol) AND '
     '(cancer OR carcinoma OR neoplasm) AND '
     '(survival OR prognosis OR outcome OR recurrence) AND '
     '("Clinical Trial"[ptyp] OR "Observational Study"[ptyp] OR "Cohort Studies"[mesh])'),

    ("UV light / phototherapy + cancer remission — case reports",
     '("ultraviolet" OR "UV radiation" OR "phototherapy" OR "photopheresis") AND '
     '(cancer OR carcinoma OR lymphoma OR melanoma) AND '
     '(remission OR regression OR response) AND '
     '"Case Reports"[ptyp]'),

    ("Spontaneous regression + UV / sunlight / vitamin D",
     '"spontaneous regression" AND (cancer OR tumor OR melanoma) AND '
     '("ultraviolet" OR "sunlight" OR "vitamin D" OR "UV")'),

    ("Heliotherapy + solar therapy + cancer (historical + modern)",
     '(heliotherapy OR "solar therapy" OR "sun therapy" OR "sunlight therapy") AND '
     '(cancer OR carcinoma OR tumor OR neoplasm)'),

    ("Calcitriol / vitamin D analog + specific cancers — case reports",
     '(calcitriol OR "1,25-dihydroxyvitamin D" OR paricalcitol OR "vitamin D analog") AND '
     '(glioblastoma OR "brain tumor" OR "renal cell" OR "prostate cancer" OR '
     '"breast cancer" OR "pancreatic cancer" OR "ovarian cancer") AND '
     '(remission OR regression OR response) AND "Case Reports"[ptyp]'),
]

def pubmed_search(query: str, max_results: int = 50) -> list[dict]:
    """POST-based PubMed esearch + esummary. Returns list of article dicts."""
    search_r = requests.post(
        f"{PUBMED_BASE}/esearch.fcgi",
        data={"db": "pubmed", "term": query, "retmax": max_results,
              "retmode": "json", "sort": "relevance"},
        headers=HEADERS, timeout=20,
    )
    ids = search_r.json().get("esearchresult", {}).get("idlist", [])
    total = search_r.json().get("esearchresult", {}).get("count", "?")
    if not ids:
        return []

    time.sleep(0.35)
    summ_r = requests.post(
        f"{PUBMED_BASE}/esummary.fcgi",
        data={"db": "pubmed", "id": ",".join(ids), "retmode": "json"},
        headers=HEADERS, timeout=20,
    )
    result_data = summ_r.json().get("result", {})

    articles = []
    for pmid in ids:
        item = result_data.get(pmid, {})
        if not item or not isinstance(item, dict):
            continue
        raw_pt = item.get("pubtype", [])
        pub_types = [pt.get("value", pt) if isinstance(pt, dict) else str(pt) for pt in raw_pt]
        articles.append({
            "pmid": pmid,
            "title": item.get("title", ""),
            "authors": ", ".join([a.get("name", "") for a in item.get("authors", [])[:3]]),
            "journal": item.get("fulljournalname", ""),
            "year": item.get("pubdate", "")[:4],
            "pub_types": pub_types,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "_total": total,
        })
    time.sleep(0.35)
    return articles


def pubmed_fetch_abstracts(pmids: list[str]) -> dict[str, str]:
    """Fetch abstracts for a list of PMIDs. Returns {pmid: abstract}."""
    if not pmids:
        return {}
    # efetch with rettype=abstract gives us text; use XML for structured parse
    r = requests.post(
        f"{PUBMED_BASE}/efetch.fcgi",
        data={"db": "pubmed", "id": ",".join(pmids), "retmode": "text", "rettype": "abstract"},
        headers=HEADERS, timeout=30,
    )
    # Parse the plain-text abstract dump: each article separated by blank lines
    # We just grab the first 400 chars per block
    blocks = r.text.split("\n\n\n")
    result = {}
    for i, (pmid, block) in enumerate(zip(pmids, blocks)):
        # Find the abstract line
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        abstract_lines = []
        in_abstract = False
        for line in lines:
            if line.startswith("AB  -") or in_abstract:
                in_abstract = True
                abstract_lines.append(line.replace("AB  -", "").strip())
                if len(" ".join(abstract_lines)) > 400:
                    break
        result[pmid] = " ".join(abstract_lines)[:400]
    time.sleep(0.35)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# EUROPE PMC
# ─────────────────────────────────────────────────────────────────────────────

EPMC_BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

EPMC_QUERIES = [
    ("Vitamin D cancer remission case report (EuropePMC)",
     '(TITLE:"vitamin D" OR TITLE:calcitriol) AND TITLE:cancer AND '
     '(TITLE:remission OR TITLE:regression) AND PUB_TYPE:"Case Report"'),
    ("UV heliotherapy cancer outcome (EuropePMC)",
     '(TITLE:heliotherapy OR TITLE:"ultraviolet" OR TITLE:"solar therapy") AND '
     '(TITLE:cancer OR TITLE:tumor OR TITLE:carcinoma)'),
    ("Spontaneous cancer regression vitamin D UV (EuropePMC)",
     '"spontaneous regression" AND (cancer OR tumor) AND '
     '("vitamin D" OR ultraviolet OR sunlight)'),
]

def epmc_search(query: str, max_results: int = 30) -> list[dict]:
    params = {
        "query": query, "resultType": "core",
        "pageSize": max_results, "format": "json",
    }
    r = requests.get(EPMC_BASE, params=params, headers=HEADERS, timeout=20)
    if r.status_code != 200:
        return []
    results = r.json().get("resultList", {}).get("result", [])
    articles = []
    for item in results:
        pub_types = item.get("pubTypeList", {}).get("pubType", [])
        articles.append({
            "pmid": item.get("pmid", ""),
            "title": item.get("title", ""),
            "authors": item.get("authorString", "")[:80],
            "journal": item.get("journalTitle", ""),
            "year": item.get("pubYear", ""),
            "pub_types": pub_types if isinstance(pub_types, list) else [str(pub_types)],
            "abstract_preview": (item.get("abstractText") or "")[:300],
            "url": (f"https://pubmed.ncbi.nlm.nih.gov/{item['pmid']}/"
                    if item.get("pmid")
                    else f"https://europepmc.org/article/{item.get('source','MED')}/{item.get('id','')}"),
        })
    time.sleep(0.5)
    return articles


# ─────────────────────────────────────────────────────────────────────────────
# REDDIT — public JSON search (no key; upgrade path: register OAuth app)
# ─────────────────────────────────────────────────────────────────────────────
#
# Upgrade to Reddit official API:
#   1. Go to reddit.com/prefs/apps → create "script" app
#   2. Set env vars: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD
#   3. Use PRAW: r = praw.Reddit(client_id=..., ...)
#   4. subreddit.search(query, limit=100, sort='relevance', time_filter='all')
#
# Upgrade to Arctic Shift (PushShift mirror, includes deleted posts):
#   curl "https://arctic-shift.photon-reddit.com/api/posts/search?q=...&subreddit=cancer"
#
REDDIT_SEARCHES = [
    ("cancer",           "vitamin D remission healed cured sun"),
    ("cancer",           "I beat cancer alternative sunlight"),
    ("breastcancer",     "vitamin D NED sun healed"),
    ("lymphoma",         "vitamin D sunlight remission cured"),
    ("melanoma",         "vitamin D sun healed no surgery"),
    ("coloncancer",      "vitamin D sun healed complete response"),
    ("prostatecancer",   "vitamin D sun healed remission"),
    ("leukemia",         "vitamin D light healed remission"),
    ("alternativehealth","vitamin D cancer cured sun healed story"),
    ("HealingFromCancer","vitamin D sunlight heliotherapy"),
    ("sunlight",         "cancer healed cured vitamin D"),
    ("raypeat",          "cancer light vitamin D healed"),
    ("Supplements",      "vitamin D cancer remission NED complete"),
]

def reddit_search_public(subreddit: str, query: str, limit: int = 25) -> list[dict]:
    url = f"https://www.reddit.com/r/{subreddit}/search.json"
    params = {"q": query, "sort": "relevance", "limit": limit,
              "restrict_sr": "1", "t": "all"}
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=12)
        if r.status_code != 200:
            return []
        posts = r.json().get("data", {}).get("children", [])
        results = []
        for p in posts:
            d = p.get("data", {})
            results.append({
                "subreddit": d.get("subreddit", ""),
                "title": d.get("title", ""),
                "score": d.get("score", 0),
                "num_comments": d.get("num_comments", 0),
                "url": f"https://reddit.com{d.get('permalink', '')}",
                "selftext_preview": d.get("selftext", "")[:400].replace("\n", " "),
            })
        time.sleep(1.2)
        return results
    except Exception as e:
        print(f"  Reddit error r/{subreddit}: {e}")
        return []

def reddit_relevance(post: dict) -> bool:
    text = (post["title"] + " " + post["selftext_preview"]).lower()
    positive = ["remission", "ned", "healed", "cured", "cleared", "gone",
                "disappeared", "beat cancer", "no evidence", "complete response",
                "cancer free", "recovered", "regression"]
    personal = ["i ", "my ", "me ", "husband", "wife", "mother", "father",
                "dad", "mom", "sister", "brother", "friend", "she ", "he "]
    sun_vd   = ["vitamin d", "sun", "sunlight", "uv ", "ultraviolet", "light therapy",
                "melanin", "heliotherapy", "d3", "cholecalciferol"]
    return (any(t in text for t in positive) and
            any(t in text for t in personal) and
            any(t in text for t in sun_vd))


# ─────────────────────────────────────────────────────────────────────────────
# OPENALEX — citations of key papers (find related work)
# ─────────────────────────────────────────────────────────────────────────────

def openalex_citations(doi_or_pmid: str, label: str, max_results: int = 20) -> list[dict]:
    """Find papers that cite a key paper."""
    # Convert PMID to OpenAlex ID first
    r = requests.get(
        f"https://api.openalex.org/works",
        params={"filter": f"ids.pmid:{doi_or_pmid}", "select": "id,title"},
        headers=HEADERS, timeout=15,
    )
    results = r.json().get("results", [])
    if not results:
        return []
    oa_id = results[0]["id"].split("/")[-1]
    time.sleep(0.5)

    citing_r = requests.get(
        f"https://api.openalex.org/works",
        params={
            "filter": f"cites:{oa_id}",
            "sort": "cited_by_count:desc",
            "per-page": max_results,
            "select": "id,title,publication_year,type,cited_by_count,doi",
        },
        headers=HEADERS, timeout=15,
    )
    papers = citing_r.json().get("results", [])
    time.sleep(0.5)
    return [{
        "title": p.get("title", ""),
        "year": p.get("publication_year", ""),
        "citations": p.get("cited_by_count", 0),
        "type": p.get("type", ""),
        "doi": p.get("doi", ""),
        "url": p.get("doi", "") or f"https://openalex.org/{p.get('id','').split('/')[-1]}",
        "_citing": label,
    } for p in papers]


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def run():
    sections = []
    print("=" * 60)

    # ── 1. PubMed ──
    print("1. PubMed")
    pm_hits: dict[str, dict] = {}
    for (label, query) in PUBMED_QUERIES:
        print(f"   {label}")
        articles = pubmed_search(query, max_results=50)
        total = articles[0]["_total"] if articles else "0"
        print(f"   → {len(articles)} retrieved (total matching: {total})")
        for a in articles:
            pm_hits[a["pmid"]] = a

    # Fetch abstracts for all unique hits
    print(f"   Fetching abstracts for {len(pm_hits)} unique articles...")
    abstracts = {}
    pmid_list = list(pm_hits.keys())
    for i in range(0, len(pmid_list), 20):
        batch = pmid_list[i:i+20]
        abstracts.update(pubmed_fetch_abstracts(batch))

    pm_section = [f"## 1. PubMed — {len(pm_hits)} Unique Articles\n\n"
                  "_Filtered to: case reports, clinical trials, observational studies. "
                  "Queries targeted vitamin D/calcitriol/UV + cancer remission/regression/survival. "
                  "Hypercalcemia noise excluded._\n"]
    pm_sorted = sorted(pm_hits.values(), key=lambda x: x["year"], reverse=True)
    for a in pm_sorted:
        pt_str = ", ".join(a["pub_types"]) if a["pub_types"] else "—"
        abstract = textwrap.shorten(abstracts.get(a["pmid"], ""), 300, placeholder=" […]")
        pm_section.append(
            f"### {a['title']}\n"
            f"**{a['authors']}** | *{a['journal']}* | {a['year']} | {pt_str}  \n"
            f"[PubMed {a['pmid']}]({a['url']})\n\n"
            + (f"> {abstract}\n" if abstract else "") + "\n"
        )
    sections.append("\n".join(pm_section))

    # ── 2. Europe PMC ──
    print("\n2. Europe PMC")
    epmc_hits: dict[str, dict] = {}
    for (label, query) in EPMC_QUERIES:
        print(f"   {label}")
        articles = epmc_search(query)
        new = 0
        for a in articles:
            key = a["pmid"] or a["url"]
            if key and key not in pm_hits and key not in epmc_hits:
                epmc_hits[key] = a
                new += 1
        print(f"   → {len(articles)} retrieved, {new} new (not in PubMed results)")

    epmc_section = [f"## 2. Europe PMC — {len(epmc_hits)} Additional Articles\n"
                    "_Not already captured by PubMed queries._\n"]
    for a in sorted(epmc_hits.values(), key=lambda x: x["year"], reverse=True):
        pt_str = ", ".join(a["pub_types"]) if a["pub_types"] else "—"
        epmc_section.append(
            f"### {a['title']}\n"
            f"**{a['authors']}** | *{a['journal']}* | {a['year']} | {pt_str}  \n"
            f"[{a['url']}]({a['url']})\n\n"
            + (f"> {a['abstract_preview']}\n" if a["abstract_preview"] else "") + "\n"
        )
    sections.append("\n".join(epmc_section))

    # ── 3. Reddit ──
    print("\n3. Reddit (public API — limited; see upgrade notes in script)")
    reddit_hits: dict[str, dict] = {}
    for (sub, q) in REDDIT_SEARCHES:
        print(f"   r/{sub}: {q[:50]}")
        posts = reddit_search_public(sub, q)
        for p in posts:
            if reddit_relevance(p):
                reddit_hits[p["url"]] = p
    print(f"   → {len(reddit_hits)} relevant personal accounts found")

    reddit_section = [
        f"## 3. Reddit — {len(reddit_hits)} Personal Accounts\n\n"
        "_Public API is rate-limited to ~10 results/query. "
        "For exhaustive search: register a Reddit OAuth app (free) or use Arctic Shift "
        "(https://arctic-shift.photon-reddit.com) for full historical search._\n"
    ]
    for p in sorted(reddit_hits.values(), key=lambda x: x["score"], reverse=True):
        preview = p["selftext_preview"] or "(link post — click to read)"
        reddit_section.append(
            f"### r/{p['subreddit']}: {p['title']}\n"
            f"Score: {p['score']} | Comments: {p['num_comments']} | "
            f"[Link]({p['url']})\n\n"
            f"> {preview}\n\n"
        )
    sections.append("\n".join(reddit_section))

    # ── 4. OpenAlex citation tracking (key papers) ──
    print("\n4. OpenAlex — citation tracking for key case reports")
    KEY_PAPERS = [
        ("11349882", "Trouillas 2001: GBM complete regression with vitamin D analog"),
        ("8238086",  "Palmieri 1993: Parathyroid cancer long-term remission with calcitriol"),
        ("21883139", "Arlet 2012: CLL responsive to vitamin D"),
        ("7918050",  "Mellibovsky 1993: Chronic myelomonocytic leukemia remission with 25-OH D3"),
    ]
    oa_hits: list[dict] = []
    for (pmid, label) in KEY_PAPERS:
        print(f"   Finding papers citing PMID {pmid}: {label[:60]}")
        citing = openalex_citations(pmid, label, max_results=15)
        oa_hits.extend(citing)
        print(f"   → {len(citing)} citing papers found")

    oa_section = [f"## 4. OpenAlex — Citation Tracking\n\n"
                  "_Papers citing the key case reports found above. "
                  "Helps find follow-up studies, meta-analyses, and reviews that reference these cases._\n"]
    for p in sorted(oa_hits, key=lambda x: x["citations"], reverse=True):
        oa_section.append(
            f"- **{p['title']}** ({p['year']}) — {p['citations']} citations  \n"
            f"  *Cites:* {p['_citing']}  \n"
            f"  [{p['url']}]({p['url']})\n"
        )
    sections.append("\n".join(oa_section))

    # ── Write output ──
    header = (
        "# Heliotherapy / UV / Vitamin D → Cancer: Evidence Search\n\n"
        "_Auto-generated by `scripts/search_heliotherapy_evidence.py`_  \n"
        "_APIs: PubMed (NCBI Entrez), Europe PMC, Reddit (public), OpenAlex_  \n\n"
        "## Upgrade Path for More Exhaustive Coverage\n\n"
        "| Source | What you get | How to unlock |\n"
        "|---|---|---|\n"
        "| Reddit full search | All posts + comments, including deleted | "
        "Register OAuth app at reddit.com/prefs/apps, or use Arctic Shift |\n"
        "| Google Custom Search | Forum posts, blogs, news articles | "
        "Google Cloud Console → Custom Search API, 100 free/day |\n"
        "| YouTube Data API | Video testimonials | "
        "Google Cloud Console → YouTube Data API v3, free |\n"
        "| Semantic Scholar | Broader academic + citation graph | "
        "Free key: semanticscholar.org/product/api |\n"
        "| PubMed full text | Abstract + full text for open-access papers | "
        "Add `&rettype=full` in efetch, or use PMC API for OA papers |\n\n"
        "---\n\n"
    )
    OUT.write_text(header + "\n\n---\n\n".join(sections))

    print(f"\n{'='*60}")
    print(f"Done → {OUT}")
    print(f"  PubMed unique:     {len(pm_hits)}")
    print(f"  Europe PMC new:    {len(epmc_hits)}")
    print(f"  Reddit accounts:   {len(reddit_hits)}")
    print(f"  OpenAlex cites:    {len(oa_hits)}")

if __name__ == "__main__":
    run()
