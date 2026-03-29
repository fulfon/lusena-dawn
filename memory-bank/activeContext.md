# Active Context

*Last updated: 2026-03-29*

## Current focus

**Phase 1B: PDP cross-sell checkbox — IN PROGRESS (final polish + testing).** Core feature works, UI redesigned and polished. Remaining: interaction testing, scope verification, bundle PDP expansion, cart explanation label.

## Recent completed work

### PDP cross-sell checkbox — UI/UX redesign (2026-03-29, session 2)

Full visual redesign of the cross-sell card to match LUSENA's premium aesthetic:

**Design decisions:**
- **White card** with 3px teal left accent (`color-mix(... accent-cta 40% ...)`, full on hover/check)
- **Compact single row:** checkbox (16px) + image (40px) + title/hint + pricing
- **"Taniej w komplecie"** educational hint instead of "Kolor:" text
- **Image-only color communication** — no color text label; image auto-matches when main product color changes
- **Image placeholder** always renders (`surface-2` bg + dashed border, matching cart drawer upsell pattern)
- **Strikethrough price** matches cart drawer style (1.2rem, `text-2`, no opacity reduction)
- **Scroll animation** — `scroll-trigger animate--slide-in` gated by `animations_reveal_on_scroll`
- **Spacing** — `margin-top: 1.6rem` on wrapper, matching buy-box rhythm

**Bug fixes (same session):**
- **Button loading animation** — `setBtnLoading()` helper targets actual `<button>` (was targeting `<product-form>` wrapper, no animation played)
- **Double-add bug** — removed duplicate cross-sell handler from `lusena-pdp-scripts.liquid` `{% javascript %}` block (code was NOT dead as assumed — compiled_assets JS included it)
- **Double-click guard** — `aria-disabled` check at top of both ATC and Buy Now handlers
- **Idempotency guard** — `data-lusena-cross-sell-init` prevents re-initialization on hot reload

### PDP cross-sell checkbox — core implementation (2026-03-29, session 1)

Cross-sell checkbox on all individual product PDPs offering scrunchie at 39 zl (BXGY discount in Shopify admin).

**Strategic decisions (changed from original plan):**
- **All individual PDPs** (not poszewka-only) — consistent pricing builds trust for new brand
- **Free shipping threshold 275 zl** (was 289) — bonnet (239) + scrunchie (39) = 278 > 275 clears threshold
- **Shopify BXGY automatic discount** handles real pricing; theme displays preview price via section setting

**Key technical decisions (discovered during implementation):**
- `all_products[handle]` instead of product picker setting — Shopify dev server doesn't resolve product picker GIDs from file sync
- Inline `<script>` instead of `{% javascript %}` — compiled_assets JS truncation (same ~73KB limit as CSS)
- `/cart/add.js` instead of `/cart/add` — dev server returns 302 without `.js` extension
- ATC intercept on parent `<product-form>` element with `{ capture: true }` — at the target element, capture doesn't help
- Cart drawer re-render via direct section fetch + `DOMParser` + `drawer.open()`



### Benefit bridge redesign (2026-03-29)

Major redesign of `lusena-benefit-bridge.liquid`:
- **Kicker field** above heading ("Jedwab morwowy 22 momme")
- **Featured card** modifier on first card (`.lusena-benefit-bridge__card--featured`)
- **Accent bar** (teal left-border via `.lusena-benefit-bridge__accent-bar`)
- **Transition text** below cards ("Wszystkie trzy - bez żadnej zmiany w rutynie.")
- **CSS extraction** from `{% stylesheet %}` → standalone `assets/lusena-benefit-bridge.css`
- **Copy refresh**: heading "Co zobaczysz rano?", rewritten card text and icons
- Schema expanded with kicker, transition_text fields

### `lusena-link-arrow` CSS component (2026-03-29)

New foundation component in `lusena-foundations.css` — CSS-only chevron via SVG mask (`::after` pseudo-element), inherits `currentColor`, hover slides 2px right. Replaces all hardcoded `→` arrow characters sitewide. Applied to:
- `lusena-heritage` (button), `lusena-problem-solution` (CTA), `lusena-quality-hero` (CTA button)
- `lusena-pdp-quality-evidence` (accordion CTAs), `lusena-article-card` (read more)
- `lusena-pdp-media` (certificate CTA)
- All `→` removed from template JSON defaults and FAQ answer HTML

### Bundle options initial state fix (2026-03-29)

`lusena-bundle-options.liquid` — first step renders open (`is-active`, fieldset visible), subsequent steps render collapsed with pending chips (`is-pending`, `is-next` on step 2). Was: all steps rendered open initially.

### Bundle PDP chip dot fix (2026-03-29)

`lusena-bundle-pdp.css` — pending chip dot changed from filled (`background: var(--lusena-accent-cta)`) to transparent outline (`background: transparent; border-color: var(--lusena-accent-cta)`). Visually distinguishes pending from completed steps.

### Cart cross-sell loading refactor (2026-03-29)

`lusena-cart-items.liquid` — replaced custom `lusena-upsell-card__dots` (3-dot pulse animation) with standard `loading__spinner` + `lusena-btn__loading-dots` pattern. Removed 10 lines of dedicated dot CSS from `lusena-cart-page.css`. Button now uses `.loading` class toggle instead of hiding/showing separate text/dots spans.

### Token compliance rule (2026-03-29)

Added mandatory "Token compliance" section to `.claude/rules/css-and-assets.md`:
- Colors: always `var(--lusena-*)`, opacity via `color-mix()`
- Typography: use foundation type classes in Liquid
- Icons: `lusena-icon-circle` + `lusena-icon-*` sizes
- Spacing: `var(--lusena-space-*)` only
- Transitions: `var(--lusena-transition-fast/base)` only
- Radius: `var(--lusena-btn-radius)` only
- Dawn traps: `div:empty` specificity, `blockquote` styles

### No-inline-scripts rule (2026-03-29)

New rule `.claude/rules/no-inline-scripts.md` — bans `node -e`, `python -c`, and multi-line Bash scripts for file analysis. Requires Grep/Glob/Read tools instead. Added to `CLAUDE.md` conventions.

### Section design loop skill (2026-03-29)

New skill `.claude/skills/lusena-section-design-loop/SKILL.md` — autonomous design iteration loop: prototype in React draft shop, validate with 5-agent Sonnet review panel, iterate up to 5 rounds.

### Migration lessons #55-61 (2026-03-29)

7 new lessons in `migration-lessons.md` from benefit bridge redesign:
- #55 `color-mix()` for opacity variants, #56 foundation type classes in Liquid
- #57 `lusena-icon-circle` + size classes, #58 `div:empty` trap for accent bars
- #59 reviewer agents must not have write access, #60 forward-reference problem on mobile
- #61 mobile card treatment (avoid merged white blocks)

### Bundle feature card copy (2026-03-29)

`product.bundle.json` — "Gotowe do wręczenia" → "Gotowe do wręczenia osobno" with expanded description about individual gift packaging.

## Next steps

1. **Cross-sell: Buy Now + Sticky ATC testing** — verify both work with checkbox checked
2. **Cross-sell: Scope verification** — confirm hidden on scrunchie PDP + bundle PDPs
3. **Cross-sell: Bundle PDP expansion** — add render slot to `lusena-main-bundle.liquid` + verify BXGY admin covers bundles
4. **Cross-sell: Cart discount explanation** — "Rabat za zakup w zestawie" label on discounted line items (option B)
5. **Cross-sell: Scrunchie PDP education** — show discount info when qualifying product is in cart
6. **Documentation updates** — threshold 289→275 refs in bundle-strategy.md

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
