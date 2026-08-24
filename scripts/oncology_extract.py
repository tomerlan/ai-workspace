#!/usr/bin/env python3
"""
Extract ideas from a book's reconstruction chunks that are relevant to oncology.

Usage:
  python scripts/oncology_extract.py --book Herrera_Melanin_the_Master_Molecule
  python scripts/oncology_extract.py --book Herrera_Melanin_the_Master_Molecule --model gpt-4o
  python scripts/oncology_extract.py -b Other_Book_Id

Reads: outputs/books/raw/<book>*_reconstruct.json (sorted by page range).
Writes: outputs/books/<book>_oncology.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import SUMMARIZE_MODEL
from src.io import get_openai_client, read_json, write_text, ensure_directory
from src.io.env import get_project_root


def _page_range_from_stem(stem: str) -> tuple[int, int]:
    m = re.search(r"_p(\d+)-(\d+)_reconstruct$", stem)
    if m:
        return int(m.group(1)), int(m.group(2))
    return 0, 0


def load_reconstruct_jsons(root: Path, book_id: str) -> list[tuple[str, dict[str, Any]]]:
    pattern = root / "outputs" / "json" / "books" / f"{book_id}*_reconstruct.json"
    files = sorted(pattern.parent.glob(pattern.name))
    out = [(f.stem, read_json(f)) for f in files]
    out.sort(key=lambda x: _page_range_from_stem(x[0]))
    return out


def build_oncology_prompt(chunks: list[tuple[str, dict[str, Any]]]) -> str:
    parts = [
        "You have reconstruction data from chapter chunks of a single book (claims with alignment to mainstream science, concepts, logical flow).",
        "",
        "TASK: Extract and list ONLY ideas that are relevant to oncology: cancer biology, carcinogenesis, tumor metabolism, cancer treatment, cancer risk/protection, or any claim/concept that clearly applies to cancer or oncology. Include alignment labels (Supported / Partially supported / Contested / Speculative / Contradicted) where given.",
        "",
        "If there are no or very few oncology-relevant ideas, say so clearly in one short paragraph and do not invent any.",
        "",
        "STYLE: Direct, declarative. Do NOT write 'the book argues' or 'the author claims'. State claims and concepts directly.",
        "Output as Markdown only. Use clear headings.",
        "",
        "--- CHUNK DATA ---",
        "",
    ]
    for stem, data in chunks:
        pages = data.get("pages", "?")
        parts.append(f"## Chunk: {stem} (pages {pages})")
        parts.append("")
        for c in (data.get("claims") or [])[:35]:
            parts.append(f"- Claim: {c.get('claim', '')} [Alignment: {c.get('alignment', '')}]")
        concepts = data.get("concepts") or []
        if concepts:
            for co in concepts[:15]:
                parts.append(f"- Concept: {co.get('term', '')} — {(co.get('definition') or '')[:180]}")
        parts.append("")
    return "\n".join(parts)


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Extract oncology-relevant ideas from a book's reconstruct chunks.")
    parser.add_argument("-b", "--book", required=True, help="Book ID (e.g. Herrera_Melanin_the_Master_Molecule)")
    parser.add_argument("-m", "--model", default=SUMMARIZE_MODEL, help="Model name (e.g. gpt-4o, gpt-5.2)")
    args = parser.parse_args()
    book_id = args.book
    model = args.model

    root = get_project_root()
    chunks = load_reconstruct_jsons(root, book_id)
    if not chunks:
        print(f"No reconstruct JSONs found for book_id={book_id!r}", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(chunks)} chunk(s) for {book_id}; extracting oncology-relevant ideas...")

    client = get_openai_client(root)
    prompt = build_oncology_prompt(chunks)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    content = response.choices[0].message.content or ""

    out_dir = root / "outputs" / "books"
    ensure_directory(out_dir)
    out_path = out_dir / f"{book_id}_oncology.md"
    write_text(out_path, content)
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
