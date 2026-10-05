// Support form. Nothing is stored: the details are turned into a WhatsApp
// message that the person reads and sends themselves.
const form = document.getElementById('supportForm');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const f = new FormData(form);
    const val = (k, d) => String(f.get(k) || d || '').trim();
    const lines = [
      'Hi ADA Tech, I need technical support.', '',
      'Name: ' + val('name'),
      'Location: ' + val('location'),
      'Device/System: ' + val('device'),
      'Problem: ' + val('problem'),
      'Started: ' + val('started', 'Not sure'),
      'Work impact: ' + val('impact'),
    ];
    location.assign('https://wa.me/264818032641?text=' + encodeURIComponent(lines.join('\n')));
  });
}
