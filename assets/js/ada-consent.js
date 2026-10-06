/* ADA cookie banner and usage records. One file, shared by the ADA division
   websites (Web, Tech, Marketing, Consulting and the Founder profile).

   What it does
   - Shows a banner on every visit with two equal choices: Accept or Decline.
     The choice lasts for one visit only. Moving between pages of the site,
     reloading, or going back and forward is the same visit. Arriving again,
     by typing the address, a bookmark, a search result or a link from
     somewhere else, or in a new tab, is a new visit and the banner asks again.
   - If the visitor accepts, it sends ADA three kinds of record: a page viewed,
     a search made on the site, and a tap on a WhatsApp, phone or email link.
   - If the visitor declines, nothing is recorded apart from the choice itself.

   What it never sends: a name, an email address, an IP address or any
   identifier for the visitor. The records are received by
   www.andreasdigitalagency.com/api/insights, which accepts them only from
   ADA's own websites.

   Options, set on the script tag:
     data-cookies="/cookies"   address of the cookie notice on this site
     data-privacy="/privacy"   address of the privacy policy on this site
   Without them, the links go to the notices on the main ADA website.

   Any element with the attribute data-cookie-settings reopens the banner. */
(function () {
  'use strict';

  var MAIN = 'https://www.andreasdigitalagency.com';
  var ENDPOINT = MAIN + '/api/insights';
  var KEY = 'ada-cookie-consent-v3';
  var NAV = 'ada-cookie-nav';
  var NAV_WINDOW = 45000; // an internal link must load its page within this time
  var BOT = /bot|crawl|spider|slurp|headless|lighthouse|preview/i;
  // Private and sign-in pages are never recorded.
  var PRIVATE = /^\/(studio|admin|client-desk|client-login|service-record|tech-publisher|staff-portal)(\/|\.html|$)/;

  var script = document.currentScript;
  var cookiesUrl = (script && script.getAttribute('data-cookies')) || MAIN + '/cookies';
  var privacyUrl = (script && script.getAttribute('data-privacy')) || MAIN + '/privacy';

  function store() {
    try { return window.sessionStorage; } catch (e) { return null; }
  }

  // "accepted", "rejected" or null when no choice has been made this visit.
  function choice() {
    try {
      var s = store();
      var raw = s && s.getItem(KEY);
      if (!raw) return null;
      return JSON.parse(raw).analytics === true ? 'accepted' : 'rejected';
    } catch (e) { return null; }
  }

  function remember(accepted) {
    try {
      var s = store();
      if (s) s.setItem(KEY, JSON.stringify({ preferences: false, analytics: accepted, thirdParty: false }));
    } catch (e) { /* the banner still works when storage is blocked */ }
  }

  // True when this page load continues a visit that is already under way.
  function sameVisit() {
    var s = store();
    if (!s) return false;
    var flag = null;
    try { flag = s.getItem(NAV); s.removeItem(NAV); } catch (e) { return false; }
    var type = 'navigate';
    try {
      var entry = performance.getEntriesByType('navigation')[0];
      if (entry && entry.type) type = entry.type;
    } catch (e) { /* older browsers: treated as a fresh arrival */ }
    if (type === 'reload' || type === 'back_forward') return true;
    return !!flag && Date.now() - Number(flag) < NAV_WINDOW;
  }

  // Called when the visitor follows a link, or sends a form, to another page of this site.
  function markInternal(url) {
    try {
      var to = new URL(url, location.href);
      if (to.origin !== location.origin) return;
      var s = store();
      if (s) s.setItem(NAV, String(Date.now()));
    } catch (e) { /* ignore addresses that cannot be read */ }
  }

  function device() {
    var w = window.innerWidth;
    return w < 768 ? 'mobile' : (w < 1024 ? 'tablet' : 'desktop');
  }

  function send(body) {
    if (BOT.test(navigator.userAgent || '')) return;
    try {
      fetch(ENDPOINT, {
        method: 'POST',
        mode: 'cors',
        credentials: 'omit',
        keepalive: true,
        headers: { 'Content-Type': 'text/plain' },
        body: JSON.stringify(body)
      }).catch(function () {});
    } catch (e) { /* records are optional; never disturb the visitor */ }
  }

  function record(body) {
    if (choice() !== 'accepted') return;
    if (PRIVATE.test(location.pathname)) return;
    body.device = device();
    send(body);
  }

  // ------------------------------------------------------------ page views

  var lastPath = null;
  var firstView = true;

  function referrerHost() {
    try {
      if (!document.referrer) return null;
      var host = new URL(document.referrer).hostname;
      return host && host !== location.hostname ? host : null;
    } catch (e) { return null; }
  }

  function pageView() {
    if (choice() !== 'accepted') return;
    var path = location.pathname || '/';
    if (path !== lastPath) {
      lastPath = path;
      record({ type: 'page_view', path: path, referrerHost: firstView ? referrerHost() : null });
      firstView = false;
    }
    // A search made without leaving the search page still counts as a search.
    searchView();
  }

  // --------------------------------------------------------------- searches

  var lastQuery = null;

  function onSearchPage() {
    return /^\/search(\.html)?\/?$/.test(location.pathname);
  }

  function tidy(q) {
    return String(q || '').toLowerCase().replace(/\s+/g, ' ').trim().slice(0, 120);
  }

  function recordSearch(q) {
    if (!q || q === lastQuery) return;
    lastQuery = q;
    // Give the page a moment to draw its results before counting them.
    window.setTimeout(function () {
      var list = document.getElementById('searchResults');
      record({ type: 'site_search', path: '/search', query: q, resultsCount: list ? list.children.length : 0 });
    }, 1500);
  }

  function searchView() {
    if (!onSearchPage()) return;
    try { recordSearch(tidy(new URLSearchParams(location.search).get('q'))); } catch (e) { /* no query */ }
  }

  // Results appear while the visitor types. Once they stop typing for a few
  // seconds, what they typed counts as one search.
  var typing = null;
  document.addEventListener('input', function (event) {
    var field = event.target;
    if (!field || field.id !== 'q' || !onSearchPage()) return;
    window.clearTimeout(typing);
    typing = window.setTimeout(function () {
      var q = tidy(field.value);
      if (q.length >= 3) recordSearch(q);
    }, 2500);
  });

  // ---------------------------------------------------------- contact taps

  function contactMethod(href) {
    if (href.indexOf('tel:') === 0) return 'phone';
    if (href.indexOf('mailto:') === 0) return 'email';
    if (/(^|\/\/)(wa\.me|api\.whatsapp\.com)\//.test(href)) return 'whatsapp';
    return null;
  }

  document.addEventListener('click', function (event) {
    var target = event.target;
    var opener = target && target.closest ? target.closest('[data-cookie-settings]') : null;
    if (opener) { event.preventDefault(); show(); return; }
    var link = target && target.closest ? target.closest('a[href]') : null;
    if (!link) return;
    var href = link.getAttribute('href') || '';
    var method = contactMethod(href);
    if (method) record({ type: 'contact_click', path: location.pathname || '/', method: method });
    else if (href.charAt(0) !== '#' && link.target !== '_blank') markInternal(link.href);
  });

  document.addEventListener('submit', function (event) {
    var form = event.target;
    if (form && form.getAttribute && !event.defaultPrevented) markInternal(form.action || location.href);
  });

  // ---------------------------------------------------------------- banner

  var CSS =
    '.ada-cc{position:fixed;left:0;right:0;bottom:0;z-index:2147483000;display:flex;justify-content:center;padding:12px;pointer-events:none;font-family:Arial,Helvetica,sans-serif}' +
    '.ada-cc[hidden]{display:none}' +
    '.ada-cc-box{pointer-events:auto;width:100%;max-width:760px;background:#081b33;color:#fff;border-top:3px solid #e3212d;box-shadow:0 18px 50px rgba(0,0,0,.35);padding:20px 22px}' +
    '.ada-cc-box h2{margin:0 0 8px;font:700 1.05rem/1.25 Arial,Helvetica,sans-serif;color:#fff;letter-spacing:0}' +
    '.ada-cc-box p{margin:0;font-size:.92rem;line-height:1.5;color:rgba(255,255,255,.88)}' +
    '.ada-cc-box a{color:#fff;text-decoration:underline}' +
    '.ada-cc-links{margin-top:8px !important;font-size:.86rem !important}' +
    '.ada-cc-row{display:flex;gap:10px;margin-top:16px}' +
    '.ada-cc-row button{flex:1 1 0;min-height:46px;padding:10px 16px;border:1px solid #fff;background:#fff;color:#081b33;font:700 .9rem/1.1 Arial,Helvetica,sans-serif;cursor:pointer;border-radius:0}' +
    '.ada-cc-row button:hover{background:#dce5ef;border-color:#dce5ef}' +
    '.ada-cc-row button:focus-visible{outline:3px solid #e3212d;outline-offset:2px}' +
    '@media (max-width:560px){.ada-cc{padding:0}.ada-cc-box{padding:16px 16px calc(16px + env(safe-area-inset-bottom,0px))}.ada-cc-box p{font-size:.875rem}}' +
    '@media print{.ada-cc{display:none !important}}';

  var banner = null;

  function build() {
    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    banner = document.createElement('div');
    banner.className = 'ada-cc';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Cookie choice');
    banner.hidden = true;

    var box = document.createElement('div');
    box.className = 'ada-cc-box';

    var h = document.createElement('h2');
    h.textContent = 'Cookies and your privacy';

    var p = document.createElement('p');
    p.textContent = 'If you accept, we record which pages are viewed, what is searched for and which contact ' +
      'buttons are tapped, so we can improve this website. We do not record your name, email address or ' +
      'IP address. We ask on every visit.';

    var links = document.createElement('p');
    links.className = 'ada-cc-links';
    var a1 = document.createElement('a');
    a1.href = cookiesUrl; a1.textContent = 'Cookie Notice';
    var a2 = document.createElement('a');
    a2.href = privacyUrl; a2.textContent = 'Privacy Policy';
    links.appendChild(a1);
    links.appendChild(document.createTextNode(' · '));
    links.appendChild(a2);

    var row = document.createElement('div');
    row.className = 'ada-cc-row';
    var no = document.createElement('button');
    no.type = 'button'; no.textContent = 'Decline';
    var yes = document.createElement('button');
    yes.type = 'button'; yes.textContent = 'Accept';
    no.addEventListener('click', function () { decide(false); });
    yes.addEventListener('click', function () { decide(true); });
    row.appendChild(no);
    row.appendChild(yes);

    box.appendChild(h);
    box.appendChild(p);
    box.appendChild(links);
    box.appendChild(row);
    banner.appendChild(box);
    document.body.appendChild(banner);
  }

  function show() {
    if (!banner) build();
    banner.hidden = false;
  }

  function decide(accepted) {
    remember(accepted);
    if (banner) banner.hidden = true;
    send({ kind: 'consent', status: accepted ? 'accepted' : 'rejected', path: location.pathname || '/' });
    if (accepted) { lastPath = null; pageView(); }
  }

  // ------------------------------------------------------------------ start

  function start() {
    // A fresh arrival is a new visit: forget the last choice and ask again.
    if (!sameVisit()) {
      try { var s = store(); if (s) s.removeItem(KEY); } catch (e) { /* storage blocked */ }
    }
    if (choice() === null) show();
    else pageView();

    // Sites that change page without a full reload (the Founder profile).
    var notify = function () { window.setTimeout(pageView, 0); };
    ['pushState', 'replaceState'].forEach(function (name) {
      var original = history[name];
      if (typeof original !== 'function') return;
      history[name] = function () {
        var result = original.apply(this, arguments);
        notify();
        return result;
      };
    });
    window.addEventListener('popstate', notify);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
