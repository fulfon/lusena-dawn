/**
 * LUSENA Bundle Swap — shared cart API logic for bundle upgrades.
 *
 * Usage:
 *   var state = await LusenaBundle.swap(bundleVariantId, [removeKey], {
 *     sections: ['cart-drawer', 'cart-icon-bubble'],
 *     sectionsUrl: '/products/poszewka-jedwabna',
 *     properties: { 'Poszewka jedwabna': 'Czarny', ... }
 *   });
 *
 * - Adds the bundle variant via /cart/add.js (with optional properties for Simple Bundles)
 * - Removes individual item(s) via /cart/change.js
 * - Last removal uses FormData with sections param for drawer re-render
 * - Returns parsed JSON response from the last /cart/change.js call
 * - Throws on failure — caller handles errors and UI
 */
window.LusenaBundle = {
  async swap(bundleVariantId, removeKeys, options) {
    var addItem = { id: parseInt(bundleVariantId), quantity: 1 };
    if (options && options.properties) {
      addItem.properties = options.properties;
    }
    var addRes = await fetch('/cart/add.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ items: [addItem] })
    });
    if (!addRes.ok) throw new Error('Failed to add bundle');

    var lastIdx = removeKeys.length - 1;
    var lastState = null;
    for (var i = 0; i < removeKeys.length; i++) {
      var needsSections = i === lastIdx && options && options.sections;

      if (needsSections) {
        // Use FormData for the last call — matches Dawn's updateLine pattern
        // which is the only format that returns rendered section HTML
        var formData = new FormData();
        formData.append('id', removeKeys[i]);
        formData.append('quantity', 0);
        formData.append('sections', options.sections.join(','));
        formData.append('sections_url', options.sectionsUrl || window.location.pathname);

        var changeRes = await fetch('/cart/change.js', {
          method: 'POST',
          headers: { 'X-Requested-With': 'XMLHttpRequest' },
          body: formData
        });
      } else {
        var changeRes = await fetch('/cart/change.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id: removeKeys[i], quantity: 0 })
        });
      }

      if (!changeRes.ok) throw new Error('Failed to remove item');
      if (i === lastIdx) {
        lastState = await changeRes.json();
      }
    }

    return lastState;
  }
};
