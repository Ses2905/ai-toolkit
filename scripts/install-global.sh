#!/usr/bin/env bash
# Install Work Kit for every Cursor project on this machine, copy skills into
# ~/.cursor/skills, pull nested catalog packs that are not vendored here, and
# delete the project-local `npx skills add` leftover (.agents/, skills-lock.json).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

"$ROOT/scripts/install-local.sh"
"$ROOT/scripts/sync-user-skills.sh"

# Owl-Listener design-practice pack (111 nested skills). Not vendored in skills/.
"$ROOT/scripts/install-catalog-skills.sh" --preset designer-skills

# Playground / npx leftover — gitignored, not the plugin catalog.
rm -rf "$ROOT/.agents" "$ROOT/skills-lock.json"

echo
echo "Global install complete."
echo "  Plugin:  ${HOME}/.cursor/plugins/local/work-kit"
echo "  Skills:  ${HOME}/.cursor/skills"
echo "  Cleaned: .agents/ and skills-lock.json"
echo
echo "Next: Command Palette → Developer: Reload Window"
echo "Cloud Agents: Settings → Agents → Context and Tools → Sync Skills for Cloud Agents"
echo "Only ~/.cursor/skills/ syncs. Local plugins do not."
