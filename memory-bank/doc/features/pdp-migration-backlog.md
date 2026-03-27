# PDP V2 Migration Backlog

> Tracks structural/product-data tasks deferred from the initial PDP v2 alignment pass.
> Each item references brandbook v2 (`memory-bank/doc/brand/LUSENA_BrandBook_v2.md`) requirements.

---

## Status legend

- [ ] Not started
- [~] In progress
- [x] Done

---

## Deferred items

### 1. Checkbox upsell directly under primary CTA

- [ ] **What:** Add a frictionless checkbox upsell under the primary CTA in the buybox (e.g. "Dodaj pasującą scrunchie (-XX% w zestawie)"), with product-type-specific logic for pillowcase/scrunchie/bonnet/curler where relevant.
- **Ref:** `memory-bank/doc/brand/LUSENA_BrandBook_v2.md:1412`, `memory-bank/doc/brand/LUSENA_BrandBook_v2.md:1725`, `memory-bank/doc/brand/LUSENA_BrandBook_v2.md:2018`.
- **Why deferred:** Requires pricing/discount logic, product mapping rules, and likely cart integration work to avoid conversion regressions.
- **Acceptance:** Checkbox appears below CTA, correctly adds upsell line item with expected bundle treatment, and remains scoped to valid product contexts.

### 2. Reviews widget/rating section on PDP

- [ ] **What:** Add review module with rating summary, filtering/sorting, photo support, and "zobacz wszystkie" path.
- **Ref:** `memory-bank/doc/brand/LUSENA_BrandBook_v2.md:1407`, `memory-bank/doc/brand/LUSENA_BrandBook_v2.md:1562`.
- **Why deferred:** Requires selecting/integrating a review platform and mapping theme placement/styling to app output.
- **Acceptance:** PDP shows rating summary plus interactive reviews list consistent with LUSENA typography and spacing.

### 3. Out-of-stock "Notify me" capture flow

- [ ] **What:** Replace disabled ATC-only behavior with "Powiadom mnie o dostępności" email capture when variant is unavailable.
- **Ref:** `memory-bank/doc/brand/LUSENA_BrandBook_v2.md:2035`.
- **Why deferred:** Needs lead-capture backend/app integration and variant-level availability subscription handling.
- **Acceptance:** For unavailable variants, ATC is replaced by notify CTA and email capture flow works end-to-end.

### 4. Cleanup of currently unused PDP schema settings

- [ ] **What:** Resolve unused settings on `sections/lusena-main-product.liquid`: `trust_shipping`, `trust_oeko`, `delivery_qualifies_label`, `delivery_free_fallback_label`, `guarantee_body`, `video_placeholder`.
- **Ref:** audit note from PDP v2 migration pass (config drift risk).
- **Why deferred:** Non-blocking cleanup decision: either wire each setting into live UI or remove from schema/template to prevent editor confusion.
- **Acceptance:** No dead settings left in PDP schema/template; each setting is either actively rendered or removed.

---

## Notes

- Current pass implemented: trust-bar tightening (3 chips) and new "Jedwab vs satyna: tabela prawdy" section.
- Gallery/video-first behavior intentionally left unchanged in this pass per decision.
