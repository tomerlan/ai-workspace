#!/usr/bin/env bash
# Push one .md file to one Notion page. You choose both every time.
# Usage: ./scripts/push-one.sh <path/to/file.md> <NOTION_PAGE_ID>
# Get NOTION_PAGE_ID from the Notion page URL (the 32-char id at the end).
set -e
cd "$(dirname "$0")/.."
.venv/bin/python3 scripts/push_to_notion.py "$1" "$2"
