#!/bin/bash
# TaskCompleted hook: runs theme check on recently modified lusena-* liquid files.
# Exit code 2 blocks task completion if errors are found.

TIMESTAMP_FILE="/tmp/.lusena-task-start"

# Find lusena-* liquid files modified since last task start
CHANGED=""
if [ -f "$TIMESTAMP_FILE" ]; then
  CHANGED=$(find sections snippets layout -name "lusena-*.liquid" -newer "$TIMESTAMP_FILE" 2>/dev/null)
fi

if [ -n "$CHANGED" ]; then
  RESULT=$(shopify theme check $CHANGED 2>&1)
  NEW_ERRORS=$(echo "$RESULT" | grep -ciE "^error" || true)

  if [ "$NEW_ERRORS" -gt 0 ]; then
    echo "Theme check found errors in recently edited files. Fix before completing task:" >&2
    echo "$RESULT" | grep -iE "error" | head -10 >&2
    exit 2  # Block task completion
  fi
fi

# Touch timestamp for next task cycle
touch "$TIMESTAMP_FILE"
exit 0
