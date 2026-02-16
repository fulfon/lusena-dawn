---
name: lusena-draftshop-fragment-parity
description: End-to-end workflow for copying any UI/UX fragment from the LUSENA draft shop (lusena-shop/, React/Tailwind) into the LUSENA Dawn Shopify theme (Liquid/CSS/JS) with 1:1 visual and interaction parity. Use for requests like "copy/match exactly/port" a fragment (gallery, drawer, header, trust rows, cards, forms, etc.) from draft shop into the theme, including planning questions, docs/*.md implementation contract, capability audits, Shopify Dev MCP validation (learn_shopify_api + validate_theme), and user-led visual verification.
---

# Lusena Draftshop Fragment Parity

## Overview

Copy a UI/UX fragment from `lusena-shop/` (draft) into the Shopify theme with the same look and behavior, using a plan-first workflow with explicit decisions, theme validation, and clear parity gates. This workflow is universal for fragment migrations, not tied to any specific surface.

Draft source location for this repo:

- Primary: `./lusena-shop` (inside the theme repository root).
- If not found, then check sibling repositories/legacy paths.

## Workflow

### 0. Mandatory setup (Liquid themes)

1. Call Shopify Dev MCP `learn_shopify_api` with `api: "liquid"` once before editing theme Liquid.
2. After any theme edits, run Shopify Dev MCP `validate_theme` and fix issues until clean.
3. Prefer Shopify Dev MCP tools over web browsing for Shopify docs (avoid outdated docs).

### 1. Intake (define the fragment and parity scope)

Collect (or ask for) these inputs:

- Source fragment: exact file path(s) in `lusena-shop/` and component name(s), or a very specific description of where it is used.
- Target surface in theme: template/section/snippet where it must land (e.g., PDP = `templates/product.json` + the section it references).
- Parity scope: which parts must match exactly (layout, spacing, states, interactions, animations, accessibility, breakpoints).
- Data scope: what is dynamic (variants, metafields, metaobjects, tags, shop-level metafields, per-section settings).

Output: a short "Parity Spec" list capturing the behaviors to reproduce.

### 2. Source capture (draft shop)

Read the source implementation and extract the non-negotiables:

- Markup structure and state model (what drives active item, ordering, visibility).
- Desktop vs mobile layout rules (breakpoints, px/vw/vh values, max widths, aspect ratios).
- Interactions (click targets, scroll behavior, snap behavior, keyboard expectations).
- Visual states (active, hover, disabled, loading).
- Edge cases (empty/min/max content, missing data, long text, loading/error/success).

When the draft uses utility classes, capture resolved values (not just class names).

Useful discovery commands:

- Find the draft fragment: `rg -n "<keyword>" -S lusena-shop/src`
- Find the theme entry point: `rg -n "templates/<page>.json|sections/<section>.liquid" -S templates sections`
- Find related theme hooks: `rg -n "<keyword>|data-<hook>|<class>" -S sections snippets assets`

### 2.5. Theme capability and conflict audit (mandatory before plan)

Before writing the plan, run a concrete capability audit:

1. Build a source class/token inventory:
- Typography sizes/line-heights
- Spacing/padding/margins/gaps
- Dimensions (width/height/min/max)
- Color/background/border/radius/shadow
- State classes (hover/disabled/active/loading)

2. Check whether each required token already exists in theme CSS:
- `assets/lusena-shop.css`
- Existing section/snippet-level styles
- `snippets/lusena-missing-utilities.liquid` (only if needed)

3. Detect class conflicts from source composition:
- Resolve final class output as rendered by draft tooling (for example, merged utility output in React).
- Do not copy conflicting classes into Liquid (for example two font-size utilities on one element).

4. Decide implementation path for each missing capability:
- Reuse existing theme primitive/class
- Add scoped semantic CSS in the fragment
- Add minimal utility backfill only when justified and reusable

5. Record audit output in the plan:
- `Exists`
- `Missing`
- `Conflict resolved`
- `Implementation path`

If this audit is incomplete, do not continue.

### 3. Ask decisions (before writing the plan)

If anything is ambiguous, ask the user with explicit choices and tradeoffs. Common decision axes:

- Data source: hardcoded copy vs locale key vs setting vs metafield/metaobject.
- Interaction model: match draft exactly vs preserve existing Dawn behavior where needed.
- Breakpoint strategy: match draft breakpoints vs match theme breakpoints.
- Animation strategy: match draft motion vs theme defaults.
- Fallback behavior: what to show when data is missing or incomplete.

Do not write the plan until these decisions are resolved.

Decision question template (copy/paste and adapt):

1. Data source: A) locale/settings-based B) object/metafield-based
2. Interaction: A) exact draft behavior B) keep existing theme behavior where conflict exists
3. Breakpoint strategy: A) draft breakpoints B) theme breakpoints
4. Motion: A) draft-like B) theme default C) reduced motion priority
5. Missing-data fallback: A) hide fragment B) show fallback copy/state

### 4. Write the plan to `docs/*.md`

Create a plan file in `/docs` that can be used as an implementation contract.

Use `docs/_Parity_Plan_Template.md` as the required base structure:

1. Copy the template to a new plan file for the fragment (for example `docs/PDP_[Fragment]_Parity_Plan.md`).
2. Fill every section in the copied template (do not leave placeholder fields unresolved).
3. Keep the template section order, so parity reviews are consistent across migrations.

Minimum required sections:

- Goal, scope, non-goals.
- Source of truth: specific draft shop file paths.
- Target in theme: which templates/sections/snippets will be changed.
- Decisions: explicit, dated, and final.
- Open questions / unresolved assumptions (must be empty before implementation).
- Data sources & content model.
- Target UX spec (desktop + mobile) with sizing/interaction details.
- Capability audit summary (existing/missing/conflict + path).
- Parity contract table (selector -> property -> draft value -> theme target value).
- State fixture matrix (all required states and expected behavior).
- Implementation approach (file list, main responsibilities per file).
- Milestones/deliverables.
- Verification checklist (computed-style checks + manual/user + optional Playwright).
- Risks/edge cases.

Example of expected detail/structure: `docs/PDP_Gallery_Parity_Plan.md`.

### 4.5. Confirmation gate (mandatory)

After the plan `.md` is created/updated, STOP and do not modify theme code yet.

In your next message to the user:

- Ask for explicit confirmation to proceed with implementation (yes/no).
- List any remaining open topics or clarifying questions that must be resolved before continuing.
- If anything is still ambiguous, treat it as blocked: do not guess, and do not start implementation until clarified.

### 5. Implement in the Shopify theme (Liquid/CSS/JS)

Rules of thumb:

- Modify the code path that is actually used by the live template. Avoid editing Dawn defaults that are not referenced by the template JSON.
- Keep changes localized (prefer snippet/section-level `{% stylesheet %}` and `{% javascript %}`).
- Add stable `data-*` hooks for JS; avoid relying on presentational classnames as selectors.
- Preserve accessibility semantics (buttons for controls, `aria-current` for active, real links for navigation).
- Prefer semantic, fragment-scoped CSS when possible. Only add utility backfills if the capability audit says it is necessary.
- Never ship conflicting utilities on the same element.
- When source uses merged utility composition, port the resolved final output (not raw conflicting class strings).
- For inline numeric styles built from Liquid math, normalize to CSS-safe values (for example ensure decimal dot in `%` values).

Theme consistency:

- Animations: follow Dawn reveal-on-scroll conventions.
  - Add `scroll-trigger animate--slide-in` conditionally: `{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}`
  - For repeated items: add `data-cascade` to the container when enabled.
- Icons: reuse `snippets/lusena-icon.liquid`; extend it if a new icon is needed.
- Metafield resolution: prefer reusing existing logic patterns already present in the theme (e.g., certificate logic on the quality page).

### 6. Validate (always)

Run Shopify Dev MCP `validate_theme` for all touched files. Fix until valid.

Then run a parity pre-check against the Parity Contract:

- Minimum breakpoints: ~390px and ~1280px
- Check critical computed values: font-size, line-height, spacing, dimensions, alignment
- Check each required state from the state fixture matrix

If something breaks or is ambiguous in UI, use Playwright to debug (only when needed or when the user asks).

### 7. Visual verification (User)

After code validation is clean, ask the user to confirm visual parity in the browser:

1. Check the fragment at minimum widths: Mobile (~390px) and Desktop (~1280px).
2. Test key interactions (click, scroll, state updates, variant changes).
3. Confirm typography/spacing/colors match the draft fragment.
4. If the user reports a mismatch, use Playwright to reproduce and iterate until parity is reached.

### 8. Wrap-up

Provide a concise summary:

- Which files changed.
- Which user decisions were implemented.
- What was validated (theme validation).
- What needs user confirmation (visual parity) or what the user confirmed.

If the change is substantial, offer:

- Update `docs/THEME_CHANGES.md`.
- Create a git commit (only if the user wants).
