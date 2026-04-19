#!/usr/bin/env bash
# Coriaxu-skills install.sh
# Sync every skill under ./skills/ to the three local skill directories.
#
# Safe by design:
# - Only syncs skills that exist in this repo's skills/ directory
# - Never touches unrelated skills already in target directories
# - Uses per-skill rsync --delete so updates to a repo skill replace its target
#
# Usage:  ./install.sh            (sync all three targets)
#         ./install.sh --dry-run  (preview without writing)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"

TARGETS=(
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.gemini/antigravity/skills"
)

DRY_RUN=""
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN="--dry-run"
  echo "🔍 DRY-RUN mode: no files will actually be written"
fi

if [[ ! -d "$SKILLS_SRC" ]]; then
  echo "❌ $SKILLS_SRC not found. Are you running this from the repo root?"
  exit 1
fi

SKILL_LIST=()
while IFS= read -r -d '' d; do
  SKILL_LIST+=("$(basename "$d")")
done < <(find "$SKILLS_SRC" -mindepth 1 -maxdepth 1 -type d -print0)

if [[ ${#SKILL_LIST[@]} -eq 0 ]]; then
  echo "⚠️  No skills found under $SKILLS_SRC — nothing to sync."
  exit 0
fi

echo "📦 Found ${#SKILL_LIST[@]} skills in repo: ${SKILL_LIST[*]}"
echo

for target in "${TARGETS[@]}"; do
  if [[ ! -d "$(dirname "$target")" ]]; then
    echo "⏭  Skipping $target (parent directory missing — not installed?)"
    continue
  fi
  mkdir -p "$target"
  echo "→ Syncing to $target"
  for skill in "${SKILL_LIST[@]}"; do
    rsync -a --delete $DRY_RUN \
      "$SKILLS_SRC/$skill/" \
      "$target/$skill/"
    echo "  ✓ $skill"
  done
  echo
done

echo "✅ Done. Restart Claude Code / Codex / Gemini to pick up new skills."
