#!/usr/bin/env bash
# Build melanin-and-cancer digest from docs/herrera_melanin.md, kruse_melanin.md, mainstream_melanin.md
# using GPT-5.2 (or set MODEL) and embedded web context.
#
#   ./scripts/run-digest.sh
#   MODEL=gpt-4o ./scripts/run-digest.sh
#   ./scripts/run-digest.sh -o outputs/melanin_cancer_digest.md

cd "$(dirname "$0")/.."
MODEL="${MODEL:-gpt-5.2}"
.venv/bin/python3 scripts/melanin_cancer_digest.py --model "$MODEL" "$@"
