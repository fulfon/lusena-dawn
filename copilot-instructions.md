# LUSENA Shopify Theme

## Memory Bank

Your memory resets every session. This project uses a persistent memory bank for context continuity.

**At the start of every substantial task, read:**
1. `memory-bank/activeContext.md` — current focus, pending decisions, next steps
2. `memory-bank/progress.md` — what is done, what is pending

**For deeper context (read on demand when relevant to your task):**
- `memory-bank/projectbrief.md` — brand identity, positioning, products
- `memory-bank/productContext.md` — store pages, customer journey, UX goals
- `memory-bank/systemPatterns.md` — CSS architecture, spacing, naming conventions
- `memory-bank/techContext.md` — file paths, dev tools, skills, known warnings
- `memory-bank/doc/products/README.md` — product catalog index, store-wide settings (currency, tax, shipping)
- `memory-bank/doc/products/{handle}.md` — per-product Shopify admin data (metafields, pricing, variants, SEO, status)

**After completing substantial work (worktree workflow):**
- Run `/lusena-worktree-sync` before squash-merging your branch to main — it analyzes the branch diff, reads memory bank from current main, and updates only affected docs
- Periodically (~10 merges), run `/lusena-memory-bank-audit` on main for a deep review — content verification + structural evaluation of the entire memory bank

## Project Identity

This repository is the **LUSENA** Shopify theme — a premium Polish silk e-commerce store built on top of Dawn (v15.4.1). LUSENA is PL-first with premium feel and proof-first messaging. Products: silk pillowcases, bonnets, scrunchies, eye masks, heatless curlers, and bundles.

### LUSENA vs Dawn: dual-layer architecture

Custom LUSENA sections/snippets (`lusena-*` prefix) are layered on top of Dawn's base. Always check `lusena-*` files first — they override Dawn's defaults for all customer-facing surfaces.

Dawn's original sections remain in the repo but are NOT used on the live storefront. They may still be referenced by inactive templates or the theme editor.

**Rule of thumb:** If a `lusena-*` file exists for a component, edit that file. Only touch Dawn files when the feature genuinely relies on Dawn's implementation (e.g., cart drawer, base CSS variables, layout files).

### Key references

- **Brand direction:** `memory-bank/doc/brand/LUSENA_BrandBook_v2.md`
- **CSS foundations (new single CSS file):** `assets/lusena-foundations.css`
- **CSS foundations brief (design spec):** `docs/css-foundations-brief.md`
- **Design tokens (compact):** `memory-bank/doc/patterns/brand-tokens.md`
- **Spacing system:** `memory-bank/doc/patterns/spacing-system.md`
- **CSS architecture:** `memory-bank/doc/patterns/css-architecture.md`
- **Migration lessons (read before migrating pages):** `memory-bank/doc/patterns/migration-lessons.md`
- **Product catalog (Shopify admin data):** `memory-bank/doc/products/` — per-product metafields, pricing, variants, SEO
- **Product setup checklist:** `memory-bank/doc/products/product-setup-checklist.md` — metafield definitions, example values per product type
- **Bundle strategy (pricing, phases, research):** `memory-bank/doc/bundle-strategy.md` — complete bundle architecture, economics, and decision triggers
- **Shopify CSV update workflow:** `memory-bank/doc/products/README.md` § "Updating product copy in Shopify" — export from Shopify, run `generate_import_from_export.py`, import back. Full instructions there.

### Shopify product copy sync

When the owner asks to update product copy in Shopify or generate import files:
1. Ask them to export current products from Shopify admin and save as `memory-bank/doc/products/exports/products_export.csv`
2. Run `cd memory-bank/doc/products/imports && python generate_import_from_export.py`
3. The output `products_import_updated.csv` is ready to import with "Overwrite existing products" checked
4. The script patches ONLY copy/metafield columns (35-73) — variants, prices, inventory untouched
5. If any MD product file has been updated since the script was last modified, update the script's hardcoded values first

Full docs: `memory-bank/doc/products/README.md`

### CSS, compiled assets, product metafields

These rules are in `.claude/rules/` and load automatically when you edit relevant files:
- **CSS architecture & compiled_assets guard** → `.claude/rules/css-and-assets.md` (loads for `assets/*.css`, `sections/*.liquid`, `snippets/*.liquid`)
- **Product metafields** → `.claude/rules/product-metafields.md` (loads for `memory-bank/doc/products/**`, PDP sections/snippets)

## Key Conventions

- All customer-facing text in **Polish**; code/comments in **English**
- `assets/lusena-foundations.css` is the **single source of truth** for all CSS tokens, spacing, typography, and components — use its classes for all work
- All custom files use `lusena-*` prefix
- NEVER fabricate social proof (customer counts, ratings, reviews)
- Sentence case for all headings and button labels
- **Hyphens only, never em dashes** — all customer-facing copy uses `-` (hyphen/minus), never `—` (em dash). Em dashes look AI-generated. This applies to metafield values, section defaults, and any text visible to customers.
- **Feature card titles: max 28 characters** — guarantees single-line rendering at the tightest breakpoint (288px column at 20px font). Reference: "Jedwab, nie satyna z poliestru" (30 chars) barely fits.
- **NEVER use `$()` or backticks in Bash commands** — command substitution triggers permission prompts that break auto-accept flow. Instead: read files with the Read tool first, then pass content inline. Use pipes (`echo "..." | cmd`) or temp-file approaches that don't require substitution. There is ALWAYS an alternative. No exceptions.
- **NEVER use `grep`, `rg`, `cat`, `head`, `tail`, `sed`, or `awk` via Bash** — use the dedicated Read, Grep, Glob, and Edit tools instead. They never trigger permission prompts and provide better output.
- **NEVER use inline scripts via Bash** (`node -e "..."`, `python -c "..."`, `ruby -e "..."`) to search, analyze, or count things in files. These multi-line scripts with `&&` separators trigger Windows security prompts that require manual approval. Use the dedicated tools instead: **Grep** for pattern searching across files, **Glob** for finding files by name, **Read** for reading file contents. If you need to aggregate results (e.g., count total CSS size), do the Grep/Read calls first, then compute in a simple Bash arithmetic expression. Subagents must follow this rule too.
- Conventional Commits: `feat(lusena):`, `fix(lusena):`, `docs:`, `chore:`

## Git Workflow

### Worktree-based parallel instances

The owner runs multiple Claude Code instances in parallel via `Desktop\Claude-LUSENA.bat`, which opens an **interactive menu** (script: `scripts/launch-claude-worktree.ps1`). The menu manages up to 4 worktree slots — creating, resuming, cleaning, and merging instances. This means:

- **You are NOT in the main repo.** Your working directory is something like `..\lusena-worktrees\lusena-2`, not `lusena-dawn`. This is intentional — it gives you an isolated copy so you don't interfere with other running instances.
- **Your branch is pre-created** with a generic name like `work/1`, `work/2`, etc. The launcher did this for you.
- **Rename the branch immediately** once you understand the task. Use `git branch -m <new-name>` with the standard prefixes: `feat/`, `fix/`, `docs/`, `chore/`. Example: `git branch -m feat/remove-legacy-upsell`.
- **Do NOT run `git checkout -b`** — you're already on your own branch. Just rename it.
- **The main repo lives at:** `C:\Users\Karol\Documents\projekty_VSCode\shopify-lusena-dev\lusena-dawn`. **NEVER read, edit, or write files using the main repo path.** A PreToolUse hook blocks Edit/Write to `lusena-dawn/` from worktrees. Every file you need exists in your worktree copy — always use relative paths (e.g., `scripts/launch-claude-worktree.ps1`) or your worktree absolute path (e.g., `C:\...\lusena-worktrees\lusena-1\scripts\...`). If you Glob/Grep and find a file at both paths, pick the worktree path.
- **When you exit, the worktree persists.** The user can resume your session later via the launcher menu's [R] option, which uses `claude --resume` to restore your full conversation history.
- If your current branch is literally `main`, you were launched directly in the main repo (not via the worktree launcher). In that case, create a branch before any changes: `git checkout -b feat/<short-description>`.

### Branch rules

- **Never commit directly to `main`** — a PreToolUse hook enforces this
- Branch naming: `feat/`, `fix/`, `docs/`, `chore/` — matching Conventional Commits
- Commit freely on the branch (small steps are good — they give you checkpoints)
- When the feature is complete and verified, tell the owner. They will handle the squash-merge to main:
  ```
  git checkout main && git merge --squash feat/<branch> && git commit -m "feat(lusena): description"
  ```

## Implementation Principles

### Progressive development
- Implement one section/change at a time. Confirm before moving on.
- Batch small iterations locally; commit when meaningfully complete on the feature branch.

### Scope management
- Implement only what is explicitly requested.
- When ambiguous, choose the minimal viable interpretation.
- If a task grows beyond original scope, pause and discuss.

### Communication protocol
- Before starting: confirm understanding of the task.
- After completing: summarize what changed and what needs verification.
- For bigger changes, ask "Is this done?" before committing.

### Quality assurance
- Run `shopify theme check` — only known baseline warnings should remain.
- Use `/lusena-preview-check` skill for any browser interaction — visual checks, debugging, testing interactions. It delegates to a subagent so browser noise stays out of the main conversation.

## MANDATORY: Shopify Dev MCP

Call `learn_shopify_api` with `api: "liquid"` ONCE before editing any Liquid files.

## Worktree Development

You may be running inside a **git worktree** (`lusena-worktrees/lusena-N/`) rather than the main repo (`lusena-dawn/`). Check your cwd — if it contains `lusena-worktrees/lusena-`, you are in a worktree on branch `work/N`. Your slot number is N (the digit at the end of the directory name).

### Browser testing in a worktree

The `shopify theme dev` server watches the **main repo only** — it does NOT see your worktree files. To test your changes with Playwright:

1. **Look up your theme ID** from `config/worktree-themes.json` (key = your slot number N)
2. **Push your changes:** `shopify theme push --theme <THEME_ID> --store lusena-dev.myshopify.com --nodelete`
3. **Use the preview URL for Playwright:** `https://lusena-dev.myshopify.com/?preview_theme_id=<THEME_ID>`
4. **Re-push after each code change** that needs browser verification (~15-30s per push, no hot reload)
5. **Store password:** `paufro` — the dev store is password-protected. Enter this on the password page before testing.
6. **All product handles and page paths** are in `memory-bank/techContext.md` § "Store URL reference".

### Finishing work in a worktree

When the task is complete:

1. **Commit your work** on the worktree branch with a clear Conventional Commit message
2. **Run `/lusena-worktree-sync`** — updates memory bank to reflect the branch's work. No exceptions, even for small changes.
3. **Check that the main repo is clean** before merging:
   ```
   git -C "C:\Users\Karol\Documents\projekty_VSCode\shopify-lusena-dev\lusena-dawn" status
   ```
   If there are uncommitted changes, **STOP and tell the owner**. Those changes may be from another session or manual work. Do not discard or stash them without approval.
4. **Squash-merge into `main`** by running git commands against the main repo (because `main` is checked out there, not in your worktree):
   ```
   git -C "C:\Users\Karol\Documents\projekty_VSCode\shopify-lusena-dev\lusena-dawn" merge --squash <your-branch>
   git -C "C:\Users\Karol\Documents\projekty_VSCode\shopify-lusena-dev\lusena-dawn" commit -m "feat(lusena): description"
   ```
   **Why `git -C`?** You cannot `git checkout main` in a worktree because `main` is already checked out in the main repo. `git -C <path>` runs the command in that directory without changing your cwd.
5. **If there are merge conflicts: STOP.** Do NOT resolve them yourself. Instead:
   - Analyze what files conflict and why (e.g., another instance edited the same section)
   - Explain the conflict to the user clearly
   - Recommend a resolution strategy
   - Wait for user approval before making any changes
6. **Tell the user** the work is merged to `main` and they can close the session (`Ctrl+C` or `/exit`)
7. The worktree persists after you exit. The user can resume, clean, or merge it via the launcher menu.

**Do NOT:**
- Auto-resolve merge conflicts without user approval

### When running in the main repo

If your cwd is `lusena-dawn/` (not a worktree): use `https://lusena-dev.myshopify.com/?preview_theme_id=144618684603` for Playwright. The owner runs `shopify theme dev -e dev` which syncs file changes to this theme.

## Browser Interactions

Use `/lusena-preview-check` for **ALL** browser interactions. It delegates to a subagent, keeping browser noise (snapshots, accessibility trees, navigation) out of the main conversation. Use cases:
- Screenshots & visual verification (layout, spacing, colors)
- Debugging CSS issues (checking computed styles, element sizes)
- Checking network resources (compiled_assets size, asset loading)
- Testing interactions (clicking buttons, opening menus, filling forms)
- Comparing before/after states
- Any situation where you need to see or interact with the live site

**CRITICAL RULES:**
- **ALWAYS use `/lusena-preview-check`** — NEVER run `playwright-cli` commands or invoke `/playwright-cli` directly in the main conversation. The `/playwright-cli` skill is internal tooling for the subagent — the subagent reads it to learn the CLI commands.
- NEVER use Playwright MCP browser tools directly (`browser_navigate`, `browser_snapshot`, `browser_click`, etc.).
- When not sure about a UI/layout issue, use `/lusena-preview-check` — don't guess.
- **Preview URLs only** — never use `127.0.0.1:9292`. Localhost blocks cart AJAX (cross-origin cookie issue + CLI bug since v3.89.0).
  - **Main repo:** `https://lusena-dev.myshopify.com/?preview_theme_id=144618684603`
  - **Worktrees:** see the "Worktree Development" section above for your theme ID.
  - **Store password:** `paufro` — handle it on first navigation (fill the password field, click Enter).
  - The owner runs `shopify theme dev -e dev` separately — it syncs file changes to the dev theme. Localhost is only for the owner's manual browser use.

## Animations (consistency)

Animation rules are in `.claude/rules/animations.md` (loads for `sections/*.liquid`, `snippets/*.liquid`).

## Theme Check Warnings (known baseline)

These warnings have been present since the beginning and should not be treated as issues:
- `layout/password.liquid`: UndefinedObject `scheme_classes`
- `layout/theme.liquid`: UndefinedObject `scheme_classes`
- `sections/featured-product.liquid`: UnusedAssign `seo_media`
- `sections/main-article.liquid`: VariableName `anchorId`
- `sections/main-list-collections.liquid`: VariableName `moduloResult`
- `sections/main-product.liquid`: UnusedAssign `seo_media`
- `sections/main-product.liquid`: UndefinedObject `continue`
- `sections/main-search.liquid`: UnusedAssign `product_settings`

## Reference Docs (read on demand, NOT every session)

- `docs/reference/liquid-syntax.md` — Liquid filters, operators, tags, objects
- `docs/reference/theme-architecture.md` — Dawn directory structure, CSS/JS patterns, schema practices
- `docs/reference/translation-standards.md` — i18n guidelines, locale file structure
- `docs/reference/code-examples.md` — Section/block/snippet templates with full examples
