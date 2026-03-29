#!/bin/bash
# PostToolUse hook (Edit|Write): runs shopify theme check on edited .liquid files.
# Non-blocking — output is shown to Claude as feedback.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('file_path', ''))
except:
    pass
" 2>/dev/null)

# Only check .liquid files
if [[ "$FILE_PATH" == *.liquid ]]; then
  RESULT=$(shopify theme check "$FILE_PATH" 2>&1)
  if echo "$RESULT" | grep -qiE "error|warning"; then
    echo "Theme check on $(basename "$FILE_PATH"):"
    echo "$RESULT" | grep -iE "error|warning|offense" | head -10
  fi
fi
