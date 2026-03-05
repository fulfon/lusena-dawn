# Product Context

## Why LUSENA exists

LUSENA exists to make premium silk accessories accessible and trustworthy in the Polish market. The store combines evidence-based product education with elegant shopping experience to convert skeptical browsers into loyal customers.

## Store pages (customer journey)

### Customer-facing pages (LUSENA-styled)
1. **Homepage** (`index.json`) — Brand first impression, trust signals, hero product showcase, social proof
2. **Collection page** (`collection.json`) — Browse products, filter, tier-based ordering
3. **Product page** (`product.json`) — Detailed evidence, proof blocks, buy flow
4. **Quality page** (`page.nasza-jakosc.json`) — Deep proof: momme, origin, certificates, fire test, comparison
5. **Returns page** (`page.zwroty.json`) — Frictionless returns messaging, trust building
6. **About page** (`page.o-nas.json`) — Brand story, heritage, values
7. **Cart page** (`cart.json`) — Full drawer parity: items + upsell cross-sell + totals/shipping/CTA footer
8. **Search page** (`search.json`) — Predictive search, product grid, empty state with bestsellers, Polish translations

### System pages (Dawn defaults, pending LUSENA styling)
- Blog, Article, 404, Password, Contact

### System pages (Shopify-managed, branded via admin)
- Checkout, Thank you, Sign in, Orders, Order status, Profile

## UX goals

- **Trust-first:** Every surface reinforces quality evidence before asking for purchase
- **Premium feel:** Generous spacing, elegant typography, muted warm color palette
- **Conversion-focused:** Strategic CTA placement, proof blocks near buy buttons
- **Mobile-first:** All layouts responsive, key flows optimized for mobile (md: 768px primary breakpoint)
- **Cohesive:** Consistent spacing, typography, and interaction patterns across all pages

## Customer journey flow

```
Awareness          → Interest            → Decision           → Action
Homepage hero      → Trust bar           → PDP evidence       → Buybox CTA
Problem/solution   → Testimonials        → Comparison tables  → Sticky ATC
                   → Heritage tiles      → Quality page       → Cart drawer
```

## Reusable sections (shared across pages)

- `lusena-trust-bar` — appears on homepage, quality page, about page
- `lusena-faq` — appears on homepage, quality page, returns page, and PDP
- `lusena-final-cta` — appears on about page, quality page, returns page
