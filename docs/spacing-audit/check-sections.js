(function() {
  var sections = document.querySelectorAll('main .shopify-section');
  var result = [];
  for (var i = 0; i < sections.length; i++) {
    var s = sections[i];
    var inner = s.querySelector('section') || s.querySelector(':scope > div');
    if (!inner) continue;
    var cs = getComputedStyle(inner);
    var rect = inner.getBoundingClientRect();
    result.push({
      id: s.id.split('__')[1] || s.id,
      bg: cs.backgroundColor,
      color: cs.color,
      height: Math.round(rect.height),
      width: Math.round(rect.width),
      top: Math.round(rect.top),
      childCount: inner.children.length,
      visible: cs.display !== 'none' && cs.visibility !== 'hidden',
      overflow: cs.overflow
    });
  }
  window.__sectionCheck = JSON.stringify(result);
})();
