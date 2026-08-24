#!/usr/bin/env bash
# Book summary from all reconstruct chunk JSONs. Edit BOOK_ID (and optionally MODEL), then run:
#   ./scripts/run-summarize-book.sh
# Or copy-paste:
#   python3 scripts/summarize_book.py Herrera_Melanin_the_Master_Molecule --model gpt-4o

BOOK_ID="Herrera_Melanin_the_Master_Molecule"
MODEL="gpt-5.2"

cd "$(dirname "$0")/.."
.venv/bin/python3 scripts/summarize_book.py "$BOOK_ID" --model "$MODEL"
