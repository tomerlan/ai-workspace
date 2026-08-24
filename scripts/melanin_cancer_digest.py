#!/usr/bin/env python3
"""
Build a melanin-and-cancer digest from three melanin docs + web context using GPT-5.2 (or --model).

Usage:
  python scripts/melanin_cancer_digest.py
  python scripts/melanin_cancer_digest.py --model gpt-5.2
  python scripts/melanin_cancer_digest.py -o outputs/melanin_cancer_digest.md

Reads: docs/herrera_melanin.md, docs/kruse_melanin.md, docs/mainstream_melanin.md
Writes: docs/melanin_cancer_digest.md (or -o path)
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import DIGEST_DEFAULT_MODEL
from src.io import get_openai_client, write_text
from src.io.env import get_project_root


# Web / current mainstream context (melanin and cancer) — inject into prompt so the digest is informed by recent consensus.
WEB_CONTEXT = """
## Web / current mainstream context (melanin and cancer)

- **Photoprotection:** Melanin is the skin's primary defense against UV: broadband absorption, reduced UV penetration to nuclei, antioxidant/radical scavenging. Darker skin correlates with lower skin cancer incidence; MC1R regulates eumelanin (more photoprotective) vs pheomelanin (less so).
- **Paradox:** ~80% of UV-induced melanoma mutations show UV-signature damage (C→T). Melanin distribution matters: in some studies, tanned skin with more melanin showed greater UV-induced DNA damage and free radicals than lighter skin.
- **Melanin chemiexcitation:** In melanoma, NOS/NOX generate reactive species that react with melanin → peroxynitrite → melanin "chemiexcitation" → carcinogenic carbonyl species and UV-like DNA damage without UV, potentially driving initiation, progression, and drug resistance. Exogenous (UV, pollutants) and endogenous stress can amplify oxidative stress from melanin synthesis and drive malignant transformation.
"""


MELANIN_DOCS = [
    "herrera_melanin.md",
    "kruse_melanin.md",
    "mainstream_melanin.md",
]


def load_docs(root: Path) -> dict[str, str]:
    docs_dir = root / "docs"
    out = {}
    for name in MELANIN_DOCS:
        path = docs_dir / name
        if not path.exists():
            raise FileNotFoundError(f"Missing: {path}")
        out[name] = path.read_text(encoding="utf-8")
    return out


def build_prompt(docs: dict[str, str]) -> str:
    parts = [
        "You are writing a **Melanin and Cancer Digest**: a single, synthesized markdown document that summarizes and compares how melanin relates to cancer across three distinct sources plus current web/mainstream context.",
        "",
        "SOURCES:",
        "1. **Herrera (Melanin: The Master Molecule)** — alternative bioenergetics; melanin as primary energy transducer via water splitting (Human Photosynthesis®); mainstream rejects the core mechanism but agrees melanin provides photoprotection and reduces skin cancer risk.",
        "2. **Kruse** — melanin as quantum/light interface, circadian and redox; cancer as redox collapse and mitochondrial failure; artificial light and circadian mismatch as drivers; distinguishes UV DNA damage vs systemic mitochondrial dysfunction.",
        "3. **Mainstream melanin biology** — chemistry, photoprotection, eumelanin vs pheomelanin, MC1R, skin cancer epidemiology, melanin chemiexcitation in melanoma, neuromelanin.",
        "4. **Web context** (below) — current consensus on photoprotection, paradox, and melanin chemiexcitation in melanoma.",
        "",
        "TASK: Produce one cohesive digest that:",
        "- Explains the **mainstream** view of melanin and cancer (photoprotection, skin cancer risk by skin type, pheomelanin vs eumelanin, chemiexcitation in melanoma).",
        "- Summarizes how **Herrera** and **Kruse** each frame melanin and cancer (and where they agree or disagree with mainstream).",
        "- Highlights **contrasts**: e.g. energy source (water-splitting vs glucose/ATP), cause of cancer (redox/circadian vs UV/mutation), and therapeutic implications.",
        "- Keeps a neutral, accurate tone; label clearly what is mainstream vs alternative/speculative.",
        "",
        "STYLE: Clear headings, short paragraphs, bullet points where useful. Markdown only. No invented references.",
        "",
        "--- SOURCE TEXTS ---",
        "",
    ]
    for name in MELANIN_DOCS:
        parts.append(f"### {name}")
        parts.append("")
        parts.append(docs[name])
        parts.append("")
        parts.append("---")
        parts.append("")
    parts.append("### Web context (for current consensus)")
    parts.append("")
    parts.append(WEB_CONTEXT.strip())
    return "\n".join(parts)


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Build melanin-and-cancer digest from three melanin docs + API + web context.")
    parser.add_argument("-m", "--model", default=DIGEST_DEFAULT_MODEL, help="Model name (e.g. gpt-5.2)")
    parser.add_argument("-o", "--output", default=None, help="Output path (default: docs/melanin_cancer_digest.md)")
    args = parser.parse_args()

    root = get_project_root()
    out_path = Path(args.output) if args.output else root / "docs" / "melanin_cancer_digest.md"
    out_path = out_path if out_path.is_absolute() else root / out_path

    print("Loading the three melanin docs...")
    docs = load_docs(root)
    print("Building prompt and calling API...")
    prompt = build_prompt(docs)

    client = get_openai_client(root)
    response = client.chat.completions.create(
        model=args.model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    content = response.choices[0].message.content or ""

    write_text(out_path, content)
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
