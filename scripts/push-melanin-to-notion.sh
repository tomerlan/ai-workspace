#!/usr/bin/env bash
# Push all 4 melanin docs to the same Notion page (as sub-pages under it).
# Usage: ./scripts/push-melanin-to-notion.sh <MELANIN_PAGE_ID>
# Get MELANIN_PAGE_ID from the Notion page URL (32-char id). Ensure the page is connected to your integration.
set -e
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
.venv/bin/python3 scripts/push_to_notion.py --parent-id "$1" \
  "$ROOT/docs/herrera_melanin.md" \
  "$ROOT/docs/kruse_melanin.md" \
  "$ROOT/docs/mainstream_melanin.md" \
  "$ROOT/docs/melanin_cancer_digest.md"
