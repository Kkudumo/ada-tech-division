"""Services hub and the nine service pages."""
from layout import (page, hero, sec, head_block, answer, sheet, table, steps, ticks, signs, faq, faq_schema,
                    service_schema, related, code_rows, cards, e, wa, DIAG)

SVC = ("services", "Services")

SEPARATE = ("Parts, paid software licences and other outside costs are separate unless a written quote says "
            "they are included.")

SERVICES = [
    {
        "slug": "computer-repair", "code": "S-01", "icon": "wrench", "group": "Devices",
        "name": "Computer and laptop repair", "row": "Slow, hot, crashing or not starting",
        "from": f"Diagnostic {DIAG}", "price": "99",
        "title": "Computer and Laptop Repair in Rundu | ADA Tech",
        "desc": "Laptop and desktop repair in Rundu, Namibia: diagnosis for slow, overheating, crashing or dead "
                f"computers, RAM and SSD upgrades, data transfer. Diagnostic {DIAG}, deducted from the repair.",
        "h1": "Computer and laptop repair",
        "lead": "For laptops and desktops that are slow, hot, crashing or will not start. The fault is found "
                "and explained before any part is replaced.",
        "answer": f"ADA Tech diagnoses and repairs laptops and desktop computers in Rundu. A standard diagnostic "
                  f"costs {DIAG} and is deducted from the repair if you go ahead. You are told what failed and "
                  "what the repair costs before any work or part is charged. Fitting RAM or an SSD starts from "
                  "N$179 for labour, and a tune-up costs N$249.",
        "where": "Workshop in Rundu",
        "covers": ["Slow performance diagnosis", "Start-up and boot faults", "Drive and memory testing",
                   "Overheating and cooling", "Isolating a hardware fault to one part",
                   "Fitting RAM and SSDs", "Malware and software-related faults", "Driver faults",
                   "Ports and accessories that stopped working"],
        "signs": ["The laptop will not turn on, or turns on and shows nothing.",
                  "It has become slow, or freezes when busy.",
                  "It overheats, or the fan never stops.",
                  "Windows crashes with a blue screen.",
                  "You want more memory or a faster drive, and need to know what fits."],
        "prices": [("Standard device diagnostic", DIAG, "Inspection and diagnosis. Deducted from the repair cost if you go ahead."),
                   ("PC tune-up and optimisation", "N$249", "Start-up clean-up, performance checks, updates and a basic system health review."),
                   ("Driver or software fault", "From N$179", "Install, repair or correct drivers and common software."),
                   ("RAM or SSD fitting (labour)", "From N$179", "Fitting and testing. The part is quoted separately."),
                   ("Data backup or transfer", "From N$249", "Basic transfer of up to 50GB. Complex recovery is quoted separately.")],
        "steps": [("Describe the symptom", "Tell us the device, what it does and when it started. You do not need to know the cause."),
                  ("Diagnosis", "We test the parts that could cause that symptom and find which one it is."),
                  ("Finding and price", "You are told what failed, the options and what each costs. You decide."),
                  ("Repair, test, hand over", "The agreed work is done and tested against the original symptom.")],
        "faq": [("Do I pay before you look at it?",
                 f"<p>The standard diagnostic costs {DIAG}. If you go ahead with the repair, that amount is "
                 "deducted from the repair cost. If you decide not to repair, the fee is not refunded. A complex "
                 "fault may need a separate quote, and you are told before that work starts.</p>"),
                ("Do you repair both laptops and desktops?",
                 "<p>Yes. Both, including Windows and software faults, drive and memory upgrades, drivers, "
                 "BIOS and firmware, performance problems and selected hardware faults.</p>"),
                ("Will my files be safe?",
                 "<p>We avoid unnecessary data loss and tell you when a repair could affect stored files. Tell "
                 "us about important files before work begins, and add a backup where it is needed. Nobody can "
                 "guarantee recovery from a drive that is failing or damaged.</p>"),
                ("How long does a repair take?",
                 "<p>It depends on the fault and on whether parts are available. We do not promise a time "
                 "before the diagnosis. After it, you know what was found and what happens next.</p>")],
        "rel": [("/problems", "Find your problem", "Twelve common faults, with checks you can do yourself."),
                ("/problems/ssd-ram-upgrade", "RAM or SSD: which upgrade first?", "Choose the right part."),
                ("/pricing", "Pricing", "Every published price in one place.")],
    },
    {
        "slug": "windows-setup", "code": "S-02", "icon": "windows", "group": "Devices",
        "name": "Windows and software setup", "row": "Install, reinstall, drivers, updates and Office",
        "from": "From N$649", "price": "649",
        "title": "Windows 10 and 11 Installation in Rundu from N$649 | ADA Tech",
        "desc": "Windows installation and reinstallation in Rundu: correct drivers, updates, Microsoft Office "
                "setup, backup and restore. Three packages from N$649. Legitimate licences only.",
        "h1": "Windows and software setup",
        "lead": "A clean installation should leave the computer ready to use: correct drivers, updates done, "
                "your programs in place, and tested.",
        "answer": "ADA Tech installs and reinstalls Windows 10 and Windows 11 in three packages. Windows Ready "
                  "(N$649) covers Windows, drivers, updates and testing. Windows + Office Complete (N$849) adds "
                  "Microsoft Office and common programs. Complete Device Refresh (N$1,049) adds backup and "
                  "restore of up to 50GB and a malware clean-up. Windows and Office are activated only with a "
                  "legitimate licence.",
        "where": "Workshop in Rundu. Some work by remote support",
        "covers": ["Windows 10 or 11 installation or reinstallation", "Correct drivers for your model",
                   "Windows updates, and update repair", "Activation with a valid licence",
                   "Microsoft Office or Microsoft 365 setup", "Browser, PDF reader and everyday programs",
                   "Basic performance settings", "A restore point and a final test"],
        "signs": ["Windows is damaged, unstable or badly infected.",
                  "You replaced the drive and need Windows on the new one.",
                  "A second-hand computer needs a clean start.",
                  "Drivers are missing: no sound, no Wi-Fi, a blurry screen.",
                  "You need Office installed and activated with your licence."],
        "prices": [("Windows Ready", "N$649", "Windows, drivers, updates, BIOS version check, essential utilities, activation with your valid licence, restore point and final test."),
                   ("Windows + Office Complete", "N$849", "Everything in Windows Ready, plus Office or Microsoft 365 with your valid licence, browser, PDF and common programs, a printer check and a final health check."),
                   ("Complete Device Refresh", "N$1,049", "Everything in Windows + Office Complete, plus backup and restore of up to 50GB, malware scan and clean-up, start-up optimisation and a 7-day workmanship follow-up."),
                   ("Microsoft Office setup only", "From N$249", "Install and configure Office or Microsoft 365 and activate it with a valid licence."),
                   ("Windows Update repair", "From N$249", "Find why updates fail and repair the update components."),
                   ("Driver or software fault", "From N$179", "Install, repair or correct drivers and common software.")],
        "steps": [("Licence and files", "We check what licence the computer has and which files must be kept."),
                  ("Backup, if agreed", "Files are copied off before anything is erased."),
                  ("Install and configure", "Windows, the correct drivers, updates and your programs."),
                  ("Test and hand over", "Sound, Wi-Fi, camera, ports and activation are checked before it goes back.")],
        "faq": [("Does the price include a Windows licence key?",
                 "<p>No, unless the written quote says so. The price covers the technical work. Most computers "
                 "that came with Windows already have a digital licence that activates again after a reinstall. "
                 "ADA Tech does not use pirated or grey-market keys. See "
                 "<a href=\"/guides/genuine-windows-and-office-licences\">how to check your licence</a>.</p>"),
                ("Can you install Microsoft Office?",
                 "<p>Yes. Office or Microsoft 365 is installed and activated with a valid licence or "
                 "subscription that belongs to you. Paid licences are separate unless a written quote includes "
                 "one.</p>"),
                ("Do you back up my files before reinstalling?",
                 "<p>Only when backup is part of the agreed service. The Complete Device Refresh includes backup "
                 "and restore of up to 50GB. Larger or more complex jobs are quoted separately.</p>"),
                ("Can my computer run Windows 11?",
                 "<p>It needs a supported processor, TPM 2.0, Secure Boot, at least 4GB of memory and 64GB of "
                 "storage. We check this before quoting. See "
                 "<a href=\"/guides/windows-10-end-of-support\">Windows 10 support has ended</a>.</p>")],
        "rel": [("/guides/windows-10-end-of-support", "Windows 10 support has ended", "Your options, with dates."),
                ("/guides/genuine-windows-and-office-licences", "Genuine Windows and Office", "How to check what you have."),
                ("/problems/windows-update-not-working", "Windows Update fails or gets stuck", "Checks to try first.")],
    },
    {
        "slug": "bios-firmware", "code": "S-03", "icon": "chip", "group": "Devices",
        "name": "BIOS and firmware", "row": "Updates, settings and start-up recovery",
        "from": "From N$249", "price": "249",
        "title": "BIOS and UEFI Update and Recovery in Rundu | ADA Tech",
        "desc": "BIOS and UEFI updates, boot settings, Secure Boot and TPM setup, and recovery after a failed "
                "firmware update. Updates from N$249, recovery from N$449. Rundu, Namibia.",
        "h1": "BIOS and firmware",
        "lead": "Firmware is the software a computer runs before Windows starts. A wrong setting or a failed "
                "update can stop a healthy computer from starting at all.",
        "answer": "ADA Tech updates BIOS and UEFI firmware, corrects boot settings, turns on Secure Boot and TPM "
                  "for Windows 11, and assesses computers that will not start after a failed firmware update. "
                  "Updates start from N$249. Recovery work starts from N$449 and depends on the model and on "
                  "how the update failed.",
        "where": "Workshop in Rundu",
        "covers": ["Checking the current BIOS or UEFI version", "Compatibility checks before an update",
                   "Firmware updates where they are needed", "Boot mode and Secure Boot settings",
                   "TPM settings for Windows 11", "Diagnosis of start-up failures",
                   "Assessment for firmware recovery", "Stability checks after an update"],
        "signs": ["The computer will not start after a BIOS update.",
                  "Windows 11 says the PC is not supported, though the hardware should be.",
                  "A new drive or memory is not being detected.",
                  "It asks for a BIOS password nobody remembers.",
                  "The maker recommends a firmware update for a fault you have."],
        "prices": [("BIOS or UEFI update", "From N$249", "Compatibility check, firmware update and verification of boot settings."),
                   ("BIOS recovery or boot fault", "From N$449", "Advanced diagnosis where firmware or boot recovery is needed."),
                   ("Standard device diagnostic", DIAG, "Deducted from the repair cost if you go ahead.")],
        "steps": [("Identify the model", "Firmware is specific to the exact model and revision."),
                  ("Check before changing", "Current version, the maker's notes, battery and power."),
                  ("Update or recover", "With stable power and the maker's own tools."),
                  ("Verify", "Boot settings, drive detection and a normal start into Windows.")],
        "faq": [("Should I update my BIOS?",
                 "<p>Only for a reason: the maker lists a fix for a fault you have, a security fix, or support "
                 "for new hardware. A BIOS update that is interrupted can leave the computer unable to start, "
                 "so it is not routine maintenance.</p>"),
                ("My laptop will not start after a BIOS update. Can it be recovered?",
                 "<p>Sometimes. Many models have a recovery method built in by the maker. Others need the "
                 "firmware chip reprogrammed, which is specialist work. We assess the model first and tell you "
                 "which applies.</p>"),
                ("Can you remove a forgotten BIOS password?",
                 "<p>It depends on the model. We will ask you to show that the computer is yours first.</p>")],
        "rel": [("/problems/laptop-not-turning-on", "Laptop will not turn on", "What to check first."),
                ("/guides/windows-10-end-of-support", "Windows 10 support has ended", "Secure Boot and TPM for Windows 11."),
                ("/services/computer-repair", "Computer and laptop repair", "Diagnosis for hardware faults.")],
    },
    {
        "slug": "networking", "code": "S-04", "icon": "wifi", "group": "Connectivity",
        "name": "Wi-Fi and networking", "row": "Routers, coverage, cabling and office networks",
        "from": "From N$349", "price": "349",
        "title": "Wi-Fi and Network Setup in Rundu from N$349 | ADA Tech",
        "desc": "Router setup, Wi-Fi troubleshooting, coverage for homes, offices and lodges, cabling and small "
                "office networks in Rundu, Namibia. Router and Wi-Fi setup from N$349.",
        "h1": "Wi-Fi and networking",
        "lead": "For homes, offices and lodges where the internet drops, does not reach every room, or has "
                "grown one device at a time with nobody planning it.",
        "answer": "ADA Tech sets up routers and Wi-Fi, finds why connections drop, extends coverage to rooms "
                  "the signal does not reach, and builds small office networks with cabling, shared printers "
                  "and basic security. Router and Wi-Fi setup starts from N$349. Larger jobs with cabling, "
                  "extra equipment or several rooms are assessed on site and quoted.",
        "where": "On site in Rundu",
        "covers": ["Router installation and configuration", "Wi-Fi troubleshooting",
                   "Coverage and router placement checks", "Small office network setup",
                   "Network cable planning", "Devices that will not connect",
                   "Printers and shared devices on the network", "Basic network security settings",
                   "Connectivity assessment for a branch or second office"],
        "signs": ["Wi-Fi drops several times a day.",
                  "Some rooms, or the far end of the property, have no signal.",
                  "A new router needs setting up properly.",
                  "Card machines, cameras or a booking system depend on the connection.",
                  "Guests or visitors need Wi-Fi that is separate from the office network."],
        "prices": [("Router and Wi-Fi setup", "From N$349", "Router configuration, Wi-Fi setup and connectivity checks."),
                   ("Printer setup on the network", "From N$179", "Installation and basic troubleshooting."),
                   ("Office network, cabling, coverage across rooms", "Quoted", "Assessed on site. Depends on the building, the distance and the equipment.")],
        "steps": [("Assess", "What is connected, where the signal falls away, and what the connection is used for."),
                  ("Recommend", "The smallest change that fixes it, with the equipment listed and priced."),
                  ("Install and configure", "Router, access points, cabling and security settings."),
                  ("Test and document", "Speed and signal are checked in the rooms that matter, and the settings are written down for you.")],
        "faq": [("Why is my Wi-Fi slow when I pay for a fast line?",
                 "<p>The line speed is what reaches the router. What reaches your laptop also depends on the "
                 "router's position, the walls in between and how many devices share it. We measure both so you "
                 "know which one is the limit.</p>"),
                ("Do you supply the router and equipment?",
                 "<p>We recommend what fits the site and quote it separately from the labour. You can also buy "
                 "the equipment yourself from the list.</p>"),
                ("Can guests have Wi-Fi without reaching our office computers?",
                 "<p>Yes. A separate guest network keeps visitors away from office devices and files. Most "
                 "current routers support it.</p>")],
        "rel": [("/problems/wifi-keeps-disconnecting", "Wi-Fi keeps disconnecting", "Checks to try first."),
                ("/services/cctv", "CCTV", "Cameras depend on the same network."),
                ("/services/business-it", "Business IT setup", "The whole office, set up together.")],
    },
    {
        "slug": "remote-support", "code": "S-05", "icon": "remote", "group": "Connectivity",
        "name": "Remote support", "row": "Software and account help anywhere in Namibia",
        "from": "From N$149", "price": "149",
        "title": "Remote IT Support Across Namibia from N$149 | ADA Tech",
        "desc": "Remote computer support anywhere in Namibia: Windows, drivers, updates, Microsoft 365, email "
                "and software problems fixed over the internet, with your permission. From N$149.",
        "h1": "Remote support",
        "lead": "Many software and account problems do not need a technician beside the computer. With your "
                "permission, we connect over the internet and fix it while you watch.",
        "answer": "ADA Tech provides remote support across Namibia for problems that can be handled safely over "
                  "an internet connection: Windows and software faults, drivers, updates, Microsoft 365, email "
                  "and account setup. Remote quick support starts from N$149, and the scope is confirmed before "
                  "work starts. Remote access always needs your permission before it begins.",
        "where": "Anywhere in Namibia with internet",
        "covers": ["Windows software faults", "Driver and update troubleshooting",
                   "Microsoft 365 and Office support", "Business email and account support",
                   "Software installation and configuration", "Guiding a user through a task",
                   "Browser and common program problems", "Basic security and two-step verification",
                   "Setting up a remote employee"],
        "signs": ["The computer starts and connects to the internet, but something on it does not work.",
                  "You are outside Rundu.",
                  "A staff member working from home needs help.",
                  "Email, Office or an account needs setting up."],
        "prices": [("Remote quick support", "From N$149", "Basic software, account or configuration support. Scope confirmed before work."),
                   ("Driver or software fault", "From N$179", "Install, repair or correct drivers and common software."),
                   ("Windows Update repair", "From N$249", "Find why updates fail and repair the update components."),
                   ("ADA First Aid subscribers", "Included", "Covered remote sessions under your plan. <a href=\"/first-aid\">See the plans</a>.")],
        "steps": [("Describe the problem", "By WhatsApp, phone or the support form."),
                  ("Scope and price", "We confirm it can be done remotely and what it costs."),
                  ("You allow the session", "You start the remote session and can watch everything on your own screen."),
                  ("Fix and confirm", "The session is ended and you confirm the problem is gone.")],
        "faq": [("Is remote access safe?",
                 "<p>A session starts only when you allow it, and you can watch what is being done on your own "
                 "screen and end it whenever you want. ADA Tech never phones people unasked to offer remote "
                 "help. Anyone who does is running a scam.</p>"),
                ("What can not be fixed remotely?",
                 "<p>Anything physical: a computer that will not start, a failed drive, a broken screen, "
                 "cabling or a router that needs moving. Those need the workshop or a visit.</p>"),
                ("What do I need?",
                 "<p>A computer that starts, a working internet connection and a phone, so we can talk while "
                 "the session runs.</p>")],
        "rel": [("/first-aid", "ADA First Aid", "Monthly care with remote sessions included."),
                ("/problems/windows-update-not-working", "Windows Update fails or gets stuck", "Often fixed remotely."),
                ("/support", "Get support", "Describe the problem.")],
    },
    {
        "slug": "security", "code": "S-06", "icon": "shield", "group": "Connectivity",
        "name": "Security and backups", "row": "Accounts, devices and data kept safe",
        "from": "Quoted", "price": None,
        "title": "Computer Security and Backups for Small Businesses | ADA Tech",
        "desc": "Practical security for small organisations in Namibia: two-step verification, password and "
                "access review, device protection, backups and staff guidance. Scoped and quoted.",
        "h1": "Security and backups",
        "lead": "Practical protection for the accounts, devices and information a small organisation depends "
                "on. Most break-ins use a stolen password, not clever hacking.",
        "answer": "ADA Tech sets up the basic protections that prevent most incidents in a small organisation: "
                  "two-step verification on email and accounts, a review of who has access to what, protection "
                  "on each device, and backups that are tested. The work is scoped to your size and quoted. "
                  "Advanced security work beyond our own capability is referred to an approved specialist, and "
                  "we say so.",
        "where": "On site in Rundu, or remote",
        "covers": ["Two-step verification (MFA) and account hardening", "Password and access guidance",
                   "Protection software on each device", "Windows security settings",
                   "Backup setup and guidance", "Review of who can access what",
                   "Basic device hardening", "Security health checks", "Plain guidance for staff"],
        "signs": ["One password is shared by several people.",
                  "A former employee may still have access.",
                  "The only copy of the business's files is on one computer.",
                  "An email account has already been broken into.",
                  "A funder, bank or client has asked how your data is protected."],
        "prices": [("Security health check and setup", "Quoted", "By number of users, devices and accounts."),
                   ("Remote quick support", "From N$149", "For a single account or device."),
                   ("Ongoing account and backup checks", "From N$2,449 a month", "Included in the Business Care <a href=\"/managed-it\">Managed IT plan</a>.")],
        "steps": [("Review", "Accounts, devices, who has access, and where the data lives."),
                  ("Prioritise", "The few changes that remove the most risk, in order."),
                  ("Set up", "Two-step verification, access changes, device protection and backups."),
                  ("Test and explain", "A backup is restored as a test, and staff are shown what changed.")],
        "faq": [("What is the single most useful thing to do?",
                 "<p>Turn on two-step verification for email. Email is the key to every other account, because "
                 "password resets go there.</p>"),
                ("Do we need paid antivirus?",
                 "<p>Windows Security, which is built into Windows 10 and 11, is adequate for most small "
                 "offices when it is switched on and the computers are kept up to date.</p>"),
                ("Do you do penetration testing or forensic investigations?",
                 "<p>No. That is specialist work. If you need it, we will say so and can point you to a "
                 "specialist.</p>")],
        "rel": [("/guides/back-up-your-files", "How to back up your files", "And how to check the backup works."),
                ("/problems/computer-virus-or-pop-ups", "Virus warnings and pop-ups", "Real infections and fake ones."),
                ("/managed-it", "Managed IT", "Ongoing care for an organisation.")],
    },
    {
        "slug": "cctv", "code": "S-07", "icon": "camera", "group": "Business",
        "name": "CCTV", "row": "Camera planning, recorders and remote viewing",
        "from": "Quoted by site", "price": None,
        "title": "CCTV Installation and Setup in Rundu | ADA Tech",
        "desc": "CCTV in Rundu, Namibia: camera placement, recorder (DVR and NVR) setup, storage planning, "
                "viewing on your phone and fault finding. Quoted after a site assessment.",
        "h1": "CCTV",
        "lead": "Cameras planned around the site: what has to be seen, from where, in what light, and for how "
                "many days the recording must be kept.",
        "answer": "ADA Tech plans and sets up CCTV systems in Rundu: where cameras should go, recorder setup, "
                  "storage sized for the number of days you need, viewing on a phone, and fault finding on "
                  "existing systems. CCTV is quoted after a site assessment, because the price depends on the "
                  "number of cameras, the recorder and storage, the cable runs and the power available.",
        "where": "On site in Rundu",
        "covers": ["Site and camera placement assessment", "Planning the installation",
                   "DVR and NVR configuration", "Viewing on a phone or computer",
                   "Storage planning", "Network connection for the cameras",
                   "Fault finding on cameras", "Fault finding on recorders", "Handover and guidance"],
        "signs": ["You want to see the premises when you are not there.",
                  "An existing system no longer records, or cannot be viewed on the phone.",
                  "A camera shows no picture, or a poor one at night.",
                  "Nobody knows the password to the recorder.",
                  "Recordings are overwritten before anyone needs them."],
        "prices": [("CCTV installation", "Quoted by site", "By camera count, recorder and storage, cabling, power and equipment."),
                   ("Fault finding on an existing system", "Quoted", "After a look at the cameras, recorder and network.")],
        "steps": [("Site assessment", "What must be seen, the distances, the light and the power."),
                  ("Written quote", "Cameras, recorder, storage, cabling and labour, listed separately."),
                  ("Install and configure", "Cameras, recorder, recording schedule and phone viewing."),
                  ("Handover", "You are shown how to view, search and export footage, and given the login details.")],
        "faq": [("How many days of recording can the system keep?",
                 "<p>It depends on the number of cameras, the picture quality and the size of the drive in the "
                 "recorder. Tell us how many days you need and the storage is sized to match.</p>"),
                ("Can I watch the cameras on my phone?",
                 "<p>Yes, if the recorder has an internet connection. Viewing uses mobile data on the phone "
                 "and upload capacity at the site.</p>"),
                ("Does CCTV work during a power cut?",
                 "<p>Only with backup power for the recorder, the cameras and the router. That can be included "
                 "in the quote.</p>"),
                ("Where am I allowed to point cameras?",
                 "<p>At your own premises. Avoid places where people expect privacy, such as toilets and "
                 "changing areas, and tell staff and visitors that cameras are in use. If recordings include "
                 "the public or employees, take advice on your legal duties.</p>")],
        "rel": [("/services/networking", "Wi-Fi and networking", "The network the cameras run on."),
                ("/services/business-it", "Business IT setup", "Cameras as part of an office setup."),
                ("/locations/rundu", "IT support in Rundu", "What we do on site.")],
    },
    {
        "slug": "server-infrastructure", "code": "S-08", "icon": "server", "group": "Business",
        "name": "Servers and infrastructure", "row": "File sharing, access, backup and planning",
        "from": "Quoted", "price": None,
        "title": "Small Business Server and IT Infrastructure Setup | ADA Tech",
        "desc": "Server and infrastructure work for small organisations in Namibia: shared files, user access, "
                "backup and recovery planning, capacity and documentation. Assessed first, then quoted.",
        "h1": "Servers and infrastructure",
        "lead": "For organisations that have outgrown one shared computer in the corner: shared files, "
                "controlled access and a backup that would actually work.",
        "answer": "ADA Tech assesses, sets up and documents small-business servers and shared infrastructure: "
                  "shared files and folders, user accounts and access, backup and recovery, and the network "
                  "underneath. This work is assessed first and then quoted, because a server for five people "
                  "and one for fifty are different jobs. There is no flat rate.",
        "where": "On site in Rundu",
        "covers": ["Assessment of the server's role and the environment", "Small-business server setup",
                   "Planning users and shared resources", "Shared files and access control",
                   "Backup and recovery planning", "Coordinating the server and the network",
                   "Basic monitoring", "Hardware and capacity planning", "Documentation of the setup"],
        "signs": ["Files are shared by USB stick or by email.",
                  "Everyone can open everything, including payroll.",
                  "The “server” is an old desktop nobody dares to restart.",
                  "There is no backup, or nobody has ever tested it.",
                  "The person who set it all up has left."],
        "prices": [("Assessment", "Quoted", "Users, data, existing equipment and what must keep working."),
                   ("Server and infrastructure setup", "Quoted", "By role, hardware, backup, users and support needs.")],
        "steps": [("Assess", "What the organisation needs the server to do, and what exists now."),
                  ("Design and quote", "Hardware or cloud, users, shares, backup, and the cost of each."),
                  ("Build and move", "Set up, move the data across, and switch over at a quiet time."),
                  ("Document and hand over", "Written record of the setup, the accounts and the recovery steps.")],
        "faq": [("Do we need a server, or is cloud storage enough?",
                 "<p>For many small offices, cloud storage such as OneDrive or Google Drive, set up properly "
                 "with accounts for each person, is enough and costs less to run. We assess that first and say "
                 "so if it is the better answer.</p>"),
                ("What happens if the server fails?",
                 "<p>That is the question the backup and recovery plan answers. It is designed and tested before "
                 "handover, not after the first failure.</p>")],
        "rel": [("/managed-it", "Managed IT", "Ongoing care once it is running."),
                ("/services/security", "Security and backups", "Access, protection and tested backups."),
                ("/services/networking", "Wi-Fi and networking", "The network underneath.")],
    },
    {
        "slug": "business-it", "code": "S-09", "icon": "office", "group": "Business",
        "name": "Business IT setup", "row": "Devices, accounts, printers and Wi-Fi for an office",
        "from": "Quoted", "price": None,
        "title": "Office IT Setup for Small Businesses in Rundu | ADA Tech",
        "desc": "Opening an office, branch or remote team in Namibia? Computers, Windows, business email, Wi-Fi, "
                "printers, user accounts and a basic security baseline, set up together and documented.",
        "h1": "Business IT setup",
        "lead": "Opening an office, adding a branch or putting a team to work from home. The technology is set "
                "up around how people will actually work, in one job.",
        "answer": "ADA Tech sets up the technology for a new or growing office in one job: computers and "
                  "Windows, business email or Microsoft 365, Wi-Fi and network, printers, user accounts and a "
                  "basic security baseline. It is quoted by the number of users and devices, the location and "
                  "the equipment needed. After setup, ongoing care is available as a monthly Managed IT plan.",
        "where": "On site in Rundu. Remote elsewhere",
        "covers": ["Computer and device setup", "Windows and software configuration",
                   "Business email or Microsoft 365 setup", "Network and Wi-Fi setup",
                   "Printers and shared devices", "CCTV coordination", "Setup for remote work",
                   "User accounts for new staff", "A basic security baseline", "Advice on what to buy"],
        "signs": ["You are opening an office or a branch.",
                  "New staff are starting and need computers and accounts.",
                  "The office grew one device at a time and nothing matches.",
                  "Staff use personal email addresses for business.",
                  "You need to know what to buy before you buy it."],
        "prices": [("Office setup", "Quoted", "By number of users, devices, location and required infrastructure."),
                   ("Router and Wi-Fi setup", "From N$349", "Where only the network is needed."),
                   ("Ongoing support", "From N$1,249 a month", "Monthly <a href=\"/managed-it\">Managed IT plans</a> for up to 5 devices and upwards.")],
        "steps": [("Understand the work", "Who does what, on which devices, from where."),
                  ("Plan and quote", "A list of what is needed, what you already have and what to buy."),
                  ("Set up", "Devices, accounts, email, network and printers, tested together."),
                  ("Document and hand over", "A record of devices, accounts and settings, and who to call.")],
        "faq": [("Can you advise on what computers to buy?",
                 "<p>Yes. Buying the right specification the first time costs less than upgrading later. Advice "
                 "on what to buy is part of the planning.</p>"),
                ("We already have equipment. Do we have to replace it?",
                 "<p>No. The plan starts from what you have. Only what is unsuitable or missing is listed to "
                 "buy.</p>"),
                ("What happens after setup?",
                 "<p>You can call us when something goes wrong, or take a monthly "
                 "<a href=\"/managed-it\">Managed IT plan</a> so that updates, checks and support happen on a "
                 "schedule.</p>")],
        "rel": [("/managed-it", "Managed IT", "Monthly plans from N$1,249."),
                ("/services/networking", "Wi-Fi and networking", "The office network."),
                ("/services/security", "Security and backups", "Accounts and data kept safe.")],
    },
]

KEYWORDS = {
    "computer-repair": "repair fix laptop desktop pc computer hardware diagnostic diagnosis technician workshop screen keyboard",
    "windows-setup": "windows install installation reinstall format windows 10 windows 11 office microsoft drivers activation licence",
    "bios-firmware": "bios uefi firmware boot secure boot tpm password recovery flash",
    "networking": "wifi wi-fi network router internet cabling ethernet access point coverage lan",
    "remote-support": "remote support online anydesk teamviewer help desk helpdesk anywhere namibia windhoek",
    "security": "security cyber mfa two-step password backup antivirus protection data hacked",
    "cctv": "cctv camera cameras surveillance dvr nvr security camera install",
    "server-infrastructure": "server servers infrastructure file sharing nas backup active directory",
    "business-it": "business office it setup company email microsoft 365 printers new office branch",
}


def by_slug(slug):
    return next(s for s in SERVICES if s["slug"] == slug)


def service_rows(group=None):
    items = [s for s in SERVICES if group is None or s["group"] == group]
    return code_rows([("/services/" + s["slug"], s["icon"], s["code"], s["name"], s["row"], s["from"])
                      for s in items])


def hub():
    body = hero(
        "What needs to work again?",
        "Nine services, each with its own page and a starting price where one can honestly be given. If you "
        "do not know which one you need, describe the symptom and we will work it out.",
        [SVC], [("/support", "Describe the problem"), ("/pricing", "See prices", "line")],
        code=("Service index", "S-01 to S-09"))
    body += sec(answer(
        "ADA Tech repairs laptops and desktops, installs Windows and Office, updates and recovers BIOS "
        "firmware, sets up Wi-Fi and office networks, gives remote support across Namibia, sets up security "
        "and backups, installs CCTV, builds small-business servers and sets up whole offices. Work on a single "
        f"device starts with a {DIAG} diagnostic that comes off the repair. Larger jobs are assessed and quoted.")
        + head_block("Devices", "For one laptop or desktop.", label="Group A", tag="h2") + service_rows("Devices"))
    body += sec(head_block("Connectivity and remote help", "Getting online, staying online and staying safe.",
                           label="Group B") + service_rows("Connectivity"), "sec--light")
    body += sec(head_block("Business and infrastructure", "When the whole organisation depends on it.",
                           label="Group C") + service_rows("Business"))
    body += sec(head_block("Ongoing care", "Monthly plans, for people and for organisations.", label="Plans")
                + cards([
                    ("/first-aid", "ADA First Aid", "Monthly care for one to three personal devices: remote "
                     "sessions, health checks and a discount on other labour.", "From N$249 a month", "Personal", "kit"),
                    ("/managed-it", "Managed IT", "Monthly support for an organisation's devices, users and "
                     "accounts, sized by the number of devices.", "From N$1,249 a month", "Business", "office"),
                    ("/support", "Not sure which fits?", "Describe what is going wrong and we will point you to "
                     "the right service.", "Describe the problem", "Help", "chat"),
                ], swipe=True), "sec--light")
    page("services", "IT Services in Rundu: Repair, Windows, Wi-Fi, CCTV | ADA Tech",
         "Computer repair, Windows setup, BIOS, Wi-Fi and networking, remote support, security, CCTV, servers "
         "and office IT in Rundu, Namibia. Starting prices published. Remote support across Namibia.",
         body, active="/services", crumbs=[SVC])


def build():
    hub()
    for s in SERVICES:
        path = "services/" + s["slug"]
        crumbs = [SVC, (path, s["name"])]
        ask = wa(f"Hello ADA Tech, I would like help with {s['name'].lower()}: ")
        body = hero(s["h1"], s["lead"], crumbs,
                    [("/support", "Get support"), (ask, "Ask on WhatsApp", "line")],
                    code=(f"Service {s['code']}", s["group"]), ico=s["icon"])
        sh = sheet("Service sheet", s["code"], [
            ("Service", e(s["name"])),
            ("Price", f"<strong>{e(s['from'])}</strong>"),
            ("Handled", e(s["where"])),
            ("Before work", "Scope and price agreed with you"),
            ("Not included", "Parts and paid licences, unless quoted"),
        ], ("/support", "Get support"))
        body += sec('<div class="intro">' + answer(s["answer"]) + sh + "</div>", "sec--tight")
        body += sec('<div class="split"><div><span class="label">Scope</span><h2 class="h2">What is covered</h2>'
                    + ticks(s["covers"]) + '</div><div><span class="label">Signs</span>'
                    '<h2 class="h2">When you need this</h2>' + signs(s["signs"]) + "</div></div>", "sec--light")
        body += sec(head_block("Prices", SEPARATE, label="Cost")
                    + table(["Work", "Price", "What it covers"], s["prices"])
                    + '<p class="mt2"><a class="more" href="/pricing">See all prices</a></p>')
        body += sec(head_block("How the job runs", label="Sequence") + steps(s["steps"], cls="steps--4")
                    + '<p class="mt2"><a class="more" href="/about">The full seven-step standard</a></p>', "sec--navy")
        body += sec(head_block("Common questions", label="Questions") + faq(s["faq"]))
        body += related(s["rel"], "Related")
        schema = [service_schema(s["name"], s["desc"], path, s["price"]), faq_schema(s["faq"])]
        page(path, s["title"], s["desc"], body, active="/services", crumbs=crumbs, schema=schema)
