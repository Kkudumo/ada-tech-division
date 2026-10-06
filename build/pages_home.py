"""Home page."""
from layout import (page, sec, head_block, steps, faq, faq_schema, ticks, buttons, cards, info_cards, icon,
                    e, wa, DIAG, PHONE)
from pages_problems import PROBLEMS, HOME_FAULTS, KEYWORDS as FAULT_WORDS
from pages_services import service_rows
from pages_plans import package_cards
from pages_company import STANDARD
from pages_news import latest

HOME_FAQ = [
    ("How much does it cost to have a laptop looked at?",
     f"<p>A standard diagnostic costs {DIAG}. If you go ahead with the repair, that amount is deducted from the "
     "repair cost. If you decide not to repair, the fee is not refunded. You are told the repair price before "
     "any work beyond the diagnostic. See <a href=\"/pricing\">all prices</a>.</p>"),
    ("Do you only work in Rundu?",
     "<p>Hands-on work, such as hardware repair, networks and CCTV, is done in Rundu. Software, Windows and "
     "account problems can be fixed by <a href=\"/services/remote-support\">remote support</a> anywhere in "
     "Namibia, with your permission.</p>"),
    ("Will my files be safe?",
     "<p>Tell us which files matter before work begins. Where a repair could affect stored files, backup is "
     "agreed first. No technician can guarantee recovery from a drive that is failing or damaged, which is why "
     "we say so before starting. See <a href=\"/guides/back-up-your-files\">how to back up your files</a>, "
     "or <a href=\"/guides/data-recovery-deleted-files-dead-drive\">data recovery in Rundu and Namibia</a> if "
     "files are already missing.</p>"),
    ("Do you install Windows with a licence?",
     "<p>Windows and Office are activated only with a valid licence you already own, or a legitimate one that "
     "is quoted separately. Most computers that came with Windows already carry a digital licence. ADA Tech "
     "does not use pirated or grey-market keys.</p>"),
    ("How long does a repair take?",
     "<p>It depends on the fault and on whether a part must be ordered. We do not promise a time before the "
     "diagnosis. After it, you know what was found, what it costs and what happens next.</p>"),
    ("What if the problem comes back?",
     "<p>Use the <a href=\"/client-desk\">Existing Client Desk</a> and choose Warranty / Rework, with your job "
     "or Service Record reference. The request is tracked, and we review whether it relates to the original "
     "work.</p>"),
]


def finder():
    rows = []
    for p in PROBLEMS:
        more = "" if p["slug"] in HOME_FAULTS else " data-more hidden"
        words = " ".join([p["short"], p["blurb"], p["area"], p["causes"], FAULT_WORDS.get(p["slug"], "")]).lower()
        rows.append(f'<li data-k="{e(words)}"{more}><a href="/problems/{p["slug"]}"><b>{p["code"]}</b>'
                    f'<span>{e(p["short"])}</span></a></li>')
    # Home shows the commonest first, in HOME_FAULTS order.
    order = {s: i for i, s in enumerate(HOME_FAULTS)}
    pairs = sorted(zip(PROBLEMS, rows), key=lambda pr: order.get(pr[0]["slug"], 99))
    return f"""<nav class="finder" aria-labelledby="finder-h">
<div class="finder-head"><h2 id="finder-h">Fault finder</h2><span id="finderCount">{len(PROBLEMS)} faults</span></div>
<div class="finder-q"><label for="finderQ" aria-hidden="true">&gt;</label><input id="finderQ" type="search" placeholder="Type the symptom: slow, blue screen, Wi-Fi…" autocomplete="off" aria-label="Type the symptom to filter the list of faults"></div>
<ul id="finderList">{''.join(r for _p, r in pairs)}</ul>
<p class="finder-none" id="finderNone" hidden>Not in the list. <a href="/support">Describe it to us</a> and we will work it out.</p>
<div class="finder-foot"><a href="/problems">All {len(PROBLEMS)} faults</a><a href="/support">Not listed? Describe it</a></div>
</nav>"""


def build():
    hero = f"""<section class="hero hero-home on-dark"><div class="hero-bg" aria-hidden="true"><span></span><span></span><span></span></div><div class="wrap">
<div>
<span class="where"><span>ADA Tech Division</span><span>Workshop: Rundu</span><span>Remote: all Namibia</span></span>
<h1 class="display">Computer repair and IT support in Rundu, diagnosed before anything is replaced.</h1>
<p class="lead">ADA Tech is an IT company in Rundu, Namibia. We repair laptops and desktops, install Windows,
fix Wi-Fi and networks, set up CCTV and look after office IT. A diagnostic costs {DIAG} and comes off the
repair if you go ahead. You hear the price before the work starts.</p>
{buttons(('/support', 'Tell us what is wrong'), ('/pricing', 'See prices', 'line'))}
</div>
{finder()}
</div></section>"""

    facts = f"""<section aria-label="Readouts"><div class="wrap"><div class="facts">
<div><i>Diagnostic</i><b>{DIAG}</b><strong>Deducted from the repair</strong><span>If you go ahead, the fee comes off the repair cost.</span></div>
<div><i>Method</i><b>7</b><strong>Steps in every job</strong><span>Assess, diagnose, recommend, approve, implement, test, document.</span></div>
<div><i>Fault index</i><b>12</b><strong>Faults explained</strong><span>Each with checks you can do yourself, at no cost.</span></div>
<div><i>Cover</i><b>Rundu</b><strong>Workshop and on-site work</strong><span>Remote support for software faults anywhere in Namibia.</span></div>
</div></div></section>"""

    services = sec(head_block(
        "What we repair and set up",
        "Nine services. Each has a page that says what is covered, when you need it and what it costs.",
        label="Service index") + service_rows()
        + '<p class="mt2"><a class="more" href="/pricing">Compare all prices</a></p>')

    how = sec(head_block(
        "How a job runs on the bench",
        "The same seven steps for one laptop or a whole office. You approve the cost before any work beyond "
        "the diagnostic.", label="ADA Tech standard") + steps(STANDARD, cls="steps--7")
        + '<p class="mt2"><a class="more" href="/about">How we work, in full</a></p>', "sec--navy")

    packages = sec('<div class="sec-head sec-head--split"><div><span class="label">Windows packages</span>'
                   '<h2 class="h2">One price for the whole installation</h2></div>'
                   '<a class="more" href="/pricing">Full price list</a></div>' + package_cards()
                   + '<p class="small muted mt2">Licences and replacement hardware are separate. Windows and '
                     'Office are activated only with a legitimate licence.</p>', "sec--light")

    proof = sec('<div class="sec-head sec-head--split"><div><span class="label">Bench records</span>'
                '<h2 class="h2">Recent case files</h2>'
                '<p>Real jobs, written up as issue, diagnosis, intervention and result. Loaded from the service '
                'database.</p></div><a class="more" href="/work">All case files</a></div>'
                '<div id="caseGrid" class="grid g3 swipe" data-limit="3" aria-live="polite">'
                '<p class="live-note">Loading case files…</p></div>'
                '<p class="mt2"><a class="more" href="/reviews">Read client reviews</a></p>')

    care = sec(head_block(
        "Do not start from nothing every time something fails",
        "Two monthly plans: one for personal devices, one for organisations.", label="Ongoing care") + cards([
            ("/first-aid", "ADA First Aid", "Monthly care for one to three personal laptops or desktops: remote "
             "sessions, health checks and 10% or 15% off other labour.", "From N$249 a month", "Personal", "kit"),
            ("/managed-it", "Managed IT", "Monthly support for an organisation's devices, users and accounts, "
             "sized by the number of devices.", "From N$1,249 a month", "Business", "office"),
        ], cols=2), "sec--light")

    trust = sec(f"""<div class="split">
<div>
<span class="label">Before you hand over a device</span>
<h2 class="h2">Check us first</h2>
<p class="mt2 muted">You should not have to take a repair shop's word for it. These are things you can verify yourself.</p>
{ticks([
    'Read the <a href="/pricing">prices</a>. They are published, with what each one covers.',
    'Read the <a href="/work">case files</a>: real jobs, written up step by step.',
    'Read the <a href="/reviews">client reviews</a>, including the ones verified against a job.',
    'Read <a href="/about">how we work</a>: seven steps, and what you approve before we start.',
    'Try the <a href="/problems">checks on the problem pages</a> yourself. If they fix it, you owe us nothing.',
])}
</div>
<div>
<span class="label">What we will not do</span>
<h2 class="h2">Three refusals</h2>
<ul class="signs mt2">
<li><strong>Replace parts on a guess.</strong> The fault is found first, then the part is recommended.</li>
<li><strong>Install pirated software.</strong> Windows and Office are activated with legitimate licences only.</li>
<li><strong>Do extra work you did not approve.</strong> If the scope changes, you are asked before it continues.</li>
</ul>
</div>
</div>""")

    start = sec("""<div class="split">
<div>
<span class="label">Not sure where to start?</span>
<h2 class="h2">Answer two questions</h2>
<p class="mt2 muted">Tell us what the thing is and what you need, and we will point you to the right page. Nothing is sent to us.</p>
</div>
<form class="form" id="startForm">
<div class="fields">
<div class="field full"><label for="start-thing">What is it?</label>
<select id="start-thing" name="thing">
<option value="computer">A laptop or desktop computer</option>
<option value="windows">Windows or a program on it</option>
<option value="wifi">Wi-Fi, a router or the internet</option>
<option value="printer">A printer</option>
<option value="cctv">Cameras (CCTV)</option>
<option value="office">A whole office: several devices and people</option>
</select></div>
<div class="field full"><label for="start-need">What do you need?</label>
<select id="start-need" name="need">
<option value="broken">It has stopped working</option>
<option value="slow">It is slow or unreliable</option>
<option value="setup">Something set up or installed</option>
<option value="care">Regular care, so it keeps working</option>
</select></div>
</div>
<div class="btn-row"><button class="btn btn--blue" type="submit">Show my starting point</button></div>
<div class="answer mt2" id="startResult" hidden role="status"></div>
</form>
</div>""", "sec--light")

    guides = sec('<div class="sec-head sec-head--split"><div><span class="label">Guides</span>'
                 '<h2 class="h2">Plain answers before you spend money</h2></div>'
                 '<a class="more" href="/guides">All guides</a></div>' + cards([
        ("/guides/windows-10-end-of-support", "Windows 10 support has ended: what to do",
         "The dates, the free security updates that run to October 2027, and how to tell whether your PC can "
         "run Windows 11.", "Read the guide", "Windows", "windows"),
        ("/guides/repair-or-replace-laptop", "Repair or replace an old laptop?",
         "Five questions that settle it, and which repairs are nearly always worth doing.", "Read the guide",
         "Buying", "laptop"),
        ("/guides/back-up-your-files", "How to back up your files",
         "A simple routine that survives a dead drive, a theft and a spilled drink, and how to test it.",
         "Read the guide", "Data", "disk"),
        ("/guides/data-recovery-deleted-files-dead-drive", "Deleted files or a dead hard drive?",
         "What to do first, what can usually be recovered, and what cannot.", "Read the guide", "Data", "disk"),
        ("/guides/cctv-installation-cost-namibia", "CCTV installation cost in Namibia",
         "What you are paying for, what changes the price, and what to ask an installer.", "Read the guide",
         "CCTV", "camera"),
    ], swipe=True))

    news = sec('<div class="sec-head sec-head--split"><div><span class="label">ADA Tech today</span>'
               '<h2 class="h2">News, updates and notices</h2></div>'
               '<a class="more" href="/news">All news</a></div>' + latest(3), "sec--light")

    questions = sec(head_block("Questions people ask first", label="Questions") + faq(HOME_FAQ)
                    + '<p class="mt2"><a class="more" href="/faq">All questions and answers</a></p>')

    body = hero + facts + services + how + packages + proof + care + trust + start + guides + news + questions
    page("", "IT Company in Rundu: Computer Repair and IT Support | ADA Tech",
         "ADA Tech is an IT company in Rundu, Namibia: computer and laptop repair, Windows, Wi-Fi, CCTV and office "
         f"IT, with remote support in Namibia. Diagnostic {DIAG}.",
         body, schema=[faq_schema(HOME_FAQ)], scripts=["/assets/js/work.js", "/assets/js/ada-updates.js"])
