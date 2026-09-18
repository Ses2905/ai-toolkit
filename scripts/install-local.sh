#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${HOME}/.cursor/plugins/local/work-kit"

mkdir -p "${HOME}/.cursor/plugins/local"
rm -rf "$DEST"
mkdir -p "$DEST"

if command -v rsync >/dev/null 2>&1; then
  rsync -a \
    --exclude '.git/' \
    --exclude 'agent-tools/' \
    --exclude '.DS_Store' \
    --exclude '.agents/' \
    --exclude 'skills-lock.json' \
    --exclude 'prompts/' \
    "$ROOT/" "$DEST/"
else
  tar -C "$ROOT" \
    --exclude '.git' \
    --exclude 'agent-tools' \
    --exclude '.DS_Store' \
    --exclude '.agents' \
    --exclude 'skills-lock.json' \
    --exclude 'prompts' \
    -cf - . | tar -C "$DEST" -xf -
fi

echo "Installed work-kit to ${DEST}"
echo
echo "Next:"
echo "  1. Command Palette → Developer: Reload Window"
echo "  2. Customize → filter User → confirm Work Kit"
echo "  3. Prompt Kit is a separate plugin: ./prompts/scripts/install-local.sh"
echo "  4. Optional for Cloud Agents: ./scripts/sync-user-skills.sh"
