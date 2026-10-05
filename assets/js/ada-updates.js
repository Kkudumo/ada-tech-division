/* ADA shared updates.
   Shows the latest news, announcements and updates published from the Andreas
   Digital Agency admin area (www.andreasdigitalagency.com/admin, Website
   Content). Publishing once there puts the item on every ADA website.

   Put data-ada-updates="3" on the element that holds the cards. Options:
     data-mode="replace"      swap the cards on the page for the feed (default)
     data-mode="merge"        add feed items to the cards on the page, newest
                              first, and keep the newest N (N = data-ada-updates)
     data-mode="append"       add feed items after the cards on the page, then
                              order everything newest first
     data-only-published      only items published from the admin area
     data-time                show the date in its own <time> element
     data-card-class, data-tag-el, data-tag-class, data-title-el,
     data-title-class, data-text-class, data-link-class, data-link-text
   If the feed cannot be reached, the cards already on the page stay as they are. */
(function () {
  'use strict';
  var FEED = 'https://www.andreasdigitalagency.com/api/updates';
  var boxes = document.querySelectorAll('[data-ada-updates]');
  if (!boxes.length || !window.fetch) return;

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }

  /* Only links to the ADA main website are accepted from the feed. */
  function safeUrl(url) {
    return typeof url === 'string' && /^https:\/\/www\.andreasdigitalagency\.com\//.test(url) ? url : null;
  }

  function card(item, box) {
    var url = safeUrl(item.url);
    if (!url || !item.title) return null;
    var d = box.dataset;
    var a = el('a', d.cardClass || 'ada-update');
    a.href = url;
    a.setAttribute('data-ada-update', '');
    var day = typeof item.date === 'string' ? item.date.slice(0, 10) : '';
    if (day) a.setAttribute('data-date', day);
    if (box.hasAttribute('data-time')) {
      if (item.label) a.appendChild(el(d.tagEl || 'span', d.tagClass || '', item.label));
      if (item.dateLabel) {
        var time = el('time', '', item.dateLabel);
        if (day) time.setAttribute('datetime', day);
        a.appendChild(time);
      }
    } else {
      var tag = [item.label, item.dateLabel].filter(Boolean).join(' · ');
      if (tag) a.appendChild(el(d.tagEl || 'span', d.tagClass || '', tag));
    }
    a.appendChild(el(d.titleEl || 'h3', d.titleClass || '', item.title));
    if (item.summary) a.appendChild(el('p', d.textClass || '', item.summary));
    a.appendChild(el('span', d.linkClass || '', d.linkText || 'Read more'));
    return a;
  }

  function newestFirst(box) {
    Array.prototype.slice.call(box.children)
      .map(function (node, index) { return { node: node, index: index, date: node.getAttribute('data-date') || '' }; })
      .sort(function (a, b) { return b.date.localeCompare(a.date) || a.index - b.index; })
      .forEach(function (entry) { box.appendChild(entry.node); });
  }

  fetch(FEED, { credentials: 'omit' })
    .then(function (response) { return response.ok ? response.json() : Promise.reject(new Error('feed ' + response.status)); })
    .then(function (data) {
      var items = data && Array.isArray(data.items) ? data.items : [];
      Array.prototype.forEach.call(boxes, function (box) {
        var count = parseInt(box.getAttribute('data-ada-updates'), 10) || 3;
        var mode = box.getAttribute('data-mode') || 'replace';
        var onlyPublished = box.hasAttribute('data-only-published');
        var cards = items
          .filter(function (item) { return !onlyPublished || !!item.date; })
          .slice(0, count)
          .map(function (item) { return card(item, box); })
          .filter(Boolean);
        if (!cards.length) return;
        if (mode === 'replace') box.textContent = '';
        cards.forEach(function (node) { box.appendChild(node); });
        if (mode !== 'replace') newestFirst(box);
        if (mode === 'merge') while (box.children.length > count) box.removeChild(box.lastElementChild);
        box.setAttribute('data-ada-updates-loaded', '');
      });
    })
    .catch(function () { /* keep the cards already on the page */ });
})();
