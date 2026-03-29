---
paths:
  - "**/*.liquid"
  - "**/*.css"
  - "**/*.js"
  - "assets/**"
  - "sections/**"
  - "snippets/**"
  - "templates/**"
  - "layout/**"
---
# No Inline Scripts in Bash (MANDATORY)

## The problem

Running `node -e "..."` or `python -c "..."` via Bash with multi-line code and `&&` separators triggers Windows security prompts ("Command contains ambiguous syntax with command separators that could be misinterpreted"). The user must manually approve each one, which breaks their workflow.

## The rule

**NEVER use Bash for file searching, pattern matching, counting, or analysis.**

Banned patterns:
- `node -e "const fs = require('fs'); ..."` — use Grep/Glob/Read instead
- `python -c "import os; ..."` — use Grep/Glob/Read instead
- Any multi-line script passed to `node`, `python`, `ruby`, `perl` via `-e` or `-c`
- Any Bash command with `&&` chaining complex logic
- **`cd <path> && <command>`** — triggers "bare repository attacks" prompt. The working directory is already the repo, so just run commands directly (e.g., `git diff` not `cd /path && git diff`). If you need a different directory, use the command's own flag (e.g., `git -C <path>`).

## What to use instead

| Task | Tool |
|------|------|
| Find files by name/pattern | **Glob** (`*.liquid`, `sections/*.liquid`) |
| Search content across files | **Grep** (supports regex, glob filters, count mode) |
| Read a specific file | **Read** |
| Count matches across files | **Grep** with `output_mode: "count"` |
| Edit a file | **Edit** |
| Complex multi-file analysis | **Agent** tool (spawn a subagent that uses Grep/Read) |

## Example: counting CSS in stylesheet blocks

BAD (triggers prompt):
```bash
node -e "const fs = require('fs'); ... findFiles(...) ... matchAll(/stylesheet/) ..."
```

GOOD (no prompt):
```
Grep pattern: "{%-?\s*stylesheet" glob: "*.liquid" output_mode: "count"
```
Then read the matched files with Read if you need the actual content.

## This applies to subagents too

When spawning Agent subagents, include in the prompt: "Use Grep/Glob/Read tools for all file searching — never use `node -e` or `python -c` via Bash."
