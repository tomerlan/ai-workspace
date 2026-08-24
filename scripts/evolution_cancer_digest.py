#!/usr/bin/env python3
"""
Synthesize a digest of Jack Kruse's cancer thesis through the lens of evolution
and life-history theory, using posts scraped by fetch_kruse_evolution.py.

Usage:
    python3 scripts/evolution_cancer_digest.py
    python3 scripts/evolution_cancer_digest.py --input outputs/evolution/raw/kruse_evolution_raw.json
    python3 scripts/evolution_cancer_digest.py --model gpt-4o --max-posts 20 --max-chars 4000
    python3 scripts/evolution_cancer_digest.py -o outputs/evolution/digest.md
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.io import get_openai_client, write_text
from src.io.env import get_project_root
from src.config import DIGEST_DEFAULT_MODEL

DEFAULT_INPUT  = "outputs/evolution/raw/kruse_evolution_raw.json"
DEFAULT_OUTPUT = "outputs/evolution/evolution_cancer_digest.md"

# Themes that define this angle of Kruse's work — used for framing the prompt.
SYNTHESIS_FRAME = """
Jack Kruse's cancer framework, viewed through evolution and life history:

- **Atavism hypothesis**: cancer as reversion to ancient unicellular metabolic programs
  (cf. Warburg effect as metabolic atavism — aerobic glycolysis as ancestral default).
- **Mitochondrial theory**: mitochondrial dysfunction as the primary driver, not somatic
  mutation; cancer as a breakdown of eukaryotic energy sovereignty.
- **Life-history tradeoffs**: cancer as a cell-level shift toward fast proliferation (r-strategy)
  at the expense of somatic maintenance; driven by environmental signals of scarcity/threat.
- **Environmental mismatch**: modern light environment (nnEMF, artificial light, blue-light
  excess, loss of solar spectrum) disrupts circadian/quantum signaling that evolution tuned
  to suppress oncogenesis.
- **Epigenetic/quantum coherence**: loss of quantum coherence in mitochondrial water/proton
  gradients as an evolutionary regression that enables malignant transformation.
- **Redox collapse**: chronic oxidative stress from evolutionary mismatches erodes the redox
  gradients that maintain differentiated cell identity.
"""


def load_posts(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def select_posts(posts, max_posts, max_chars, post_ids=None):
    """Take specific post IDs (if given) or top N by relevance score, truncate each to max_chars."""
    if post_ids:
        id_set = set(post_ids)
        selected = [p for p in posts if p.get("post_id") in id_set]
    else:
        selected = sorted(posts, key=lambda p: p.get("relevance_score", 0), reverse=True)[:max_posts]
    out = []
    for p in selected:
        p = dict(p)
        if max_chars and len(p.get("text", "")) > max_chars:
            p["text"] = p["text"][:max_chars] + "\n[… truncated …]"
        out.append(p)
    return out


def build_prompt(posts: list[dict]) -> str:
    corpus_parts = []
    for i, p in enumerate(posts, 1):
        header = f"### Post {i}: {p['title']} ({p['date']})\nURL: {p['url']}\n"
        corpus_parts.append(header + "\n" + p.get("text", ""))

    corpus = "\n\n---\n\n".join(corpus_parts)

    return f"""You are synthesizing a research digest titled:
**"Cancer Through the Lens of Evolution and Life History: Jack Kruse's Framework"**

## Background framing
{SYNTHESIS_FRAME.strip()}

## Your task
Read the blog post excerpts below and produce a single, well-structured Markdown document that:

1. **Opens with Kruse's core thesis** — what is his central claim about cancer as an
   evolutionary/life-history phenomenon? State it plainly, including how it departs from
   mainstream oncology.

2. **Unpacks the key mechanisms** Kruse invokes:
   - Atavism / metabolic regression (Warburg, aerobic glycolysis)
   - Mitochondrial dysfunction as the upstream driver
   - Life-history tradeoffs at the cellular level (r vs K, somatic maintenance)
   - Quantum biology / coherence loss
   - Environmental mismatch (light, nnEMF, circadian disruption)

3. **Explains the evolutionary logic** — why does evolution produce organisms vulnerable
   to these failure modes? How does Kruse frame the selection pressures involved?

4. **Notes his proposed interventions** (if present in the posts) — what does Kruse say
   corrects the evolutionary mismatch?

5. **Flags what is speculative vs. what connects to mainstream evolutionary oncology**
   (e.g. somatic evolution theory, atavism hypothesis of Davies/Lineweaver, life-history
   tradeoff models of cancer).

## Style
- Clear H2/H3 headings, short paragraphs, bullet points where useful.
- Neutral, accurate tone. Label clearly what is Kruse's claim vs. mainstream consensus.
- Markdown only. Do not invent references or URLs.
- Length: thorough but tight — aim for 1500–2500 words.
- **Define every non-standard term on first use** — this includes jargon from evolutionary
  biology (e.g. r/K selection), biophysics (e.g. biophotons, EZ water, proton motive force),
  biochemistry (e.g. pseudohypoxia, heteroplasmy, NAD+/NADH ratio), and Kruse-specific
  concepts. A reader with a general science background but no specialist knowledge should
  be able to follow the entire document without external references.

## Source posts
{corpus}
"""


def main():
    parser = argparse.ArgumentParser(
        description="Synthesize Kruse's cancer/evolution thesis from scraped blog posts."
    )
    parser.add_argument("-i", "--input",     default=DEFAULT_INPUT,
                        help="Path to kruse_evolution_raw.json")
    parser.add_argument("-o", "--output",    default=DEFAULT_OUTPUT,
                        help="Output markdown path")
    parser.add_argument("-m", "--model",     default=DIGEST_DEFAULT_MODEL)
    parser.add_argument("--max-posts",  type=int, default=25,
                        help="Max posts to include (by relevance score, default: 25)")
    parser.add_argument("--max-chars",  type=int, default=5000,
                        help="Max characters per post (default: 5000, 0 = no limit)")
    parser.add_argument("--post-ids", default=None,
                        help="Comma-separated post IDs to use instead of top-N scoring")
    args = parser.parse_args()

    root      = get_project_root()
    in_path   = Path(args.input) if Path(args.input).is_absolute() else root / args.input
    out_path  = Path(args.output) if Path(args.output).is_absolute() else root / args.output

    if not in_path.exists():
        print(f"ERROR: input file not found: {in_path}")
        print("Run fetch_kruse_evolution.py first.")
        raise SystemExit(1)

    post_ids = [int(x.strip()) for x in args.post_ids.split(",")] if args.post_ids else None
    max_chars = args.max_chars if args.max_chars > 0 else None

    print(f"Loading posts from {in_path} ...")
    all_posts = load_posts(in_path)
    print(f"  {len(all_posts)} posts loaded.")

    posts = select_posts(all_posts, args.max_posts, max_chars, post_ids=post_ids)
    label = f"IDs {post_ids}" if post_ids else f"top {len(posts)} by relevance score"
    print(f"  Using {label}.\n")

    prompt = build_prompt(posts)
    print(f"Prompt length: ~{len(prompt):,} chars")
    print(f"Calling {args.model} ...")

    client   = get_openai_client(root)
    response = client.chat.completions.create(
        model=args.model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    content = response.choices[0].message.content or ""

    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_text(out_path, content)
    print(f"\nWrote digest: {out_path}")


if __name__ == "__main__":
    main()
