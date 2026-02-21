class CartDrawer extends HTMLElement {
  constructor() {
    super();

    this.shouldRestoreFocus = true;
    this.historyStateKey = 'lusenaCartDrawerOpen';
    this.historyEntryActive = false;
    this.pushedHistoryEntry = false;
    this.isClosingFromHistory = false;
    this.addEventListener('keyup', (evt) => evt.code === 'Escape' && this.close());
    this.querySelector('#CartDrawer-Overlay').addEventListener('click', this.close.bind(this));
    window.addEventListener('popstate', this.handlePopState.bind(this));
    this.setHeaderCartIconAccessibility();
  }

  setHeaderCartIconAccessibility() {
    const cartLink = document.querySelector('#cart-icon-bubble');
    if (!cartLink) return;

    cartLink.setAttribute('role', 'button');
    cartLink.setAttribute('aria-haspopup', 'dialog');
    cartLink.addEventListener('click', (event) => {
      event.preventDefault();
      this.open(cartLink, event.detail === 0);
    });
    cartLink.addEventListener('keydown', (event) => {
      if (event.code.toUpperCase() === 'SPACE') {
        event.preventDefault();
        this.open(cartLink, true);
      }
    });
  }

  open(triggeredBy, shouldRestoreFocus = true) {
    const wasOpen = this.classList.contains('active');

    this.shouldRestoreFocus = shouldRestoreFocus;
    if (triggeredBy) this.setActiveElement(triggeredBy);
    const cartDrawerNote = this.querySelector('[id^="Details-"] summary');
    if (cartDrawerNote && !cartDrawerNote.hasAttribute('role')) this.setSummaryAccessibility(cartDrawerNote);
    // here the animation doesn't seem to always get triggered. A timeout seem to help
    setTimeout(() => {
      this.classList.add('animate', 'active');
    });

    this.addEventListener(
      'transitionend',
      () => {
        const containerToTrapFocusOn = this.classList.contains('is-empty')
          ? this.querySelector('.drawer__inner-empty') || document.getElementById('CartDrawer')
          : document.getElementById('CartDrawer');
        const focusElement = this.querySelector('.drawer__inner') || this.querySelector('.drawer__close');
        if (containerToTrapFocusOn) trapFocus(containerToTrapFocusOn, focusElement);
      },
      { once: true }
    );

    document.body.classList.add('overflow-hidden');
    if (!wasOpen) this.pushHistoryEntry();
  }

  close() {
    this.classList.remove('active');
    if (this.shouldRestoreFocus && this.activeElement) {
      removeTrapFocus(this.activeElement);
    } else {
      removeTrapFocus();
      this.activeElement?.blur();
    }
    this.shouldRestoreFocus = true;
    document.body.classList.remove('overflow-hidden');

    if (this.historyEntryActive && this.pushedHistoryEntry && !this.isClosingFromHistory) {
      this.historyEntryActive = false;
      this.pushedHistoryEntry = false;
      history.back();
      return;
    }
    this.historyEntryActive = false;
    this.pushedHistoryEntry = false;
  }

  setSummaryAccessibility(cartDrawerNote) {
    cartDrawerNote.setAttribute('role', 'button');
    cartDrawerNote.setAttribute('aria-expanded', 'false');

    if (cartDrawerNote.nextElementSibling.getAttribute('id')) {
      cartDrawerNote.setAttribute('aria-controls', cartDrawerNote.nextElementSibling.id);
    }

    cartDrawerNote.addEventListener('click', (event) => {
      event.currentTarget.setAttribute('aria-expanded', !event.currentTarget.closest('details').hasAttribute('open'));
    });

    cartDrawerNote.parentElement.addEventListener('keyup', onKeyUpEscape);
  }

  renderContents(parsedState) {
    this.querySelector('.drawer__inner').classList.contains('is-empty') &&
      this.querySelector('.drawer__inner').classList.remove('is-empty');
    this.productId = parsedState.id;
    this.getSectionsToRender().forEach((section) => {
      const sectionElement = section.selector
        ? document.querySelector(section.selector)
        : document.getElementById(section.id);

      if (!sectionElement) return;
      sectionElement.innerHTML = this.getSectionInnerHTML(parsedState.sections[section.id], section.selector);
    });

    setTimeout(() => {
      this.open();
    });
  }

  getSectionInnerHTML(html, selector = '.shopify-section') {
    return new DOMParser().parseFromString(html, 'text/html').querySelector(selector).innerHTML;
  }

  getSectionsToRender() {
    return [
      {
        id: 'cart-drawer',
        selector: '#CartDrawer',
      },
      {
        id: 'cart-icon-bubble',
      },
    ];
  }

  getSectionDOM(html, selector = '.shopify-section') {
    return new DOMParser().parseFromString(html, 'text/html').querySelector(selector);
  }

  setActiveElement(element) {
    this.activeElement = element;
  }

  pushHistoryEntry() {
    const state = history.state || {};
    if (state[this.historyStateKey]) {
      this.historyEntryActive = true;
      this.pushedHistoryEntry = false;
      return;
    }

    history.pushState({ ...state, [this.historyStateKey]: true }, '', window.location.href);
    this.historyEntryActive = true;
    this.pushedHistoryEntry = true;
  }

  handlePopState() {
    if (!this.classList.contains('active')) {
      this.historyEntryActive = false;
      this.pushedHistoryEntry = false;
      return;
    }

    this.isClosingFromHistory = true;
    this.close();
    this.isClosingFromHistory = false;
  }
}

customElements.define('cart-drawer', CartDrawer);

class CartDrawerItems extends CartItems {
  getSectionsToRender() {
    return [
      {
        id: 'CartDrawer',
        section: 'cart-drawer',
        selector: '.drawer__inner',
      },
      {
        id: 'cart-icon-bubble',
        section: 'cart-icon-bubble',
        selector: '.shopify-section',
      },
    ];
  }
}

customElements.define('cart-drawer-items', CartDrawerItems);
