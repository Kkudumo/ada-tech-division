// Existing Client Desk: open a ticket and track one.
import { esc, safeUrl, post, privateParams } from './tech-api.js';

const { values, moved } = privateParams(['ticket', 'token', 'job', 'device']);
const { ticket, token, job, device } = values;

if (moved && (ticket || token)) {
  const h = new URLSearchParams();
  if (ticket) h.set('ticket', ticket);
  if (token) h.set('token', token);
  if (job) h.set('job', job);
  if (device) h.set('device', device);
  history.replaceState(null, '', location.pathname + '#' + h.toString());
}

if (ticket) {
  document.getElementById('trackCode').value = ticket;
  document.getElementById('trackToken').value = token;
}
if (job) document.getElementById('jobRef').value = job;
if (device) document.getElementById('deviceSystem').value = device;

const ticketForm = document.getElementById('ticketForm');
ticketForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  if (!ticketForm.reportValidity()) return;
  const f = new FormData(ticketForm);
  const out = document.getElementById('ticketResult');
  out.style.display = 'block';
  out.textContent = 'Creating ticket…';
  const body = { action: 'create_ticket' };
  for (const [k, v] of f) body[k] = v;
  try {
    const d = await post(body);
    if (!d.ok) throw new Error(d.error || 'Could not create the ticket.');
    out.innerHTML = '<div class="ticket-code">' + esc(d.ticket.code) + '</div>'
      + '<p>Status: <strong>' + esc(d.ticket.status) + '</strong></p>'
      + '<p><a class="more" href="' + esc(safeUrl(d.tracking_url)) + '">Open the private tracking link</a></p>'
      + '<p><strong>Keep this link private.</strong> Its token is the key to your ticket history.</p>';
  } catch (err) {
    out.textContent = err.message || 'Could not create the ticket.';
  }
});

const trackForm = document.getElementById('trackForm');
trackForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  if (!trackForm.reportValidity()) return;
  const f = new FormData(trackForm);
  const out = document.getElementById('trackResult');
  out.style.display = 'block';
  out.textContent = 'Checking…';
  try {
    const d = await post({ action: 'track_ticket', ticket_code: f.get('ticket_code'), access_token: f.get('access_token') });
    if (!d.ok) throw new Error(d.error || 'Ticket not found.');
    out.innerHTML = '<div class="ticket-code">' + esc(d.ticket.ticket_code) + '</div>'
      + '<p>' + esc(d.ticket.subject) + ' / <strong>' + esc(d.ticket.status) + '</strong></p>'
      + '<div class="timeline">' + (d.updates || []).map((u) => '<article><b>' + esc(u.status || 'Update') + '</b><p>'
        + esc(u.message) + '</p><small>' + esc(new Date(u.created_at).toLocaleString()) + '</small></article>').join('') + '</div>';
  } catch (err) {
    out.textContent = err.message || 'Ticket not found.';
  }
});
