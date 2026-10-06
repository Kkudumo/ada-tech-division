"""Guides: longer answers to questions people ask before they spend money
on a computer. Each one gives the answer first, links its sources and
carries a review date."""
from layout import (page, hero, sec, answer, table, related, cards, head_block, e, url, wa, SITE, REVIEWED,
                    REVIEWED_ISO, WA, PHONE, PHONE_TEL, DIAG)

G = ("guides", "Guides")

GUIDES = [
    ("guides/windows-10-end-of-support", "Windows 10 support has ended: what to do with your PC",
     "The dates, the security updates that now run to October 2027, and how to tell whether your PC can run "
     "Windows 11.", "Windows", "windows"),
    ("guides/repair-or-replace-laptop", "Repair or replace: is an old laptop worth fixing?",
     "Five questions that settle it, and a table of which repairs are usually worth doing.", "Buying", "laptop"),
    ("guides/back-up-your-files", "How to back up your files, and check the backup works",
     "A simple routine that survives a dead drive, a theft and a spilled drink.", "Data", "disk"),
    ("guides/genuine-windows-and-office-licences", "Genuine Windows and Office: how to check your licence",
     "How to see what you have, what survives a reinstall, and the free legal alternatives.", "Licences", "key"),
    ("guides/data-recovery-deleted-files-dead-drive", "Deleted files or a dead hard drive: can the data be recovered?",
     "What to do first, what can usually be recovered, what cannot, and what ADA Tech does.", "Data", "disk"),
    ("guides/cctv-installation-cost-namibia", "CCTV installation cost in Namibia: what you are paying for",
     "The parts of a system, what changes the price, wired against wireless and solar, and questions for an installer.",
     "CCTV", "camera"),
]

KEYWORDS = {
    "guides": "guides articles advice tips help how to learn",
    "guides/windows-10-end-of-support": "windows 10 end of life eol support ended esu extended security updates "
                                        "windows 11 upgrade requirements tpm secure boot 2025 2026 2027",
    "guides/repair-or-replace-laptop": "repair replace worth fixing old laptop buy new second hand cost",
    "guides/back-up-your-files": "backup back up files data external drive onedrive google drive cloud 3-2-1 "
                                 "file history restore lost files",
    "guides/genuine-windows-and-office-licences": "genuine licence license key activation activate windows office "
                                                  "microsoft 365 pirated crack kms free libreoffice product key",
    "guides/data-recovery-deleted-files-dead-drive": "data recovery namibia data recovery rundu recover deleted files dead hard drive "
                                                     "hard disk failing clicking formatted drive ssd dead usb flash drive lost files undelete",
    "guides/cctv-installation-cost-namibia": "cctv installation cost cctv installation cost for home cctv camera price in namibia "
                                             "security cameras namibia surveillance cameras namibia cctv camera namibia solar cctv camera price "
                                             "solar cctv camera with sim card solar cctv camera wifi dvr nvr storage",
}


def article(path, title, desc, h1, lead, capsule, body_html, sources, rel):
    crumbs = [G, (path, h1)]
    src = ""
    if sources:
        src = '<div class="sources"><strong>Sources</strong><ol>' + "".join(
            f'<li><a href="{e(u)}" rel="noopener">{e(t)}</a></li>' for u, t in sources) + "</ol></div>"
    body = hero(h1, lead, crumbs, None, code=("Guide", f"Reviewed {REVIEWED}"))
    body += sec(f"""<div class="with-aside"><article class="prose">
<p class="byline">By ADA Tech Division, Rundu, Namibia. Reviewed {REVIEWED}.</p>
{answer(capsule, "Short answer")}
{body_html}
{src}
</article>
<aside class="aside" aria-label="Contact ADA Tech">
<h2 class="h4">Want this checked on your own computer?</h2>
<p class="small muted">Tell us the make and model and what you want to do. A standard diagnostic costs {DIAG} and comes off the repair if you go ahead.</p>
<p><a class="btn" href="/support">Get support</a></p>
<p class="small"><a href="{WA}" target="_blank" rel="noopener">WhatsApp 081 803 2641</a><br><a href="tel:{PHONE_TEL}">Call {PHONE}</a></p>
</aside></div>""")
    body += related(rel, "Read next")
    schema = [{
        "@type": "Article", "headline": h1, "description": desc, "url": url(path),
        "datePublished": REVIEWED_ISO, "dateModified": REVIEWED_ISO, "inLanguage": "en",
        "author": {"@id": SITE + "/#organization"}, "publisher": {"@id": SITE + "/#organization"},
        "mainEntityOfPage": url(path), "image": SITE + "/assets/img/og-ada-tech.png",
    }]
    page(path, title, desc, body, active="/guides", crumbs=crumbs, schema=schema, og_type="article")


def guide_cards(n=None, swipe=False):
    items = GUIDES[:n] if n else GUIDES
    return cards([("/" + p, t, d, "Read the guide", tag, ic) for p, t, d, tag, ic in items],
                 cols=2 if not n else 3, swipe=swipe)


def hub():
    body = hero(
        "Guides",
        "Plain answers to questions people ask before they spend money on a computer. Each guide gives the "
        "answer first, links its sources and carries a review date.",
        [G], None, code=("Reference", f"{len(GUIDES)} guides"))
    body += sec('<h2 class="vh">All guides</h2>' + guide_cards())
    body += sec(head_block("Is something broken right now?",
                           'Guides are for decisions. For a fault, start from the '
                           '<a href="/problems">problem pages</a>, which list what to check, or '
                           '<a href="/support">describe it to us</a>.', label="Faults"), "sec--light sec--tight")
    page("guides", "Computer Guides: Windows 10, Backups, Licences | ADA Tech",
         "Plain guides from ADA Tech: what to do now Windows 10 support has ended, whether to repair or replace "
         "a laptop, how to back up your files, and how to check a Windows or Office licence.",
         body, active="/guides", crumbs=[G])


def build():
    hub()

    # ---------------------------------------------------------- Windows 10
    article(
        "guides/windows-10-end-of-support",
        "Windows 10 Support Has Ended: What to Do With Your PC (2026) | ADA Tech",
        "Windows 10 support ended on 14 October 2025. Home PCs can get Extended Security Updates until 12 October "
        "2027. How to check whether your PC can run Windows 11, and what to do if it cannot.",
        "Windows 10 support has ended: what to do with your PC",
        "Windows 10 still starts and still works, which is why this is easy to ignore. What stopped is the "
        "supply of security fixes. Here are the dates and your three options.",
        "Microsoft ended support for Windows 10 on 14 October 2025. A Windows 10 PC still works, but it no "
        "longer receives security fixes unless it is enrolled in Extended Security Updates, which for home PCs "
        "now runs until 12 October 2027. You have three options: upgrade to Windows 11 if the hardware "
        "qualifies, enrol in Extended Security Updates to buy time, or replace the PC. Check which applies "
        "before you spend anything.",
        "<h2>The dates</h2>"
        + table(["Date", "What happens"], [
            ["14 October 2025", "Microsoft's support for Windows 10 ended. No more free security fixes, bug fixes or technical support."],
            ["12 October 2027", "Extended Security Updates for home PCs end. Microsoft first set this for October 2026 and later moved it by a year."],
        ], caption="Dates as published by Microsoft, checked " + REVIEWED + ".")
        + "<h2>What “end of support” means in practice</h2>"
        "<p>Nothing switches off. The PC starts, your programs run and your files are where you left them. "
        "What changes is slower and less visible:</p>"
        "<ul><li>Newly discovered security holes in Windows 10 are no longer fixed, unless the PC is enrolled "
        "in Extended Security Updates.</li>"
        "<li>Over time, new versions of programs and some websites stop supporting it.</li>"
        "<li>Microsoft no longer gives technical support for it.</li></ul>"
        "<p>The risk matters most on a PC used for banking, business email or client records.</p>"
        "<h2>Option 1: upgrade to Windows 11</h2>"
        "<p>The upgrade is free for an eligible Windows 10 PC. Whether yours is eligible depends on its "
        "hardware. These are Microsoft's minimum requirements:</p>"
        + table(["Part", "Minimum for Windows 11"], [
            ["Processor", "1GHz or faster, 2 or more cores, on Microsoft's list of compatible 64-bit processors"],
            ["Memory (RAM)", "4GB"],
            ["Storage", "64GB or larger"],
            ["Firmware", "UEFI, capable of Secure Boot"],
            ["TPM", "Trusted Platform Module version 2.0"],
            ["Graphics", "Compatible with DirectX 12 or later, with a WDDM 2.0 driver"],
            ["Screen", "720p, larger than 9 inches"],
        ], caption="Source: Microsoft, Windows 11 specifications and system requirements.")
        + "<h3>How to check your own PC</h3>"
        "<ol><li>Open <em>Settings</em>, <em>Update &amp; Security</em>, <em>Windows Update</em>. An eligible PC "
        "shows a message that it can run Windows 11.</li>"
        "<li>For the detail, install Microsoft's free <em>PC Health Check</em> app and run its Windows 11 check. "
        "It names the requirement that fails.</li>"
        "<li>To see the TPM, press <kbd>Windows</kbd> + <kbd>R</kbd>, type <code>tpm.msc</code> and press Enter. "
        "Look for <em>Specification Version: 2.0</em>.</li></ol>"
        "<p>A common result is “TPM not found” on a PC that does have one. On many computers, TPM and Secure "
        "Boot are present but switched off in the BIOS. Turning them on is a settings change, not a new part. "
        "If the check fails on the processor, the PC cannot be made eligible.</p>"
        "<h2>Option 2: Extended Security Updates</h2>"
        "<p>Extended Security Updates (ESU) keep security fixes coming to a Windows 10 PC for a limited time. "
        "For home PCs, the programme runs until 12 October 2027. According to Microsoft:</p>"
        "<ul><li>The PC must run Windows 10 version 22H2 (Home, Pro, Pro Education or Workstations edition) "
        "with the latest updates installed.</li>"
        "<li>You sign in with a Microsoft account that is an administrator on the PC.</li>"
        "<li>You enrol in <em>Settings</em>, <em>Update &amp; Security</em>, <em>Windows Update</em>, where an "
        "enrolment link appears on eligible PCs.</li>"
        "<li>Microsoft lists three ways to enrol: at no cost if you sync your PC settings, with 1,000 Microsoft "
        "Rewards points, or with a one-time purchase of US$30 plus tax. One enrolment covers up to 10 devices.</li>"
        "<li>It provides security updates only. No new features and no technical support.</li></ul>"
        "<p>Microsoft notes that enrolment options and timing can vary by region. The reliable way to see what "
        "is offered in Namibia is to look at the Windows Update page on your own PC. PCs that are joined to a "
        "company domain or managed by an organisation are not covered by the home programme. Businesses have a "
        "separate, paid programme.</p>"
        "<p>ESU is a way to buy time, not a destination. It ends in October 2027.</p>"
        "<h2>Option 3: replace the PC</h2>"
        "<p>If the processor is not on Microsoft's compatible list, no upgrade or setting will make the PC "
        "eligible for Windows 11. Replacement makes most sense when the PC also has other age problems: a "
        "mechanical hard drive, 4GB of memory, a worn battery. Our guide on "
        "<a href=\"/guides/repair-or-replace-laptop\">repairing or replacing a laptop</a> covers how to decide.</p>"
        "<h2>What not to do</h2>"
        "<ul><li><strong>Do not ignore it on a PC used for money or client data.</strong> Enrol in ESU at least.</li>"
        "<li><strong>Do not force Windows 11 onto hardware that fails the check.</strong> Microsoft does not "
        "promise updates for PCs that do not meet the requirements, which defeats the purpose.</li>"
        "<li><strong>Do not install a pirated copy.</strong> It adds the risk you are trying to remove.</li></ul>"
        "<h2>What ADA Tech can do</h2>"
        "<p>We check whether your PC qualifies and name the requirement that fails if it does not. Where TPM "
        "or Secure Boot only needs switching on, that is <a href=\"/services/bios-firmware\">BIOS work</a>. The "
        "upgrade itself, or a clean installation of Windows 11, is part of our "
        "<a href=\"/services/windows-setup\">Windows packages from N$649</a>. Your existing Windows 10 licence "
        "normally activates Windows 11 of the same edition.</p>",
        [("https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro", "Microsoft: Windows 10 Home and Pro lifecycle (end of support 14 October 2025)"),
         ("https://www.microsoft.com/en-us/windows/extended-security-updates", "Microsoft: Windows 10 Extended Security Updates (programme ends 12 October 2027)"),
         ("https://www.microsoft.com/en-us/windows/windows-11-specifications", "Microsoft: Windows 11 specifications and system requirements"),
         ("https://www.helpnetsecurity.com/2026/06/26/microsoft-windows-10-free-security-updates-esu-program/", "Help Net Security, 26 June 2026: Microsoft extends Windows 10 consumer ESU by a year")],
        [("/services/windows-setup", "Windows and software setup", "Upgrade or clean installation, from N$649."),
         ("/problems/windows-update-not-working", "Windows Update fails or gets stuck", "If the upgrade will not install."),
         ("/guides/genuine-windows-and-office-licences", "Genuine Windows and Office", "Check your licence before upgrading.")])

    # ------------------------------------------------------ repair/replace
    article(
        "guides/repair-or-replace-laptop",
        "Repair or Replace a Laptop? How to Decide | ADA Tech",
        "Is an old laptop worth repairing? Five questions that settle it, a table of which repairs usually pay "
        "off, and what to do with your files before you replace it.",
        "Repair or replace: is an old laptop worth fixing?",
        "A repair is worth it when it is cheap next to a replacement and the laptop will still do the job "
        "afterwards. Five questions decide both halves of that.",
        "Repair a laptop when the repair costs well under half the price of an equivalent replacement and the "
        "laptop can still run a supported version of Windows. Batteries, chargers, memory and a change from a "
        "hard drive to an SSD are nearly always worth doing. A failed motherboard on an old laptop, or several "
        "parts failing together, usually is not. Get the repair price first: you cannot decide without it.",
        "<h2>Five questions</h2>"
        "<h3>1. What has actually failed?</h3>"
        "<p>You cannot decide until you know. “It will not turn on” could be a charger or it could be a "
        f"motherboard. A diagnostic costs {DIAG} with us and comes off the repair if you go ahead.</p>"
        "<h3>2. Can it run a supported version of Windows?</h3>"
        "<p>Windows 10 support ended in October 2025. A laptop that cannot run Windows 11 has a limited "
        "future, whatever is repaired. See <a href=\"/guides/windows-10-end-of-support\">how to check</a>.</p>"
        "<h3>3. What does the repair cost next to a replacement?</h3>"
        "<p>A common rule of thumb is to stop when the repair passes half the price of an equivalent "
        "replacement. Compare with a laptop that would do the same job, not with the cheapest one in the shop.</p>"
        "<h3>4. What else is worn?</h3>"
        "<p>One fault on an otherwise sound laptop is a repair. A dead battery, a cracked hinge, a failing "
        "drive and a broken key together are a replacement.</p>"
        "<h3>5. Is it fast enough for what you do?</h3>"
        "<p>If it was already too slow before the fault, repairing the fault does not change that, although an "
        "<a href=\"/problems/ssd-ram-upgrade\">SSD or memory upgrade</a> might.</p>"
        "<h2>Which repairs are usually worth it</h2>"
        + table(["Fault or upgrade", "Usually worth doing?", "Why"], [
            ["Battery", "Yes", "A standard part, and the laptop is otherwise unchanged."],
            ["Charger", "Yes", "The cheapest fix there is. Use the correct wattage."],
            ["Hard drive to SSD", "Yes", "The biggest speed improvement for the money on an older laptop."],
            ["More memory", "Yes, if the slots allow", "Cheap where the memory is not soldered."],
            ["Keyboard", "Usually", "Depends on the model. Some keyboards are part of the top case."],
            ["Screen", "Depends", "Compare the price of the panel with the value of the laptop."],
            ["Hinges or casing", "Depends", "Parts for older models can be hard to find."],
            ["Motherboard", "Often not on an older laptop", "Usually the most expensive part in the machine."],
            ["Liquid damage", "Uncertain", "It depends where the liquid went. See <a href=\"/problems/liquid-spilled-on-laptop\">liquid spills</a>."],
        ], caption="General guidance. The decision for your laptop depends on the model and the quoted price.")
        + "<h2>The cost that is easy to forget: your files</h2>"
        "<p>Whether you repair or replace, the files on the old drive usually matter more than the laptop. If "
        "the laptop is dead, the drive can often be removed and copied. Ask for that before the laptop is "
        "scrapped, sold or handed in.</p>"
        "<h2>Before you replace it</h2>"
        "<ol><li>Copy your files off. See <a href=\"/guides/back-up-your-files\">how to back up your files</a>.</li>"
        "<li>Sign out of your Microsoft, Google and other accounts on it.</li>"
        "<li>Wipe it: <em>Settings</em>, <em>System</em>, <em>Recovery</em>, <em>Reset this PC</em>, "
        "<em>Remove everything</em>. On Windows 10, Recovery is under <em>Update &amp; Security</em>.</li>"
        "<li>Keep the charger with it if you sell or pass it on.</li></ol>"
        "<h2>Buying second-hand instead</h2>"
        "<p>A used business laptop can be good value. Before paying, check four things: that it meets the "
        "Windows 11 requirements, the battery report (run <code>powercfg /batteryreport</code>), that Windows "
        "shows as activated, and that there is no BIOS password you have not been given.</p>",
        [("https://www.microsoft.com/en-us/windows/windows-11-specifications", "Microsoft: Windows 11 specifications and system requirements"),
         ("https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro", "Microsoft: Windows 10 Home and Pro lifecycle")],
        [("/problems/ssd-ram-upgrade", "RAM or SSD: which upgrade first?", "The upgrades that extend a laptop's life."),
         ("/services/computer-repair", "Computer and laptop repair", "Get the fault and the price first."),
         ("/guides/windows-10-end-of-support", "Windows 10 support has ended", "Check whether it can run Windows 11.")])

    # -------------------------------------------------------------- backup
    article(
        "guides/back-up-your-files",
        "How to Back Up Your Files on Windows (and Test It) | ADA Tech",
        "A backup routine for a Windows laptop or a small office: an external drive, a cloud copy and a monthly "
        "test. What to back up, how to set it up, and the mistakes that make a backup useless.",
        "How to back up your files, and check the backup works",
        "Drives fail without warning, laptops are stolen and drinks are spilled. A backup is the only repair "
        "that works for all three, and it takes about twenty minutes to set up.",
        "Keep three copies of anything you cannot replace: the one on your computer, one on an external drive "
        "and one somewhere else, such as cloud storage. Set the external drive up with File History so it runs "
        "by itself, let OneDrive or Google Drive keep the second copy, and once a month open a file from the "
        "backup to prove it works. A backup that has never been tested is a hope, not a backup.",
        "<h2>The rule: three copies, two kinds of storage, one somewhere else</h2>"
        "<p>This is usually called the 3-2-1 rule. One copy on the laptop, one on a different device, and one "
        "in a different place. Each part covers a different disaster: the second device covers a dead drive, "
        "and the copy elsewhere covers theft, fire or a power surge that takes out everything on the desk.</p>"
        "<h2>What to back up</h2>"
        "<ul><li>Documents, Desktop and Pictures folders</li>"
        "<li>Accounting, invoicing or stock files, wherever that program keeps them</li>"
        "<li>Email, if your mail program stores it on the computer</li>"
        "<li>Browser bookmarks and saved passwords, by signing in to the browser's sync</li>"
        "<li>Photos on the phone, which are a separate backup from the laptop</li></ul>"
        "<p>You do not need to back up Windows or your programs. Those can be installed again.</p>"
        "<h2>Copy 2: an external drive with File History</h2>"
        "<p>File History is built into Windows 10 and 11. It copies your personal folders to an external drive "
        "and keeps older versions of each file.</p>"
        "<ol><li>Plug in an external drive that is larger than the files you want to protect.</li>"
        "<li>Open <em>Control Panel</em>, <em>System and Security</em>, then <em>Save backup copies of your files "
        "with File History</em>.</li>"
        "<li>Select the drive and turn File History on.</li>"
        "<li>Plug the drive in regularly, for example every Friday. Unplug it and put it away afterwards.</li></ol>"
        "<p>Do not leave the drive plugged in all the time. A drive that is always connected is lost to the "
        "same theft, power surge or ransomware as the laptop.</p>"
        "<h2>Copy 3: cloud storage</h2>"
        "<p>OneDrive is built into Windows and can keep your Desktop, Documents and Pictures folders in the "
        "cloud. A free Microsoft account includes 5GB of storage, and paid plans give more. Google Drive is an "
        "alternative.</p>"
        "<p>The first upload can be large. Do it on Wi-Fi or an uncapped line, not on prepaid mobile data.</p>"
        "<h2>For an office</h2>"
        "<p>The same rule applies, with two additions. Decide who is responsible for checking the backup, and "
        "make sure the copy kept elsewhere really is elsewhere, not in the same room as the server. See "
        "<a href=\"/services/security\">security and backups</a>.</p>"
        "<h2>Test it</h2>"
        "<p>Once a month, open the backup and restore one file: a document from the external drive, and a "
        "photo from the cloud. If that works, the backup works. If it does not, you have found out on a quiet "
        "day and not on the day the laptop died.</p>"
        "<h2>Mistakes that make a backup useless</h2>"
        "<ul><li>The only “backup” is a flash drive that also holds the only copy.</li>"
        "<li>The external drive lives in the laptop bag, so both are stolen together.</li>"
        "<li>The backup was set up once and has not run for a year.</li>"
        "<li>Nobody has ever tried to restore a file.</li>"
        "<li>The drive is encrypted with BitLocker and nobody saved the recovery key. Check that your key is "
        "stored in your Microsoft account.</li></ul>"
        "<h2>If the drive has already failed</h2>"
        "<p>Stop using the computer. Every attempt to start it can make recovery harder. Recovery from a "
        "failed drive is uncertain and nobody can guarantee it, which is the whole case for backing up first. "
        "Read <a href=\"/guides/data-recovery-deleted-files-dead-drive\">deleted files or a dead hard drive: "
        "can the data be recovered?</a> for what to do next.</p>",
        [("https://support.microsoft.com/en-us/windows/back-up-and-restore-with-file-history-7bf065bf-f1ea-0a78-c1cf-7dcf51cc8bfc", "Microsoft Support: Back up and restore with File History"),
         ("https://www.microsoft.com/en-us/microsoft-365/free-office-online-for-the-web", "Microsoft: free Microsoft 365 on the web, including 5GB of cloud storage")],
        [("/services/security", "Security and backups", "Backups set up and tested for an office."),
         ("/problems/liquid-spilled-on-laptop", "Liquid spilled on a laptop", "One of the reasons to back up."),
         ("/guides/data-recovery-deleted-files-dead-drive", "Data recovery in Rundu and Namibia", "When the files are already gone.")])

    # ------------------------------------------------------------ licences
    article(
        "guides/genuine-windows-and-office-licences",
        "Is My Windows Genuine? How to Check Windows and Office Licences | ADA Tech",
        "How to check whether Windows and Office are properly licensed, what happens to the licence when Windows "
        "is reinstalled, the risks of cracked software, and the free legal alternatives.",
        "Genuine Windows and Office: how to check your licence",
        "Most laptops that were sold with Windows already carry a licence that survives a reinstall. Two "
        "minutes in Settings tells you what you have.",
        "To check Windows, open Settings, then System, then Activation. “Windows is activated with a digital "
        "license” means the licence is genuine and tied to the computer, so it activates again by itself after "
        "a reinstall of the same edition. To check Office, open any Office program and look under File, then "
        "Account. If either one is not properly licensed, there are free legal alternatives, including Office "
        "on the web.",
        "<h2>Check Windows</h2>"
        "<ol><li>Windows 11: <em>Settings</em>, <em>System</em>, <em>Activation</em>.</li>"
        "<li>Windows 10: <em>Settings</em>, <em>Update &amp; Security</em>, <em>Activation</em>.</li></ol>"
        + table(["What it says", "What it means"], [
            ["Windows is activated with a digital license", "Genuine. The licence is stored against this computer's hardware."],
            ["Windows is activated with a digital license linked to your Microsoft account", "Genuine, and easier to reactivate after a hardware change."],
            ["Windows is activated using your organization's activation service", "A company licence. Normal on a work PC. On a personal PC bought second-hand, ask where it came from."],
            ["Windows is not activated", "No valid licence is in use. A watermark appears and some settings are locked."],
        ])
        + "<h2>Will I lose the licence if Windows is reinstalled?</h2>"
        "<p>No, provided the same edition goes back on: Home for Home, Pro for Pro. A digital licence is held "
        "by Microsoft against the computer, so Windows activates again when it connects to the internet. "
        "Microsoft recommends linking the licence to your Microsoft account, which lets you reactivate after a "
        "significant hardware change such as a new motherboard.</p>"
        "<h2>Check Office</h2>"
        "<p>Open Word or Excel, then <em>File</em>, <em>Account</em>. It shows the product and whether it is "
        "activated. There are two legitimate kinds:</p>"
        "<ul><li><strong>Microsoft 365</strong>, a subscription paid monthly or yearly, signed in with your "
        "account.</li>"
        "<li><strong>A one-time purchase</strong> of Office for one computer.</li></ul>"
        "<h2>Signs that software is not genuine</h2>"
        "<ul><li>An “Activate Windows” watermark on the desktop.</li>"
        "<li>Office repeatedly asks for activation, or shows a red or yellow licence bar.</li>"
        "<li>The seller “activated” it with a small program rather than an account or a key.</li>"
        "<li>A key was bought for a small fraction of the normal price.</li></ul>"
        "<h2>Why it matters</h2>"
        "<ul><li><strong>Security.</strong> Activation tools are a common carrier for malware, and they usually "
        "have to be run with antivirus protection switched off.</li>"
        "<li><strong>Reliability.</strong> Keys resold against their terms can be blocked later, without warning.</li>"
        "<li><strong>For a business,</strong> unlicensed software is a legal exposure.</li></ul>"
        "<h2>Free and low-cost legal options</h2>"
        "<ul><li><strong>Office on the web.</strong> Word, Excel and PowerPoint run free in a browser with a "
        "Microsoft account.</li>"
        "<li><strong>LibreOffice.</strong> A free office suite that opens and saves Word, Excel and PowerPoint "
        "files.</li>"
        "<li><strong>Students and teachers.</strong> Many schools and universities provide Microsoft 365 "
        "through a school email address. Ask your institution.</li>"
        "<li><strong>Your existing licence.</strong> If the computer came with Windows, you very likely do not "
        "need to buy Windows again.</li></ul>"
        "<h2>What ADA Tech does</h2>"
        "<p>We activate Windows and Office only with a licence you already own or a legitimate one that is "
        "quoted separately, and we check what the computer already has before suggesting you buy anything. The "
        "cost of a licence is never hidden inside a labour price. See the "
        "<a href=\"/services/windows-setup\">Windows packages</a>.</p>",
        [("https://support.microsoft.com/en-us/windows/activate-windows-c39005d4-95ee-b91e-b399-2820fda32227", "Microsoft Support: Activate Windows"),
         ("https://www.microsoft.com/en-us/microsoft-365/free-office-online-for-the-web", "Microsoft: free Microsoft 365 on the web"),
         ("https://www.libreoffice.org/", "LibreOffice: free office suite")],
        [("/services/windows-setup", "Windows and software setup", "Installation with legitimate licences only."),
         ("/guides/windows-10-end-of-support", "Windows 10 support has ended", "What your licence means for Windows 11."),
         ("/problems/computer-virus-or-pop-ups", "Virus warnings and pop-ups", "What cracked software brings with it.")])

    # ------------------------------------------------------- data recovery
    article(
        "guides/data-recovery-deleted-files-dead-drive",
        "Data Recovery in Rundu and Namibia: Deleted Files | ADA Tech",
        "Deleted files or a dead hard drive? What to do first, what can usually be recovered, what cannot, and "
        "what ADA Tech does in Rundu.",
        "Deleted files or a dead hard drive: can the data be recovered?",
        "Sometimes. What decides it is what happened to the drive and what has been written to it since. The "
        "first hour matters more than the repair.",
        "Stop using the drive now. Files you deleted, or a drive you formatted, can often be recovered if "
        "nothing has been written over them. A hard drive that clicks or has failed is uncertain, and a dead "
        "SSD is the hardest case. Nobody can promise recovery, and ADA Tech does not. A standard diagnostic "
        f"costs {DIAG}, and complex data recovery is quoted separately.",
        "<h2>What to do in the first hour</h2>"
        "<ol><li><strong>Stop using the drive.</strong> Every file saved, program installed or update that "
        "runs can overwrite the space where your old files still sit.</li>"
        "<li><strong>Do not install recovery software on the same drive.</strong> It writes to the drive you "
        "are trying to save.</li>"
        "<li><strong>Do not keep restarting a drive that clicks or grinds.</strong> Each attempt can make "
        "damage worse.</li>"
        "<li><strong>Do not reinstall Windows or format the drive to see if it helps.</strong> That writes "
        "over what you want back.</li>"
        "<li><strong>Write down what happened.</strong> A drop, a power cut, a deleted folder, a Windows "
        "update. It tells us where to look.</li></ol>"
        "<h2>What can usually be recovered, and what cannot</h2>"
        + table(["What happened", "Usually recoverable?", "Why"], [
            ["Deleted files", "Often, if you stop at once", "Deleting removes the entry in the list, not always the data. The data stays until something is written over it. On an SSD it can be cleared sooner."],
            ["Formatted drive", "Often, after a quick format", "A quick format clears the list. A full format, or a Windows reinstall on top, writes over the data."],
            ["Failing hard disk (clicking, freezing, slow)", "Uncertain", "Parts are wearing out. Some files copy, some do not, and every start-up can make it worse."],
            ["Dead SSD", "Rarely, and not guaranteed", "There is no spinning part to repair. When the controller fails, the data can be out of reach."],
            ["Drive that was in a laptop with liquid or a drop", "Uncertain", "Depends on whether the drive itself was damaged. See <a href=\"/problems/liquid-spilled-on-laptop\">liquid spills</a>."],
            ["Phone", "Not something ADA Tech handles", "We do not repair or recover phones. Check whether the photos or contacts were synced to your account, and ask the phone maker or a phone repairer."],
        ], caption="General guidance. The real answer depends on the drive in front of us.")
        + "<h2>A dead laptop is not always a dead drive</h2>"
        "<p>When a laptop will not start, the drive that holds your files is often a separate part that is "
        "still healthy. It can be taken out and copied to another drive. That is a transfer, not a recovery, "
        "and it is much more likely to work. See <a href=\"/problems/laptop-not-turning-on\">laptop or computer "
        "will not turn on</a>. If the drive is encrypted with BitLocker, you need the recovery key from your "
        "Microsoft account before any files can be read.</p>"
        "<h2>What ADA Tech does</h2>"
        f"<p>We start with a standard diagnostic, {DIAG}, which comes off the repair if you go ahead. It "
        "tells us whether the drive is healthy, failing or dead, and whether the laptop is the problem and "
        "not the drive.</p>"
        "<ul><li><strong>The drive reads normally.</strong> We copy your files to another drive. Basic backup "
        "or transfer of up to 50GB starts from N$249.</li>"
        "<li><strong>The drive is failing or the files were deleted.</strong> We tell you what we find and "
        "what is realistic. Complex data recovery is quoted separately, and you decide before it starts.</li>"
        "<li><strong>The drive has failed physically.</strong> We say so, and say whether it is something we "
        "can attempt or whether it needs a specialist. We do not promise a result and we do not quote a "
        "success rate.</li></ul>"
        "<p>Tell us before any work starts which files matter. Message us from anywhere in Namibia for "
        "advice, but a drive that has to be examined has to come to the workshop in Rundu.</p>"
        "<h2>Common questions</h2>"
        "<h3>Can deleted files be recovered?</h3>"
        "<p>Often, if you stop using the drive straight away. The longer you keep working on it, the more "
        "likely the old data is overwritten.</p>"
        "<h3>Is the Recycle Bin the answer?</h3>"
        "<p>Check it first. Files deleted normally go there and can be restored in one click. If you emptied "
        "it, or held Shift while deleting, they are gone from it and the steps above apply.</p>"
        "<h3>Can you guarantee my files will come back?</h3>"
        "<p>No. No technician honestly can, from a drive that is failing or damaged. That is why the "
        "<a href=\"/guides/back-up-your-files\">backup guide</a> exists: a copy beats any recovery.</p>"
        "<h2>Once you have the files back</h2>"
        "<p>Set up a backup so you are never here again. Three copies, one of them somewhere else, and a "
        "monthly test. It takes about twenty minutes. See <a href=\"/guides/back-up-your-files\">how to back up "
        "your files</a>.</p>",
        [],
        [("/guides/back-up-your-files", "How to back up your files", "So the next failure costs a drive, not your work."),
         ("/services/computer-repair", "Laptop and computer repair in Rundu", "The diagnostic and what it covers."),
         ("/problems/laptop-not-turning-on", "Laptop or computer will not turn on", "When the drive may be fine.")])

    # ----------------------------------------------------------- CCTV cost
    article(
        "guides/cctv-installation-cost-namibia",
        "CCTV Installation Cost in Namibia: What You Pay For | ADA Tech",
        "What a CCTV system is made of, what changes the price, wired against wireless and solar cameras, and "
        "questions to ask before you accept a quote.",
        "CCTV installation cost in Namibia: what you are paying for",
        "Two quotes for four cameras can differ a great deal and both be honest. The difference is in what each "
        "one includes. Here is how to read them.",
        "A CCTV system costs what its parts and its installation cost: cameras, a recorder, a storage drive, "
        "cables or power, a router connection for viewing on your phone, and labour. The price moves with the "
        "number of cameras, the distance the cable has to run, how many days of recording you want, and "
        "whether mains power is available. ADA Tech does not publish a CCTV price. It quotes after a site "
        "visit, with every part listed separately, so you can compare like with like.",
        "<h2>The parts of a CCTV system</h2>"
        "<ul><li><strong>Cameras.</strong> The more of them, and the better their picture and night view, the "
        "higher the cost.</li>"
        "<li><strong>A recorder</strong> (DVR or NVR). It records what the cameras see. The number of camera "
        "channels it supports sets how many cameras you can add later.</li>"
        "<li><strong>Storage.</strong> A hard drive in the recorder holds the footage. A bigger drive keeps "
        "more days.</li>"
        "<li><strong>Cabling and power.</strong> Cable from each camera to the recorder, and power for both. "
        "Long runs, roofs and walls add labour and material.</li>"
        "<li><strong>Network and remote viewing.</strong> Watching from your phone needs the recorder on an "
        "internet connection, and mobile data on the phone.</li>"
        "<li><strong>Backup power.</strong> Without it, a power cut stops the recording.</li>"
        "<li><strong>Labour.</strong> Mounting, cabling, set-up, and showing you how to use it.</li></ul>"
        "<h2>What changes the price</h2>"
        "<ul><li><strong>Number of cameras.</strong> Each one adds a camera, a cable run and fitting time.</li>"
        "<li><strong>Distance and building.</strong> A short run inside one room is cheap. A long run across a "
        "yard or between buildings is not.</li>"
        "<li><strong>Days of recording.</strong> Recording around the clock for thirty days needs far more "
        "storage than recording on movement for a week.</li>"
        "<li><strong>Picture quality.</strong> A camera for reading number plates is a different camera from "
        "one that shows a person at a door.</li>"
        "<li><strong>Power.</strong> Whether there is a plug where each camera sits, and whether a power cut "
        "must not stop recording.</li></ul>"
        "<p>The same factors apply to the cost of CCTV installation for a home and for a business. A house "
        "with a few cameras and short runs is a smaller job. It is not a different kind of job.</p>"
        "<h2>Wired, wireless or solar with a SIM card</h2>"
        + table(["Type", "Suits", "Watch out for"], [
            ["Wired, with a recorder", "Houses, shops and offices with mains power. The most dependable.", "The cabling takes the most labour. Plan the cable runs first."],
            ["Wireless (Wi-Fi) cameras", "Places where running cable is hard.", "\"Wireless\" usually refers to the picture only. Each camera still needs power, and a weak Wi-Fi signal drops the picture."],
            ["Solar camera with a SIM card", "Places with no mains power and no cable: a farm gate, a shed, a building site.", "It needs sun on the panel and mobile signal with data on the SIM card, which you pay for. Shade or no signal and it will not work."],
        ])
        + "<h2>Questions to ask any installer</h2>"
        "<ol><li>How many cameras does this price cover, and what does each camera show?</li>"
        "<li>Which recorder is it, and how many more cameras can it take later?</li>"
        "<li>How many days of footage will the drive keep, with this many cameras?</li>"
        "<li>What is included in the cabling, and what happens if the run is longer than planned?</li>"
        "<li>Can I watch on my phone, and what does that need from my internet line?</li>"
        "<li>What happens during a power cut?</li>"
        "<li>Who is the equipment guaranteed by, and who do I call when a camera stops working?</li>"
        "<li>Is the quote written, with every part listed separately?</li></ol>"
        "<h2>What ADA Tech does</h2>"
        "<p>We assess the site, write a quote that lists cameras, recorder, storage, cabling and labour "
        "separately, install and configure the system, set up phone viewing, and show you how to search and "
        "export footage. There is no published CCTV price, because it depends on the site. "
        "See <a href=\"/services/cctv\">CCTV installation in Rundu</a>.</p>"
        "<p>Point cameras at your own premises. Avoid places where people expect privacy, and tell staff and "
        "visitors that cameras are in use. If recordings include the public or employees, take advice on your "
        "legal duties.</p>",
        [],
        [("/services/cctv", "CCTV installation in Rundu", "What ADA Tech covers, and how a quote works."),
         ("/services/networking", "Wi-Fi and networking", "The network the cameras run on."),
         ("/pricing", "Pricing", "Every published price in one place.")])
