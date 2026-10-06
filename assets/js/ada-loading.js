/* ADA loading state. One file, shared by every ADA website.

   When a visitor taps a link or sends a form that leads to another page of the
   same site, a thin bar runs along the top of the screen so they can see that
   something is happening. If the page takes more than a moment, a small
   "Loading" label appears as well. Both disappear when the next page arrives.

   It works on sites that load a whole new page (Web, Tech, Marketing,
   Consulting) and on sites that change page without a full reload (the main
   site and the Founder profile).

   Options, set on the script tag:
     data-color="#e3212d"   colour of the bar (default: ADA red)

   Nothing is recorded or sent anywhere. */
(function () {
  'use strict';

  var tag = document.currentScript || document.querySelector('script[src*="ada-loading"]');
  var color = (tag && tag.getAttribute('data-color')) || '#e3212d';
  var calm = false;
  try { calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { /* older browsers */ }

  var CSS =
    '.ada-load{position:fixed;left:0;top:0;height:3px;width:0;z-index:2147483001;background:' + color + ';' +
    'box-shadow:0 0 12px ' + color + ';opacity:0;pointer-events:none}' +
    '.ada-load.on{opacity:1;animation:adaLoad 9s cubic-bezier(.08,.7,.2,1) forwards}' +
    '.ada-load.done{opacity:0;width:100%;animation:none;transition:width .18s ease-out,opacity .3s ease .12s}' +
    '@keyframes adaLoad{0%{width:0}12%{width:38%}45%{width:72%}100%{width:94%}}' +
    '.ada-load-note{position:fixed;left:50%;top:14px;transform:translate(-50%,-6px);z-index:2147483001;' +
    'display:inline-flex;align-items:center;gap:9px;padding:9px 14px;background:#081b33;color:#fff;' +
    'font:700 .8125rem/1 Arial,Helvetica,sans-serif;letter-spacing:.01em;box-shadow:0 10px 30px rgba(8,27,51,.28);' +
    'opacity:0;pointer-events:none;transition:opacity .2s ease,transform .2s ease}' +
    '.ada-load-note.on{opacity:1;transform:translate(-50%,0)}' +
    '.ada-load-note i{width:12px;height:12px;border:2px solid rgba(255,255,255,.35);border-top-color:#fff;' +
    'border-radius:50% !important;animation:adaSpin .7s linear infinite}' +
    '@keyframes adaSpin{to{transform:rotate(360deg)}}' +
    '@media (prefers-reduced-motion:reduce){.ada-load.on{animation:none;width:100%}.ada-load-note i{animation:none;border-top-color:rgba(255,255,255,.35)}' +
    '.ada-load-note{transition:none}}' +
    '@media print{.ada-load,.ada-load-note{display:none !important}}';

  var bar = null;
  var note = null;
  var noteTimer = null;
  var giveUp = null;
  var active = false;

  function build() {
    if (bar || !document.body) return;
    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    bar = document.createElement('div');
    bar.className = 'ada-load';
    bar.setAttribute('aria-hidden', 'true');

    note = document.createElement('div');
    note.className = 'ada-load-note';
    note.setAttribute('role', 'status');
    note.setAttribute('aria-live', 'polite');

    document.body.appendChild(bar);
    document.body.appendChild(note);
  }

  function start() {
    build();
    if (!bar || active) return;
    active = true;
    bar.classList.remove('done');
    // Restart the animation if the bar was used a moment ago.
    void bar.offsetWidth;
    bar.classList.add('on');

    window.clearTimeout(noteTimer);
    noteTimer = window.setTimeout(function () {
      note.innerHTML = '';
      note.appendChild(document.createElement('i'));
      note.appendChild(document.createTextNode('Loading'));
      note.classList.add('on');
    }, calm ? 250 : 700);

    // If the page never arrives (the visitor pressed stop, or the link opened
    // an app such as WhatsApp), stop showing a loading state.
    window.clearTimeout(giveUp);
    giveUp = window.setTimeout(finish, 12000);
  }

  function finish() {
    window.clearTimeout(noteTimer);
    window.clearTimeout(giveUp);
    if (!bar || !active) return;
    active = false;
    bar.classList.remove('on');
    bar.classList.add('done');
    note.classList.remove('on');
    note.textContent = '';
    window.setTimeout(function () { if (!active && bar) bar.classList.remove('done'); }, 500);
  }

  // True when following this address loads another page of this website.
  function leadsToAnotherPage(address) {
    try {
      var to = new URL(address, location.href);
      if (to.origin !== location.origin) return false;
      if (!/^https?:$/.test(to.protocol)) return false;
      // Same page, different section: nothing loads.
      if (to.pathname === location.pathname && to.search === location.search) return false;
      // Files open or download; they are not pages.
      if (/\.(pdf|zip|png|jpe?g|webp|gif|svg|mp4|docx?|xlsx?)$/i.test(to.pathname)) return false;
      return true;
    } catch (e) { return false; }
  }

  document.addEventListener('click', function (event) {
    if (event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    var link = event.target && event.target.closest ? event.target.closest('a[href]') : null;
    if (!link || link.target === '_blank' || link.hasAttribute('download')) return;
    if (!leadsToAnotherPage(link.href)) return;
    // Let the page's own scripts decide first: some links only open a menu.
    window.setTimeout(function () { if (!event.defaultPrevented || link.dataset.adaLoad === 'always') start(); }, 0);
    // Sites that change page in place cancel the click themselves, then load.
    if (window.next || document.getElementById('__next') || document.querySelector('script[src*="/_next/"]')) start();
  });

  document.addEventListener('submit', function (event) {
    var form = event.target;
    if (!form || !form.getAttribute || form.target === '_blank') return;
    var method = (form.getAttribute('method') || 'get').toLowerCase();
    if (method !== 'get') return;
    window.setTimeout(function () {
      if (!event.defaultPrevented && leadsToAnotherPage(form.action || location.href)) start();
    }, 0);
  });

  // The next page has arrived.
  window.addEventListener('pageshow', finish);
  window.addEventListener('popstate', function () { window.setTimeout(finish, 0); });
  ['pushState', 'replaceState'].forEach(function (name) {
    var original = history[name];
    if (typeof original !== 'function') return;
    history[name] = function () {
      var result = original.apply(this, arguments);
      window.setTimeout(finish, 60);
      return result;
    };
  });
})();
