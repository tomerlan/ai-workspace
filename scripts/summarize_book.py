#!/usr/bin/env python3
"""
Produce a book-level summary from all reconstruction chunk JSONs for a given book.

Usage:
  python scripts/summarize_book.py Herrera_Melanin_the_Master_Molecule
  python scripts/summarize_book.py Herrera_Melanin_the_Master_Molecule --model gpt-4o

Reads: outputs/json/books/<book>*_reconstruct.json (sorted by page range).
Writes: outputs/books/<book>_book_summary.md
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import SUMMARIZE_MODEL
from src.io import get_openai_client, read_json, write_text, ensure_directory
from src.io.env import get_project_root


def _page_range_from_stem(stem: str) -> tuple[int, int]:
    """Parse '..._p79-123_reconstruct' -> (79, 123). Default (0, 0) if no match."""
    m = re.search(r"_p(\d+)-(\d+)_reconstruct$", stem)
    if m:
        return int(m.group(1)), int(m.group(2))
    return 0, 0


def load_reconstruct_jsons(root: Path, book_id: str) -> list[tuple[str, dict[str, Any]]]:
    """Load all *_reconstruct.json for this book; return list of (path_stem, data) sorted by page range."""
    pattern = root / "outputs" / "json" / "books" / f"{book_id}*_reconstruct.json"
    files = sorted(pattern.parent.glob(pattern.name))
    out = []
    for f in files:
        data = read_json(f)
        stem = f.stem
        out.append((stem, data))
    # Sort by (start_page, end_page)
    out.sort(key=lambda x: _page_range_from_stem(x[0]))
    return out


def build_book_summary_prompt(chunks: list[tuple[str, dict[str, Any]]]) -> str:
    """Build prompt that includes combined chunk data (claims, concepts, logical_flow) for synthesis."""
    parts = [
        "You have reconstruction data from chapter chunks of a single book. Each chunk has claims (with alignment to mainstream science), concepts, and logical flow.",
        "Produce ONE book-level summary that:",
        "1) Synthesizes the main thesis and overall argument across all chunks.",
        "2) Lists the most important claims (merge/rephrase as needed; note alignment).",
        "3) Key concepts and definitions.",
        "4) Overall logical flow of the argument.",
        "",
        "STYLE (STRICT): Write in DIRECT, declarative exposition. Do NOT describe the text or the author.",
        "Do NOT write: 'the book argues', 'the author claims', 'the text states', 'the book proposes', 'the book advances', 'the book then extends', 'is presented as', 'the book asserts', 'the book reframes'.",
        "DO write as if stating facts and claims directly: 'Melanin is proposed to...', 'Glucose is reframed as...', 'The mechanism implies...'.",
        "Output as Markdown only (no JSON). Use clear headings.",
        "",
        "--- CHUNK DATA ---",
        "",
    ]
    for stem, data in chunks:
        pages = data.get("pages", "?")
        parts.append(f"## Chunk: {stem} (pages {pages})")
        parts.append("")
        claims = data.get("claims") or []
        for c in claims[:30]:  # cap per chunk to avoid token explosion
            parts.append(f"- Claim: {c.get('claim', '')} [Alignment: {c.get('alignment', '')}]")
        if len(claims) > 30:
            parts.append(f"- ... and {len(claims) - 30} more claims")
        concepts = data.get("concepts") or []
        if concepts:
            parts.append("Concepts:")
            for co in concepts[:15]:
                parts.append(f"  - {co.get('term', '')}: {co.get('definition', '')[:200]}...")
        logical = data.get("logical_flow") or []
        if logical:
            parts.append("Logical flow:")
            for step in logical[:10]:
                parts.append(f"  - {step}")
        parts.append("")
    return "\n".join(parts)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/summarize_book.py <book_id> [--model MODEL]", file=sys.stderr)
        print("  book_id: e.g. Herrera_Melanin_the_Master_Molecule", file=sys.stderr)
        sys.exit(1)

    book_id = sys.argv[1]
    model = SUMMARIZE_MODEL
    if "--model" in sys.argv:
        i = sys.argv.index("--model")
        if i + 1 < len(sys.argv):
            model = sys.argv[i + 1]

    root = get_project_root()
    chunks = load_reconstruct_jsons(root, book_id)
    if not chunks:
        print(f"No reconstruct JSONs found for book_id={book_id!r}", file=sys.stderr)
        print(f"Looked in: {root / 'outputs' / 'json' / 'books' / (book_id + '*_reconstruct.json')}", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(chunks)} chunk(s) for {book_id}")

    client = get_openai_client(root)
    prompt = build_book_summary_prompt(chunks)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    content = response.choices[0].message.content or ""

    out_dir = root / "outputs" / "books"
    ensure_directory(out_dir)
    out_path = out_dir / f"{book_id}_book_summary.md"
    write_text(out_path, content)
    print(f"Saved book summary to {out_path}")


if __name__ == "__main__":
    main()
