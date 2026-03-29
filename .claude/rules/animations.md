---
paths:
  - "sections/*.liquid"
  - "snippets/*.liquid"
---
# Animation Patterns

Dawn's `scroll-trigger` classes gated by `settings.animations_reveal_on_scroll`:
- New section/block: add `scroll-trigger animate--slide-in` conditionally:
  `{% if settings.animations_reveal_on_scroll %} scroll-trigger animate--slide-in{% endif %}`
- Repeated items: `data-cascade` on container for stagger effect.
- If element needs `transform` for layout, put scroll-trigger on a wrapper.
