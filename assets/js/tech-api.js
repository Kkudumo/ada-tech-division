// Shared by the pages that talk to the ADA Tech service database.
export const API = 'https://vjbdosprwtelfbpqpdcc.supabase.co/functions/v1/tech-public-api';

export const esc = (s) => String(s ?? '').replace(/[&<>"']/g,
  (m) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m]));

// Only https links, or links on this site, are ever written into a page.
export function safeUrl(u) {
  try {
    const x = new URL(String(u || ''), location.origin);
    return (x.protocol === 'https:' || x.origin === location.origin) ? x.href : '#';
  } catch (err) {
    return '#';
  }
}

export async function call(url, options) {
  const r = await fetch(url, options);
  const d = await r.json().catch(() => ({ ok: false, error: 'Invalid server response.' }));
  if (!r.ok && !d.error) d.error = 'Request failed.';
  return d;
}

export function post(body) {
  return call(API, { method: 'POST', headers: { 'content-type': 'application/json' }, cache: 'no-store', body: JSON.stringify(body) });
}

// Private values travel in the URL fragment, never the query string. Old links
// that still carry them in the query are rewritten in place.
export function privateParams(names) {
  const hash = new URLSearchParams(location.hash.replace(/^#/, ''));
  const legacy = new URLSearchParams(location.search);
  const out = {};
  let moved = false;
  names.forEach((n) => {
    out[n] = hash.get(n) || legacy.get(n) || '';
    if (legacy.get(n)) moved = true;
  });
  return { values: out, moved };
}
