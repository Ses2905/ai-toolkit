#!/usr/bin/env bash
# Install Work Kit for every Cursor project on this machine, copy skills into
# ~/.cursor/skills, pull nested catalog packs that are not vendored here, and
# delete the project-local `npx skills add` leftover (.agents/, skills-lock.json).
#
# Run from a Work Kit checkout:
#   bash scripts/install-global.sh
set -euo pipefail

if [[ -n "${BASH_SOURCE[0]:-}" ]]; then
  ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
else
  ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fi
cd "$ROOT"

if [[ ! -f "$ROOT/scripts/install-local.sh" || ! -d "$ROOT/skills" ]]; then
  echo "install-global.sh must run from a Work Kit checkout (the repo that contains scripts/install-local.sh and skills/)." >&2
  echo "Current directory: $(pwd)" >&2
  echo >&2
  echo "If this file is missing, you are probably on main. Get the branch that added it:" >&2
  echo "  git fetch origin cursor/ppt-visual-skill-e4e5 && git checkout cursor/ppt-visual-skill-e4e5" >&2
  echo "  bash scripts/install-global.sh" >&2
  exit 1
fi

chmod +x "$ROOT/scripts/install-local.sh" \
  "$ROOT/scripts/sync-user-skills.sh" \
  "$ROOT/scripts/install-catalog-skills.sh" \
  "$ROOT/scripts/install-global.sh" 2>/dev/null || true

echo "==> 1/4  Install local Work Kit plugin"
bash "$ROOT/scripts/install-local.sh"

echo
echo "==> 2/4  Copy vendored skills to ~/.cursor/skills"
bash "$ROOT/scripts/sync-user-skills.sh"

echo
echo "==> 3/4  Install Owl-Listener designer-skills pack"
if ! bash "$ROOT/scripts/install-catalog-skills.sh" --preset designer-skills; then
  echo "warning: designer-skills catalog install failed; Work Kit plugin + vendored skills are still installed." >&2
fi

echo
echo "==> 4/4  Remove project-local npx leftover"
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
