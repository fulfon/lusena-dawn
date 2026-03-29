#!/bin/bash
# PostCompact hook: re-injects critical LUSENA rules after context compaction.
# Content verified against 54 documented migration lessons — these are the
# most frequently violated and most damaging rules when forgotten.

cat << 'RULES'
=== LUSENA Critical Rules (post-compaction reminder) ===

ARCHITECTURE:
1. Edit `lusena-*` files, not Dawn originals. If a `lusena-*` file exists, use it.
2. CSS specificity: section CSS MUST use 0-2-0 (parent+child) to beat foundations.
   `.parent .child {}` not `.child {}` alone. This is the #1 recurring bug.
3. compiled_assets: {% stylesheet %} blocks max 50 lines. Total must stay < 55KB.
   Truncation is silent — no error, CSS just stops mid-rule.

COPY & LANGUAGE:
4. Customer-facing text in Polish; code/comments in English.
5. Hyphens only (-), NEVER em dashes. Sentence case for all headings.
6. Never fabricate social proof (customer counts, ratings, reviews).

WORKFLOW:
7. `/playwright-cli` with `-s=<name>` for ALL browser work. Never MCP browser tools directly.
8. `memory-bank/activeContext.md` has current focus and next steps.

VALUES: Free shipping 289 zl | Cross-sell scrunchie 39 zl | CTA #0E5E5A | Feature card title max 28 chars | Tiers: full-bleed/compact/standard/spacious/hero
RULES
