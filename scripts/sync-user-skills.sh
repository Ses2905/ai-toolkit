#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${ROOT}/skills"
DEST="${HOME}/.cursor/skills"

if [[ ! -d "$SRC" ]]; then
  echo "No skills/ directory at ${SRC}" >&2
  exit 1
fi

mkdir -p "$DEST"

copied=0
for skill_dir in "$SRC"/*; do
  [[ -d "$skill_dir" && -f "$skill_dir/SKILL.md" ]] || continue
  name="$(basename "$skill_dir")"
  rm -rf "${DEST}/${name}"
  cp -R "$skill_dir" "${DEST}/${name}"
  copied=$((copied + 1))
  echo "Copied ${name} → ${DEST}/${name}"
done

echo
echo "Copied ${copied} skill(s) to ${DEST}"
echo "Enable Settings → Agents → Context and Tools → Sync Skills for Cloud Agents"
echo "Only ~/.cursor/skills/ syncs. Local plugins do not."
