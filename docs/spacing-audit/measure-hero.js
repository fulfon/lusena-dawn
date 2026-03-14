// Measure hero section top-to-first-content and last-content-to-bottom
(function() {
  var hero = document.querySelector('[class*="hero"][class*="lusena-spacing"]');
  if (!hero) return 'NO HERO FOUND';
  var s = getComputedStyle(hero);
  var kicker = hero.querySelector('.lusena-kicker');
  var h1 = hero.querySelector('h1');
  var firstEl = kicker || h1;
  var container = hero.querySelector('[class*="container"]');
  var allLinks = container ? container.querySelectorAll('a') : [];
  var lastEl = allLinks.length > 0 ? allLinks[allLinks.length - 1] : (container ? container.lastElementChild : h1);
  var topToFirst = Math.round(firstEl.getBoundingClientRect().top - hero.getBoundingClientRect().top);
  var lastToBot = Math.round(hero.getBoundingClientRect().bottom - lastEl.getBoundingClientRect().bottom);
  return 'padTop=' + s.paddingTop + ' | padBot=' + s.paddingBottom + ' | topToFirst=' + topToFirst + ' | lastToBot=' + lastToBot;
})();
