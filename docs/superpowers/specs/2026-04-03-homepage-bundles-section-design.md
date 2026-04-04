# Homepage Bundles Section — Design Spec

*Date: 2026-04-03*
*Status: Approved (updated 2026-04-04 — card standardization pass)*
*Branch: feat/homepage-bundles-wiring*

> **2026-04-04 updates:** CTA buttons removed (cards are full `<a>` links), badge consolidated to shared `.lusena-badge--overlay`, savings moved to gold-tinted badge overlay on image, type hierarchy revised (1.6/1.4/1.3/1.2), title underline hover added.

## Overview

Rewrite the homepage `lusena-bundles` section from static placeholder text blocks to a product-driven, editorial-style discovery gateway. The section pulls real data from Shopify bundle products (prices, URLs, images) while maintaining hand-crafted editorial copy for contents descriptions and "why together" messaging.

**Position in homepage flow:** Section 7 of 10 (after hero, trust bar, benefit bridge, bestsellers, testimonials, problem/solution). By this point the customer knows the individual products — the bundles section is a "now combine them" moment.

## Design decisions

### 1. Section role: Discovery gateway

Editorial, routine-framing approach. The section introduces bundles as curated routines and drives clicks to bundle PDPs. NOT a quick-shop surface — no color selectors or ATC buttons on the homepage. Aligns with bundle strategy principle: "story/routine framing, not savings framing."

### 2. Section heading and intro copy

- **Kicker:** "Zestawy Premium" (gold accent, uppercase, letter-spaced — existing pattern)
- **Heading:** "Zbuduj swoją nocną rutynę" (routine-framing, not product-name-led)
- **Body:** "Każdy zestaw to gotowy pomysł - na nocną rutynę albo idealny prezent."

The heading frames the section around the customer's need (building a routine). Each card is an answer to that need. Body copy covers both customer segments: self-buyers (routine) and gift-buyers (prezent).

### 3. Desktop layout (768px+)

**Equal 3-column grid.** All 3 bundle cards are identical in structure and size. Nocna Rutyna gets a "Bestseller" gold badge on the image corner — same pattern as `lusena-product-card` badges. No asymmetric hero layout on desktop.

Grid: `grid-template-columns: repeat(3, 1fr)`, gap: `var(--lusena-space-5)`.

### 4. Mobile layout (<768px)

**Hero card + 2 compact rows:**

- **Nocna Rutyna:** Full card (image + name + contents + editorial line + pricing + savings + CTA button). Same structure as desktop card, just full-width.
- **Piekny Sen:** Compact row (no image area, SVG thumbnail on left). Name + price on same line, contents text, savings + text link CTA.
- **Scrunchie Trio:** Same compact row pattern.

Mobile compact rows include a small SVG illustration thumbnail (~48-56px) on the left side to give each row visual identity.

### 5. Card anatomy (full card — desktop + mobile hero)

Top to bottom:

1. **Image area** — 4:5 aspect ratio. Renders the Shopify product's featured image. Fallback: if no featured image, shows circular thumbnails of component products pulled from Shopify. Worst case (dev only): no image area rendered.
2. **Badge** — "Bestseller" on Nocna Rutyna only. Gold background (`--lusena-accent-2`), white text, top-left corner. Rendered via `lusena.badge_bestseller` metafield.
3. **Bundle name** — `lusena-type-h2` or equivalent. Source Serif 4, medium weight.
4. **Contents list** — "Poszewka jedwabna + Czepek do spania". Secondary text color (`--lusena-text-2`).
5. **"Why together" editorial line** — Italic, teal accent (`--lusena-accent-cta`). One-liner answering "why buy these together." Per-bundle, hand-crafted.
6. **Price** — Bundle price (bold, primary text) + original price (strikethrough, secondary text, 50% opacity). Order: [current] [~~original~~] — matches theme standard.
7. **Savings badge** — "Oszczedzasz X zl" as gold-tinted chip overlay on bottom-right of card image. Style: `rgba(140, 106, 60, 0.08)` + `backdrop-filter: blur(4px)` + `border-radius`. Matches bundle PDP savings chip. *(Updated 2026-04-04: moved from inline text to image overlay.)*
8. ~~**CTA**~~ — *Removed 2026-04-04.* Entire card is now an `<a>` link (matching product card pattern). No separate button.

### 6. Compact row anatomy (mobile only — Piekny Sen, Scrunchie Trio)

Single row layout:

```
[SVG thumbnail 56px]  Bundle Name                Price  Strikethrough
                       Contents text
                       Oszczedzasz X zl
```

- Entire row is an `<a>` link (no separate CTA) *(Updated 2026-04-04)*
- SVG thumbnail on the left (custom uploaded illustrations per bundle)
- Name + price on same line (CSS grid: 1fr auto)
- Contents text below
- Savings in gold text, spans full width

### 7. Pricing display

- **Bundle price:** Bold, primary text color, prominent
- **Original price:** Strikethrough, secondary text, 50% opacity strikethrough line (using `color-mix` pattern from existing `lusena-bundles.css`)
- **Savings:** "Oszczedzasz X zl" in plain gold text (`--lusena-accent-2`). No chip — subordinate to CTA.
- **Never show percentages** — absolute zloty amounts only (per bundle strategy)

### 8. Image strategy

| Surface | Nocna Rutyna | Piekny Sen | Scrunchie Trio |
|---------|-------------|------------|----------------|
| Desktop (full card) | Product photo from Shopify | Product photo from Shopify | Product photo from Shopify |
| Mobile (hero card) | Product photo from Shopify | N/A (compact row) | N/A (compact row) |
| Mobile (compact row) | N/A (hero card) | SVG thumbnail (fallback: product thumbnails) | SVG thumbnail (fallback: product thumbnails) |

**Image fallback chain:**
1. Shopify product featured image exists → render it
2. No featured image → render circular thumbnails of component products (pulled via `all_products` lookup)
3. No featured image AND no component photos (dev-only) → skip image area entirely

### 9. SVG illustrations (mobile compact rows)

Two custom SVG thumbnails, designed as permanent design elements (not placeholders):

- **Piekny Sen SVG:** Minimal line-art of folded pillowcase + contoured 3D sleep mask. Stroke `#2E2D2B`, gold strap detail `#8C6A3C`. ViewBox `0 0 56 56`.
- **Scrunchie Trio SVG:** Three overlapping scrunchie ring shapes in brand colors (Czarny `#2E2D2B`, Brudny roz `#C4A08A`, Szampan `#D4C9BD`). Gold center detail. ViewBox `0 0 56 56`.

SVGs are uploaded by the owner as theme assets. Already generated and approved.

### 10. Per-bundle content

| Field | Nocna Rutyna | Piekny Sen | Scrunchie Trio |
|-------|-------------|------------|----------------|
| **Shopify handle** | `nocna-rutyna` | `piekny-sen` | `scrunchie-trio` |
| **Contents text** | Poszewka jedwabna + Czepek do spania | Poszewka jedwabna + Maska 3D do spania | 3x Scrunchie jedwabny w trzech kolorach |
| **"Why together" line** | Twarz i wlosy - kompletna ochrona na noc | Gladkosc dla skory, ciemnosc dla oczu | Kolor pod nastroj - idealny prezent |
| **Bundle price** | 399 zl | 349 zl | 139 zl |
| **Original price** | 508 zl | 438 zl | 177 zl |
| **Savings** | 109 zl | 89 zl | 38 zl |
| **Badge** | Bestseller | (none) | (none) |
| ~~**CTA**~~ | *(Removed 2026-04-04 — full-card link)* | | |

### 11. Data architecture

The section uses a **product picker** per block instead of hardcoded text fields. Each block references a Shopify product, and the template pulls:

- **From Shopify product:** title, price, URL, featured_image, available
- **From metafields:** `lusena.bundle_original_price` (original sum before discount, in zl — used for strikethrough price and savings calculation), `lusena.badge_bestseller`
- **From block settings (hand-crafted):** contents text, "why together" editorial line, mobile SVG asset filename

**Savings calculation:** `lusena.bundle_original_price * 100 - product.price` (metafield stores zl as integer, product.price is in grosz/cents). Format with `money_without_trailing_zeros`.

**Out-of-stock handling:** If `product.available == false`, the card still renders but with reduced opacity (greyed out image). Card still links to the PDP. Same `--oos` visual pattern as `lusena-product-card`. *(Updated 2026-04-04: no separate disabled CTA — card link handles navigation.)*

This means prices, images, and URLs stay in sync with Shopify automatically. Editorial copy is maintained in the theme editor.

### 12. Section settings schema

**Section-level settings:**
- Kicker text (default: "Zestawy Premium")
- Heading text (default: "Zbuduj swoja nocna rutyne")
- Body text (default: "Kazdy zestaw to gotowy pomysl...")
- Spacing overrides (existing pattern — padding top/bottom desktop/mobile)

**Block settings (type: `bundle_card`):**
- Product picker (`type: product`) — the bundle product
- Contents text (text field) — "Poszewka jedwabna + Czepek do spania"
- Editorial line (text field) — "Twarz i wlosy - kompletna ochrona na noc"
- Mobile SVG asset (text field) — filename of the SVG in assets/ (e.g., `lusena-bundle-piekny-sen.svg`)
- ~~CTA label~~ *(Removed 2026-04-04 — no separate CTA button)*

### 13. CSS changes

Modify existing `assets/lusena-bundles.css`:
- Add mobile compact row styles (`.lusena-bundles__compact-row`)
- Add SVG thumbnail styles (`.lusena-bundles__compact-thumb`)
- Savings badge: gold-tinted chip overlay on bottom-right of card image (`.lusena-bundles__savings-badge`) *(Updated 2026-04-04)*
- Add responsive breakpoint: desktop grid → mobile hero + compact rows at 768px
- Badge: shared `.lusena-badge--overlay` from foundations (frosted glass) *(Updated 2026-04-04 — replaces custom badge classes)*

### 14. Template JSON changes

Update `templates/index.json`:
- Replace hardcoded text block settings with product picker references
- Set the 3 bundle product handles
- Add contents text and editorial lines per block
- Update section heading and body copy
- Fix links (currently `shopify://collections/all` → actual product URLs via product picker)

### 15. Out of scope

- Color selection on homepage (happens on PDP only)
- Add-to-cart from homepage (CTA links to PDP)
- Carousel or horizontal scroll (rejected during brainstorming)
- Bundle product media/photography (blocked on physical products)

## Files to modify

1. `sections/lusena-bundles.liquid` — rewrite template (product picker blocks, mobile layout, fallback chain)
2. `assets/lusena-bundles.css` — add mobile compact rows, SVG thumbnails, savings chip, responsive breakpoint
3. `templates/index.json` — update block settings with product pickers and editorial copy
4. `assets/lusena-bundle-piekny-sen.svg` — NEW: upload SVG (provided by owner)
5. `assets/lusena-bundle-scrunchie-trio.svg` — NEW: upload SVG (provided by owner)
