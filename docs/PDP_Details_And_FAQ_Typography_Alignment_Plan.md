---
title: PDP Details & FAQ Typography Alignment Plan
date: 2026-02-09
status: implemented
---

## Goal

Match the draft shop typography (font family, size, weight, line-height, and spacing) for:

- Accordion triggers (titles)
- Accordion body content (paragraphs, lists)
- Specs table text and labels

## Source Of Truth (Draft Shop)

- `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-mockup\lusena-shop\src\components\ui\Accordion.tsx`
- `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-mockup\lusena-shop\tailwind.config.js`

## Current Theme Targets

- `snippets/lusena-pdp-styles.liquid`
- `snippets/lusena-pdp-buybox-panels.liquid`
- `sections/lusena-pdp-details.liquid`

## Findings (From Code)

- Draft triggers rely on `font-medium` + default `text-base` sizing from Tailwind.
- Draft content uses `text-sm` (14px / 20px).
- Draft uses Inter for body and Source Serif 4 for headings via Tailwind config.

## Gaps To Verify

- Verify computed styles on both draft and theme at 390px and 1280px:
  - `font-family`, `font-size`, `line-height`, `font-weight`, `letter-spacing`.
- Check for global font-size scaling differences between Tailwind (1rem=16px) and Dawn (root font-size).
- Check if any browser/OS font smoothing or inheritance causes perceived weight differences.

## Implementation Plan

1. Measure computed styles
   - Run draft shop dev server and capture computed styles for:
     - accordion trigger
     - accordion content body (paragraph + list item)
     - table cell text
   - Capture the same for Shopify theme PDP.

2. Align typography in theme
   - Set explicit typography values on:
     - `.lusena-pdp-accordion__trigger`
     - `.lusena-pdp-accordion__body`
     - `.lusena-pdp-accordion__body table, td, li`
   - If needed, add `letter-spacing: normal` and `-webkit-font-smoothing: antialiased`.

3. Validate and verify
   - Run `validate_theme`.
   - Playwright check on PDP at 390px and 1280px for computed styles and visual parity.

## Open Questions

- None (use draft values exactly).
