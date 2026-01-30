# LUSENA Shopify (Dawn) Migration Plan
**Source mockup:** `lusena-shop/` (React 19 + TypeScript + Tailwind SPA with static/mock data)  
**Target:** Shopify **Online Store 2.0 theme** based on **Dawn (v15.4.1)**, matching frontend **1:1** (layout, spacing, typography, components) while making the *right* parts configurable in Admin/Theme Editor.

**This plan follows:** `docs/shopify_dawn_migration_high_level.md` (expanded + made LUSENA-specific).

---

## 0) Current status (what’s already migrated)

### 0.1 Draft (React) inventory

**Routes (from `lusena-shop/src/App.tsx`)**
- `/` → `lusena-shop/src/pages/Home.tsx`
- `/collections/all` → `lusena-shop/src/pages/Collection.tsx`
- `/products/:id` → `lusena-shop/src/pages/Product.tsx`
- `/nasza-jakosc` → `lusena-shop/src/pages/Quality.tsx`
- `/o-nas` → `lusena-shop/src/pages/About.tsx`
- `/zwroty` → `lusena-shop/src/pages/Returns.tsx`

**Key UI components**
- Layout: `lusena-shop/src/components/layout/Header.tsx`, `lusena-shop/src/components/layout/Footer.tsx`
- Commerce: `lusena-shop/src/components/cart/CartDrawer.tsx`, `lusena-shop/src/components/product/ProductCard.tsx`
- Content blocks: `lusena-shop/src/components/ui/TrustStrip.tsx`, `lusena-shop/src/components/ui/ReviewCard.tsx`, `lusena-shop/src/components/ui/Accordion.tsx`
- Motion: GSAP patterns via `lusena-shop/src/lib/gsap.ts` (hero intro + scroll reveals)

**Mock data + logic**
- Product catalog: `lusena-shop/src/lib/products.ts` (handles: `silk-pillowcase`, `silk-sleep-mask`, `silk-scrunchie`, `heatless-curler`, `silk-bonnet`)
- Upsell decision tree: `lusena-shop/src/lib/upsell.ts` (suppression + priority rules)
- Cart state + operations: `lusena-shop/src/context/CartContext.tsx`

**Media**
- Draft uses local placeholder images (e.g., hero + product images). In Shopify these must be replaced with:
  - product media (Admin → Products)
  - section image pickers (Theme Editor)

### 0.2 Current Dawn migration status (what already exists in theme)

The theme already contains a 1:1 UI implementation of the draft pages using OS 2.0 templates/sections:
- Templates: `templates/index.json`, `templates/collection.json`, `templates/product.json`, `templates/page.o-nas.json`, `templates/page.nasza-jakosc.json`, `templates/page.zwroty.json`
- Header/Footer groups: `sections/header-group.json`, `sections/footer-group.json` using `sections/lusena-header.liquid` + `sections/lusena-footer.liquid`
- Styling: Tailwind-compiled CSS imported as `assets/lusena-shop.css`
- Cart drawer + upsell: `snippets/cart-drawer.liquid` (metafields + theme settings; see §7)
- Motion: GSAP-powered reveal animations in `assets/lusena-animations.js`

What remains for “fully production Shopify” is primarily **Admin data setup**, **structured content migration (metafields/metaobjects)**, and **QA + launch hardening**.

---

## 1) Goal and constraints

### 1.1 Objective
Recreate the draft UI/UX inside Dawn using **Liquid + JSON templates + sections/blocks + snippets**, with **small JS islands** for interactivity (cart drawer, upsell, variant UX), so the merchant can manage content from Shopify Admin without code edits.

### 1.2 Definition of done (DoD)

**Visual parity (1:1)**
- Home / PLP / PDP / About / Quality / Returns match the draft: spacing, typography, component sizes, and states.
- Mobile + desktop parity (including sticky header and sticky PDP add-to-cart).
- Media is replaceable via Shopify Admin (product images, section image pickers).

**Functional**
- Add to cart works from PDP and from cart-drawer upsell (AJAX, no reload).
- Cart drawer quantity +/- and remove are correct and re-render state without breaking header/cart badge.
- Variant selection (chips) keeps URL/variant id correct and disables CTAs for unavailable variants.
- Upsell rules are correct (priority + suppression + no duplicates).

**Merchant-operable**
- Navigation menus come from Shopify “Menus”.
- Homepage content is editable via Theme Editor (sections/blocks).
- Product-specific data (upsell mapping, optional benefit copy) is editable via metafields/metaobjects.

**Quality**
- No Liquid errors; no console errors in theme.
- Theme Check passes (except explicitly accepted baseline warnings, if any).
- Accessibility sanity: focus visible, keyboard usable cart drawer, form labels, `aria-*` where needed.
- Performance sanity: no large blocking JS; images sized and lazy-loaded appropriately.

### 1.3 Constraints (do not fight these)
- Shopify themes are **multi-page**. Do not attempt SPA routing.
- Server-render first (Liquid); JS enhances behavior.
- Keep Dawn architecture intact; extend rather than rewrite.

### 1.4 Non-goals
- Headless rebuild (Hydrogen/Remix).

---

## 2) Architecture mapping (React → Dawn)

| React/SPA concept | Dawn / Shopify equivalent | LUSENA implementation notes |
|---|---|---|
| Routes/pages | `templates/*.json` | Home/PLP/PDP + page templates for About/Quality/Returns |
| Page components | `sections/*.liquid` | Each major “block” from draft becomes a section |
| Repeatable items | Blocks in section schema | Trust items, reviews, FAQ items, benefits, etc. |
| UI primitives | `snippets/*.liquid` | Icons + product cards; keep building atoms as snippets |
| Mock/static data | Shopify objects + theme settings + metafields/metaobjects | Use metafields for product-specific; metaobjects for reusable libraries |
| Interactivity/state | Dawn JS + small JS islands + `/cart/*.js` endpoints | Cart drawer, upsell add, PDP variant UX |

---

## 3) Output structure expectations (what exists + what to add)

### 3.1 Templates (JSON)
**Exists now**
- Home: `templates/index.json`
- PLP: `templates/collection.json`
- PDP: `templates/product.json`
- Pages: `templates/page.o-nas.json`, `templates/page.nasza-jakosc.json`, `templates/page.zwroty.json`

**Still recommended**
- Cart page parity (optional if cart drawer is primary): `templates/cart.json` (if you want a dedicated `/cart` design)
- Optional additional templates: `templates/page.faq.json` if FAQ becomes a separate page later

### 3.2 Sections (Liquid)
**Home**
- `sections/lusena-hero.liquid`
- `sections/lusena-trust-bar.liquid`
- `sections/lusena-problem-solution.liquid`
- `sections/lusena-bestsellers.liquid`
- `sections/lusena-heritage.liquid`
- `sections/lusena-testimonials.liquid`
- `sections/lusena-bundles.liquid` (repurposed as “Gift Ready”)
- `sections/lusena-faq.liquid`

**PLP**
- `sections/lusena-main-collection.liquid`

**PDP**
- `sections/lusena-main-product.liquid`

**Pages**
- `sections/lusena-page-about.liquid`
- `sections/lusena-page-quality.liquid`
- `sections/lusena-page-returns.liquid`

**Global**
- `sections/lusena-header.liquid`
- `sections/lusena-footer.liquid`

### 3.3 Snippets (Liquid)
- `snippets/lusena-icon.liquid` (Lucide subset)
- `snippets/lusena-product-card.liquid`
- Cart drawer lives in: `snippets/cart-drawer.liquid`

### 3.4 Assets
- `assets/lusena-shop.css` (Tailwind build output imported from the draft)
- `assets/lusena-animations.js` (GSAP scroll + hero intro)

---

## 4) Build strategy (Tailwind + parity)

### 4.1 Strategy used now (fastest 1:1)
- Keep Tailwind in the draft app and import a compiled output into the theme as `assets/lusena-shop.css`.

### 4.2 Recommended hardening (so edits stay maintainable)
**Option A (recommended): build Tailwind for Liquid**
- Add a small Tailwind build pipeline that scans:
  - `sections/**/*.liquid`, `snippets/**/*.liquid`, `templates/**/*.json`, `layout/**/*.liquid`
- Output to `assets/lusena-shop.css`
- Add a **safelist** for:
  - conditional classes (e.g., `bg-green-500` / `bg-red-500`)
  - state classes used by JS (`translate-y-full`, `active`, etc.)

**Rule:** avoid constructing Tailwind classes dynamically in Liquid; prefer fixed class strings + simple toggles.

---

## 5) Configurable vs hardcoded (decision framework + LUSENA rules)

### 5.1 Make configurable (Theme Editor / Admin)
**A) Content & merchandising**
- Headlines, subheadings, body copy
- Trust strip items (icon + title + subtitle)
- Featured collection for bestsellers
- Testimonials and FAQ entries
- Gift section copy and CTA
- Header menu + footer menus

**B) Bounded layout variants**
- Section visibility toggles
- Item counts (e.g., bestsellers product limit)
- Sticky ATC enable/disable (PDP)

**C) Upsell controls (guardrailed)**
- Enable/disable cart upsell
- Max tiles (1–2)
- Suppression threshold (distinct product count)
- Global fallback product
- Labels/copy (module title + “Add” label)

### 5.2 Hardcode (do not expose)
- Cart correctness: line item updates, totals, error handling
- Accessibility behaviors: focus trap, keyboard flow, aria relationships
- Performance-critical DOM structure required by Dawn JS
- Upsell decision engine logic (priority + suppression), while exposing only safe knobs

---

## 6) Data model plan (mock → Shopify objects)

### 6.1 Products (replace `lusena-shop/src/lib/products.ts`)
Create Shopify products matching draft handles (recommended to keep URLs consistent):
- `silk-pillowcase`
- `silk-sleep-mask`
- `silk-scrunchie`
- `heatless-curler`
- `silk-bonnet`

**Variants**
- Pillowcase: options like `Color`, `Size` (matches the draft chip UI).
- Others: `One size` single variant is fine.

**Media**
- Product images managed in Shopify Admin.
- Optional: attach additional gallery media for PDP parity (secondary image hover on cards).

### 6.2 Collections
- Use Shopify collections for merchandising:
  - `all` (Shopify auto)
  - optional: `pillowcases`, `accessories`, `bundles`

Homepage “Bestsellers” section should reference a collection selected in Theme Editor.

### 6.3 Pages + URLs
Shopify “Pages” live under `/pages/<handle>`. To match draft routes (root paths), create URL redirects:
- `/o-nas` → `/pages/o-nas`
- `/nasza-jakosc` → `/pages/nasza-jakosc`
- `/zwroty` → `/pages/zwroty`

Assign templates:
- Page `o-nas` → `page.o-nas`
- Page `nasza-jakosc` → `page.nasza-jakosc`
- Page `zwroty` → `page.zwroty`

### 6.4 Metafields (product-specific data)
**Required for upsell (see §7)**
Namespace: `lusena`
- `lusena.upsell_primary` (product reference)
- `lusena.upsell_secondary` (product reference)
- `lusena.upsell_suppress` (boolean)
- `lusena.upsell_role` (single line text: `hero` / `addon` / `bundle`)
- `lusena.upsell_message` (single line text; optional)

**Recommended for PDP content scaling (optional, but future-proof)**
- `lusena.pdp_emotional_headline` (single line text)
- `lusena.pdp_tagline` (single line text)
- `lusena.pdp_benefits` (list via metaobject references, or JSON string as MVP)
- `lusena.pdp_accordions` (metaobject references for title + rich text)

### 6.5 Metaobjects (structured reusable content)
Use metaobjects when you want the same items reused across pages:
- `lusena_testimonial` (author, quote, optional rating)
- `lusena_faq_item` (question, answer)
- `lusena_benefit_item` (title/text/icon)

MVP can keep testimonials/FAQ as section blocks; metaobjects are recommended once content grows or needs reuse.

### 6.6 Menus
Create menus in Shopify Admin:
- Header: `main-menu` (matches `sections/lusena-header.liquid` default)
- Footer: `footer-shop`, `footer-help` (or assign via Theme Editor settings)

---

## 7) Upsell implementation plan (Cart drawer + PDP)

**Source of truth:** `docs/LUSENA_Upsell_Spec_v1.md` (this section implements it in Shopify terms).

### 7.1 Surfaces
1. **Primary:** Cart drawer (1-tap add-on)
2. **Secondary:** PDP “Pairs well with” (below the fold)

### 7.2 Admin configuration (no code)
1. Create metafield definitions (Products) per §6.4.
2. Assign mappings:
   - Heatless Curler → primary: Bonnet, secondary: Scrunchie, role: `hero`
   - Pillowcase → primary: 3D Eye Mask, secondary: Scrunchie, role: `hero`
3. Mark bundle/set products:
   - `lusena.upsell_suppress = true`
   - `lusena.upsell_role = bundle`
4. (Optional) Install Search & Discovery and set complementary products for PDP.

### 7.3 Theme settings (guardrails)
Theme settings should expose only:
- enable/disable cart upsell
- max tiles (1–2)
- suppression threshold (distinct product count)
- global fallback product (Scrunchie)
- module title + add button label + fallback message

### 7.4 Decision engine (theme code)
Implement the spec without hardcoding product IDs by:
1. Determine “trigger product”:
   - Prefer the first cart line item with `lusena.upsell_role == hero`
   - Else fallback to first non-suppressed LUSENA product in cart
2. Candidate upsells:
   - `trigger.metafields.lusena.upsell_primary`
   - `trigger.metafields.lusena.upsell_secondary`
   - Optional global fallback (theme setting)
3. Filter:
   - Suppress module if:
     - distinct LUSENA products count ≥ threshold (default 2)
     - any cart item has `lusena.upsell_role == bundle` or `lusena.upsell_suppress == true`
   - Remove candidates already in cart
   - Remove unavailable/out-of-stock products
4. Limit output to max tiles (default 1, max 2).

### 7.5 AJAX add + re-render
- Use `/cart/add.js` for 1-tap adds
- Re-render cart drawer via Dawn section rendering (`sections` param) or existing `cart-drawer.js` APIs
- Must not break focus trap or header cart badge

### 7.6 PDP “Pairs well with”
Two viable modes:
- **Metafields mode:** read current product’s `upsell_primary/secondary` and show as “Pairs well with”
- **Search & Discovery mode:** render Shopify recommendations/complementary products

### 7.7 QA checklist (upsell)
- No upsell shown if already 2+ distinct items (default rule)
- No upsell shown when bundle present
- No duplicate offers (item already in cart)
- Out-of-stock items are not offered (or shown disabled per spec choice)
- Add works without reload; cart drawer updates correctly

---

## 8) Migration phases (do in this order)

### Phase 1 — Inventory + token freeze
- Extract tokens: colors, typography, spacing, radii, shadows.
- Create component inventory from draft and classify:
  - Section / Block / Snippet / JS island

**Deliverable:** token sheet + component inventory.

### Phase 2 — Dawn shell + styling
- Fonts, global CSS (Tailwind output), base layout parity.
- Ensure Tailwind build strategy is stable (see §4.2).

**Deliverable:** global styles locked + rebuildable.

### Phase 3 — Layout parity via templates + sections
Build/verify in this order:
1) Home  
2) PDP  
3) PLP  
4) Cart (drawer + optional cart page)  
5) Ancillary pages

**Deliverable:** pixel/spacing parity for primary pages.

### Phase 4 — Interactivity (JS islands only)
- Cart drawer UX (open/close, quantity, remove)
- Upsell add-to-cart
- PDP option chips + sticky ATC

**Deliverable:** SPA-like smoothness without SPA routing.

### Phase 5 — Replace mock data with Shopify data
- Products/collections/variants from Shopify Admin
- Marketing content moved to schema/blocks/metaobjects/metafields
- Navigation menus wired to Admin

**Deliverable:** merchant can operate store without code edits.

### Phase 6 — QA, performance, launch
- Run full QA checklist (see §10)
- Verify Lighthouse/Core Web Vitals basics
- Verify analytics events (if implemented)
- Push theme, create redirects, set primary theme

**Deliverable:** launch-ready theme + runbook.

---

## 9) Agent operating rules (guardrails)
1. Server-render first (Liquid); JS only enhances.
2. Use OS 2.0 properly: JSON templates + sections.
3. Do not hardcode homepage layout in `theme.liquid`.
4. Do not rewrite Dawn core unless required; prefer new sections/snippets.
5. Merchant-editable content must come from schema/metafields/metaobjects.
6. Avoid inline CSS; prefer compiled CSS + section CSS via `{% stylesheet %}`.
7. Accessibility is required (keyboard nav, focus, aria labels).
8. Keep JS light; no React in-theme unless explicitly approved.

---

## 10) QA checklist (definition of done)

### Visual parity
- Home / PDP / PLP / About / Quality / Returns match draft
- Breakpoints: mobile / tablet / desktop

### Functional
- Add to cart (PDP + upsell)
- Cart drawer updates correctly (quantity, remove, totals)
- Variant selection updates price + availability correctly
- URL redirects for `/o-nas`, `/zwroty`, `/nasza-jakosc`

### Quality
- No Liquid errors, no console errors
- Keyboard: open/close cart drawer, tab through controls, visible focus
- Images: correct aspect ratios, lazy loading where appropriate

---

## 11) Quick acceptance criteria
- Merchant-editable: hero content, featured collection, testimonials/FAQ, upsell toggles + picks.
- Hardcoded correctness: cart + variant handling + upsell filtering + accessibility behaviors.
- Parity: primary pages match mockup without per-page hacks.
