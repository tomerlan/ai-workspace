#!/usr/bin/env bash
# Extract oncology-relevant ideas from a book's reconstruct chunks. Edit BOOK_ID (and MODEL), then run:
#   ./scripts/run-oncology-extract.sh

BOOK_ID="Herrera_Melanin_the_Master_Molecule"
MODEL="gpt-5.2"

cd "$(dirname "$0")/.."
# Use venv Python so dotenv and other deps are available
.venv/bin/python3 scripts/oncology_extract.py --book "$BOOK_ID" --model "$MODEL"
