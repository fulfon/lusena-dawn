---
description: Quick-reference catalog of all LUSENA sections — page, tier, CSS, JS
---
# LUSENA Section Catalog

**CSS** = standalone `assets/lusena-*.css` | **JS** = `<script>` or `{% javascript %}`

## Global (every page via layout groups)
| Section | CSS | JS | Notes |
|---------|-----|-----|-------|
| `lusena-header` | YES (lusena-header.css) | YES | Auto-hide + mobile menu |
| `lusena-footer` | - | - | |

## Homepage (`index.json`)
| Section | Tier | CSS | Notes |
|---------|------|-----|-------|
| `lusena-hero` | full-bleed | - | Standalone CSS via lusena-hero.css |
| `lusena-trust-bar` | custom padding | - | Reused on 3 pages |
| `lusena-benefit-bridge` | standard | YES (lusena-benefit-bridge.css) | Kicker, 3 benefit cards (first featured), accent bar, transition text |
| `lusena-bestsellers` | spacious | - | Uses `lusena-product-card` snippet |
| `lusena-testimonials` | spacious | - | |
| `lusena-problem-solution` | spacious | - | Moved to pos 6 for evaluation flow |
| `lusena-bundles` | spacious | YES | Product-driven full-card links, mobile compact rows, shared badge overlay, savings badge, hover underline |
| `lusena-heritage` | spacious | - | |
| `lusena-faq` | standard | - | Reused on 5 pages |
| `lusena-final-cta` | spacious | - | Reused on 5 pages |
| `lusena-newsletter` | standard | - | Reused on 2 pages |

## PDP — Standard (`product.json`)
| Section | Tier | CSS | Notes |
|---------|------|-----|-------|
| `lusena-main-product` | compact | YES (lusena-pdp.css) | Delegates to 13 snippets |
| `lusena-pdp-feature-highlights` | standard | YES | 6 feature cards from metafields |
| `lusena-pdp-quality-evidence` | standard | - | JS: `{% javascript %}` |
| `lusena-pdp-truth-table` | standard | - | Uses `.lusena-truth-table` from foundations |
| `lusena-faq` | standard | - | Shared |
| `lusena-final-cta` | spacious | - | Shared |

## PDP — Bundle (`product.bundle.json`)
| Section | Tier | CSS | Notes |
|---------|------|-----|-------|
| `lusena-main-bundle` | compact | YES (lusena-bundle-pdp.css) | Progressive disclosure steps |
| `lusena-pdp-feature-highlights` | standard | YES | Shared |
| `lusena-pdp-quality-evidence` | standard | - | Shared |
| `lusena-pdp-truth-table` | standard | - | Shared |
| `lusena-faq` | standard | - | Shared |
| `lusena-final-cta` | spacious | - | Shared |

## Cart (`cart.json`)
| Section | Tier | CSS | Notes |
|---------|------|-----|-------|
| `lusena-cart-items` | compact | YES (lusena-cart-page.css, 625 lines) | AJAX re-render, upsell |
| `lusena-cart-footer` | - | - | Totals + checkout button |

## Collection (`collection.json`)
| Section | Tier | Notes |
|---------|------|-------|
| `lusena-main-collection` | compact | Product grid |

## Quality (`page.nasza-jakosc.json`)
| Section | Tier | Notes |
|---------|------|-------|
| `lusena-quality-hero` | hero + snug-top | |
| `lusena-trust-bar` | custom | Shared |
| `lusena-quality-origin` | spacious | |
| `lusena-quality-momme` | standard | |
| `lusena-quality-certificates` | spacious | |
| `lusena-quality-fire-test` | standard | |
| `lusena-quality-qc` | standard | |
| `lusena-quality-comparison-table` | standard | Uses `.lusena-truth-table` |
| `lusena-faq` | standard | Shared |
| `lusena-final-cta` | spacious | Shared |

## About (`page.o-nas.json`)
| Section | Tier | Notes |
|---------|------|-------|
| `lusena-about-hero` | hero + snug-top | |
| `lusena-about-story` | spacious | |
| `lusena-about-values` | standard | |
| `lusena-trust-bar` | custom | Shared |
| `lusena-final-cta` | spacious | Shared |

## Returns (`page.zwroty.json`)
| Section | Tier | Notes |
|---------|------|-------|
| `lusena-returns-hero` | hero + snug-top | |
| `lusena-returns-steps` | spacious | |
| `lusena-returns-editorial` | standard | |
| `lusena-faq` | standard | Shared |
| `lusena-returns-final-cta` | spacious | |

## Other pages
| Section | Template | Tier | Notes |
|---------|----------|------|-------|
| `lusena-search` | `search.json` | standard | YES standalone CSS |
| `lusena-404` | `404.json` | standard | |
| `lusena-article` | `article.json` | compact | |
| `lusena-blog` | `blog.json` | compact | |
| `lusena-contact-form` | `page.contact.json` | compact | |
| `lusena-main-page` | `page.json` | compact | Generic richtext |

## Unused (not in any template)
| Section | Notes |
|---------|-------|
| `lusena-comparison` | Draft/archived |
| `lusena-quality-6a` | Draft/archived |
| `lusena-science` | Draft/archived |

## Most reusable sections
- `lusena-faq` — 5 pages
- `lusena-final-cta` — 5 pages
- `lusena-trust-bar` — 3 pages
- `lusena-newsletter` — 2 pages
- `lusena-testimonials` — 1 page (could be reused)
