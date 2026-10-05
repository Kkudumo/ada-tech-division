// Client reviews: the public feed and the review form.
import { API, esc, call, post, privateParams } from './tech-api.js';

const { values, moved } = privateParams(['record', 'review_token', 'job']);
const serviceRecord = values.record;
const reviewToken = values.review_token;
const job = values.job || serviceRecord || '';

if (moved && (serviceRecord || reviewToken)) {
  const h = new URLSearchParams();
  if (job) h.set('job', job);
  if (serviceRecord) h.set('record', serviceRecord);
  if (reviewToken) h.set('review_token', reviewToken);
  history.replaceState(null, '', location.pathname + '#' + h.toString());
}

const jobField = document.getElementById('jobReference');
if (job && jobField) jobField.value = job;
if (serviceRecord && reviewToken) document.getElementById('serviceVerified').classList.add('show');

const grid = document.getElementById('reviewGrid');
const note = document.getElementById('refreshNote');

async function loadReviews() {
  try {
    const d = await call(API + '?action=list_reviews', { cache: 'no-store' });
    if (!d.ok) throw new Error(d.error || 'Review feed unavailable');
    if (!d.reviews || !d.reviews.length) {
      grid.innerHTML = '<div class="empty"><strong>No published reviews yet.</strong>Verified client feedback will appear here.</div>';
      return;
    }
    grid.innerHTML = d.reviews.map((r) => {
      const n = Math.max(0, Math.min(5, Number(r.rating) || 0));
      return '<article class="review"><div class="stars" role="img" aria-label="' + n + ' out of 5">'
        + '★'.repeat(n) + '☆'.repeat(5 - n) + '</div><h3>' + esc(r.client_name) + '</h3>'
        + (r.client_company ? '<p class="small muted">' + esc(r.client_company) + '</p>' : '')
        + '<blockquote>“' + esc(r.review) + '”</blockquote>'
        + (r.verified ? '<span class="verified">Verified ADA Tech client</span>' : '') + '</article>';
    }).join('');
    note.textContent = 'Live from ADA Tech. Last checked '
      + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + '.';
  } catch (err) {
    note.textContent = 'The review feed is temporarily unavailable.';
    if (grid.querySelector('.live-note')) grid.innerHTML = '<div class="empty"><strong>Reviews could not be loaded.</strong>Please try again in a little while.</div>';
  }
}

if (grid) {
  loadReviews();
  setInterval(loadReviews, 30000);
}

const form = document.getElementById('reviewForm');
if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const f = new FormData(form);
    const msg = document.getElementById('reviewMsg');
    msg.style.display = 'block';
    msg.textContent = 'Submitting…';
    const body = {
      action: 'submit_review',
      website: f.get('website'),
      client_name: f.get('client_name'),
      client_company: f.get('client_company'),
      rating: Number(f.get('rating')),
      review: f.get('review'),
      job_reference: f.get('job_reference'),
      contact_method: f.get('contact_method'),
      contact_value: f.get('contact_value'),
      consent_to_publish_name: !!f.get('consent'),
      service_record_code: serviceRecord || null,
      review_token: reviewToken || null,
    };
    try {
      const d = await call(API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) });
      msg.textContent = d.message || d.error || 'Unable to submit the review.';
      if (d.ok) {
        form.reset();
        if (job && jobField) jobField.value = job;
        loadReviews();
      }
    } catch (err) {
      msg.textContent = 'Unable to submit the review right now.';
    }
  });
}
