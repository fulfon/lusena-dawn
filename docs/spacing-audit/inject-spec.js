/**
 * Auto-generated spec injector.
 * Sets window.__lusenaSpacingSpec from the embedded JSON.
 * Inject via: page.addScriptTag({ path: "docs/spacing-audit/inject-spec.js" })
 */
window.__lusenaSpacingSpec = {
  "$schema": "../spec-schema.md",
  "page": "homepage",
  "url": "/",
  "viewport": { "width": 1440, "height": 900 },
  "tolerancePx": 4,
  "notes": "Desktop homepage spec. Tolerance 4px accounts for sub-pixel rounding from 62.5% font-size and inline element bounding box variance.",

  "sectionGaps": [
    { "between": ["hero", "trust"], "expectedGapPx": 0 },
    { "between": ["trust", "problem_solution"], "expectedGapPx": 0 },
    { "between": ["problem_solution", "bestsellers"], "expectedGapPx": 0 },
    { "between": ["bestsellers", "reviews"], "expectedGapPx": 0 },
    { "between": ["reviews", "gift"], "expectedGapPx": 0 },
    { "between": ["gift", "heritage"], "expectedGapPx": 0 },
    { "between": ["heritage", "faq"], "expectedGapPx": 0 },
    { "between": ["faq", "final_cta"], "expectedGapPx": 0 }
  ],

  "sections": {
    "hero": {
      "matchClass": "lusena-hero",
      "expectedPaddingTop": 0,
      "expectedPaddingBottom": 0
    },

    "trust": {
      "matchClass": "lusena-section-gap-different",
      "notes": "Trust bar has its own internal padding, not via spacing tiers",
      "expectedPaddingTop": 0,
      "expectedPaddingBottom": 0
    },

    "problem_solution": {
      "matchClass": "lusena-problem-solution",
      "expectedPaddingTop": 96,
      "expectedPaddingBottom": 96,
      "containers": {
        ".lusena-container": [
          {
            "matchClass": "lusena-split-problem-solution",
            "expectedGapToNext": 24,
            "note": "lusena-gap-body (24px margin-bottom) minus margin collapse"
          },
          {
            "matchClass": "lusena-text-center",
            "note": "CTA link"
          }
        ]
      }
    },

    "bestsellers": {
      "matchClass": "lusena-bestsellers",
      "expectedPaddingTop": 96,
      "expectedPaddingBottom": 96,
      "containers": {
        ".lusena-container": [
          {
            "matchClass": "lusena-bestsellers__header",
            "expectedGapToNext": 32,
            "note": "lusena-gap-section-intro (32px margin-bottom)"
          },
          {
            "matchClass": "lusena-bestsellers__grid",
            "note": "Product grid"
          }
        ]
      }
    },

    "reviews": {
      "matchClass": "lusena-testimonials",
      "expectedPaddingTop": 96,
      "expectedPaddingBottom": 96,
      "containers": {
        ".lusena-container": [
          {
            "matchClass": "lusena-text-center",
            "expectedGapToNext": 32,
            "note": "lusena-gap-section-intro (32px)"
          },
          {
            "matchClass": "lusena-grid",
            "note": "Testimonial cards grid"
          }
        ]
      }
    },

    "gift": {
      "matchClass": "lusena-bundles",
      "expectedPaddingTop": 96,
      "expectedPaddingBottom": 96,
      "containers": {
        ".lusena-container": [
          {
            "matchClass": "lusena-text-center",
            "expectedGapToNext": 32,
            "note": "lusena-gap-section-intro (32px)",
            "children": [
              {
                "matchClass": "lusena-type-caption",
                "expectedGapToNext": 16,
                "tolerancePx": 4,
                "note": "Kicker is display:inline, 3px variance from inline bounding box"
              },
              {
                "matchClass": "lusena-type-h1",
                "note": "Section heading"
              }
            ]
          },
          {
            "matchClass": "lusena-type-body",
            "expectedGapToNext": 48,
            "note": "lusena-gap-body (24px mb) + lusena-bundles__grid margin-top (48px)"
          },
          {
            "matchClass": "lusena-bundles__grid",
            "note": "Bundle product cards"
          }
        ]
      }
    },

    "heritage": {
      "matchClass": "lusena-heritage",
      "expectedPaddingTop": 96,
      "expectedPaddingBottom": 96,
      "containers": {
        ".lusena-container": [
          {
            "matchClass": "lusena-text-center",
            "expectedGapToNext": 32,
            "note": "lusena-gap-section-intro (32px)"
          },
          {
            "matchClass": "lusena-grid",
            "expectedGapToNext": 32,
            "note": "Heritage tiles grid, lusena-gap-cta-top (32px) below"
          },
          {
            "matchClass": "lusena-text-center",
            "note": "CTA link"
          }
        ]
      }
    },

    "faq": {
      "matchClass": "lusena-faq",
      "expectedPaddingTop": 64,
      "expectedPaddingBottom": 64,
      "containers": {
        ".lusena-container--narrow": [
          {
            "matchClass": "lusena-text-center",
            "expectedGapToNext": 32,
            "note": "lusena-gap-section-intro (32px)",
            "children": [
              {
                "matchClass": "lusena-type-h1",
                "expectedGapToNext": 16,
                "note": "lusena-content-flow--tight (16px)"
              },
              {
                "matchClass": "lusena-type-body",
                "note": "Subheading text"
              }
            ]
          },
          {
            "matchClass": "lusena-faq__list",
            "note": "Accordion items",
            "children": [
              {
                "matchClass": "lusena-accordion",
                "expectedGapToNext": 0,
                "repeat": true,
                "note": "Accordion items are flush (border separates them)"
              }
            ]
          }
        ]
      }
    },

    "final_cta": {
      "matchClass": "lusena-final-cta",
      "expectedPaddingTop": 64,
      "expectedPaddingBottom": 64,
      "containers": {
        ".lusena-container--narrow": [
          {
            "matchClass": "lusena-type-h1",
            "expectedGapToNext": 24,
            "note": "lusena-content-flow (24px)"
          },
          {
            "matchClass": "lusena-type-body",
            "expectedGapToNext": 24,
            "note": "lusena-content-flow (24px)"
          },
          {
            "matchClass": "lusena-gap-cta-top",
            "note": "CTA button"
          }
        ]
      }
    }
  }
};
