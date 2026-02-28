#!/bin/sh
# Install git hooks for the LUSENA theme project
# Run this once after cloning: bash scripts/install-hooks.sh

cp scripts/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
echo "Git hooks installed successfully."
