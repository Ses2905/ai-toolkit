#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${HOME}/.cursor/plugins/local/prompt-kit"

mkdir -p "${HOME}/.cursor/plugins/local"
rm -rf "$DEST"
mkdir -p "$DEST"

if command -v rsync >/dev/null 2>&1; then
  rsync -a \
    --exclude '.git/' \
    --exclude 'agent-tools/' \
    --exclude '.DS_Store' \
    "$ROOT/" "$DEST/"
else
  tar -C "$ROOT" \
    --exclude '.git' \
    --exclude 'agent-tools' \
    --exclude '.DS_Store' \
    -cf - . | tar -C "$DEST" -xf -
fi

echo "Installed prompt-kit to ${DEST}"
echo
echo "Next:"
echo "  1. Command Palette → Developer: Reload Window"
echo "  2. Customize → filter User → confirm Prompt Kit"
echo "  3. Add prompts with /add-to-library (routes skills → Work Kit, prompts → Prompt Kit)"
