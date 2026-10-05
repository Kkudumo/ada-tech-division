// Site search. Reads /assets/search-index.json (written by build/pages_search.py)
// and ranks pages in the browser. Tolerates plurals and small typing mistakes,
// so "price3s" still finds the pricing page. Results are built with
// textContent, never innerHTML.

const STOP = new Set(['a', 'an', 'the', 'and', 'or', 'of', 'to', 'for', 'in', 'on', 'is', 'are', 'my', 'our',
  'we', 'i', 'do', 'does', 'can', 'you', 'your', 'with', 'what', 'me', 'it']);

function clean(word) {
  // Letters only when the word has letters, so "price3s" becomes "prices".
  let w = word.toLowerCase();
  if (/[a-z]/.test(w)) w = w.replace(/[^a-z]/g, '');
  return w;
}

function stem(w) {
  if (w.length > 5 && w.endsWith('ing')) return w.slice(0, -3);
  if (w.length > 4 && w.endsWith('ies')) return w.slice(0, -3) + 'y';
  if (w.length > 4 && w.endsWith('es')) return w.slice(0, -2);
  if (w.length > 3 && w.endsWith('s') && !w.endsWith('ss')) return w.slice(0, -1);
  return w;
}

function tokens(text) {
  return text.split(/[^A-Za-z0-9$]+/).map(clean).filter((w) => w.length > 1 && !STOP.has(w)).map(stem);
}

function distance(a, b, max) {
  // Edit distance with an early exit; used only for short vocabularies.
  if (Math.abs(a.length - b.length) > max) return max + 1;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    let best = cur[0];
    for (let j = 1; j <= b.length; j++) {
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      if (cur[j] < best) best = cur[j];
    }
    if (best > max) return max + 1;
    prev = cur;
  }
  return prev[b.length];
}

function fieldScore(term, words, exact, prefix, fuzzy) {
  let best = 0;
  for (const w of words) {
    if (w === term) return exact;
    if (w.startsWith(term) || (term.length > 3 && term.startsWith(w) && w.length > 3)) best = Math.max(best, prefix);
    else if (fuzzy && term.length >= 4 && distance(term, w, term.length >= 8 ? 2 : 1) <= (term.length >= 8 ? 2 : 1)) {
      best = Math.max(best, fuzzy);
    }
  }
  return best;
}

let INDEX = null;

async function loadIndex() {
  if (INDEX) return INDEX;
  const res = await fetch('/assets/search-index.json', { cache: 'no-cache' });
  const docs = await res.json();
  INDEX = docs.map((d) => ({
    ...d,
    tw: tokens(d.t), kw: tokens(d.k), hw: tokens(d.h), dw: tokens(d.d), bw: tokens(d.b),
  }));
  return INDEX;
}

function search(docs, query) {
  const terms = tokens(query);
  if (!terms.length) return [];
  const scored = [];
  for (const doc of docs) {
    let total = 0;
    let matched = 0;
    for (const term of terms) {
      const bodyHits = doc.bw.filter((w) => w === term || w.startsWith(term)).length;
      const s = fieldScore(term, doc.tw, 12, 8, 5) + fieldScore(term, doc.kw, 10, 7, 4) +
        fieldScore(term, doc.hw, 5, 3, 0) + fieldScore(term, doc.dw, 4, 2, 0) + Math.min(bodyHits, 6) * 0.5;
      if (s > 0) matched += 1;
      total += s;
    }
    if (matched === 0) continue;
    // Pages matching every word rank above pages matching some.
    scored.push({ doc, score: total + (matched === terms.length ? 20 : 0), all: matched === terms.length });
  }
  const anyAll = scored.some((r) => r.all);
  return scored.filter((r) => !anyAll || r.all).sort((a, b) => b.score - a.score).slice(0, 15);
}

function snippet(doc, query) {
  const terms = tokens(query);
  const sentences = doc.b.split(/(?<=[.?!])\s+/);
  const hit = sentences.find((s) => tokens(s).some((w) => terms.some((t) => w === t || w.startsWith(t))));
  return (hit || doc.d).slice(0, 220);
}

function highlight(target, text, query) {
  const terms = tokens(query);
  text.split(/(\s+)/).forEach((part) => {
    const w = stem(clean(part));
    if (w && terms.some((t) => w === t || w.startsWith(t))) {
      const mark = document.createElement('mark');
      mark.textContent = part;
      target.appendChild(mark);
    } else {
      target.appendChild(document.createTextNode(part));
    }
  });
}

function render(results, query) {
  const list = document.getElementById('searchResults');
  const count = document.getElementById('searchCount');
  const popular = document.getElementById('searchPopular');
  list.textContent = '';
  if (!query.trim()) {
    count.textContent = '';
    popular.hidden = false;
    return;
  }
  popular.hidden = results.length > 0;
  if (!results.length) {
    count.textContent = 'Nothing found for "' + query + '". Try a different word, pick a page below, or contact us and ask.';
    return;
  }
  count.textContent = results.length + (results.length === 1 ? ' page' : ' pages') + ' found for "' + query + '"';
  results.forEach(({ doc }) => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = doc.u;
    const title = document.createElement('strong');
    highlight(title, doc.t, query);
    const text = document.createElement('span');
    highlight(text, snippet(doc, query), query);
    const where = document.createElement('em');
    where.textContent = doc.c + '  ' + (doc.u === '/' ? 'Home' : doc.u);
    a.append(title, text, where);
    li.appendChild(a);
    list.appendChild(li);
  });
}

async function run(query) {
  try {
    const docs = await loadIndex();
    render(search(docs, query), query);
  } catch (err) {
    console.error('ADA site: search failed', err);
    document.getElementById('searchCount').textContent =
      'Search could not load. Please use the menu, or try again in a moment.';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('q');
  const form = document.getElementById('searchForm');
  if (!input || !form) return;
  const initial = new URLSearchParams(window.location.search).get('q') || '';
  input.value = initial;
  if (initial) run(initial);

  let timer = null;
  input.addEventListener('input', () => {
    window.clearTimeout(timer);
    timer = window.setTimeout(() => run(input.value), 140);
  });
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const q = input.value.trim();
    const url = new URL(window.location.href);
    if (q) url.searchParams.set('q', q); else url.searchParams.delete('q');
    window.history.replaceState(null, '', url);
    run(q);
  });
});
