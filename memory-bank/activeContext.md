# Active Context

*Last updated: 2026-02-28*

## Current focus

**CSS & spacing standardization** — Ensuring all LUSENA-styled pages use the spacing tier system consistently, with unified typography and visual coherence across the entire store.

## Recent completed work

- Homepage v2 copy migration + newsletter capture section
- Quality page sections (hero, 6a, comparison table, final CTA)
- Returns page sections (hero, editorial, steps, FAQ, final CTA)
- About page sections (hero, story, values)
- PDP v2 proof blocks (truth table, quality evidence, feature highlights)
- Global spacing system standardization (tier classes, content-flow, gap utilities)
- Button system unification across PDP and cart
- Memory bank architecture restructuring (this session)

## Pending decisions

- CSS standardization scope: which pages to audit first, how deep to go
- Whether to clean up `lusena-missing-utilities.liquid` (rebuild Tailwind) now or defer

## Next steps

1. Complete CSS spacing audit across all LUSENA-styled pages
2. Ensure typography consistency (font families, sizes, weights) on every page
3. PDP migration backlog items (see `memory-bank/doc/features/pdp-migration-backlog.md`)
4. Homepage migration backlog items (see `memory-bank/doc/features/homepage-migration-backlog.md`)
5. Cart page LUSENA styling
6. Blog/article LUSENA styling
7. Remaining Dawn-default pages (search, 404, account, etc.)

## Known issues

- `lusena-missing-utilities.liquid` (351 lines) growing as Tailwind patch file — tech debt
- `main-product.liquid` (100KB) is dead code alongside `lusena-main-product.liquid`
- Dawn's spacing system (`--spacing-sections-desktop/mobile`) coexists with LUSENA's — intentionally neutralized but creates cognitive overhead
