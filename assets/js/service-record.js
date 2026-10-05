// Private Service Record: look one up with its code and token, and show it.
import { esc, post, privateParams } from './tech-api.js';

const view = document.getElementById('recordView');

function readPrivateParams() {
  const { values, moved } = privateParams(['record', 'token']);
  if (moved && (values.record || values.token)) {
    const h = new URLSearchParams();
    if (values.record) h.set('record', values.record);
    if (values.token) h.set('token', values.token);
    history.replaceState(null, '', location.pathname + '#' + h.toString());
  }
  return values;
}

function drawRecord(r, recordUrl) {
  const ref = r.job_reference || r.record_code;
  const reviewHash = new URLSearchParams({ job: ref, record: r.record_code, review_token: r.review_token });
  const helpHash = new URLSearchParams({ job: ref, device: r.device_system || '' });
  const reviewUrl = location.origin + '/reviews#' + reviewHash.toString();
  const helpUrl = location.origin + '/client-desk#' + helpHash.toString();
  const row = (k, v) => '<div><dt>' + k + '</dt><dd>' + esc(v) + '</dd></div>';
  view.innerHTML = '<div class="sheet"><div class="sheet-head"><span>ADA Technical Service Record</span><span>'
    + esc(r.record_code) + '</span></div><dl>'
    + row('Client', r.client_name || 'Private client')
    + row('Device', r.device_system)
    + row('Service', r.service_type)
    + row('Summary', r.service_summary)
    + row('Result', r.result)
    + row('Completed', r.completed_on)
    + (r.follow_up_note ? row('Follow-up', r.follow_up_note) : '')
    + '</dl></div>'
    + '<div class="record-actions"><div><span class="tag">Verified review</span><h3>Review this service</h3>'
    + '<p>The verification token stays in the link fragment and is sent only inside the protected review submission.</p>'
    + '<a class="more" href="' + esc(reviewUrl) + '">Leave a verified review</a></div>'
    + '<div><span class="tag">Need help again?</span><h3>Existing Client Desk</h3>'
    + '<p>The original job reference is carried into a new follow-up ticket.</p>'
    + '<a class="more" href="' + esc(helpUrl) + '">Request follow-up</a></div></div>'
    + '<div class="stop mt2"><strong>Private Service Record</strong><p>Do not post or forward the original record link publicly. Anyone with the private token can open this handover.</p></div>'
    + '<div class="record-tools"><button id="copyRecord" class="btn btn--blue" type="button">Copy private record link</button>'
    + '<button id="copyReview" class="btn btn--line" type="button">Copy review link</button>'
    + '<button id="printRecord" class="btn btn--line" type="button">Print or save as PDF</button></div>';
  const copy = (id, text) => {
    const b = document.getElementById(id);
    b.onclick = () => navigator.clipboard.writeText(text).then(() => { b.textContent = 'Copied'; });
  };
  copy('copyRecord', recordUrl);
  copy('copyReview', reviewUrl);
  document.getElementById('printRecord').onclick = () => window.print();
}

async function openRecord(record, token) {
  view.innerHTML = '<p class="live-note">Opening Service Record…</p>';
  try {
    const d = await post({ action: 'get_service_record', record, token });
    if (!d.ok) {
      view.innerHTML = '<h2 class="h2">Record unavailable</h2><p class="mt2">' + esc(d.error || 'Unable to open the record.')
        + '</p><p><a class="more" href="/service-record">Try again</a></p>';
      return;
    }
    const h = new URLSearchParams({ record, token });
    drawRecord(d.record, location.origin + '/service-record#' + h.toString());
  } catch (err) {
    view.innerHTML = '<h2 class="h2">Record unavailable</h2><p class="mt2">ADA Tech could not open this record right now.</p>'
      + '<p><a class="more" href="/service-record">Try again</a></p>';
  }
}

const lookup = document.getElementById('lookupForm');
lookup.addEventListener('submit', (e) => {
  e.preventDefault();
  if (!lookup.reportValidity()) return;
  const f = new FormData(lookup);
  const record = String(f.get('record') || '').trim();
  const token = String(f.get('token') || '').trim();
  const h = new URLSearchParams({ record, token });
  history.replaceState(null, '', location.pathname + '#' + h.toString());
  openRecord(record, token);
});

const initial = readPrivateParams();
if (initial.record && initial.token) openRecord(initial.record, initial.token);
