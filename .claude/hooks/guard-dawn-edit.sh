#!/bin/bash
# PreToolUse hook (Edit|Write): warns when editing a Dawn original file
# that has a lusena-* counterpart. Blocks the edit with exit code 2.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('file_path', ''))
except:
    pass
" 2>/dev/null)

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
