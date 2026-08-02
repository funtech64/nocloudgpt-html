#!/usr/bin/env bash
# Copy exact Phase 4A P4-Public-Catalog from terminal-glass/8-ball.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
SRC="${1:?Usage: $0 /path/to/terminal-glass/8-ball/P4-Public-Catalog}"
DEST="$ROOT/models/data/P4-Public-Catalog"

if [[ ! -f "$SRC/manifest.json" ]]; then
  echo "manifest.json not found in $SRC" >&2
  exit 1
fi

rm -rf "$DEST"
mkdir -p "$DEST"
cp -a "$SRC/." "$DEST/"

echo "Pinned authoritative catalog from $SRC"
echo "Run: npm run build && npm test"
