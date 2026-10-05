// Case files, loaded from the ADA Tech service database. Used on /work (all
// of them) and on the home page (the newest few, via data-limit).
import { API, esc, safeUrl, call } from './tech-api.js';

const grid = document.getElementById('caseGrid');

function card(c) {
  const cover = c.cover_image_url
    ? `<img src="${esc(safeUrl(c.cover_image_url))}" alt="${esc(c.title)}" loading="lazy">` : '';
  const videos = (c.video_urls && c.video_urls.length)
    ? `<div class="case-media ${c.video_urls.length === 1 ? 'single' : ''}">` + c.video_urls.slice(0, 4).map((u, i) =>
      `<video controls preload="metadata" playsinline src="${esc(safeUrl(u))}" aria-label="${esc(c.title)} video ${i + 1}"></video>`).join('') + '</div>'
    : '';
  const row = (k, v) => `<div><dt>${k}</dt><dd>${esc(v)}</dd></div>`;
  return `<article class="case">${cover}${videos}<div class="case-body">
<span class="tag">${esc(c.category || 'Case file')}</span>
<h3 class="h3">${esc(c.title)}</h3>
<div class="case-meta"><span>${esc(c.device_system || 'Technical job')}</span><span>${esc(c.location || 'Rundu')}</span><span>${esc(c.completed_on || '')}</span></div>
<dl class="case-flow">${row('Issue', c.reported_issue)}${row('Diagnosis', c.diagnosis)}${row('Intervention', c.intervention)}${row('Result', c.result)}</dl>
</div></article>`;
}

if (grid) {
  const limit = Number(grid.dataset.limit) || 0;
  call(API + '?action=list_case_files').then((d) => {
    let list = d.case_files || [];
    if (!list.length) {
      grid.innerHTML = '<div class="empty"><strong>Published repair work will appear here.</strong>'
        + 'ADA Tech does not invent portfolio projects. Only real, documented jobs are published.</div>';
      return;
    }
    if (limit) list = list.slice(0, limit);
    grid.innerHTML = list.map(card).join('');
  }).catch(() => {
    grid.innerHTML = '<div class="empty"><strong>Case files are temporarily unavailable.</strong>Please try again in a little while.</div>';
  });
}
