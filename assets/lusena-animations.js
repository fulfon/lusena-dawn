/**
 * LUSENA Motion Layer
 * Lightweight, conversion-friendly animations (no external libraries).
 *
 * Principles:
 * - Animate only for feedback + gentle reveals (not "decorative motion everywhere")
 * - Prefer transform/opacity for performance
 * - Respect prefers-reduced-motion (no movement)
 */
(() => {
  'use strict';

  const prefersReducedMotion = window.matchMedia?.('(prefers-reduced-motion: reduce)')?.matches;
  if (prefersReducedMotion) return;

  const root = document.documentElement;
  root.classList.add('lusena-motion');

  const revealSelectors = [
    '.lusena-animate-fade-up',
    '.lusena-animate-scale-in',
    '[data-lusena-stagger] > *',
    '[data-lusena-stagger-rows] .lusena-comparison__item',
  ];

  const revealElements = Array.from(document.querySelectorAll(revealSelectors.join(','))).filter((el) => el instanceof HTMLElement);

  function markVisible(el) {
    el.classList.add('is-visible');
  }

  function setupStaggers() {
    document.querySelectorAll('[data-lusena-stagger]').forEach((container) => {
      const children = Array.from(container.children).filter((el) => el instanceof HTMLElement);
      children.forEach((child, index) => {
        child.style.setProperty('--lusena-delay', `${index * 70}ms`);
      });
    });

    document.querySelectorAll('[data-lusena-stagger-rows]').forEach((container) => {
      const rows = Array.from(container.querySelectorAll('.lusena-comparison__item')).filter((el) => el instanceof HTMLElement);
      rows.forEach((row, index) => {
        row.style.setProperty('--lusena-delay', `${index * 55}ms`);
      });
    });
  }

  function initRevealObserver() {
    if (revealElements.length === 0) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          if (el instanceof HTMLElement) markVisible(el);
          observer.unobserve(el);
        });
      },
      { rootMargin: '0px 0px -12% 0px' }
    );

    revealElements.forEach((el) => observer.observe(el));
  }

  function init() {
    setupStaggers();
    initRevealObserver();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }

  if (window.Shopify?.designMode) {
    document.addEventListener('shopify:section:load', init);
    document.addEventListener('shopify:section:reorder', init);
  }
})();
