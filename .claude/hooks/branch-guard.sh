#!/bin/bash
# PreToolUse hook: blocks git commit on protected branches.
# Exit 0 = allow, exit 2 = block (message sent to Claude via stderr).

INPUT=$(cat)

# Only act on git commit commands (grep the raw JSON input)
if ! echo "$INPUT" | grep -q "git commit"; then
  exit 0
fi

BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
  echo "BLOCKED: Direct commits to '$BRANCH' are not allowed. Create a feature branch first: git checkout -b feat/<description>" >&2
  exit 2
fi

exit 0
