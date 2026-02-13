---
title: PDP Details & FAQ Accordion Fix Plan
date: 2026-02-09
status: implemented
---

## Goal

Fix accordion animation jitter and typography mismatches in the PDP "Szczegóły i pytania" area, and ensure the two buy-box panels (specs + care) match the same UI/UX on both mobile and desktop as the draft shop.

## Root Causes (Verified)

1. Missing zebra row styles in specs table.
   - Evidence: computed `background-color` on table rows is `rgba(0, 0, 0, 0)`.
   - Cause: utility classes like `bg-surface-2/50` and `bg-brand-bg/60` are not present in `assets/lusena-shop.css`, so the zebra/definition row colors never apply.

2. Empty "Pielęgnacja" content for products without metafields.
   - Evidence: `innerTextLength` for the `Pielęgnacja` panel is `0`, so the content height collapses to near zero.
   - Cause: `pdp_care_steps` metafield is optional; when unset, the panel opens to empty content (looks broken).

3. Close animation stutter due to `hidden` + manual state control.
   - Draft shop uses Radix Accordion: no `hidden`, only `data-state` with height keyframes and `transition-all`.
   - Our theme sets `hidden` after close and re-measures height manually, which can produce a visible snap (especially when content height is small or changes).

## Fix Plan

1. Accordion animation parity
   - Remove `hidden` toggling on accordion content.
   - Use `data-state` only, with `accordion-up/down` keyframes (0.2s ease-out).
   - Add a `ResizeObserver` per content node to keep `--radix-accordion-content-height` in sync (e.g., when spec definitions expand/collapse).
   - Keep single-open and collapsible behavior as-is.

2. Content fallback rules
   - Add section-level fallback for "Pielęgnacja" bullet list.
   - Hide the panel only if both product metafields and fallbacks are empty.
   - Keep product-specific overrides when metafields are set.

3. Zebra row styling (specs table)
   - Introduce explicit CSS for zebra striping and definition rows in `snippets/lusena-pdp-styles.liquid`:
     - `tbody tr:nth-child(odd)` background `rgba(240, 238, 235, 0.5)`
     - definition rows background `rgba(247, 245, 242, 0.6)`
   - Alternatively, replace missing utility classes with existing ones that do exist in `lusena-shop.css` (e.g. `bg-surface-2`, `bg-brand-bg/50`) if we want to stay utility-only.

4. Typography alignment
   - Enforce draft font + sizes for:
     - Section heading (`Source Serif 4`, 24/32 mobile, 28/36 desktop)
     - Triggers (`Inter`, 16/24, weight 500)
     - Body copy (`Inter`, 14/20)
   - Apply explicit styles to `table`, `td`, `ul`, and `li` inside `.lusena-pdp-accordion__body` to avoid inheritance drift from Dawn defaults.

5. Verification
   - Run `validate_theme` on all touched files.
   - Playwright check on PDP:
     - Open/close each panel (buy-box + details section).
     - Confirm animation is smooth (no snap on close).
     - Verify zebra striping visible.
     - Verify typography matches draft at 390px and 1280px widths.

## Open Questions (Resolved)

1. For products without `pdp_care_steps`: show section-level default steps.
