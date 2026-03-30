#!/bin/bash
# PreToolUse hook (Edit|Write):
# 1. Blocks edits to the main repo (lusena-dawn/) when running from a worktree
# 2. Warns when editing a Dawn original file that has a lusena-* counterpart

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('file_path', ''))
except:
    pass
" 2>/dev/null)

# --- Guard 1: Block main-repo edits from worktrees ---
CWD=$(pwd)
if [[ "$CWD" == *"lusena-worktrees"* ]] && [[ "$FILE_PATH" == *"lusena-dawn"* ]]; then
  echo "BLOCKED: You are in a worktree but targeting a file in the main repo (lusena-dawn/). Use your worktree path instead. Every file exists in your worktree — use relative paths or your worktree absolute path." >&2
  exit 2
fi

# --- Guard 2: Block Dawn originals when lusena-* override exists ---
# Only check sections/ and snippets/ directories
BASENAME=$(basename "$FILE_PATH" 2>/dev/null)
DIRNAME=$(dirname "$FILE_PATH" 2>/dev/null)
DIRBASE=$(basename "$DIRNAME" 2>/dev/null)

if [[ "$DIRBASE" != "sections" && "$DIRBASE" != "snippets" ]]; then
  exit 0
fi

# Skip if already a lusena-* file
if [[ "$BASENAME" == lusena-* ]]; then
  exit 0
fi

# Check if a lusena-* counterpart exists
# Try direct prefix: header.liquid -> lusena-header.liquid
LUSENA_FILE="$DIRNAME/lusena-$BASENAME"
if [ -f "$LUSENA_FILE" ]; then
  echo "BLOCKED: You are editing a Dawn original ($BASENAME) but a LUSENA override exists: lusena-$BASENAME. Edit that file instead." >&2
  exit 2
fi

# Try main- prefix replacement: main-product.liquid -> lusena-main-product.liquid
if [[ "$BASENAME" == main-* ]]; then
  LUSENA_MAIN="$DIRNAME/lusena-$BASENAME"
  if [ -f "$LUSENA_MAIN" ]; then
    echo "BLOCKED: You are editing a Dawn original ($BASENAME) but a LUSENA override exists: lusena-$BASENAME. Edit that file instead." >&2
    exit 2
  fi
fi

exit 0
