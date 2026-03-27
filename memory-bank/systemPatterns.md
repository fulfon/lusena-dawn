# System Patterns

## CSS Architecture

### CSS layer stack

1. **Inline font-faces & root CSS** — Custom fonts (Inter, Source Serif 4), CSS custom properties
2. **Dawn base:** `assets/base.css` — Foundation styles
3. **Cart CSS** (conditional — `cart_type == 'drawer'`)
4. **Standalone LUSENA assets** (loaded globally via `<link>` in `theme.liquid`):
   - `lusena-foundations.css` (~40KB) — tokens, spacing, typography, components, body/main rules
   - `lusena-button-system.css` — button/icon-button primitives
   - `lusena-header.css` — header section styles
   - `lusena-hero.css` — hero section styles
   - `lusena-footer.css` — footer section styles
5. **Page-specific assets** (loaded per-page/section via `<link>` in their section):
   - `lusena-pdp.css` (~34KB) — PDP styles (loaded in lusena-main-product.liquid and lusena-main-bundle.liquid)
   - `lusena-cart-page.css` (634 lines) — cart items + footer + quantity styles (loaded in lusena-cart-items.liquid)
   - `lusena-search.css` (156 lines) — search page styles (loaded in lusena-search.liquid)
   - `lusena-bundle-pdp.css` — bundle PDP buy box styles (loaded in lusena-main-bundle.liquid)
   - `lusena-bundles.css` — bundle card grid (loaded in lusena-bundles.liquid)
6. **Component `{% stylesheet %}` blocks** — small section-scoped CSS only (~59KB compiled after 2026-03-26 extraction, 73KB hard limit)

### compiled_assets truncation guard (MANDATORY)
`{% stylesheet %}` blocks compile into `compiled_assets/styles.css` which **silently truncates at ~73KB**. Rules:
- **≤50 lines** section-scoped CSS → OK in `{% stylesheet %}`
- **>50 lines** or shared CSS → standalone `assets/lusena-*.css` file
- **After adding section CSS:** check compiled_assets size in DevTools — must stay **under 55KB**

> Full CSS architecture details + extraction steps: `memory-bank/doc/patterns/css-architecture.md`

## Naming conventions

- All LUSENA files: `lusena-*` prefix
- Sections: `sections/lusena-{component}.liquid`
- Snippets: `snippets/lusena-{component}.liquid`
- Assets: `assets/lusena-{name}.{css|js}`
- CSS classes: `lusena-spacing--*`, `lusena-content-flow*`, `lusena-gap-*`, `lusena-btn*`
- CSS variables: `--lusena-space-*`, `--lusena-section-*`, `--lusena-tier-*`

## Spacing system (LUSENA foundations is source of truth)

### Section padding: tier classes (values from `lusena-foundations.css`)
| Tier | Mobile | Desktop | Usage |
|------|--------|---------|-------|
| `lusena-spacing--full-bleed` | 0 | 0 | Edge-to-edge media |
| `lusena-spacing--compact` | 32px | 48px | Utility sections |
| `lusena-spacing--standard` | 48px | 64px | Informational content |
| `lusena-spacing--spacious` | 64px | 96px | Trust-building, CTAs |
| `lusena-spacing--hero` | 80px | 128px | Hero sections |

Modifier: `lusena-spacing--snug-top` — reduces top to 32/48px for heroes sharing bg with header.

### Container rhythm: content-flow utilities
- `lusena-content-flow` — 24px (standard)
- `lusena-content-flow--tight` — 16px (kicker + heading pairs)
- `lusena-content-flow--relaxed` — 32px (hero/editorial)

### Element gaps: semantic classes
`lusena-gap-kicker`, `lusena-gap-heading`, `lusena-gap-body`, `lusena-gap-cta`, `lusena-gap-cta-top`, `lusena-gap-section-intro`, `lusena-gap-subsection`

### Key spacing rules
1. Always use LUSENA classes, never hardcode spacing
2. When in doubt, go one tier up — premium feel means generous spacing
3. Prefer content-flow on parent over gap classes on children
4. Kicker+heading = wrap in `<div class="lusena-content-flow--tight lusena-gap-section-intro">`
5. Same-bg section gap is a floor (`max` formula), not additive — detector handles automatically
6. Snug-top modifier: use when hero has same bg as header

> Full specification: `memory-bank/doc/patterns/spacing-system.md`
> CSS source: `assets/lusena-foundations.css`

## Color scheme architecture

5 color schemes configured in Shopify admin:
| Scheme | Background | Usage |
|--------|------------|-------|
| scheme-1 | #F7F5F2 (brand-bg) | Default sections |
| scheme-2 | #F0EEEB (surface-2) | Alternating sections |
| scheme-3 | #2E2D2B | Dark accent sections |
| scheme-4 | #111111 | Full dark sections |
| scheme-5 | #8C6A3C (gold) | Gold accent sections |

## Animation conventions

- Scroll-reveal: Dawn's `scroll-trigger` system gated by `settings.animations_reveal_on_scroll`
- Pattern: `scroll-trigger animate--slide-in` (conditionally applied)
- Repeated items: `data-cascade` on container for stagger effect
- If element needs `transform` for layout, put scroll-trigger on a wrapper

## Component systems

- **Buttons:** `assets/lusena-button-system.css` + `snippets/lusena-button-system.liquid` — primary, outline, ghost, text, link variants (CSS in standalone asset, Liquid renders markup)
- **Icons (static):** `snippets/lusena-icon.liquid` — centralized SVG rendering
- **Icons (animated):** `snippets/lusena-icon-animated.liquid` + `assets/lusena-icon-animations.css` — 8 animated SVG icons (heart, layers, droplets, wind, shield-check, sparkles, gift, clock). Each icon has CSS animation classes on sub-elements. Stagger via `--lusena-anim-stagger` custom property. `prefers-reduced-motion` disables all animations. Falls back to static `lusena-icon` for unknown names. Loaded per-section (currently only in `lusena-pdp-feature-highlights`). Animation specs per product documented in `memory-bank/doc/products/{handle}.md`.
- **Product cards:** `snippets/lusena-product-card.liquid`
- **Breadcrumbs:** `snippets/lusena-breadcrumbs.liquid`
- **Final CTA:** `sections/lusena-final-cta.liquid` — generic reusable section (replaces per-page copies)
- **Upsell cards:** `.lusena-upsell-card` — unified container for cross-sell (`__xs-row`, `__xs-img`, `__xs-info`, `__xs-bottom`, `__xs-price`) and bundle two-tile (`__bn-headline`, `__bn-tiles`, `__bn-have`, `__bn-add`, `__bn-bottom`, `__bn-pricing`). CSS scoped per-surface: drawer selectors under `.lusena-cart-drawer__upsell` (inline `<style>`), cart page selectors under `.lusena-cart-upsell` (`assets/lusena-cart-page.css`). Gain-framed headlines, real product titles/images via `bundle_nudge_map` handles. Image placeholders use `:empty { display: block }` to override Dawn's `div:empty { display: none }` rule.

## Page migration workflow

Each page follows a **single-pass workflow** (Phases A–E). Read the full workflow and 18 lessons learned before migrating any page:

> **Mandatory reading:** `memory-bank/doc/patterns/migration-lessons.md`

Quick reference:
- **Phase A:** Plan — read template JSON, map Tailwind → foundations, identify bugs
- **Phase B:** Implement — replace classes, write section CSS, fix HTML bugs
- **Phase C:** Validate — `validate_theme`, grep for remaining Tailwind, `shopify theme check`
- **Phase D:** Visual verify — **use `/playwright-cli` skill with `-s=<name>`** (NEVER Playwright MCP tools, ALWAYS use named session) — desktop (1280x800) + mobile (375x812)
- **Phase E:** UX audit — conversion-focused review (dead ends, readability, balance, mobile, customer journey)

> Full design tokens: `memory-bank/doc/patterns/brand-tokens.md`
