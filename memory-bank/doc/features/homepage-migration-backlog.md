# Homepage V2 Migration Backlog

> Tracks bigger structural redesigns deferred from the initial v1→v2 homepage alignment pass.
> Each item references the brandbook v2 (`docs/LUSENA_BrandBook_v2.md`) specification.

---

## Status legend

- [ ] Not started
- [~] In progress
- [x] Done

---

## Deferred items

### 1. Bundles section — full product-card redesign

- [x] **Done (2026-03-07).** Rebuilt as 3-card grid with bundle image, name, CTA. Standalone CSS extracted to `assets/lusena-bundles.css`. Price display deferred until real bundle products are configured in Shopify admin.
- **Ref:** `LUSENA_BrandBook_v2.md:1245` (homepage item 7), `LUSENA_BrandBook_v2.md:1687` (Phase 1 bundle table).

### 2. Bestsellers — price anchors under product cards

- [x] **Done (2026-03-08).** Added `show_value_anchor` parameter to `lusena-product-card.liquid`. Computes per-night price (price ÷ 365), displayed in teal. Currently homepage bestsellers only.
- **Ref:** `LUSENA_BrandBook_v2.md:1245` (homepage item 4, "kotwica wartości").

### 3. Bestsellers — tier-based display ordering

- [ ] **What:** Enforce Tier 1 → Tier 2 product display order: (1) Poszewka 50×60, (2) Scrunchie bestseller or Scrunchie Trio, (3) Bundle "Nocna Rutyna" or Bonnet, (4) optionally Curler. Currently products come from collection sort order.
- **Ref:** `LUSENA_BrandBook_v2.md:97` (tier hierarchy), `LUSENA_BrandBook_v2.md:1245` (homepage item 4).
- **Why deferred:** Requires either a manual product list in the section schema, a dedicated "homepage-bestsellers" collection with manual sort, or tag-based tier sorting in Liquid.
- **Acceptance:** Products render in the specified tier order regardless of collection default sort.

### 4. Testimonials — UGC photo/screenshot grid

- [ ] **What:** Convert `lusena-testimonials` from text-only review cards to a UGC photo/screenshot grid with real customer images. Headline: "Tak śpią Polki" or "Sprawdzone przez [liczba] klientek".
- **Ref:** `LUSENA_BrandBook_v2.md:1245` (homepage item 6, "Grid 3-4 zdjęć UGC / screenów opinii").
- **Why deferred:** Requires UGC image sourcing, new card component with image + quote overlay, and potentially a review app integration (Judge.me, Loox, etc.).
- **Acceptance:** 3–4 UGC cards with customer photo, star rating, short quote excerpt, and author name. Link to full reviews page.

### 5. Hero — gentle-float product animation

- [ ] **What:** Add optional "gentle float" product animation on the hero section with `prefers-reduced-motion: static` fallback.
- **Ref:** `LUSENA_BrandBook_v2.md:1245` (homepage item 1, "Opcjonalnie").
- **Why deferred:** Low priority — purely aesthetic enhancement with no conversion impact. Requires careful motion design and performance testing.
- **Acceptance:** Subtle floating animation on a product element overlaid on the hero image, disabled when reduced motion is preferred.

### 6. Problem/Solution — expandable accordion alternative

- [ ] **What:** V2 mentions CTA option "Dlaczego to ważne? →" can either link to an educational page OR expand an inline accordion with more detail.
- **Ref:** `LUSENA_BrandBook_v2.md:1245` (homepage item 3, "prowadzi do strony edukacyjnej lub rozwija akordeon").
- **Why deferred:** Current link-to-page approach is functional. Accordion alternative is a nice-to-have UX enhancement.
- **Acceptance:** CTA toggles an inline details section with deeper educational content about silk vs cotton.

---

## Notes

- Items should be tackled one by one as separate PRs/commits.
- Each item should be verified with Playwright visual checks after implementation.
- Cross-reference `docs/LUSENA_BrandBook_v2.md` for exact copy and specifications.
