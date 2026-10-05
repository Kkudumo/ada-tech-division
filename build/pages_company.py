"""How we work, case files, reviews, support, contact, FAQ, Rundu, who we
help, and the two private client pages.

The pages that talk to the service database (work, reviews, client desk and
service record) keep the element ids their scripts in assets/js/ rely on.
"""
from layout import (page, hero, sec, head_block, answer, sheet, table, steps, ticks, signs, faq, faq_schema,
                    related, cards, info_cards, code_rows, photo, stop, e, wa, WA, DIAG, MAIN, PHONE, PHONE_TEL,
                    COMPANY_LINE, COMPANY_TEL, EMAIL, PLACE)

PRIVACY = (f'<label class="consent"><input type="checkbox" required> <span>I understand that the information I '
           f'send will be handled as described in ADA\'s <a href="{MAIN}/privacy" target="_blank" '
           f'rel="noopener">Privacy Policy</a>.</span></label>')

STANDARD = [
    ("Assess", "We ask about the device or system, the symptoms, what changed recently and how much it is stopping your work."),
    ("Diagnose", "The parts that could cause that symptom are tested, so the cause is found and not guessed."),
    ("Recommend", "You are told what was found and the options: repair, replace, configure, update or refer."),
    ("Approve", "Where there is a cost beyond the diagnostic, nothing happens until you have agreed to it."),
    ("Implement", "The repair, setup or installation is done to the agreed scope."),
    ("Test", "The original symptom is checked again, and the device is tested as a whole."),
    ("Document", "Completed work can be handed over with a private Service Record and a route for follow-up."),
]


# ------------------------------------------------------------------ about

def about():
    c = [("about", "How we work")]
    body = hero(
        "Diagnose first. Fix the right fault.",
        "Every job at ADA Tech follows the same seven steps, whether it is one laptop or a whole office. This "
        "page sets out what happens after you contact us.",
        c, [("/support", "Get support"), ("/work", "See case files", "line")],
        code=("ADA Tech standard", "7 steps"))
    body += sec('<div class="intro">' + answer(
        "ADA Tech works in seven steps: assess, diagnose, recommend, approve, implement, test and document. The "
        f"diagnostic costs {DIAG} and comes off the repair if you go ahead. You approve the cost before any "
        "work beyond the diagnostic. Parts are not replaced on a guess, software is activated only with "
        "legitimate licences, and a completed job can be handed over with a private Service Record.")
        + sheet("Standard", "ADA-T", [
            ("Steps", "7, the same for every job"),
            ("Diagnostic", f"<strong>{DIAG}</strong>, deducted from the repair"),
            ("Approval", "Before any cost beyond the diagnostic"),
            ("Licences", "Legitimate only"),
            ("Handover", "Private Service Record"),
        ]) + "</div>", "sec--tight")
    body += sec(head_block("Seven steps from fault to handover",
                           "The aim is work that can be explained: less guessing, and no surprises on the bill.",
                           label="The bench sequence") + steps(STANDARD, cls="steps--7"), "sec--navy")
    body += sec(head_block("What you can hold us to", label="Boundaries") + info_cards([
        ("No guesswork", "Parts are not the first answer", "A cheap guess can become an expensive mistake. The "
         "fault is diagnosed before any replacement is recommended.", "wrench"),
        ("Legitimate software", "No grey-market keys", "Windows and Microsoft Office are activated only with a "
         "valid licence you own, or a legitimate one that is quoted separately.", "key"),
        ("Your files", "Important data is identified first", "Where work could affect stored files, backup or "
         "transfer is agreed before anything is erased.", "disk"),
        ("Real proof", "Case files, not invented projects", "What we publish comes from real jobs that were "
         "documented on the bench.", "doc"),
    ], cols=4, swipe=True))
    body += sec('<div class="split"><div><span class="label">Handover</span>'
                '<h2 class="h2">What a Service Record is</h2>'
                '<p class="mt2">After a completed job, ADA Tech can issue a private digital record of the '
                'device, the service performed, a summary of the work, the result and any follow-up note.</p>'
                + ticks(["It opens with a record code and a private token, and is not searchable.",
                         "From it you can leave a review that is verified against the job.",
                         "From it you can ask for follow-up with the original job reference attached.",
                         "It can be printed or saved as a PDF."])
                + '<p><a class="more" href="/service-record">Open a Service Record</a></p></div>'
                + photo("photo-repair", "") + "</div>", "sec--light")
    body += sec(head_block("Check the work", label="Proof") + cards([
        ("/work", "Case files", "Real jobs set out as issue, diagnosis, intervention and result.", "Open case files", "Proof", "doc"),
        ("/reviews", "Client reviews", "Approved feedback, loaded from the service database.", "Read reviews", "Clients", "chat"),
        (MAIN + "/about", "Andreas Digital Agency", "The company ADA Tech is a division of.", "Visit the main site", "Company", "office"),
    ], swipe=True))
    page("about", "How ADA Tech Works: Diagnose First, Then Fix | ADA Tech",
         "The seven steps ADA Tech follows on every job: assess, diagnose, recommend, approve, implement, test "
         "and document. No parts replaced on a guess, legitimate licences only.",
         body, active="/about", crumbs=c)


# ------------------------------------------------------------- case files

def work():
    c = [("work", "Case files")]
    body = hero(
        "Case files",
        "Real repair, diagnostic, network and setup jobs. Each one is written up the same way: the issue, the "
        "diagnosis, what was done and the result.",
        c, [("/reviews", "Read client reviews"), ("/support", "Get support", "line")],
        code=("Bench records", "Live"))
    body += sec(head_block("Published work",
                           "New jobs appear here after ADA Tech documents and publishes them. Nothing on this "
                           "page is invented.", label="From the service database")
                + '<div id="caseGrid" class="grid g2" aria-live="polite"><p class="live-note">Loading case files…</p></div>'
                + '<noscript><p class="note">Case files are loaded with JavaScript. Please switch it on, or '
                  f'<a href="{WA}">ask us on WhatsApp</a> for examples of recent work.</p></noscript>')
    body += sec(head_block("How to read a case file", label="Format") + steps([
        ("Issue", "What the client reported, in their words."),
        ("Diagnosis", "What testing showed the cause to be."),
        ("Intervention", "The work that was agreed and done."),
        ("Result", "What the device or system does now."),
    ], cls="steps--4"), "sec--navy")
    page("work", "Tech Case Files: Real Repair and IT Jobs | ADA Tech",
         "Documented ADA Tech jobs from Rundu, Namibia: the reported issue, the diagnosis, the work done and "
         "the result. Published from real repair and IT support work.",
         body, active="/work", crumbs=c, scripts=["/assets/js/work.js"])


# ---------------------------------------------------------------- reviews

def reviews():
    c = [("reviews", "Client reviews")]
    body = hero(
        "Client reviews",
        "Feedback from people and organisations ADA Tech has worked for. Reviews are loaded from the service "
        "database, and those sent through a Service Record are verified against the job.",
        c, [("#leave", "Leave a review"), ("/work", "See case files", "line")],
        code=("Review feed", "Live"))
    body += sec('<div class="sec-head sec-head--split"><div><span class="label">Published feedback</span>'
                '<h2 class="h2">Latest reviews</h2></div>'
                '<p class="live-note" id="refreshNote">The list checks for newly approved feedback automatically.</p></div>'
                '<div id="reviewGrid" class="grid g3" aria-live="polite"><p class="live-note">Loading reviews…</p></div>'
                '<noscript><p class="note">Reviews are loaded with JavaScript. Please switch it on to read them.</p></noscript>')
    form = f"""<form id="reviewForm" class="form" novalidate>
<div id="serviceVerified" class="verified-note">Official ADA Service Record detected. Your review can be verified automatically if the private token is valid.</div>
<div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="fields">
<div class="field"><label for="reviewName">Name</label><input id="reviewName" name="client_name" maxlength="120" autocomplete="name" required></div>
<div class="field"><label for="reviewCompany">Company or organisation <span class="opt">(optional)</span></label><input id="reviewCompany" name="client_company" maxlength="160" autocomplete="organization"></div>
<div class="field"><label for="reviewRating">Rating</label><select id="reviewRating" name="rating"><option value="5">5 / Excellent</option><option value="4">4 / Very good</option><option value="3">3 / Good</option><option value="2">2 / Fair</option><option value="1">1 / Poor</option></select></div>
<div class="field"><label for="jobReference">Job or Service Record reference <span class="opt">(optional)</span></label><input name="job_reference" id="jobReference" maxlength="120"></div>
<div class="field full"><label for="reviewText">Your review</label><textarea id="reviewText" name="review" rows="5" maxlength="2000" required></textarea></div>
<div class="field"><label for="contactMethod">Verification contact</label><select id="contactMethod" name="contact_method"><option>WhatsApp</option><option>Phone</option><option>Email</option></select></div>
<div class="field"><label for="contactValue">Number or email</label><input id="contactValue" name="contact_value" maxlength="180" autocomplete="email" required><span class="hint">Kept private. Never shown with the review.</span></div>
</div>
<label class="consent"><input type="checkbox" name="consent" checked> <span>My name may appear with this review if it is published.</span></label>
{PRIVACY}
<div id="reviewMsg" class="form-msg" role="status" aria-live="polite"></div>
<div class="btn-row"><button class="btn" type="submit">Submit review</button></div>
</form>"""
    body += sec('<div class="split" id="leave"><div><span class="label">Worked with ADA Tech?</span>'
                '<h2 class="h2">Leave a review</h2>'
                '<p class="mt2">If you opened this page from your private Service Record, the review is checked '
                'against that record. Other submissions are moderated before they are published.</p>'
                '<p>The contact you give is used only to verify the review. It is never returned by the public '
                'review feed.</p></div>' + form + "</div>", "sec--light")
    page("reviews", "Client Reviews of ADA Tech in Rundu | ADA Tech",
         "Approved reviews from ADA Tech clients in Rundu and across Namibia, loaded from the service database. "
         "Reviews sent through a Service Record are verified against the job.",
         body, active="/work", crumbs=c, scripts=["/assets/js/reviews.js"])


# ---------------------------------------------------------------- support

def support():
    c = [("support", "Get support")]
    body = hero(
        "Tell us what is going wrong",
        "You do not need to know whether the cause is hardware, Windows, the BIOS or the Wi-Fi. Give us the "
        "symptom and we start from there.",
        c, None, code=("Support request", "Opens WhatsApp"))
    form = f"""<form id="supportForm" class="form" novalidate>
<div class="fields">
<div class="field"><label for="supportName">Your name</label><input id="supportName" name="name" maxlength="120" autocomplete="name" required></div>
<div class="field"><label for="supportLocation">Where are you?</label><select id="supportLocation" name="location"><option>Rundu</option><option>Elsewhere in Namibia (remote support)</option><option>Other or not sure</option></select></div>
<div class="field full"><label for="supportDevice">Device or system</label><input id="supportDevice" name="device" maxlength="180" placeholder="For example: HP laptop, office Wi-Fi, Windows PC" required></div>
<div class="field full"><label for="supportProblem">What is happening?</label><textarea id="supportProblem" name="problem" rows="5" maxlength="1800" placeholder="Describe the symptom in your own words" required></textarea></div>
<div class="field"><label for="supportStarted">When did it start? <span class="opt">(optional)</span></label><input id="supportStarted" name="started" maxlength="180" placeholder="For example: this morning, after an update"></div>
<div class="field"><label for="supportImpact">Has work stopped?</label><select id="supportImpact" name="impact"><option>No, it is still usable</option><option>Partly, work is affected</option><option>Yes, I cannot work</option></select></div>
</div>
{PRIVACY}
<div class="btn-row"><button class="btn" type="submit">Send to ADA Tech on WhatsApp</button></div>
<p class="small muted mt2">This form does not store your message on the website. It opens WhatsApp with your details filled in, so you can read them before you send.</p>
</form>"""
    body += sec('<div class="split"><div><span class="label">Four useful details</span>'
                '<h2 class="h2">What helps us diagnose faster</h2>'
                + steps([
                    ("Device or system", "Laptop make and model, desktop, router, printer, office network or other system."),
                    ("Symptom", "What exactly happens: an error message, a blue screen, no power, slow, dropping connection."),
                    ("When it started", "After an update, a fall, a power cut, new software or a hardware change, or for no clear reason."),
                    ("Impact", "Whether the device is still usable, or work has stopped."),
                ], vertical=True)
                + sheet("Diagnostic", DIAG, [
                    ("Covers", "Standard laptop or desktop diagnosis"),
                    ("If you repair", "The fee is deducted from the repair cost"),
                    ("If you do not", "The fee is not refunded"),
                ]) + "</div>" + form + "</div>")
    body += sec(head_block("Already know what you need?", label="Other routes") + cards([
        (wa("Hello ADA Tech, I would like a quote for: "), "Request a quote", "For a known service, installation or "
         "project where you already understand the need.", "Ask on WhatsApp", "Quote", "tag"),
        ("/client-desk", "Follow up on previous work", "Priority review, warranty or rework, complaints and ticket "
         "tracking go through the Client Desk.", "Open the Client Desk", "Existing client", "doc"),
        ("/managed-it", "Ongoing support for an organisation", "For teams that need regular support across users, "
         "devices and business technology.", "See Managed IT", "Business", "office"),
    ], swipe=True), "sec--light")
    page("support", "Get Computer and IT Support in Rundu or Remotely | ADA Tech",
         "Describe a computer, Windows, Wi-Fi or office IT problem to ADA Tech. The form opens WhatsApp with your "
         f"details filled in. Diagnostic {DIAG}, deducted from the repair.",
         body, active="/support", crumbs=c, scripts=["/assets/js/support.js"], cta=False)


# ---------------------------------------------------------------- contact

def contact():
    c = [("contact", "Contact")]
    body = hero(
        "Contact ADA Tech",
        "The quickest reply comes from choosing the right route: a fault, a quote, ongoing support for an "
        "organisation, or follow-up on earlier work.",
        c, [("/support", "Describe a problem"), (WA, "Open WhatsApp", "line")], code=("Contact", "4 routes"))
    body += sec(head_block("What do you need?", label="Routes") + cards([
        ("/support", "Something is not working", "A laptop, Windows, Wi-Fi, a printer or another technical "
         "fault.", "Start support", "Fault", "wrench"),
        (wa("Hello ADA Tech, I would like a quote for: "), "I know what I need", "An installation, a setup, an "
         "upgrade, CCTV, a network or other defined work.", "Request a quote", "Quote", "tag"),
        ("/managed-it", "We need ongoing support", "For organisations that need regular help across users and "
         "devices.", "Book an IT assessment", "Business", "office"),
        ("/client-desk", "ADA Tech worked on this before", "Priority review, warranty or rework, a complaint or "
         "general follow-up.", "Open the Client Desk", "Existing client", "doc"),
    ], cols=4, swipe=True))
    body += sec(f"""<div class="split"><div><span class="label">Direct</span><h2 class="h2">Phone, WhatsApp and email</h2>
<ul class="contact-list mt2">
<li><span>WhatsApp</span><a href="{WA}" target="_blank" rel="noopener">{PHONE}</a></li>
<li><span>Phone</span><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
<li><span>Company line</span><a href="tel:{COMPANY_TEL}">{COMPANY_LINE}</a></li>
<li><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
</ul>
<p class="mt2 muted small">WhatsApp is the preferred route for support, diagnostics, quick questions and bookings. Email suits formal requests, documents and specifications.</p></div>
<div>{sheet("Where we work", "Rundu", [
        ("Workshop", e(PLACE)),
        ("On site", "Rundu"),
        ("Remote", "Across Namibia, where the fault allows"),
        ("Diagnostic", f"<strong>{DIAG}</strong>, deducted from the repair"),
        ("Company", f'<a href="{MAIN}/">Andreas Digital Agency</a>'),
    ])}</div></div>""", "sec--light")
    page("contact", "Contact ADA Tech: Phone, WhatsApp and Email | Rundu",
         "Contact ADA Tech in Rundu, Namibia by WhatsApp, phone or email for computer repair, IT support, quotes "
         "and follow-up on previous work.",
         body, active="/contact", crumbs=c, cta=False)


# -------------------------------------------------------------------- faq

FAQ_GROUPS = [
    ("Diagnosis and repair", [
        ("Do I have to pay before you diagnose my laptop or computer?",
         f"<p>The standard device diagnostic costs {DIAG}. If you go ahead with the repair, the fee is deducted "
         "from the repair cost. If you decide not to repair, the fee is not refunded. More complex faults may "
         "need a separate quote.</p>"),
        ("How long will my repair take?",
         "<p>It depends on the fault, on whether parts are available and on whether more testing is needed. "
         "ADA Tech does not promise a fixed repair time before the diagnosis. You are told what was found and "
         "what the next step is before more work is approved.</p>"),
        ("Do you repair both laptops and desktop computers?",
         "<p>Yes. Both, including diagnostics, Windows and software faults, drive and memory upgrades, drivers, "
         "BIOS and UEFI, performance problems and selected hardware faults.</p>"),
        ("Can you replace or upgrade RAM and SSDs?",
         "<p>Yes, where the device supports it. Fitting starts from N$179 for labour. Hardware and parts are "
         "quoted separately unless the written quotation says otherwise. See "
         "<a href=\"/problems/ssd-ram-upgrade\">RAM or SSD: which first?</a></p>"),
        ("Can you fix Wi-Fi, routers, printers and small office technology?",
         "<p>Yes. Router and Wi-Fi setup, printers, workstation setup, Windows and software faults and general "
         "small-business technology problems. Larger networks and infrastructure are assessed before a quote "
         "is issued.</p>"),
    ]),
    ("Windows, Office and licences", [
        ("Can you install Windows 10 or Windows 11?",
         "<p>Yes. ADA Tech installs or reinstalls supported Windows versions with drivers, updates and "
         "essential utilities. Activation uses an existing valid digital entitlement or a legitimate licence "
         "that you already own or that is quoted separately.</p>"),
        ("Does the Windows package include a new Windows licence key?",
         "<p>No, unless the written quote explicitly includes a legitimate licence. The service price covers "
         "the technical work. ADA Tech does not use pirated or grey-market activation keys.</p>"),
        ("Can you install Microsoft Office?",
         "<p>Yes. Office or Microsoft 365 is installed and activated with a valid licence or subscription that "
         "belongs to you. Paid Microsoft licences are separate unless included in a written quote.</p>"),
    ]),
    ("Your files", [
        ("Will my files be safe during the repair?",
         "<p>ADA Tech tries to avoid unnecessary data loss and explains when a repair could affect stored "
         "files. Tell us about important data before work begins. Backup and transfer can be added where "
         "needed. No technician can guarantee recovery of data from a failing or damaged drive.</p>"),
        ("Do you back up my files before reinstalling Windows?",
         "<p>Only when backup or transfer is part of the approved service. The Complete Device Refresh includes "
         "basic backup and restore of up to 50GB. Larger or complex data jobs may be quoted separately.</p>"),
    ]),
    ("Remote support and monthly care", [
        ("Do you provide remote support outside Rundu?",
         "<p>Yes. ADA Tech provides remote support across Namibia where the problem can be handled safely over "
         "an internet connection. Remote work always needs your permission before access begins.</p>"),
        ("What is ADA First Aid?",
         "<p>A monthly device-care and support relationship. It provides defined remote support, maintenance "
         "checks and labour discounts, depending on the plan. It is not insurance, and it does not include "
         "unlimited physical repairs, replacement parts or paid software licences. "
         "<a href=\"/first-aid\">See the plans</a>.</p>"),
    ]),
    ("After the job", [
        ("I am an old client. Can I ask for priority help?",
         "<p>Yes. Use the <a href=\"/client-desk\">Existing Client Desk</a> and choose Priority Support. Being "
         "a returning client helps us understand the history, but priority is reviewed against workload, "
         "severity, warranty or rework status and any active care plan.</p>"),
        ("What if a problem comes back after ADA worked on it?",
         "<p>Use the <a href=\"/client-desk\">Existing Client Desk</a> and select Warranty / Rework. Include the "
         "previous job or Service Record reference and say what changed. ADA Tech reviews whether the new "
         "symptom is related to the original work before deciding the next action.</p>"),
        ("How do I make a complaint?",
         "<p>Use the <a href=\"/client-desk\">Existing Client Desk</a> and select Complaint. This creates a "
         "tracked ticket, so the issue is recorded, reviewed and updated and is not lost in informal "
         "messages.</p>"),
        ("What is an ADA Service Record?",
         "<p>A private digital handover record created after a completed ADA Tech job. It can show the device, "
         "the type of service, a summary of the work, the result and a follow-up note. You receive a private "
         "link, with direct actions to review the service or ask for help again.</p>"),
        ("Are my Service Record and support ticket public?",
         "<p>No. Service Records and ticket history use private access tokens. Public case files and verified "
         "reviews are separate, and are published deliberately.</p>"),
        ("Can ADA publish my repair as a case file?",
         "<p>ADA Tech may document technical work as a case file, but information that identifies a client is "
         "shown only where appropriate and with permission. Case files exist to show the technical issue, the "
         "diagnosis, the work and the result.</p>"),
    ]),
]


def faq_page():
    c = [("faq", "Questions and answers")]
    body = hero(
        "Questions before you hand over your device",
        "Plain answers about diagnostics, repairs, Windows and Office licences, your files, parts, remote "
        "support, follow-up, complaints and Service Records.",
        c, [("/support", "Get support"), (WA, "Ask on WhatsApp", "line")],
        code=("Reference", f"{sum(len(g[1]) for g in FAQ_GROUPS)} answers"))
    alt = False
    for name, items in FAQ_GROUPS:
        body += sec(head_block(name, label="Questions") + faq(items), "sec--light" if alt else "")
        alt = not alt
    allq = [qa for _n, items in FAQ_GROUPS for qa in items]
    page("faq", "ADA Tech FAQ: Repairs, Windows Licences, Data and Support",
         "Answers about ADA Tech computer and laptop repairs, the diagnostic fee, Windows and Office licences, "
         "data safety, remote support, monthly care, complaints and Service Records.",
         body, active="/faq", crumbs=c, schema=[faq_schema(allq)])


# ------------------------------------------------------------------ rundu

def rundu():
    path = "locations/rundu"
    c = [(path, "IT support in Rundu")]
    body = hero(
        "Computer repair and IT support in Rundu",
        "ADA Tech is based in Rundu, Kavango East. Work that needs hands on the equipment is done here: "
        "laptop and desktop repair, Wi-Fi and networks, CCTV and office setups.",
        c, [("/support", "Tell us what is wrong"), (wa("Hello ADA Tech, I am in Rundu and need help with: "), "WhatsApp from Rundu", "line")],
        code=("Workshop", "Rundu, Kavango East"))
    body += sec('<div class="intro">' + answer(
        "ADA Tech repairs laptops and desktop computers, installs Windows, fixes Wi-Fi and networks, installs "
        f"CCTV and sets up office IT in Rundu, Namibia. A standard diagnostic costs {DIAG} and comes off the "
        "repair if you go ahead. Windows installation packages start at N$649, and router and Wi-Fi setup "
        "starts from N$349. Software faults can also be fixed remotely anywhere in Namibia.")
        + sheet("Local sheet", "Rundu", [
            ("Base", e(PLACE)),
            ("On site", "Repair, networks, CCTV, office setup"),
            ("Diagnostic", f"<strong>{DIAG}</strong>, deducted from the repair"),
            ("Contact", f'<a href="tel:{PHONE_TEL}">{PHONE}</a>'),
            ("Before you come", "Send the device and the symptom first"),
        ], ("/support", "Tell us what is wrong")) + "</div>", "sec--tight")
    body += sec(head_block("What is handled in Rundu",
                           "Hardware, networks and cameras are best assessed with the equipment in front of us.",
                           label="On site") + code_rows([
        ("/services/computer-repair", "wrench", "S-01", "Computer and laptop repair", "Slow, not starting, overheating, drive, memory and upgrades.", f"Diagnostic {DIAG}"),
        ("/services/windows-setup", "windows", "S-02", "Windows and software setup", "Clean installation, drivers, updates and Office.", "From N$649"),
        ("/services/networking", "wifi", "S-04", "Wi-Fi and networking", "Routers, coverage, small-office networks and cabling.", "From N$349"),
        ("/services/cctv", "camera", "S-07", "CCTV", "Camera planning, recorder setup and viewing on your phone.", "Quoted by site"),
        ("/services/business-it", "office", "S-09", "Business IT setup", "Devices, accounts, printers and Wi-Fi for an office.", "Quoted"),
    ]), "sec--light")
    body += sec('<div class="split"><div><span class="label">Before you visit</span>'
                '<h2 class="h2">Start with the symptom</h2>'
                '<p class="mt2">Send a message first with the device and what it is doing. Often we can tell you '
                'what to check, whether it can be fixed remotely, or what to bring.</p>'
                + ticks(['<a href="/problems">Look up the fault</a>: twelve common problems, with checks you can do yourself.',
                         '<a href="/pricing">See the prices</a> before you decide.',
                         '<a href="/work">Read the case files</a> to see how jobs are documented.',
                         'Bring the charger with a laptop. It is part of the diagnosis.'])
                + "</div>" + photo("photo-laptop", "") + "</div>")
    qa = [
        ("Where is ADA Tech in Rundu?",
         f"<p>ADA Tech works from Rundu, Kavango East. Message or call {PHONE} before coming, so we can tell you "
         "where to bring the device and when.</p>"),
        ("Do you come to homes and offices in Rundu?",
         "<p>Yes, for work that has to be done on site, such as Wi-Fi, networks, CCTV and office setups. A "
         "single laptop is usually better diagnosed on the bench.</p>"),
        ("Do you help people in Nkurenkuru, Divundu or elsewhere in the Kavango regions?",
         "<p>Software and account problems can be handled by remote support anywhere in Namibia. On-site work "
         "outside the normal Rundu service area is quoted, including travel.</p>"),
        ("How much does laptop repair cost in Rundu?",
         f"<p>The diagnostic is {DIAG} and comes off the repair. After it, you get the repair price before any "
         "work. Published starting prices are on the <a href=\"/pricing\">pricing page</a>.</p>"),
    ]
    body += sec(head_block("Questions from Rundu", label="Questions") + faq(qa), "sec--light")
    body += related([("/problems", "Find your problem", "Twelve common faults and what to check."),
                     ("/first-aid", "ADA First Aid", "Monthly care for a personal device."),
                     ("/managed-it", "Managed IT", "Monthly support for an organisation.")], cls="")
    page(path, "Computer Repair and IT Support in Rundu, Namibia | ADA Tech",
         f"Laptop and computer repair, Windows installation, Wi-Fi, CCTV and office IT in Rundu, Kavango East. "
         f"Diagnostic {DIAG}, deducted from the repair. Call or WhatsApp {PHONE}.",
         body, active="", crumbs=c, schema=[faq_schema(qa)])


# -------------------------------------------------------------- who we help

def solutions():
    c = [("solutions", "Who we help")]
    body = hero(
        "Who ADA Tech helps",
        "From one student laptop to an office of twenty. The fault-finding is the same. What changes is how "
        "much depends on the device.",
        c, [("/support", "Get support"), ("/pricing", "See prices", "line")], code=("Clients", "6 situations"))
    body += sec(head_block("Choose the situation closest to yours", label="Situations") + cards([
        ("/services/computer-repair", "Individuals and students", "A personal laptop or desktop that is slow, "
         "will not start, overheats or needs Windows.", "Computer repair", "One device", "laptop"),
        ("/first-aid", "Households", "Two or three computers that keep needing small fixes. One monthly plan "
         "covers up to three devices.", "ADA First Aid", "Up to 3 devices", "kit"),
        ("/services/remote-support", "Remote workers", "Software, accounts, Microsoft 365 and connection problems "
         "fixed over the internet, anywhere in Namibia.", "Remote support", "Anywhere", "remote"),
        ("/services/business-it", "Small businesses", "Devices, Wi-Fi, printers, email and accounts set up "
         "together, without employing IT staff.", "Business IT setup", "Office", "office"),
        ("/services/networking", "Lodges, schools and sites", "Wi-Fi that has to reach rooms, classrooms or "
         "several buildings, and cameras to watch the site.", "Wi-Fi and networking", "Site", "wifi"),
        ("/managed-it", "Growing organisations", "Monthly support across users, devices and accounts, with a "
         "record of what you have.", "Managed IT", "Ongoing", "server"),
    ], swipe=True))
    body += sec(head_block("The same seven steps for all of them",
                           "Assess, diagnose, recommend, approve, implement, test, document.", label="Standard")
                + steps(STANDARD, cls="steps--7")
                + '<p class="mt2"><a class="more" href="/about">How we work</a></p>', "sec--navy")
    page("solutions", "Who ADA Tech Helps: Individuals, Offices and Organisations",
         "IT support for individuals, students, households, remote workers, small businesses, lodges, schools "
         "and growing organisations in Rundu and across Namibia.",
         body, active="", crumbs=c)


# ------------------------------------------------------------ client desk

def client_desk():
    c = [("client-desk", "Existing Client Desk")]
    body = hero(
        "Existing Client Desk",
        "Already worked with ADA Tech? Open a request that can be tracked: priority review, warranty or "
        "rework, a complaint or a general follow-up.",
        c, [("#open", "Open a ticket"), ("#track", "Track a ticket", "line")], code=("Client desk", "Private"))
    body += sec(head_block("Three kinds of request", label="Routes") + info_cards([
        ("Priority support", "Returning-client priority review", "Your previous job reference gives us useful "
         "context. Priority requests are reviewed. They do not automatically jump every queue.", "doc"),
        ("Warranty / rework", "Something related to earlier work", "Put the original job reference and what "
         "changed on record for review.", "wrench"),
        ("Complaint", "Something was not handled well", "Submit it properly so ADA Tech can review it, respond "
         "and record how it was resolved.", "chat"),
    ], swipe=True), "sec--tight")
    ticket = f"""<form id="ticketForm" class="form" novalidate>
<div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="fields">
<div class="field full"><label for="ticketType">Request type</label><select id="ticketType" name="ticket_type"><option value="priority_support">Priority support request</option><option value="warranty_rework">Warranty / rework follow-up</option><option value="complaint">Complaint</option><option value="general_followup">General follow-up</option></select></div>
<div class="field"><label for="clientName">Your name</label><input id="clientName" name="client_name" maxlength="120" autocomplete="name" required></div>
<div class="field"><label for="jobRef">Original job reference <span class="opt">(recommended)</span></label><input id="jobRef" name="original_job_reference" maxlength="120"></div>
<div class="field"><label for="contactMethod">Contact method</label><select id="contactMethod" name="contact_method"><option>WhatsApp</option><option>Phone</option><option>Email</option></select></div>
<div class="field"><label for="contactValue">Number or email</label><input id="contactValue" name="contact_value" maxlength="180" required></div>
<div class="field full"><label for="deviceSystem">Device or system <span class="opt">(optional)</span></label><input id="deviceSystem" name="device_system" maxlength="180"></div>
<div class="field full"><label for="ticketSubject">Subject</label><input id="ticketSubject" name="subject" maxlength="180" required></div>
<div class="field full"><label for="ticketDescription">What happened?</label><textarea id="ticketDescription" name="description" rows="5" maxlength="3000" required></textarea></div>
<div class="field full"><label for="ticketUrgency">Urgency</label><select id="ticketUrgency" name="urgency"><option value="normal">Normal</option><option value="high">High: work is affected</option><option value="critical">Critical: work has stopped</option></select></div>
</div>
{PRIVACY}
<div class="btn-row"><button class="btn" type="submit">Create client ticket</button></div>
<div id="ticketResult" class="result" role="status" aria-live="polite"></div>
</form>"""
    body += sec('<div class="split" id="open"><div><span class="label">Open a client ticket</span>'
                '<h2 class="h2">Request follow-up</h2>'
                '<p class="mt2">After you submit, save the private tracking link. Anyone with that link can see '
                'the status of the ticket, so treat it like a password.</p></div>' + ticket + "</div>", "sec--light")
    track = """<form id="trackForm" class="form" novalidate>
<div class="fields">
<div class="field full"><label for="trackCode">Ticket code</label><input id="trackCode" name="ticket_code" maxlength="80" autocomplete="off" required></div>
<div class="field full"><label for="trackToken">Private tracking token</label><input id="trackToken" type="password" name="access_token" maxlength="100" autocomplete="off" spellcheck="false" required></div>
</div>
<div class="btn-row"><button class="btn btn--blue" type="submit">Track ticket</button></div>
<div id="trackResult" class="result" role="status" aria-live="polite"></div>
</form>"""
    body += sec('<div class="split" id="track"><div><span class="label">Track a ticket</span>'
                '<h2 class="h2">See its current status</h2>'
                '<p class="mt2">The ticket code is not enough on its own. The separate private tracking token '
                'is also needed. Tokens are kept out of normal page addresses.</p></div>' + track + "</div>")
    page("client-desk", "Existing Client Desk | ADA Tech",
         "Open and track a private ADA Tech client ticket for priority support, warranty or rework, complaints "
         "and follow-up on previous work.",
         body, active="", crumbs=c, noindex=True, scripts=["/assets/js/client-desk.js"], cta=False)


# --------------------------------------------------------- service record

def service_record():
    c = [("service-record", "Service Record")]
    body = hero(
        "Service Record",
        "Open the private handover for a completed ADA Tech job: the device, the service performed, the "
        "result and the route for follow-up.",
        c, None, code=("Private record", "Token required"))
    lookup = """<div id="recordView" class="record"><span class="label">Open your record</span>
<h2 class="h2">Enter the code and token</h2>
<p class="mt2">Use the record code and the private token ADA Tech gave you. The two work together, and records cannot be searched for.</p>
<form id="lookupForm" class="form mt2" novalidate>
<div class="fields">
<div class="field full"><label for="recordCode">Record code</label><input id="recordCode" name="record" maxlength="80" placeholder="ADA-SR-2026-XXXXXX" autocomplete="off" spellcheck="false" required></div>
<div class="field full"><label for="recordToken">Private token</label><input id="recordToken" type="password" name="token" maxlength="100" autocomplete="off" spellcheck="false" required></div>
</div>
<div class="btn-row"><button class="btn btn--blue" type="submit">Open Service Record</button></div>
</form></div>"""
    side = sheet("Privacy", "Private", [
        ("Not indexed", "Service Records are kept out of search engines."),
        ("No lookup", "A record code alone cannot open the handover."),
        ("No third party", "Private tokens are not sent to any outside QR service."),
        ("Private links", "Review and follow-up links keep their tokens out of referrer headers."),
    ]) + '<p class="small muted mt2">Treat the private link like a password. Anyone who has it can open the record.</p>'
    body += sec('<div class="split split--wide">' + lookup + "<div>" + side + "</div></div>")
    page("service-record", "ADA Tech Service Record",
         "Open a private ADA Tech Service Record with your record code and private token.",
         body, active="", crumbs=c, noindex=True, scripts=["/assets/js/service-record.js"], cta=False)


def build():
    about()
    work()
    reviews()
    support()
    contact()
    faq_page()
    rundu()
    solutions()
    client_desk()
    service_record()
