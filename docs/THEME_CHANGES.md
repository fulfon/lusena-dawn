# LUSENA × Dawn — Theme change log (tracked in Git)

## What is this codebase?

This repository started from the official Shopify **Dawn** theme and is being adapted into a **LUSENA**-ready storefront (PL-first, premium feel, proof-first messaging, WCAG-minded UI).

Source of truth for brand direction: `docs/LUSENA_BrandBook_v1.md` (local path: `C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn\docs\LUSENA_BrandBook_v1.md`).

## How to use this file

- For each “bigger” change set, create a Git commit and add an entry here.
- Entries should be **semi-detailed**: what changed, why, and where (key files/settings).
- Always reference the commit (hash + message) so it’s easy to diff/revert.

---

## Commits

### 2f6787f — fix(lusena): match homepage to draft spacing + CTAs

**Goal:** Make the Shopify homepage match the `lusena-shop/` draft 1:1 by removing Dawn’s implicit section spacing and restoring missing draft UI details (CTAs, badges, FAQ motion, utility colors).

**What changed**
- Removed `"class": "section"` from LUSENA section schemas to avoid Dawn’s `.section + .section` margin stacking (fixed hero→trust gap and unintended top/bottom spacers across sections).
- Added a small “missing utilities” snippet and loaded it globally so draft-referenced classes are always present (`opacity-80`, `text-red-900/40`, `text-green-900/40`, `md:text-sm`).
- Bestsellers: ensured “View all products” renders consistently (with a safe URL fallback) and made `New`/`Bestseller` badges auto-drive from product tags (case-insensitive).
- Reviews: render the “Read 127 verified reviews” CTA even when no link URL is configured (so it’s not blocked by missing reviews app/content).
- Footer: adjusted newsletter UI to match the draft’s “input-only” visual (submit remains accessible but visually hidden).
- FAQ: added smooth accordion-like open/close animation while keeping native `<details>/<summary>` semantics.

**Key files**
- `layout/theme.liquid`
- `snippets/lusena-missing-utilities.liquid`
- `snippets/lusena-product-card.liquid`
- `sections/lusena-bestsellers.liquid`
- `sections/lusena-faq.liquid`
- `sections/lusena-testimonials.liquid`
- `sections/lusena-hero.liquid`
- `sections/lusena-trust-bar.liquid`
- `sections/lusena-problem-solution.liquid`
- `sections/lusena-heritage.liquid`
- `sections/lusena-bundles.liquid`
- `sections/lusena-footer.liquid`

### d93971a — feat(lusena): migrate draft-shop UI into Dawn

**Goal:** Bring the `lusena-shop/` draft UI into the Dawn theme 1:1 using OS 2.0 sections/templates, with Shopify-native data hooks (products/pages/metafields) and a working cart drawer + upsell layer.

**What changed**
- Added LUSENA OS 2.0 sections/templates to match the draft Home, collection, product, About, Quality, and Returns pages.
- Implemented a draft-matching cart drawer (`snippets/cart-drawer.liquid`) including upsell logic driven by product metafields + theme settings.
- Added Tailwind-compiled styling (`assets/lusena-shop.css`) and GSAP reveal animations (`assets/lusena-animations.js`) used by the new sections.
- Fixed Theme Editor schema constraints (richtext/url defaults, upsell max-items setting) and stabilized cart drawer JS/CSS (overlay visibility + CartItems dependency).

**Key files**
- `layout/theme.liquid`
- `config/settings_schema.json`
- `assets/lusena-shop.css`
- `assets/lusena-animations.js`
- `assets/cart-drawer.js`
- `assets/component-cart-drawer.css`
- `snippets/cart-drawer.liquid`
- `sections/lusena-hero.liquid`
- `sections/lusena-header.liquid`
- `sections/lusena-footer.liquid`
- `templates/index.json`
- `templates/collection.json`
- `templates/product.json`
- `templates/page.o-nas.json`
- `templates/page.nasza-jakosc.json`
- `templates/page.zwroty.json`

---

### feat(lusena): homepage sections per brandbook 5.1.1

**Goal:** Implement custom LUSENA homepage sections per brandbook Section 5.1.1 specifications, replacing generic Dawn sections with brand-aligned, conversion-focused components.

**New sections created**

1. `sections/lusena-trust-bar.liquid` — Compact 4-column trust/proof bar with emoji icons
   - 16px compact padding, 2-column grid on mobile
   - Configurable blocks: icon + title + subtitle
   - Color scheme selection

2. `sections/lusena-testimonials.liquid` — Customer reviews/UGC grid with star ratings
   - 3-column grid (2 tablet, 1 mobile)
   - 1-5 star rating with visual stars
   - Verified purchase badge option
   - Heading + "View all reviews" link

3. `sections/lusena-comparison.liquid` — Cotton vs Silk visual comparison
   - 2-column layout with red X (cotton negatives) and green checkmarks (silk positives)
   - Configurable comparison rows as blocks
   - CTA button with outline style option

4. `sections/lusena-bundles.liquid` — Gift sets/bundles with savings display
   - 2-column grid of bundle cards
   - Product picker OR manual title/price
   - Strikethrough original price + savings badge
   - Badge text (e.g., "Best value", "Popular")

**Homepage section order (updated)**
```
1. hero (image-banner)
2. lusena_trust_bar (NEW)
3. lusena_comparison (NEW)
4. bestsellers (featured-collection)
5. heritage (image-with-text)
6. lusena_testimonials (NEW)
7. lusena_bundles (NEW)
8. faq (collapsible-content)
9. newsletter
```

**Localization (i18n)**
- Added storefront translation keys in `locales/en.default.json` and `locales/pl.json`:
  - `sections.lusena_trust_bar.*`, `sections.lusena_testimonials.*`, `sections.lusena_bundles.*`
- Added schema translations in `locales/en.default.schema.json` and `locales/pl.schema.json`:
  - Full section names, settings labels, block names, and presets for all 4 new sections

**Files touched (high-signal)**
- New sections: `sections/lusena-trust-bar.liquid`, `sections/lusena-testimonials.liquid`, `sections/lusena-comparison.liquid`, `sections/lusena-bundles.liquid`
- Template: `templates/index.json` (complete rewrite with new section order and Polish content)
- Locales: `locales/en.default.json`, `locales/pl.json`, `locales/en.default.schema.json`, `locales/pl.schema.json`

---

### fcd1a02 — refactor(css,i18n): brandbook-aligned typography, animations & localization

**Goal:** Align global CSS with brandbook typography/animation specs and move hardcoded Polish strings to locale files.

**Typography scale (brandbook alignment)**
- H2: increased from 20/24px to 24/28px (mobile/desktop) with line-height 1.286 per brandbook spec (28/36px ratio)
- H3: increased from 17/18px to 18/20px (mobile/desktop) with line-height 1.4 per brandbook spec (20/28px ratio)

**Animation timing**
- `--duration-short`: changed from 100ms to 150ms for calmer, more premium UI transitions per brandbook's "calm, gentle" guideline

**Focus states (accessibility)**
- Updated focus outline to use `--color-button` (teal accent) instead of foreground at 50% opacity for better brand consistency and WCAG compliance

**Localization (i18n)**
- Added new `lusena.cart` translation keys for cart conversion features:
  - `free_shipping`, `free_shipping_remaining`, `free_shipping_unlocked`, `free_shipping_threshold`
  - `upsell_title`, `upsell_add`
  - `gift_mode_title`, `gift_note_label`, `gift_note_placeholder`, `gift_note_hint`
- Added Polish translations in `locales/pl.json`
- Updated `snippets/cart-drawer.liquid` to use translation filters instead of hardcoded Polish
- Updated `sections/main-cart-footer.liquid` to use translation filters instead of hardcoded Polish

**Files touched**
- CSS: `assets/base.css` (typography scale, animation timing, focus states)
- Locales: `locales/en.default.json`, `locales/pl.json`
- Liquid: `snippets/cart-drawer.liquid`, `sections/main-cart-footer.liquid`

---

### 1b99f37 — feat(lusena): brandbook-aligned UI + cart conversion layer

**Goal:** Align Dawn foundations to the LUSENA brandbook and add the first conversion-focused layer (PDP + cart).

**Theme settings / foundations**
- Set LUSENA default look (Route A-inspired): porcelain background, ink text, teal CTA; Source Serif 4 (head) + Inter (body), calmer spacing and radii.
- Fixed local dev schema mismatch for page width by aligning `page_width` to allowed steps (now 1300).
- Added a new Theme settings group: **LUSENA** (cart conversion + PDP CTA controls).

**Header / footer (PL-first copy)**
- Updated announcement bar and footer boilerplate to LUSENA-style, calm, proof-first Polish messaging (shipping 24h, OEKO‑TEX, 60 days).
- Disabled country/language selectors for a PL-first launch default.

**Homepage (Home)**
- Rebuilt `templates/index.json` to match the brandbook’s recommended narrative flow: hero → proof bar → problem/solution → bestsellers → heritage → FAQ → newsletter.

**Product page (PDP)**
- Updated `templates/product.json` layout to be more proof-first (trust bar, risk reversal, pricing anchor helpers).
- Implemented a safe primary CTA label override for the main PDP button and made it persist across variant / selling-plan changes.

**Cart drawer + cart page conversion layer**
- Cart drawer: added free-shipping progress, gift-mode (cart note), low-friction upsell, and reassurance copy under checkout.
- Cart page (`/cart`): added the same conversion elements in the cart footer for parity.

**Collections & search**
- Updated collection/search/list-collections templates to match visual standards for product cards (4:5 portrait, hover secondary image, ratings where available).

**Files touched (high-signal)**
- Theme settings: `config/settings_schema.json`, `config/settings_data.json`
- Core UX: `snippets/cart-drawer.liquid`, `sections/main-cart-footer.liquid`, `snippets/buy-buttons.liquid`, `assets/product-form.js`
- Templates: `templates/index.json`, `templates/product.json`, `templates/cart.json`, `templates/collection.json`, `templates/search.json`, `templates/list-collections.json`, `templates/page.nasza-jakosc.json`
- Copy: `locales/pl.json`, `sections/header-group.json`, `sections/footer-group.json`

