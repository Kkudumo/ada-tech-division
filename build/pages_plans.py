"""Pricing, ADA First Aid and Managed IT.

Every amount on the site comes from PRICES, PACKAGES, FIRST_AID and MANAGED
below. Change a price here and rebuild.
"""
from layout import (page, hero, sec, head_block, answer, sheet, table, steps, ticks, faq, faq_schema,
                    service_schema, related, cards, info_cards, plan, stop, e, wa, DIAG, MAIN, REVIEWED)

PRICES = [
    ("Standard device diagnostic", DIAG, "Inspection and diagnosis. Deducted from the repair cost if you go ahead."),
    ("Remote quick support", "From N$149", "Basic software, account or configuration support, scoped before work."),
    ("PC tune-up and optimisation", "N$249", "Start-up clean-up, performance checks, updates and a basic system health review."),
    ("Driver or software fault", "From N$179", "Install, repair or correct drivers and common software."),
    ("Windows Update repair", "From N$249", "Find why updates fail and repair the update components."),
    ("BIOS or UEFI update", "From N$249", "Compatibility check, firmware update and verification of boot settings."),
    ("BIOS recovery or boot fault", "From N$449", "Advanced diagnosis where firmware or boot recovery is needed."),
    ("Microsoft Office setup", "From N$249", "Install and configure Office or Microsoft 365 and activate it with a valid licence."),
    ("Printer setup", "From N$179", "Installation on a computer or a network, and basic troubleshooting."),
    ("RAM or SSD fitting (labour)", "From N$179", "Fitting and testing. The part is quoted separately."),
    ("Data backup or transfer", "From N$249", "Basic transfer of up to 50GB. Complex recovery is quoted separately."),
    ("Router and Wi-Fi setup", "From N$349", "Router configuration, Wi-Fi setup and connectivity checks."),
]

PACKAGES = [
    ("Most chosen", "Windows Ready", "N$649", "Windows installed properly on a computer that is otherwise healthy.",
     ["Windows 10 or 11 installation or reinstallation", "Correct drivers for your model", "Windows updates",
      "BIOS and firmware version check", "Essential utilities", "Activation with your existing valid licence",
      "Basic performance settings", "Restore point and final test"], False),
    ("Best value", "Windows + Office Complete", "N$849", "Windows and Office, ready for work or study.",
     ["Everything in Windows Ready", "Microsoft Office or Microsoft 365 installed",
      "Office activated with a valid licence", "Browser, PDF reader and common utilities",
      "Basic printer check or setup", "Windows and Office updates verified", "Final system health check"], True),
    ("Full refresh", "Complete Device Refresh", "N$1,049", "A clean start that keeps your files.",
     ["Everything in Windows + Office Complete", "Backup and restore of up to 50GB",
      "Malware scan and clean-up", "Start-up optimisation", "Your user profile and common programs set up",
      "Device health review after installation", "7-day workmanship follow-up"], False),
]

FIRST_AID = [
    ("1 device", "First Aid Essential", "N$249", "One laptop or desktop that needs occasional help.",
     ["1 registered laptop or desktop", "Up to 3 remote support sessions a month",
      "Monthly software and update health check", "Driver and common software troubleshooting",
      "Help with Windows settings", "Priority WhatsApp support queue", "10% off other ADA Tech labour"], False),
    ("Recommended", "First Aid Plus", "N$399", "One device you depend on for work or study.",
     ["1 registered laptop or desktop", "Reasonable-use remote support during business hours",
      "Monthly maintenance session", "Windows, updates, drivers and common programs",
      "Basic malware clean-up", "Backup guidance and restore-point checks",
      "15% off other ADA Tech labour", "One in-depth health review each quarter"], True),
    ("Up to 3 devices", "First Aid Family", "N$699", "A household or a very small office.",
     ["Up to 3 registered devices", "6 remote support sessions a month", "Monthly health checks",
      "Windows, software and update support", "Basic malware clean-up", "Priority WhatsApp support",
      "15% off other ADA Tech labour"], False),
]

MANAGED = [
    ("Up to 5 devices", "Micro Business Care", "N$1,249", "A small office that needs someone to call.",
     ["Remote helpdesk for covered devices", "Monthly update and health schedule", "Basic device register",
      "Common Windows and software support", "Priority support handling", "10% off approved on-site labour"], False),
    ("Up to 10 devices", "Business Care", "N$2,449", "A growing team with staff joining and leaving.",
     ["Everything in Micro Business Care", "Support when staff join or leave",
      "Basic account and two-step verification review", "Backup status guidance",
      "Technology review each quarter", "Priority support handling", "15% off approved on-site labour"], True),
    ("11 or more devices", "Managed IT", "From N$3,949", "An organisation where technology runs the work.",
     ["Assessment of the environment first", "Device and user cover agreed to fit",
      "Support workflow and service records", "Maintenance and security baseline",
      "Network and Microsoft 365 coordination", "Regular operational review", "Response priorities agreed with you"], False),
]

PR = ("pricing", "Pricing")
FA = ("first-aid", "ADA First Aid")
MI = ("managed-it", "Managed IT")

LICENCE_NOTE = ("<strong>The cost of a software licence is never hidden inside a labour price.</strong> Windows "
                "and Microsoft Office are activated only with a valid licence or digital entitlement that you "
                "already own, or with a legitimate licence that is supplied and quoted separately. Hardware, "
                "replacement parts, complex data recovery, travel outside the normal Rundu service area and "
                "specialist third-party licences are also quoted separately.")


def package_cards():
    return '<div class="grid g3 swipe">' + "".join(
        plan(tag, name, price, "once-off", who, items,
             (wa(f"Hello ADA Tech, I would like to book {name} ({price}). My device is: "), "Book on WhatsApp"), main)
        for tag, name, price, who, items, main in PACKAGES) + "</div>"


def pricing():
    body = hero(
        "Prices",
        "Starting prices for defined work on one device. Networks, CCTV, servers and office setups depend on "
        "the site, so they are assessed and quoted.",
        [PR], [("/support", "Get support"), (wa("Hello ADA Tech, I would like a quote for: "), "Ask for a quote", "line")],
        code=("Price list", f"Reviewed {REVIEWED}"))
    body += sec('<div class="intro">' + answer(
        f"A standard diagnostic costs {DIAG} and is deducted from the repair cost if you go ahead. Windows "
        "installation packages cost N$649, N$849 and N$1,049. Remote support starts from N$149, a PC tune-up "
        "is N$249, and fitting RAM or an SSD starts from N$179 for labour. Monthly care starts from N$249 for "
        "one personal device and N$1,249 for an office of up to five devices. Prices are in Namibian dollars.")
        + sheet("How pricing works", "NAD", [
            ("Diagnostic", f"<strong>{DIAG}</strong>, deducted from the repair if you go ahead"),
            ("“From”", "The price when nothing unusual is found"),
            ("If scope changes", "You are told and asked before the work continues"),
            ("Parts", "Quoted separately"),
            ("Licences", "Legitimate only, quoted separately"),
        ], ("/support", "Get support")) + "</div>", "sec--tight")
    body += sec(head_block("Windows installation packages",
                           "One price for the whole job instead of paying for each step. Licences and replacement "
                           "hardware are separate.", label="Packages") + package_cards()
                + f'<p class="note mt2">{LICENCE_NOTE}</p>', "sec--light")
    body += sec(head_block("One-time work",
                           "Diagnosis comes first. If the scope changes after inspection, the new scope is "
                           "confirmed with you before major work.", label="Price list")
                + table(["Work", "Price", "What it covers"], PRICES))
    body += sec(head_block("Quoted after an assessment",
                           "These depend too much on the site, the equipment and the distance for one number to "
                           "be honest.", label="Projects") + cards([
        ("/services/networking", "Office networks and Wi-Fi", "Router-only setup starts from N$349. Cabling, "
         "equipment and coverage across several rooms are quoted.", "Wi-Fi and networking", "S-04", "wifi"),
        ("/services/cctv", "CCTV", "Camera count, recorder, storage, cabling, power and phone viewing decide the "
         "price.", "CCTV", "S-07", "camera"),
        ("/services/server-infrastructure", "Servers and infrastructure", "The server's role, the hardware, "
         "backup, users and network are assessed first.", "Servers", "S-08", "server"),
    ], swipe=True), "sec--light")
    covers = ["1 device, up to 3 remote sessions a month", "1 device, reasonable-use remote support",
              "Up to 3 devices, 6 remote sessions a month", "Up to 5 devices", "Up to 10 devices",
              "11 or more devices, after an assessment"]
    plans = [("/first-aid", n, p) for _t, n, p, _w, _i, _m in FIRST_AID] + \
            [("/managed-it", n, p) for _t, n, p, _w, _i, _m in MANAGED]
    monthly = [(f'<a href="{h}">{n}</a>', p + " a month", c) for (h, n, p), c in zip(plans, covers)]
    body += sec(head_block("Monthly care",
                           "For people and organisations that would rather not start from nothing each time "
                           "something goes wrong.", label="Plans")
                + table(["Plan", "Price", "Covers"], monthly)
                + '<p class="mt2"><a class="more" href="/first-aid">ADA First Aid for personal devices</a> &nbsp; '
                  '<a class="more" href="/managed-it">Managed IT for organisations</a></p>')
    qa = [
        ("Is the diagnostic fee refunded if I do not repair?",
         f"<p>No. The {DIAG} covers the inspection and diagnosis, which is done whether or not you go ahead. If "
         "you do go ahead with the repair, the full amount is deducted from the repair cost.</p>"),
        ("What does “from” mean on a price?",
         "<p>It is the price when the job is what it appears to be. If the inspection shows more is needed, you "
         "are told what and what it costs, and nothing extra is done until you agree.</p>"),
        ("Why are parts and licences not in the price?",
         "<p>Because they differ for every model and every customer. A stick of memory for one laptop costs "
         "something different from another, and many computers already carry a valid Windows licence. Quoting "
         "them separately means you pay for what your device actually needs.</p>"),
        ("Is travel charged?",
         "<p>Travel outside the normal Rundu service area is quoted separately, before the visit.</p>"),
        ("How do I pay, and what if I cancel?",
         f"<p>Payment, refunds and cancellations follow Andreas Digital Agency's "
         f"<a href=\"{MAIN}/payment-refund-cancellation\">payment, refund and cancellation policy</a>.</p>"),
    ]
    body += sec(head_block("Questions about prices", label="Questions") + faq(qa), "sec--light")
    schema = [faq_schema(qa)] + [
        service_schema(name, who, "pricing", price.replace("N$", "").replace(",", ""))
        for _t, name, price, who, _i, _m in PACKAGES]
    page("pricing", "Computer Repair and IT Support Prices in Rundu | ADA Tech",
         f"ADA Tech price list: diagnostic {DIAG}, Windows installation from N$649, remote support from N$149, "
         "tune-up N$249, upgrades from N$179, monthly care from N$249. Rundu, Namibia.",
         body, active="/pricing", crumbs=[PR], schema=schema)


def first_aid():
    ask = wa("Hello ADA Tech, I am interested in ADA First Aid. I have this many devices: ")
    body = hero(
        "ADA First Aid: monthly care for your computer",
        "For people whose laptop or desktop keeps needing small fixes. A known person to call, a monthly "
        "check, and a discount when something bigger goes wrong.",
        [FA], [("#plans", "See the three plans"), ("/support", "I need a one-time repair", "line")],
        code=("Care plan", "Personal devices"))
    body += sec('<div class="intro">' + answer(
        "ADA First Aid is a monthly care plan for personal laptops and desktops. It covers remote support, "
        "monthly health checks and help with Windows, updates, drivers and everyday software, with 10% or 15% "
        "off other ADA Tech labour. Plans cost N$249, N$399 and N$699 a month. It is not insurance: parts, paid "
        "licences and major physical repairs are separate.")
        + sheet("Plan sheet", "First Aid", [
            ("For", "Individuals, students and households"),
            ("Price", "<strong>N$249 to N$699</strong> a month"),
            ("Devices", "1 to 3 registered devices"),
            ("Delivered", "Remotely, anywhere in Namibia"),
            ("Not covered", "Parts, paid licences, major physical repairs"),
        ], (ask, "Ask which plan fits")) + "</div>", "sec--tight")
    body += sec(head_block("Is First Aid right for you?", label="Fit") + info_cards([
        ("Good fit", "Small faults keep coming back", "Windows settings, drivers, updates and software keep "
         "needing attention, a little at a time.", "update"),
        ("Good fit", "You want someone to call", "You would rather have a known support route than look for "
         "help from nothing every time.", "chat"),
        ("Not the first step", "The laptop is already broken", "No power, physical damage, a failed drive or a "
         "broken screen needs a diagnosis and repair first. <a href=\"/support\">Start one-time support</a>.", "wrench"),
    ], swipe=True), "sec--light")
    body += sec('<div id="plans">' + head_block("Three plans", "Billed monthly. Parts, paid software licences and "
                                                "major physical repairs are separate.", label="Cover")
                + '<div class="grid g3 swipe">' + "".join(
                    plan(tag, name, price, "a month", who, items,
                         (wa(f"Hello ADA Tech, I would like to start {name} ({price} a month). My device is: "),
                          "Start on WhatsApp"), main)
                    for tag, name, price, who, items, main in FIRST_AID) + "</div></div>")
    body += sec(head_block("Know what is included before you subscribe", label="Limits") + info_cards([
        ("Included", "Remote technical care", "Software faults, update problems, settings, drivers, common "
         "Windows problems and routine health checks, within the limits of your plan."),
        ("Discounted", "Other labour", "Physical repair and other approved labour get the plan discount. They "
         "are not unlimited work under the subscription."),
        ("Separate", "Parts, licences and specialist costs", "SSDs, memory, batteries, chargers, screens, paid "
         "licences, complex data recovery and third-party costs are quoted separately."),
    ], swipe=True), "sec--light")
    qa = [
        ("Is First Aid insurance?",
         "<p>No. It is a support relationship. It does not include unlimited physical repairs, replacement "
         "parts or paid software licences.</p>"),
        ("Can I use it outside Rundu?",
         "<p>Yes. The support in the plans is remote, so it works anywhere in Namibia with an internet "
         "connection. Physical repairs still need the workshop in Rundu.</p>"),
        ("How many remote sessions are included?",
         "<p>Essential includes up to three a month and Family includes six. Plus covers reasonable use during "
         "business hours. If you are not sure whether something is covered, ask before the session starts.</p>"),
        ("My laptop is broken now. Can I subscribe to get it fixed?",
         "<p>Start with a one-time diagnosis and repair. First Aid is for keeping a working device working. "
         "Once it is repaired, a plan makes sense.</p>"),
    ]
    body += sec(head_block("Questions about First Aid", label="Questions") + faq(qa))
    body += related([("/pricing", "One-time prices", "If you only need a single job."),
                     ("/managed-it", "Managed IT", "The same idea, for an organisation."),
                     ("/services/remote-support", "Remote support", "How a remote session works.")])
    schema = [faq_schema(qa)] + [service_schema("ADA " + n, w, "first-aid", p.replace("N$", ""), "month")
                                 for _t, n, p, w, _i, _m in FIRST_AID]
    page("first-aid", "ADA First Aid: Monthly Laptop and PC Care from N$249 | ADA Tech",
         "Monthly care for personal laptops and desktops in Namibia: remote support, health checks, help with "
         "Windows, updates and drivers, and a discount on repairs. From N$249 a month.",
         body, active="/first-aid", crumbs=[FA], schema=schema)


def managed_it():
    ask = wa("Hello ADA Tech, we would like a Managed IT assessment. Users: , devices: , main problems: ")
    body = hero(
        "Managed IT: IT support for small businesses",
        "ADA Tech is an IT company in Rundu. This is ongoing IT support for small businesses and other "
        "organisations where several people depend on the same technology, and waiting for something to "
        "break has started to cost working time.",
        [MI], [(ask, "Book an IT assessment"), ("#plans", "See monthly plans", "line")],
        code=("Care plan", "Organisations"))
    body += sec('<div class="intro">' + answer(
        "Managed IT is a monthly support plan for organisations that do not have their own IT staff. It covers "
        "a remote helpdesk for the registered devices, scheduled updates and health checks, and help when staff "
        "join or leave. Plans cost N$1,249 a month for up to 5 devices, N$2,449 for up to 10, and from N$3,949 "
        "for 11 or more. Hardware, licences and large projects are scoped separately.")
        + sheet("Plan sheet", "Managed IT", [
            ("For", "Organisations without their own IT staff"),
            ("Price", "<strong>From N$1,249</strong> a month"),
            ("Sized by", "Number of devices and users"),
            ("Starts with", "An assessment of what you have"),
            ("Not covered", "Hardware, licences, large projects"),
        ], (ask, "Book an IT assessment")) + "</div>", "sec--tight")
    body += sec(head_block("Signs that you need this model", label="Fit") + info_cards([
        ("Sign 1", "Several people keep needing help", "Support is no longer one laptop repair. Several people "
         "depend on the same setup.", "office"),
        ("Sign 2", "Small faults interrupt the work", "Updates, accounts, printers, Wi-Fi and new-starter setup "
         "keep taking productive time.", "update"),
        ("Sign 3", "You want continuity", "A known support relationship is more useful than finding a technician "
         "after the work has already stopped.", "doc"),
    ], swipe=True), "sec--light")
    body += sec('<div id="plans">' + head_block("Monthly plans, by size", "Hardware, licences, large projects and "
                                                "infrastructure are scoped separately.", label="Cover")
                + '<div class="grid g3 swipe">' + "".join(
                    plan(tag, name, price, "a month", who, items,
                         (wa(f"Hello ADA Tech, we would like to discuss {name}. Users: , devices: "),
                          "Discuss on WhatsApp"), main)
                    for tag, name, price, who, items, main in MANAGED) + "</div></div>")
    body += sec(head_block("Before a plan starts", "We need to understand the users, the devices and the "
                           "recurring problems before promising what a monthly plan will cover.", label="Sequence")
                + steps([
                    ("Discover", "What people use, what keeps failing and what causes downtime now."),
                    ("Baseline", "Accounts, updates, devices, backup status, Wi-Fi and common support needs."),
                    ("Scope", "What belongs in the monthly plan, and what stays as separately quoted project work."),
                ], cls="steps--3"), "sec--navy")
    qa = [
        ("What is the difference between Managed IT and calling when something breaks?",
         "<p>Calling when something breaks means the work has already stopped. A managed plan schedules the "
         "updates and checks that prevent many faults, keeps a record of your devices and accounts, and gives "
         "staff one place to ask for help.</p>"),
        ("Are on-site visits included?",
         "<p>The plans cover the remote helpdesk and scheduled checks. Approved on-site labour is discounted by "
         "10% or 15%, depending on the plan.</p>"),
        ("We are outside Rundu. Can we still use it?",
         "<p>The remote helpdesk works anywhere in Namibia. On-site work outside Rundu is quoted, including "
         "travel.</p>"),
    ]
    body += sec(head_block("Questions about Managed IT", label="Questions") + faq(qa))
    body += related([("/services/business-it", "Business IT setup", "The one-time setup that comes first."),
                     ("/services/security", "Security and backups", "Accounts and data kept safe."),
                     ("/first-aid", "ADA First Aid", "The same idea, for personal devices.")])
    schema = [faq_schema(qa)] + [service_schema(n, w, "managed-it", p.replace("From ", "").replace("N$", "").replace(",", ""), "month")
                                 for _t, n, p, w, _i, _m in MANAGED]
    page("managed-it", "IT Support for Small Businesses: Managed IT Plans | ADA Tech",
         "IT support for small businesses from an IT company in Rundu: remote helpdesk, scheduled updates and "
         "staff onboarding. From N$1,249 a month.",
         body, active="/managed-it", crumbs=[MI], schema=schema)


def build():
    pricing()
    first_aid()
    managed_it()
