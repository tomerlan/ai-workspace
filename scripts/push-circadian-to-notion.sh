#!/usr/bin/env bash
# Push the 4 circadian knowledge-base chapters to Notion.
# Usage: ./scripts/push-circadian-to-notion.sh
# Target page must be connected to your integration (same as melanin push).
set -e
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
.venv/bin/python3 scripts/push_to_notion.py --parent-id 308fe132d7738175b629e7bbff074e12 \
  "$ROOT/docs/circadian_primer.md" \
  "$ROOT/docs/circadian_theory.md" \
  "$ROOT/docs/circadian_evidence.md" \
  "$ROOT/docs/circadian_measurements_tracking.md" \
  "$ROOT/docs/circadian_interventions.md" \
  "$ROOT/docs/circadian_protocol.md" \
  "$ROOT/docs/circadian_experts.md"
