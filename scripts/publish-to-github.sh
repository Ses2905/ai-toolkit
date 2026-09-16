#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

URL="https://github.com/Ses2905/cursor-skills.git"
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
TOKEN="${GH_TOKEN:-${GITHUB_TOKEN:-}}"

if git remote get-url github >/dev/null 2>&1; then
  git remote set-url github "$URL"
else
  git remote add github "$URL"
fi

echo "Publishing ${BRANCH} → ${URL}"

export GIT_TERMINAL_PROMPT=0

if [[ -n "$TOKEN" ]]; then
  git push "https://x-access-token:${TOKEN}@github.com/Ses2905/cursor-skills.git" \
    "HEAD:refs/heads/${BRANCH}"
else
  git push -u github "HEAD:refs/heads/${BRANCH}"
fi

echo
echo "Published. On desktop, install into the Cursor skill library with:"
echo "  git clone ${URL}"
echo "  cd cursor-skills && ./scripts/install-local.sh && ./scripts/sync-user-skills.sh"
echo "Then enable Settings → Agents → Context and Tools → Sync Skills for Cloud Agents."
