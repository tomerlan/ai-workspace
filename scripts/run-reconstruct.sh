#!/usr/bin/env bash
# Reconstruct a chapter: edit PDF path and page numbers below, then either:
#   ./scripts/run-reconstruct.sh
# or copy-paste the one-liner (after editing) into your terminal.

# One-liner (edit path, numbers, model, then copy-paste):
# python3 scripts/reconstruct.py data/books/Herrera_Melanin_the_Master_Molecule.pdf 129 149 --model gpt-4o

# PDF path: set this to where your PDF actually is (relative to project root or full path).
# Example: "/Users/you/Desktop/Herrera_Melanin_the_Master_Molecule.pdf" or "data/books/Book.pdf"
PDF="data/books/Herrera_Melanin_the_Master_Molecule.pdf"

# Page range (inclusive: start and end page of the chapter)
START_PAGE=264
END_PAGE=304

# Model (e.g. gpt-4o, gpt-4o-mini)
MODEL="gpt-5.2"

cd "$(dirname "$0")/.."
if [ ! -f "$PDF" ]; then
  echo "PDF not found: $PDF"
  echo "Edit the PDF path at the top of this script to point to your file."
  exit 1
fi
.venv/bin/python3 scripts/reconstruct.py "$PDF" "$START_PAGE" "$END_PAGE" --model "$MODEL"
