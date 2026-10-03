#!/usr/bin/env bash
# Copy every vendored skill (skills/*/SKILL.md) into Claude Code's user skills
# directory so it is available in every project. Only touches the skill folders
# it copies; anything else in the destination (e.g. synced account skills) is
# left alone.
#
#   bash scripts/install-claude.sh                      # → ~/.claude/skills
#   CLAUDE_SKILLS_DIR=.claude/skills bash scripts/install-claude.sh   # project-local
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${ROOT}/skills"
DEST="${CLAUDE_SKILLS_DIR:-${HOME}/.claude/skills}"

if [[ ! -d "$SRC" ]]; then
  echo "No skills/ directory at ${SRC}" >&2
  exit 1
fi

mkdir -p "$DEST"

copied=0
for skill_dir in "$SRC"/*; do
  [[ -d "$skill_dir" && -f "$skill_dir/SKILL.md" ]] || continue
  name="$(basename "$skill_dir")"
  rm -rf "${DEST:?}/${name}"
  cp -R "$skill_dir" "${DEST}/${name}"
  copied=$((copied + 1))
done

echo "Copied ${copied} skill(s) to ${DEST}"
echo "Claude Code: restart the session (or run /skills) to pick them up."
echo "claude.ai / Desktop: skills are uploaded per skill (Settings → Capabilities → Skills); this script does not cover that."
