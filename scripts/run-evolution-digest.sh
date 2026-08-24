#!/usr/bin/env bash
# Fetch Jack Kruse blog posts on cancer/evolution/life-history, then synthesize a digest.
#
#   ./scripts/run-evolution-digest.sh
#   ./scripts/run-evolution-digest.sh --no-fetch        # skip fetch, reuse existing JSON
#   MODEL=gpt-4o ./scripts/run-evolution-digest.sh
#   COOKIES=path/to/cookies.txt ./scripts/run-evolution-digest.sh

set -e
cd "$(dirname "$0")/.."

COOKIES="${COOKIES:-cookies.txt}"
MODEL="${MODEL:-gpt-5.2}"
OUT="outputs/evolution"

if [[ "$1" != "--no-fetch" ]]; then
    echo "=== Fetching posts ==="
    .venv/bin/python3 scripts/fetch_kruse_evolution.py --cookies "$COOKIES" --out "$OUT"
    echo
fi

echo "=== Building digest ==="
.venv/bin/python3 scripts/evolution_cancer_digest.py \
    --input "$OUT/raw/kruse_evolution_raw.json" \
    --output "$OUT/evolution_cancer_digest.md" \
    --model "$MODEL"

echo
echo "Digest: $OUT/evolution_cancer_digest.md"
