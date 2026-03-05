---
name: lusena-v2-page-migration
description: Migrate any LUSENA Shopify theme page to align with brandbook v2. Use when the user says "migrate [page] to v2", "align [page] with v2 brandbook", or any variation. Covers audit, copy conversion to PL, section redesigns, new sections, backlog creation, and docs updates. Keywords: migrate, v2, brandbook, page migration, align, content update, Polish copy.
---

# LUSENA v2 page migration skill

## Goal

Systematically migrate any page in the LUSENA Shopify theme from v1 to v2 of the brandbook. Every page migration produces the same deliverables as the homepage migration: updated Polish copy, section-level changes, new sections if needed, a per-page backlog for deferred items, and docs updates.

---

## Prerequisites — read before ANY work

1. **Read the brandbook v2 changelog** — `docs/lusena_brandbook_update_changelog_v1_to_v2.md` — to understand what changed globally (positioning, copy tone, product hierarchy, etc.).
2. **Read brandbook v2** — `docs/LUSENA_BrandBook_v2.md` — find the specific page's section specs, copy, and UX guidance.
3. **Read the UI/UX implementation guide** — `docs/theme-brandbook-uiux.md` — to understand current design tokens, spacing tiers, component inventory, and section ordering conventions.
4. **Call `learn_shopify_api`** (Shopify Dev MCP) once before editing any Liquid files.

---

## Workflow

### Phase 1: Audit

1. **Identify the target page template** — find the JSON template in `templates/` (e.g., `templates/page.nasza-jakosc.json`, `templates/product.json`, `templates/collection.json`).
2. **List all sections** referenced in that template and their types.
3. **Read every section file** (`sections/lusena-*.liquid`) used on the page.
4. **Cross-reference with brandbook v2** — for the target page, find:
   - Which sections v2 specifies (new, removed, reordered)
   - Exact copy/headlines/subheadlines (PL)
   - Any new messaging frameworks or positioning shifts
   - Product hierarchy / tier ordering requirements
   - CTA text and link targets
5. **Produce a diff summary** — for each section, categorize the required change:

| Category | Description | Action |
|---|---|---|
| **Copy-only** | Text/translation update, no structural change | Do now |
| **Small redesign** | CSS/layout tweak, new block type, minor Liquid change | Do now |
| **Medium redesign** | New section file, schema changes, new snippet | Do now |
| **Large redesign** | New component system, external integrations, complex logic | Defer to backlog |

### Phase 2: User confirmation

Present the audit as a structured plan and **ask the user** exactly 3–4 questions:

1. **Scope confirmation** — "Here's what I'll do now vs. defer. Does this split look right?"
2. **Copy review** — Flag any claims in v2 copy that might be premature (e.g., customer counts, review counts, features not yet live). User may want to soften or remove these.
3. **Section-specific decisions** — If any section has multiple valid approaches (e.g., accordion vs. link, grid vs. list), ask the user to pick.
4. **Anything to skip?** — "Is there anything in this plan you want me to skip entirely?"

**KEY LESSON (from homepage migration):** The user WILL reject fake social proof ("12,000 klientek", star ratings without real reviews). Always flag claims that require real data and propose neutral alternatives.

### Phase 3: Implementation

Execute in this order:

#### Step 1: Create per-page migration backlog

- File: `memory-bank/doc/features/{page-name}-migration-backlog.md`
- Format: same as `memory-bank/doc/features/homepage-migration-backlog.md` — status legend, numbered items, each with What/Ref/Why deferred/Acceptance criteria.
- Only create if there are deferred items; skip if everything fits in the current pass.

#### Step 2: Update the page template JSON

- File: `templates/{page-template}.json`
- Update all section `settings` with Polish copy aligned to v2.
- Add/remove sections from `sections` object and `order` array as needed.
- If adding new sections, ensure the section `.liquid` file exists (create in Step 3).

#### Step 3: Create or redesign section files

For each section that needs structural changes:

- Edit existing `sections/lusena-*.liquid` files, or create new ones.
- Follow LUSENA architecture rules from `CLAUDE.md` / `AGENTS.md`:
  - Use `{% stylesheet %}` for section-scoped CSS. Use `assets/lusena-foundations.css` classes for spacing, typography, and layout.
  - Use `{% javascript %}` for JS.
  - Use LUSENA spacing tier classes (`lusena-spacing--compact/standard/spacious/hero`).
  - Use LUSENA icon system (`snippets/lusena-icon.liquid`) for icons.
  - Use brand CSS variables (`--accent-cta`, `--primary`, `--text-secondary`, etc.).
  - Support scroll-trigger animations when `settings.animations_reveal_on_scroll` is enabled.
  - Include `{% schema %}` with proper settings, presets, and translatable labels where appropriate.
- When creating new snippets, include `{% doc %}` header.

#### Step 4: Update section order in template

- Ensure the `order` array in the template JSON matches v2's recommended flow.
- Cross-reference `docs/theme-brandbook-uiux.md` § 5.1 for ordering conventions.

#### Step 5: Update `docs/theme-brandbook-uiux.md`

After all edits, update the implementation guide:

- **Homepage surface table** (§1) — if a new section was added to the page, add it.
- **Component inventory** (§ component table) — add any new `lusena-*` section/snippet.
- **Background alternation pattern** (§ bg alternation) — add new sections to the pattern.
- **Section ordering conventions** (§5.1) — update the page's ordering row.

**⚠️ ENCODING WARNING:** This file has mojibake arrow characters (`→` stored as `â†'`). The `replace_string_in_file` tool often fails on these lines. Use PowerShell line-based insertion/replacement instead:
```powershell
$lines = [System.Collections.ArrayList]@(Get-Content "docs\theme-brandbook-uiux.md")
$lines.Insert($targetLineIndex, "NewSection   â†' bg-surface-X")
$lines | Set-Content "docs\theme-brandbook-uiux.md" -Encoding UTF8
```

### Phase 4: Validation

1. **Check for errors** — use `get_errors` on all edited files.
2. **Verify dev server** — confirm the page loads at `http://127.0.0.1:9292/{page-path}` (start `shopify theme dev` if not running).
3. **Visual check** — if Playwright MCP is available, take a screenshot. Otherwise ask the user to verify.

---

## Copy rules (PL-first, v2 tone)

These rules apply to ALL copy written during migration:

| Rule | Detail |
|---|---|
| **Language** | All user-facing text in Polish. |
| **Positioning** | "Nocna rutyna piękna" (night beauty routine), NOT "pillowcase hero". Frame silk as part of a nightly self-care ritual. |
| **Tone** | Premium but approachable. No exclamation marks in headings. Sentence case (capitalize only first word + proper nouns). |
| **Social proof** | NEVER fabricate customer counts, review numbers, or star ratings. If v2 brandbook suggests a metric, check with user first. Use neutral alternatives like "Co mówią klientki" (no count) or "Produkty, które pokochasz od pierwszej nocy." |
| **Value anchors** | Use "0,XX zł/noc" framing per v2 when price data is available. Defer if price data isn't set up. |
| **CTAs** | Primary: "Sprawdź kolekcję", "Dodaj do koszyka", "Zobacz więcej". Avoid English CTAs. |
| **Product hierarchy** | Tier 1: Poszewka jedwabna 50×60. Tier 2: Scrunchie, Bonnet. Tier 3: Bundles. Always present in this order when listing products. |
| **"Jedwab" not "silk"** | In Polish copy, say "jedwab" / "jedwabna", not "silk". Exception: brand name "LUSENA" stays as-is. |

---

## Section design patterns (reuse these)

### Trust bar items
- 4–5 short badges with icons from `lusena-icon.liquid`
- Example: `layers` → "22 momme jedwab", `shield-check` → "Certyfikat OEKO-TEX", `truck` → "Darmowa dostawa od 199 zł", `clock` → "30 dni na zwrot"
- Background: `bg-brand-bg`

### Evidence/heritage tiles
- 3-tile grid (1-col mobile, 3-col desktop)
- Each tile: optional image with icon fallback (56px circle), title, subtitle
- White cards on `bg-brand-bg`, subtle hover shadow

### Newsletter capture
- Centered layout, `bg-surface-2`
- Email input + button joined on desktop (left-rounded input, right-rounded button, split on mobile)
- Hidden `contact[tags]` = "newsletter" for Shopify customer form
- Self-contained `sr-only` label styles (don't rely on external `sr-only` class)
- Privacy text below

### FAQ accordion
- Uses Dawn's `collapsible-content` pattern or native `<details>`/`<summary>`
- 4–6 questions, all in Polish, sorted by purchase-intent relevance

---

## Common pitfalls (learned from homepage migration)

1. **`sr-only` class not available** — LUSENA sections can't rely on Tailwind's `sr-only`. Always include a self-contained visually-hidden class in the section's `{% stylesheet %}` block.

2. **New section files require dev server restart** — `shopify theme dev` does NOT hot-reload new files. After creating a new `.liquid` section file, tell the user to restart the dev server.

3. **Template JSON copy vs schema defaults** — When updating copy, update BOTH:
   - The template JSON file (`templates/*.json`) — this is what the live page uses.
   - The schema `default` values in the section `.liquid` file — this is what new instances get.

4. **Encoding in theme-brandbook-uiux.md** — Arrow characters are double-encoded. Use PowerShell for edits to that file (see Phase 3, Step 5).

5. **Don't touch Dawn base files** — If a `lusena-*` version exists, always edit that. Dawn's originals (`header.liquid`, `footer.liquid`, `main-product.liquid`) are NOT used on the live store.

6. **Spacing classes not inline styles** — Use `lusena-spacing--standard` etc., not `padding: 64px 0`. See `memory-bank/doc/patterns/spacing-system.md` for the full system.

---

## Deliverables checklist

After every page migration, confirm these are done:

- [ ] Per-page migration backlog created (if deferred items exist)
- [ ] Template JSON updated with PL copy + v2 content
- [ ] Section files created/redesigned as needed
- [ ] Section order matches v2 spec
- [ ] `docs/theme-brandbook-uiux.md` updated (surface table, component inventory, bg pattern, ordering)
- [ ] No compile/lint errors in edited files
- [ ] Page loads on dev server without errors
- [ ] User has visually verified the result (or Playwright screenshot taken)
