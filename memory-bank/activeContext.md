# Active Context

*Last updated: 2026-03-29*

## Current focus

**Phase 1B: PDP cross-sell checkbox** - scrunchie at 39 zl on poszewka PDP. This is the last remaining item from the bundle/upsell system.

## Recent completed work

### Card 5 creative sessions — all 8 products DONE (2026-03-28)

Feature card 5 freed from universal OEKO-TEX (already covered by quality evidence section + specs accordion). Each product now has a product-specific card 5 with unique angle:

| Product | Title | Icon | Angle |
|---------|-------|------|-------|
| Poszewka | Czysty jedwab, czysta skóra | sparkles | Material purity / 8h face contact |
| Bonnet | Olejek zostaje we włosach | droplets | Product retention (oils/masks work overnight) |
| Maska 3D | Nawet gumka jest jedwabna | feather | Silk-covered elastic band detail |
| Scrunchie | Bez śladu po gumce | feather | Crease-free / no visible marks |
| Heatless Curlers | Miękki - nie uciska w nocy | feather | Open-crown sleep comfort |
| Nocna Rutyna | Poranek bez porannej rutyny | sparkles | Morning result of both products |
| Piękny Sen | Nic nowego w Twojej rutynie | clock | Zero-effort material swap |
| Scrunchie Trio | Po prostu jedwab | sparkles | Silk as new normal (1→3 shift) |

All 8 went through full creative workflow: Polish copywriter agent → legal check → customer validation (2-3 runs each) → refinement → finalization. Detailed session logs in each product MD file.

**Universal cards reduced from 4 to 3:** positions 2, 4, 6 (was 2, 4, 5, 6). Updated across all product docs, metafields reference, setup checklist, import script, re-evaluation prompts, AGENTS.md, copilot-instructions.md.

### Icon consistency overhaul + 3 new animated icons (2026-03-28)

**New semantic icon system** defined in `product-setup-checklist.md`:
- `heart` = gentle on body, `wind` = cool & gentle, `droplets` = locks moisture in
- `sparkles` = radiant & fresh, `moon` = all night/every night, `clock` = fits your routine
- `feather` = weightless & traceless, `palette` = your colors

**Icons reassigned** across products to match semantic meanings (e.g., Bonnet C3 `wind`→`moon` for "stays on all night", Scrunchie Trio C1 `droplets`→`palette` for "color variety").

**3 new animated SVGs** added to `lusena-icon-animated.liquid` + `lusena-icon-animations.css`:
- `moon` — gentle glow pulse (scale 1→1.04→1, opacity 1→0.82→1), 8s
- `feather` — subtle float (translateY 0→-2px→0, rotate ±1°), 8s
- `palette` — sequential swatch opacity pulse across 3 circles, 7s

All with `prefers-reduced-motion` fallback. Schema dropdown in `lusena-pdp-feature-highlights` updated.

### Quality evidence accordion rewrite (2026-03-28)

Rewrote `lusena-pdp-quality-evidence.liquid` accordion JS and CSS:
- **Animation:** `max-height`/opacity → explicit `height` transitions with `requestAnimationFrame` for smooth open/close
- **State management:** `.is-open` class → `data-state` attribute (`open`/`closed`/`closing`)
- **Accessibility:** `prefers-reduced-motion` → instant open/close (no transitions)
- **CSS:** `contain: layout style` on items, `-webkit-tap-highlight-color: transparent`, `will-change: height`
- **Cleanup:** Arrow functions → `function` declarations (consistent with Dawn's JS style)

### Claude Code infrastructure (2026-03-28)

**Hooks** (`.claude/hooks/`, 5 scripts):
- `guard-dawn-edit.sh` — PreToolUse: blocks editing Dawn originals when lusena-* counterpart exists
- `session-context.sh` — SessionStart: injects activeContext.md focus/next/issues
- `post-compact-rules.sh` — PostCompact: re-injects critical LUSENA rules after context compaction
- `theme-check-on-edit.sh` — PostToolUse: runs `shopify theme check` on edited .liquid files
- `task-quality-gate.sh` — TaskCompleted: runs theme check on recently modified lusena-* files

**Rules** (`.claude/rules/`, 6 files):
- `animations.md`, `bundle-system.md`, `cart-system.md`, `css-and-assets.md`, `css-cascade.md`, `product-metafields.md`
- Auto-load by file path patterns (e.g., css-cascade loads when editing `assets/*.css`)

**Skills** (2 new):
- `lusena-new-section` — scaffolds a new LUSENA section with correct boilerplate
- `lusena-product-copy-session` — orchestrates full creative copy workflow

**Settings** (`.claude/settings.json`): shared settings with all hook configurations + deny rules.

**CLAUDE.md refactored:** CSS architecture, compiled_assets guard, product metafields, and animation rules moved to `.claude/rules/` (auto-loaded). Added Bash command restrictions ($(), backticks, grep/cat/sed).

### Minor fixes (2026-03-28)

- `assets/cart.js` — null guard on `trapFocus` when `.drawer__inner-empty` missing
- `snippets/lusena-pdp-scripts.liquid` — `is-gesturing` class toggle on lightbox image during touch
- `templates/index.json` — benefit bridge hair card icon `star` → `wind`
- `memory-bank/doc/products/imports/generate_import_from_export.py` — all 8 products updated with card 5 values

### Cart interaction locking during bundle swap (2026-03-29)

Added full-cart interaction locking when "zamień na zestaw" / "dodaj do zestawu" swap is in flight:
- **Cart page:** `cart__items--disabled` class on `#main-cart-items` — blocks all qty/remove/upsell interactions. Explicitly removed after `reRenderSections()` on success (container element survives innerHTML swap). Removed on error.
- **Cart drawer:** `lusena-cart-drawer__item--loading` on ALL `[data-cart-item]` rows + all buttons disabled. Cleaned up naturally on success (full DOM replacement). Restored on error.
- **Cross-sell "Dodaj":** Not locked — single add doesn't conflict with existing item mutations.

Key lesson: `reRenderSections()` replaces `.js-contents` innerHTML, but the parent `#main-cart-items` element persists — classes on it must be manually cleaned up.

## Next steps

1. **Phase 1B: PDP cross-sell checkbox (NEXT TASK)** — scrunchie at 39 zl on poszewka PDP

## Known issues

- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- **Swap race condition:** If `/cart/add.js` succeeds but `/cart/change.js` fails, customer has both items in cart. #13 cart merge handles this - the merge card appears on next render, offering to combine them.
- **Trigger item quantity > 1:** Swap removes all units (quantity 0), not just 1.
- **Cart color editing:** Bundle added via nudge auto-matches colors. Customer cannot change colors in cart — must use bundle PDP.

## Architecture note

**Cart drawer is now a section** (not a snippet render). `theme.liquid` uses `{%- section 'cart-drawer' -%}`. This enables Shopify's section rendering API for AJAX updates.

**Upsell card CSS scoping:**
- Cart drawer: `<style>` tag in `snippets/cart-drawer.liquid`. All upsell selectors scoped under `.lusena-cart-drawer__upsell`.
- Cart page: `assets/lusena-cart-page.css` (standalone file). Upsell selectors scoped under `.lusena-cart-upsell`.
- This prevents CSS bleed between drawer (loads on every page) and cart page (loads only on /cart).

**Bidirectional cart sync:**
- Cart page → drawer: publishes `PUB_SUB_EVENTS.cartUpdate`, drawer subscriber fetches fresh section HTML
- Drawer → cart page: publishes `PUB_SUB_EVENTS.cartUpdate`, cart page `onCartUpdate()` override fetches sections
- Both use `DOMParser` to swap inner HTML of target containers
