(function () {
  // mobile menu
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  // videos: pause controls, reduced motion, process clips play only while visible
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hero = document.querySelector('.hero-video');
  var clips = Array.prototype.slice.call(document.querySelectorAll('.clip'));
  var state = { hero: !reduce, clips: !reduce }; // true = playing
  var visible = new Set();

  function play(v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  function apply(target) {
    if (target === 'hero' && hero) { state.hero ? play(hero) : hero.pause(); }
    if (target === 'clips') { clips.forEach(function (v) { (state.clips && visible.has(v)) ? play(v) : v.pause(); }); }
    document.querySelectorAll('.vid-toggle[data-target="' + target + '"]').forEach(function (b) {
      b.textContent = state[target] ? b.dataset.pause : b.dataset.play;
    });
  }
  document.querySelectorAll('.vid-toggle').forEach(function (b) {
    b.addEventListener('click', function () { var t = b.dataset.target; state[t] = !state[t]; apply(t); });
  });
  if (hero && reduce) hero.removeAttribute('autoplay');
  apply('hero');

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { en.isIntersecting ? visible.add(en.target) : visible.delete(en.target); });
      apply('clips');
    }, { threshold: 0.35 });
    clips.forEach(function (v) { io.observe(v); });
  }
  apply('clips');
})();
