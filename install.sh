#!/usr/bin/env bash
# Coriaxu-skills install.sh
#
# Sync one or more skills from this repo's skills/ to the neutral skill hub:
#   ~/.agent/skills/
# Claude Code, Codex, and Gemini Antigravity keep compatibility through symlinks:
#   ~/.claude/skills -> ~/.agent/skills
#   ~/.codex/skills -> ~/.agent/skills
#   ~/.gemini/antigravity/skills -> ~/.agent/skills
#
# Usage:
#   ./install.sh                        # install ALL skills in this repo
#   ./install.sh yao-meta-skill         # install one skill
#   ./install.sh yao-meta-skill 三级笔记  # install multiple skills
#   ./install.sh --dry-run yao-meta-skill  # preview without writing
#   ./install.sh --list                 # list available skills
#   ./install.sh --help                 # show this help

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"
SKILL_HUB="$HOME/.agent/skills"

COMPAT_LINKS=(
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.gemini/antigravity/skills"
)

usage() {
  awk '/^$/{exit} NR>1 {sub(/^# ?/,""); print}' "$0"
}

list_available() {
  if [[ ! -d "$SKILLS_SRC" ]]; then
    echo "❌ $SKILLS_SRC not found"
    exit 1
  fi
  echo "Available skills in this repo:"
  find "$SKILLS_SRC" -mindepth 1 -maxdepth 1 -type d \
    -exec basename {} \; | sort | sed 's/^/  - /'
}

DRY_RUN=""
REQUESTED=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)      usage; exit 0 ;;
    --list)         list_available; exit 0 ;;
    --dry-run)      DRY_RUN="--dry-run"; shift ;;
    -*)             echo "❌ Unknown option: $1"; usage; exit 1 ;;
    *)              REQUESTED+=("$1"); shift ;;
  esac
done

if [[ ! -d "$SKILLS_SRC" ]]; then
  echo "❌ $SKILLS_SRC not found. Are you running this from the repo root?"
  exit 1
fi

# Build skill list
SKILL_LIST=()
if [[ ${#REQUESTED[@]} -eq 0 ]]; then
  while IFS= read -r -d '' d; do
    SKILL_LIST+=("$(basename "$d")")
  done < <(find "$SKILLS_SRC" -mindepth 1 -maxdepth 1 -type d -print0)
  echo "📦 Installing ALL ${#SKILL_LIST[@]} skills"
else
  for s in "${REQUESTED[@]}"; do
    if [[ ! -d "$SKILLS_SRC/$s" ]]; then
      echo "❌ skill '$s' not found in $SKILLS_SRC"
      echo
      list_available
      exit 1
    fi
    SKILL_LIST+=("$s")
  done
  echo "📦 Installing ${#SKILL_LIST[@]} skill(s): ${SKILL_LIST[*]}"
fi

if [[ -n "$DRY_RUN" ]]; then
  echo "🔍 DRY-RUN: no files will actually be written"
fi
echo

if [[ ${#SKILL_LIST[@]} -eq 0 ]]; then
  echo "⚠️  No skills to sync — nothing to do."
  exit 0
fi

if [[ -n "$DRY_RUN" ]]; then
  echo "→ Hub: $SKILL_HUB"
  for link in "${COMPAT_LINKS[@]}"; do
    echo "→ Compatibility link: $link -> $SKILL_HUB"
  done
else
  mkdir -p "$SKILL_HUB"
  for link in "${COMPAT_LINKS[@]}"; do
    parent="$(dirname "$link")"
    [[ -d "$parent" ]] || continue
    if [[ -L "$link" ]]; then
      current="$(readlink "$link")"
      if [[ "$current" != "$SKILL_HUB" ]]; then
        rm "$link"
        ln -s "$SKILL_HUB" "$link"
      fi
    elif [[ -e "$link" ]]; then
      backup="${link}.backup-$(date +%Y%m%d-%H%M%S)"
      mv "$link" "$backup"
      ln -s "$SKILL_HUB" "$link"
      echo "  backup: $backup"
    else
      ln -s "$SKILL_HUB" "$link"
    fi
  done
fi

echo "→ Target: $SKILL_HUB"
for skill in "${SKILL_LIST[@]}"; do
  rsync -a --delete --exclude='.git' --exclude='.DS_Store' $DRY_RUN \
    "$SKILLS_SRC/$skill/" \
    "$SKILL_HUB/$skill/"
  echo "  ✓ $skill"
done
echo

for link in "${COMPAT_LINKS[@]}"; do
  if [[ -L "$link" ]]; then
    echo "  link: $link -> $(readlink "$link")"
  elif [[ -e "$link" ]]; then
    echo "  link: $link is not a symlink"
  else
    echo "  link: $link missing"
  fi
done

echo "✅ Done. Restart Claude Code / Codex / Gemini Antigravity to pick up the new skill(s)."
