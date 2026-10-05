/* ADA Tech Division — small site script. Loaded in <head> so the menu
   state is set before first paint. No dependencies. */
(function () {
  var root = document.documentElement;
  root.classList.add('js');

  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('menuBtn');
    var nav = document.getElementById('nav');
    if (btn && nav) {
      btn.addEventListener('click', function () {
        var open = nav.classList.toggle('open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        btn.textContent = open ? 'Close' : 'Menu';
      });
    }

    /* Search: the header button opens a search bar. Without this script it
       is an ordinary link to the search page. */
    var sBtn = document.getElementById('searchBtn');
    var sBar = document.getElementById('searchBar');
    if (sBtn && sBar) {
      var setSearch = function (open) {
        sBar.hidden = !open;
        sBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
        if (open) { var q = document.getElementById('q-head'); if (q) q.focus(); }
      };
      sBtn.addEventListener('click', function (e) { e.preventDefault(); setSearch(sBar.hidden); });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && !sBar.hidden) { setSearch(false); sBtn.focus(); }
      });
    }

    /* Reveal on scroll. Only elements below the first screen are hidden, and
       only when the browser supports the observer and motion is allowed. */
    var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if ('IntersectionObserver' in window && !calm) {
      var targets = document.querySelectorAll(
        'main .sec-head, main .grid:not(.swipe) > *, main .swipe, main .rows > li, main .steps > li, main .tiles > *, ' +
        'main .facts > div, main .tbl-wrap, main .checks > li, main .sheet, main .stop, main .split > *, main .faq, main .answer, main .cta .wrap > *, main .person');
      var fold = window.innerHeight * 0.92;
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          io.unobserve(el);
          el.classList.add('in');
          window.setTimeout(function () {
            el.classList.remove('reveal', 'in');
            el.style.removeProperty('--d');
          }, 1100);
        });
      }, { threshold: 0.08, rootMargin: '0px 0px -5% 0px' });
      Array.prototype.forEach.call(targets, function (el) {
        if (el.closest('.hero') || el.querySelector('.reveal') || el.closest('.reveal')) return;
        if (el.getBoundingClientRect().top < fold) return;
        var i = Array.prototype.indexOf.call(el.parentNode.children, el);
        el.style.setProperty('--d', Math.min(i, 5) * 70 + 'ms');
        el.classList.add('reveal');
        io.observe(el);
      });
    }

    /* Phones: slide the header away while reading down, bring it back on the
       way up. Never while the menu or search bar is open. */
    var head = document.querySelector('.head');
    if (head && window.matchMedia) {
      var narrow = window.matchMedia('(max-width: 760px)');
      var lastY = window.pageYOffset;
      var ticking = false;
      window.addEventListener('scroll', function () {
        if (ticking) return;
        ticking = true;
        window.requestAnimationFrame(function () {
          var y = window.pageYOffset;
          var busy = (nav && nav.classList.contains('open')) || (sBar && !sBar.hidden);
          if (!narrow.matches || busy || y < 160 || y < lastY - 6) head.classList.remove('head--away');
          else if (y > lastY + 6) head.classList.add('head--away');
          lastY = y;
          ticking = false;
        });
      }, { passive: true });
    }

    var year = document.getElementById('year');
    if (year) year.textContent = String(new Date().getFullYear());

    /* Fault finder on the home page: typing filters the list of faults. */
    var fq = document.getElementById('finderQ');
    var fl = document.getElementById('finderList');
    if (fq && fl) {
      var items = Array.prototype.slice.call(fl.querySelectorAll('li'));
      var none = document.getElementById('finderNone');
      var count = document.getElementById('finderCount');
      var total = items.length;
      var words = function (t) { return t.toLowerCase().replace(/[^a-z0-9 ]+/g, ' ').split(/\s+/).filter(function (w) { return w.length > 1; }); };
      fq.addEventListener('input', function () {
        var q = words(fq.value);
        var shown = 0;
        items.forEach(function (li) {
          var hay = li.getAttribute('data-k') || '';
          var hit = !q.length ? !li.hasAttribute('data-more') : q.every(function (w) { return hay.indexOf(w) !== -1 || hay.indexOf(w.replace(/ies$/, 'y').replace(/(ing|es|s)$/, '')) !== -1; });
          li.hidden = !hit;
          if (hit) shown++;
        });
        if (none) none.hidden = shown > 0;
        if (count) count.textContent = q.length ? shown + ' of ' + total : total + ' faults';
      });
    }

    /* Starting-point helper on the home page: two answers, one suggestion. */
    var form = document.getElementById('startForm');
    if (form) {
      var routes = {
        computer: { broken: 'services/computer-repair', slow: 'problems/slow-laptop', setup: 'services/windows-setup', care: 'first-aid' },
        windows:  { broken: 'services/windows-setup', slow: 'problems/windows-update-not-working', setup: 'services/windows-setup', care: 'first-aid' },
        wifi:     { broken: 'problems/wifi-keeps-disconnecting', slow: 'problems/wifi-keeps-disconnecting', setup: 'services/networking', care: 'managed-it' },
        printer:  { broken: 'problems/printer-not-printing', slow: 'problems/printer-not-printing', setup: 'services/business-it', care: 'managed-it' },
        cctv:     { broken: 'services/cctv', slow: 'services/cctv', setup: 'services/cctv', care: 'managed-it' },
        office:   { broken: 'support', slow: 'managed-it', setup: 'services/business-it', care: 'managed-it' }
      };
      var names = {
        'services/computer-repair': 'a diagnostic on the bench (N$99, deducted from the repair)',
        'problems/slow-laptop': 'finding what is slowing it down, which takes about two minutes in Task Manager',
        'services/windows-setup': 'a Windows package (from N$649)',
        'problems/windows-update-not-working': 'the Windows Update checks, then a repair if they do not work (from N$249)',
        'first-aid': 'ADA First Aid, monthly care for a personal device (from N$249 a month)',
        'problems/wifi-keeps-disconnecting': 'working out whether it is the router or the device',
        'services/networking': 'router and Wi-Fi setup (from N$349)',
        'problems/printer-not-printing': 'the printer checks, then printer setup if they do not work (from N$179)',
        'services/business-it': 'an office setup, quoted by users and devices',
        'services/cctv': 'a site assessment for cameras, then a written quote',
        'managed-it': 'a Managed IT plan (from N$1,249 a month)',
        'support': 'describing the fault to us, so we can tell you what to bring or check'
      };
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var thing = form.elements.thing.value;
        var need = form.elements.need.value;
        var path = (routes[thing] || {})[need];
        var out = document.getElementById('startResult');
        if (!path || !out) return;
        out.innerHTML = '';
        var p = document.createElement('p');
        p.appendChild(document.createTextNode('A sensible place to start is ' + names[path] + '. '));
        var a = document.createElement('a');
        a.href = '/' + path;
        a.className = 'more';
        a.textContent = 'Open that page';
        p.appendChild(a);
        out.appendChild(p);
        out.hidden = false;
      });
    }
  });
})();
