# Active Context

*Last updated: 2026-03-25*

## Current focus

**Cart upsell UI — cart drawer and cart page fully polished, ready for end-to-end testing.** Both surfaces share unified design: gain-framed headlines, real product titles/images via restructured `bundle_nudge_map`, scrollable upsell positioning, consistent cross-sell bottom-row layout. compiled_assets truncation at 85KB needs extraction in next session.

## Recent completed work

### Cart upsell UI polish — cart drawer + cart page (2026-03-25)

**Bug fixes:**
- **Image placeholder 0x0 root cause found:** Dawn's `base.css` line 473 has `div:empty { display: none }` — hides ALL empty divs. Fixed with `.lusena-upsell-card__bn-add-img:empty { display: block }` (specificity `0,2,0` beats `div:empty` `0,1,1`). Same fix applied to cross-sell image (`.lusena-upsell-card__xs-img:empty`)
- **HTML nesting error:** Moving upsell inside scrollable body broke `<cart-drawer>` nesting — body `</div>` was placed outside `{%- endif -%}`. Fixed and verified via `shopify theme check` (0 errors)

**Cart drawer changes:**
- Removed redundant savings chip ("Oszczedzasz X zl") — headline already communicates savings
- Removed "Kontynuuj zakupy" button — redundant with X close button
- "Was" price: bigger (1.4rem) and darker (`--lusena-text-2`) — now visible as discount anchor
- Image placeholders: dashed border + background on all empty image containers (bundle have/add tiles + cross-sell)
- Check mark badge: repositioned to top-right corner (`top: -0.7rem; right: -0.7rem`), parent `overflow: visible`, img gets own `border-radius`
- Plus sign: darker color (`--lusena-text-2`), heavier weight (400)
- Tiles vertically centered: `justify-content: center` on both tiles, `margin-top: 0.7rem` on have-img to compensate for badge overhang
- Mobile `justify-content` reset to `flex-start` (prevents horizontal centering in row direction)
- **Upsell moved inside scrollable body** — no longer fixed between body and footer. Scrolls naturally with cart items on all screen sizes. Eliminated all height-threshold media queries.
- Cross-sell card restructured: price + button moved to bottom row (matches bundle card's `bn-bottom` pattern)

**Data architecture:**
- `bundle_nudge_map` metafield restructured from flat strings to objects: `{"label": "accusative name", "handle": "product-handle", "tile_label": "optional override"}`
- Real product titles resolved via `all_products[nudge_entry.handle]` — tile shows actual product name (nominative) while headline keeps accusative form
- Real product images resolved via `added_component.featured_image` — shows component product's image instead of bundle's empty image
- `tile_label` field for Scrunchie Trio: "2x Scrunchie jedwabny"
- Fallback chain: `nudge_entry.label | default: nudge_entry` for backward compatibility with old flat string format

**Cart page changes (lusena-cart-items.liquid):**
- All drawer changes mirrored: nudge_map restructure, real titles/images, no savings chip, visible "was" price, placeholder styling, check mark repositioning, plus sign visibility, tile centering, cross-sell bottom-row layout
- Desktop: upsell card constrained to `max-width: 42rem`, right-aligned (`margin-left: auto`), accent `border-left` removed
- Desktop: label aligned with card (same `max-width` + `margin-left: auto`)
- Full-width separator line preserved (`.lusena-cart-upsell` border-top spans full content width)

**Compact layout (max-height: 700px):**
- Kept for iPhone SE and small Androids: reduced header/footer padding, smaller upsell zone padding, smaller image sizes

**Metafield values set in Shopify admin:**
- Nocna Rutyna: `{"poszewka-jedwabna":{"label":"czepek jedwabny","handle":"silk-bonnet"},"silk-bonnet":{"label":"poszewke jedwabna","handle":"poszewka-jedwabna"}}`
- Piekny Sen: `{"poszewka-jedwabna":{"label":"maske 3D","handle":"jedwabna-maska-3d"},"jedwabna-maska-3d":{"label":"poszewke jedwabna","handle":"poszewka-jedwabna"}}`
- Scrunchie Trio: `{"silk-scrunchie":{"label":"dwie kolejne jedwabne gumki","handle":"silk-scrunchie","tile_label":"2x Scrunchie jedwabny"}}`

### Previous session summary (2026-03-24)

Cart upsell UI redesign — brainstorming + initial implementation. 5 commits. See `docs/superpowers/specs/2026-03-24-cart-upsell-ui-redesign.md` for spec.

## Next steps

1. **CRITICAL: Extract cart page CSS to standalone asset** — `compiled_assets/styles.css` is 85KB, truncated at ~73KB. `lusena-cart-items.liquid` `{% stylesheet %}` block is a prime candidate for extraction to `assets/lusena-cart-page.css`. Last CSS rules are being silently dropped.
2. **End-to-end testing** — cross-sell (all products), all 3 bundle swaps (Nocna Rutyna, Piekny Sen, Scrunchie Trio), cart page + cart drawer
3. **Commit** all current changes
4. **#13 Cart merge** — detect when both bundle components are in cart separately, suggest "Zamien na zestaw"
6. **#12 PDP bundle detection banner** — "Masz poszewke w koszyku?" when cart has complement
7. **Phase 1B: PDP cross-sell checkbox** — scrunchie at 39 zl on poszewka PDP

## Known issues

- **compiled_assets truncation (CRITICAL):** File is 85KB, silently truncated at ~73KB. Last rules in file are cut off mid-property. Cart page `{% stylesheet %}` block needs extraction to standalone CSS asset. Confirmed via Playwright: file ends mid-rule (`font-size: 1.2rem;` without closing brace).
- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- `snippets/lusena-pdp-styles.liquid` is a doc-only stub (CSS moved to `assets/lusena-pdp.css`)
- **Swap race condition:** If `/cart/add.js` succeeds but `/cart/change.js` fails, customer has both items in cart. #13 (cart merge) will handle this.
- **Trigger item quantity > 1:** Swap removes all units (quantity 0), not just 1.
- **Cart color editing:** Bundle added via nudge auto-matches colors. Customer cannot change colors in cart — must use bundle PDP.

## Architecture note

**Upsell card CSS placement:**
- Cart drawer: `<style>` tag inside `snippets/cart-drawer.liquid` (~150 lines). Not in compiled_assets.
- Cart page: `{% stylesheet %}` block in `sections/lusena-cart-items.liquid`. Compiles into `compiled_assets/styles.css`. **Currently truncated — needs extraction.**

**Upsell HTML position:**
- Cart drawer: upsell zone is INSIDE the scrollable `.lusena-cart-drawer__body` div (after cart items, before body close). Scrolls with items on all screen sizes.
- Cart page: upsell is inside `.js-contents` div, after cart items list.

**Cross-sell card layout change:** Price + button moved from right-side column (`xs-aside`) to full-width bottom row (`xs-bottom`). Same visual rhythm as bundle card's `bn-bottom`. Applied to both drawer and cart page.

CSS load order unchanged. compiled_assets is now 85KB (was ~38KB noted previously — growth from cart page and other section stylesheets).
