/**
 * LUSENA Animation Layer
 * Uses GSAP + ScrollTrigger for premium scroll-based animations
 * Respects prefers-reduced-motion
 */

(function() {
  'use strict';

  // Check for reduced motion preference
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  // Early exit if user prefers reduced motion
  if (prefersReducedMotion) {
    document.querySelectorAll('.lusena-animate-fade-up, .lusena-animate-scale-in').forEach(function(el) {
      el.classList.add('is-visible');
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
    return;
  }

  // Wait for GSAP to be available
  function initAnimations() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
      setTimeout(initAnimations, 100);
      return;
    }

    gsap.registerPlugin(ScrollTrigger);

    // Set default ease for LUSENA (calm, gentle)
    gsap.defaults({
      ease: 'power2.out',
      duration: 0.8
    });

    // Hero intro animation (matches draft)
    initHeroIntro();

    // Hero parallax effect
    initHeroParallax();
    
    // Generic section reveal animations (matches draft pages)
    initSectionReveals();

    // Section fade-up animations
    initFadeUpAnimations();
    
    // Scale-in animations for images
    initScaleInAnimations();
    
    // Stagger text reveals
    initTextReveals();
    
    // Comparison section row stagger
    initComparisonAnimations();
  }

  /**
   * Hero intro animation (Home)
   * Image scales down + hero text staggers in.
   */
  function initHeroIntro() {
    const hero = document.querySelector('.lusena-hero');
    if (!hero) return;

    const heroImage = hero.querySelector('[data-lusena-hero-image]') || hero.querySelector('img');
    const heroText = hero.querySelector('[data-lusena-hero-text]');
    const heroTextChildren = heroText ? Array.from(heroText.children) : [];

    const tl = gsap.timeline({ defaults: { ease: 'power2.out' } });

    if (heroImage) {
      tl.fromTo(
        heroImage,
        { scale: 1.1, opacity: 0 },
        { scale: 1, opacity: 1, duration: 1.5 }
      );
    }

    if (heroTextChildren.length > 0) {
      tl.fromTo(
        heroTextChildren,
        { y: 30, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.8, stagger: 0.15 },
        heroImage ? '-=1.0' : 0
      );
    }
  }

  /**
   * Generic section reveal animations for main content.
   * Mirrors draft: y + opacity on scroll.
   */
  function initSectionReveals() {
    const main = document.querySelector('#MainContent');
    if (!main) return;

    const sections = gsap.utils.toArray('section', main);
    sections.forEach(function(section) {
      if (!section || !(section instanceof HTMLElement)) return;
      if (section.classList.contains('lusena-hero')) return;

      gsap.fromTo(
        section,
        { y: 40, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 0.8,
          scrollTrigger: {
            trigger: section,
            start: 'top 85%',
            toggleActions: 'play none none none'
          }
        }
      );
    });
  }

  /**
   * Hero section parallax effect
   * Background image moves slower than scroll
   */
  function initHeroParallax() {
    const heroSections = document.querySelectorAll('.lusena-hero');
    
    heroSections.forEach(function(hero) {
      const parallaxImage = hero.querySelector('.lusena-hero__image.lusena-parallax');
      
      if (parallaxImage) {
        gsap.to(parallaxImage, {
          yPercent: 20,
          ease: 'none',
          scrollTrigger: {
            trigger: hero,
            start: 'top top',
            end: 'bottom top',
            scrub: true
          }
        });
      }
    });
  }

  /**
   * Fade-up animations for elements entering viewport
   */
  function initFadeUpAnimations() {
    const fadeElements = document.querySelectorAll('.lusena-animate-fade-up:not(.is-visible)');
    
    fadeElements.forEach(function(el) {
      gsap.set(el, {
        opacity: 0,
        y: 30
      });
      
      gsap.to(el, {
        opacity: 1,
        y: 0,
        duration: 0.6,
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        },
        onComplete: function() {
          el.classList.add('is-visible');
        }
      });
    });
  }

  /**
   * Scale-in animations for images
   */
  function initScaleInAnimations() {
    const scaleElements = document.querySelectorAll('.lusena-animate-scale-in:not(.is-visible)');
    
    scaleElements.forEach(function(el) {
      gsap.set(el, {
        opacity: 0,
        scale: 1.1
      });
      
      gsap.to(el, {
        opacity: 1,
        scale: 1,
        duration: 0.8,
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        },
        onComplete: function() {
          el.classList.add('is-visible');
        }
      });
    });
  }

  /**
   * Staggered text reveal for headlines
   */
  function initTextReveals() {
    const staggerContainers = document.querySelectorAll('[data-lusena-stagger]');
    
    staggerContainers.forEach(function(container) {
      const children = container.children;
      
      if (children.length > 0) {
        gsap.set(children, {
          opacity: 0,
          y: 20
        });
        
        gsap.to(children, {
          opacity: 1,
          y: 0,
          duration: 0.6,
          stagger: 0.1,
          scrollTrigger: {
            trigger: container,
            start: 'top 80%',
            toggleActions: 'play none none none'
          }
        });
      }
    });
  }

  /**
   * Comparison section row animations
   * Rows slide in with stagger effect
   */
  function initComparisonAnimations() {
    const rowContainers = document.querySelectorAll('[data-lusena-stagger-rows]');
    
    rowContainers.forEach(function(container) {
      const rows = container.querySelectorAll('.lusena-comparison__item');
      
      if (rows.length > 0) {
        gsap.set(rows, {
          opacity: 0,
          x: container.closest('.lusena-comparison__column--cotton') ? -20 : 20
        });
        
        gsap.to(rows, {
          opacity: 1,
          x: 0,
          duration: 0.5,
          stagger: 0.08,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: container,
            start: 'top 85%',
            toggleActions: 'play none none none'
          }
        });
      }
    });
  }

  // Refresh ScrollTrigger on Shopify section load/unload (Theme Editor)
  if (window.Shopify && window.Shopify.designMode) {
    document.addEventListener('shopify:section:load', function() {
      if (typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.refresh();
      }
    });
    
    document.addEventListener('shopify:section:unload', function() {
      if (typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.refresh();
      }
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAnimations);
  } else {
    initAnimations();
  }
})();
