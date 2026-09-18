#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOCAL="${HOME}/.cursor/plugins/local"
WORK_DEST="${LOCAL}/work-kit"
PROMPT_DEST="${LOCAL}/prompt-kit"

mkdir -p "${LOCAL}"

install_tree() {
  local src="$1"
  local dest="$2"
  shift 2
  rm -rf "$dest"
  mkdir -p "$dest"
  extra_excludes=("$@")
  if command -v rsync >/dev/null 2>&1; then
    rsync -a \
      --exclude '.git/' \
      --exclude 'agent-tools/' \
      --exclude '.DS_Store' \
      --exclude '.agents/' \
      --exclude 'skills-lock.json' \
      "${extra_excludes[@]}" \
      "$src/" "$dest/"
  else
    tar_excludes=(
      --exclude '.git'
      --exclude 'agent-tools'
      --exclude '.DS_Store'
      --exclude '.agents'
      --exclude 'skills-lock.json'
    )
    # Convert rsync --exclude=foo / --exclude foo into tar --exclude foo
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --exclude=*)
          tar_excludes+=(--exclude "${1#--exclude=}")
          shift
          ;;
        --exclude)
          tar_excludes+=(--exclude "$2")
          shift 2
          ;;
        *)
          die_unknown="$1"
          echo "error: unknown install_tree arg: $die_unknown" >&2
          return 1
          ;;
      esac
    done
    tar -C "$src" "${tar_excludes[@]}" -cf - . | tar -C "$dest" -xf -
  fi
}

# Work Kit = repo root minus the prompt library subtree (Prompt Kit is separate)
install_tree "$ROOT" "$WORK_DEST" --exclude=prompts
# Belt-and-suspenders: never ship Prompt Kit inside Work Kit, even if tar/rsync miss the exclude.
rm -rf "${WORK_DEST}/prompts"
echo "Installed work-kit to ${WORK_DEST}"

# Prompt Kit = prompts/ (own plugin.json)
if [[ -f "${ROOT}/prompts/.cursor-plugin/plugin.json" ]]; then
  install_tree "${ROOT}/prompts" "$PROMPT_DEST"
  echo "Installed prompt-kit to ${PROMPT_DEST}"
else
  echo "warning: prompts/.cursor-plugin/plugin.json missing; skipped prompt-kit" >&2
fi

echo
echo "Next:"
echo "  1. Command Palette → Developer: Reload Window"
echo "  2. Customize → filter User → confirm Work Kit + Prompt Kit"
echo "  3. Add items with /add-to-library (or ./scripts/library-add.py)"
echo "  4. Optional for Cloud Agents: ./scripts/sync-user-skills.sh"
