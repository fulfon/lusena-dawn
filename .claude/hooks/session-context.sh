#!/bin/bash
# SessionStart hook: injects key sections from activeContext.md
# so Claude always sees orientation context at session start.

# Git branch awareness
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
  echo "WARNING: On protected branch '$BRANCH'. Create a feature branch before committing."
else
  echo "On branch: $BRANCH"
fi
echo ""

FILE="memory-bank/activeContext.md"
if [ -f "$FILE" ]; then
  echo "=== LUSENA Active Context (auto-injected) ==="
  echo ""
  # Extract "Current focus" section (from header to next ## header)
  awk '/^## Current focus$/{found=1; next} /^## /{if(found) exit} found' "$FILE"
  echo ""
  # Extract "Next steps" section
  awk '/^## Next steps$/{found=1; next} /^## /{if(found) exit} found' "$FILE"
  echo ""
  # Extract "Known issues" section
  awk '/^## Known issues$/{found=1; next} /^## /{if(found) exit} found' "$FILE"
fi
