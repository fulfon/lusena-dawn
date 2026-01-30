# Shopify (Dawn) Migration — High-Level Plan for Coding Agent
**Source mockup:** React 19 + TypeScript + Tailwind SPA with static/mock data  
**Target:** Shopify **Online Store 2.0 theme** based on **Dawn**, matching frontend **1:1** (layout, spacing, typography, components) while making the *right* parts configurable in Admin/Theme Editor.

---

## 1) Goal and constraints

### Goal
Recreate the mockup UI/UX inside Dawn using **Liquid + JSON templates + sections/blocks + snippets**, with **small JS “islands”** for interactivity (cart, upsell, toggles), so the merchant can manage content from Shopify Admin.

### Constraints (do not fight these)
- Shopify themes are **multi-page** (not a true SPA). Do not attempt SPA routing.
- Server-render first (Liquid). JS enhances behavior.
- Keep Dawn core architecture intact; extend rather than rewrite.

### Non-goals
- Full headless Hydrogen/Remix rebuild.
---

## 2) Architecture mapping (React → Dawn)

| React/SPA concept | Dawn/Shopify theme equivalent |
|---|---|
| Routes/pages | `templates/*.json` (e.g., `index.json`, `product.json`, `collection.json`, `cart.json`) |
| Page components | **Sections** (`sections/*.liquid`) |
| Repeatable items | **Blocks** (inside section schema) |
| UI primitives (Button, Badge, Card) | **Snippets** (`snippets/*.liquid`) |
| Mock/static data | Shopify objects + Metafields + Metaobjects + Theme settings |
| Interactivity/state | Dawn JS + custom JS modules (“islands”) + `/cart/*.js` endpoints |

---

## 3) Output structure expectations (what to create)

### Templates (JSON)
- `templates/index.json` (Home)
- `templates/product.json` (PDP)
- `templates/collection.json` (PLP)
- `templates/cart.json` (Cart page)
- optional: `templates/page.faq.json`, `page.about.json`, etc.

### Sections (Liquid)
Create sections to mirror major mockup blocks (hero, benefits grid, featured products, testimonials, FAQ, upsell module, trust bar, etc.).

### Snippets (Liquid)
Create reusable UI snippets for shared atoms/molecules (button, icon, badge, price, rating, tag, etc.).

### Assets
- Tailwind compiled CSS (if using build step)
- minimal JS modules for interactive features

---

## 4) Build strategy (Tailwind + parity)

### Preferred approach (fastest 1:1)
- Keep Tailwind via build step and output a single compiled CSS file in `assets/`.
- Ensure Tailwind scans `.liquid` and `.json` files.
- Add a **safelist** for any conditional/dynamic classes.

**Rule:** avoid constructing Tailwind classes dynamically in Liquid where possible.

---

## 5) Configurable vs hardcoded (decision framework)

### Make configurable (Theme Editor / Admin)
**A) Content & merchandising**
- headings, subheadings, body copy
- images, icons, trust badges text
- featured products / collections selections
- testimonials, FAQ entries
- section visibility toggles

**B) Bounded layout variants**
- layout A/B toggles
- grid columns (3/4), alignment options
- spacing presets (compact/normal/airy)
- enable/disable sticky add-to-cart

**C) Upsell merchandising controls (guardrailed)**
- enable/disable upsell module
- placement toggles (PDP, cart drawer, cart page)
- max items to show (1–3)
- manual picks vs recommendations (mode)
- copy/labels

### Hardcode (do not expose as free-form settings)
- cart correctness + add-to-cart behavior
- accessibility behaviors (focus, keyboard, aria)
- performance-critical DOM structure and JS module boundaries
- analytics event contract (event names/payload schema)
- upsell **decision algorithm** (business logic), while exposing only safe parameters (thresholds/toggles/limits)

---

## 6) Data sources (where each type of data should live)

Use this rule: **content changes often → configurable; product-specific → metafields; structured reusable sets → metaobjects**.

### Theme settings / section schema
- simple marketing content (hero copy, trust bar, static benefits list)
- homepage blocks managed by merchant
- bounded layout switches

### Metafields (product-specific)
- PDP feature bullets / care instructions
- badge text (e.g., “22 momme”)
- upsell product references (manual upsell picks)

### Metaobjects (structured reusable content)
- testimonials library reused across pages
- FAQ sets reused across templates
- “benefit blocks” reused across sections/pages

---

## 7) Upsell implementation (target behavior)

Please read "C:\Users\Karol\Documents\BusinessIdeas\SilkStore\sklepOnline\shopify-lusena-dev\lusena-dawn\docs\LUSENA_Upsell_Spec_v1.md" for more details

---

## 8) Migration phases (do in this order)

### Phase 1 — Inventory + token freeze
- Extract design tokens (type scale, spacing, radii, shadows, colors).
- Create a component inventory from the React mockup and classify each component as:
  - Section / Block / Snippet / JS island.

**Deliverable:** Component inventory list + token definitions.

### Phase 2 — Dawn shell + styling
- Add fonts + base CSS (Tailwind compiled).
- Confirm baseline pages render with correct typography and spacing.

**Deliverable:** Theme loads with correct global styles.

### Phase 3 — Layout parity via templates + sections
Build in this order:
1) Home (index)  
2) PDP (product)  
3) PLP (collection)  
4) Cart (page + drawer)  
5) ancillary pages

**Deliverable:** Pixel/spacing parity for primary pages.

### Phase 4 — Interactivity (JS islands only)
- Cart drawer interactions
- Upsell add-to-cart
- variant selection extras (if required)
- accordions/tabs

**Deliverable:** SPA-like smoothness without SPA routing.

### Phase 5 — Replace mock data with Shopify data
- Product cards use Shopify product objects
- Marketing content moved to schema/blocks/metaobjects/metafields as defined above

**Deliverable:** Merchant can operate store without code edits.

---

## 9) Agent operating rules (guardrails)

1. **Server-render first:** Liquid outputs HTML; JS only enhances.
2. **Use OS 2.0 properly:** build pages with JSON templates + sections.
3. **Do not hardcode homepage layout** in `theme.liquid`.
4. **Do not rewrite Dawn core** unless explicitly required; prefer new sections/snippets.
5. **All merchant-editable content must come from schema/metafields/metaobjects**, not hardcoded strings.
6. **No inline CSS** unless truly unavoidable; prefer Tailwind/util classes or compiled CSS.
7. **Accessibility is required** (keyboard nav, focus states, aria labels).
8. **Performance:** avoid heavy JS; no React in-theme unless explicitly approved.

---

## 10) QA checklist (definition of done)

### Visual parity (1:1)
- Home / PDP / PLP / Cart match mockup: spacing, typography, component sizes, states
- Mobile + desktop parity

### Functional
- Add to cart works (PDP and upsell)
- Cart drawer updates correctly
- Upsell excludes items already in cart
- Variant selection behaves correctly

### Quality
- No Liquid errors, no console errors
- Basic accessibility: tab order, focus visible, aria where needed
- Performance sanity check (no unbounded JS, images optimized)

---

## 11) Quick acceptance criteria

- **Merchant-editable:** hero content, benefits/testimonials/FAQ, featured products, upsell toggles + picks.
- **Hardcoded correctness:** cart, variant handling, upsell algorithm filtering, accessibility behaviors.
- **Parity:** primary pages visually match mockup without manual per-page hacks.
