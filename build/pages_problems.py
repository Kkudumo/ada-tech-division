"""Problem pages and the problems hub.

Each page answers one thing people type into a search engine when a device
goes wrong: what the symptom usually means, what they can safely check
themselves, when to stop, and what ADA Tech would do and charge.
"""
from layout import (page, hero, sec, head_block, answer, sheet, table, checks, stop, faq, faq_schema,
                    howto_schema, related, cards, icon, e, wa, DIAG)

PRB = ("problems", "Problems")

DIAG_LINE = (f"A standard diagnostic costs {DIAG}. If you go ahead with the repair, that amount comes off the "
             "repair cost. Parts are quoted separately, and nothing beyond the diagnostic is done until you "
             "have agreed to it.")

FILES_FAQ = ("Can my files be saved?",
             "<p>Often, yes. In most laptops the drive that holds your files is a separate part from the one "
             "that has failed, so it can be removed and the files copied to another drive. Basic backup or "
             "transfer of up to 50GB starts from N$249. Two limits apply: if the drive itself has failed, "
             "recovery is not guaranteed, and if the drive is encrypted with BitLocker you will need the "
             "recovery key from your Microsoft account. Tell us before any work starts which files matter. See "
             "<a href=\"/guides/data-recovery-deleted-files-dead-drive\">data recovery in Rundu and Namibia</a> "
             "for what can and cannot be recovered.</p>")

TIME_FAQ = ("How long will the repair take?",
            "<p>It depends on the fault and on whether a part has to be ordered. We do not promise a time before "
            "the diagnosis. After it, you are told what was found, what it costs and how long it should take, "
            "and you decide whether to go ahead.</p>")

PROBLEMS = [
    # ------------------------------------------------------------------ F-01
    {
        "slug": "laptop-not-turning-on", "code": "F-01", "icon": "power", "area": "Power and startup",
        "short": "My laptop will not turn on",
        "blurb": "No lights, lights but no picture, or it starts and then stops.",
        "title": "Laptop or Computer Won't Turn On? What to Check | ADA Tech",
        "desc": "Laptop not turning on, or a computer that won't start? Plugged in, power light on, after a power "
                "outage or Windows update: checks and diagnosis cost.",
        "h1": "Why will my laptop or computer not turn on?",
        "extra": [
            ("Laptop not turning on when plugged in",
             "<p>If the laptop is plugged in and still shows no sign of life, the fault is usually the charger, "
             "the charging port or a dead battery. Try another wall socket, look at the charger's own light, "
             "and do the power reset in the checks above. If the charger's light is on but the laptop shows nothing, "
             "or its charging light flickers, the charging port or the battery is the likely cause. A laptop "
             "that is plugged in and charging but still will not start has power and a different fault, such "
             "as the screen, the memory or the drive.</p>"),
            ("Laptop not turning on but the power light is on",
             "<p>A power light means power is reaching the laptop. If the fan spins and the screen stays black, "
             "go to <a href=\"/problems/windows-black-screen\">laptop screen black but the power is on</a>. "
             "Connect a TV or monitor first: a picture there means the laptop is working and the fault is in "
             "its own screen. If the light is on but nothing happens at all, repeat the power reset and "
             "disconnect everything plugged into the USB ports.</p>"),
            ("Computer won't start after a power outage",
             "<p>A power cut can end with a surge when the power comes back. On a desktop, check the switch "
             "on the back of the power supply and the power cable, try another socket, and take the computer "
             "off any surge protector that has tripped. On a laptop, test the charger on a different socket. "
             "If the charger or the power supply lights up and the computer still does nothing, stop trying: "
             "repeated attempts on a damaged power supply can do more harm. A surge can damage the charger, "
             "the power supply or the motherboard, and a diagnostic finds which. If the computer starts but "
             "complains about the drive or says there is nothing to boot from, the power cut may have "
             "interrupted Windows while it was writing, and the files on the drive matter more than the "
             "computer.</p>"),
            ("Computer won't start after a Windows update",
             "<p>If it was updating when it stopped, leave it alone for an hour before forcing it off: the "
             "screen can sit for a long time on \"Working on updates\" with the drive light busy. If it is "
             "stuck for much longer, or restarts in a loop, read "
             "<a href=\"/problems/windows-update-not-working\">Windows Update fails or gets stuck</a>. A "
             "computer that goes to a black screen after the update has its own checks on the "
             "<a href=\"/problems/windows-black-screen\">black screen</a> page.</p>"),
        ],
        "lead": "“Will not turn on” covers three different faults: no power at all, power but no picture, and "
                "power but no Windows. The lights and sounds tell you which one you have.",
        "answer": "A laptop that will not turn on usually has one of three faults. No power is reaching it "
                  "(charger, charging port or battery). It powers up but shows nothing (screen, memory or "
                  "firmware). Or it starts but cannot load Windows (the drive or the startup files). Check the "
                  "lights first, because each fault has a different fix and a different cost.",
        "causes": "Charger, charging port, battery, power cut or surge, memory, drive, motherboard",
        "where": "Workshop in Rundu",
        "clues": [
            ("No lights, no fan, no sound at all", "No power is reaching the laptop: the charger, the charging port, a flat or failed battery, or the power circuit on the motherboard."),
            ("The charging light is on, but nothing happens when you press the power button", "The battery, the power button or the motherboard."),
            ("Lights and fan come on, the screen stays dark", "The screen, the memory (RAM) or the firmware. See <a href=\"/problems/windows-black-screen\">black screen</a>."),
            ("The maker's logo appears, then it restarts, freezes or says “no bootable device”", "The drive is failing or the Windows startup files are damaged."),
            ("It beeps, or a light blinks in a repeating pattern", "A diagnostic code. HP, Dell, Lenovo and others publish what each pattern means for each model."),
        ],
        "checks": [
            ("Check the charger and the wall socket",
             "Try a different wall socket. Look for a light on the charger or beside the charging port, and check "
             "the cable for cuts or bent pins. Use the original charger, or one with the same voltage and connector."),
            ("Do a power reset",
             "Unplug the charger and everything connected by USB. If the battery comes out, take it out. Hold the "
             "power button down for 30 seconds. Then connect only the charger and try again."),
            ("Leave it charging for 30 minutes",
             "A battery that is completely flat can need time on charge before the laptop will start."),
            ("Look and listen",
             "In a dark room, shine a torch at the screen at an angle. A faint picture means the screen backlight "
             "has failed, not the laptop. Listen for the fan, and count any beeps or blinks."),
            ("Try another screen",
             "If lights come on, connect a TV or monitor with an HDMI cable. A picture there means the laptop "
             "works and the fault is in its own screen or screen cable."),
        ],
        "stop": [
            "You smell burning, or the charger or the laptop gets very hot.",
            "The battery looks swollen: the case bulges, or the touchpad or keyboard is lifting. Do not charge it.",
            "Liquid went into it. Follow the <a href=\"/problems/liquid-spilled-on-laptop\">liquid spill steps</a> instead.",
            "It stopped during a BIOS or firmware update. Do not keep interrupting it.",
            "The drive clicks or grinds and the files matter. Every start-up attempt can make recovery harder.",
        ],
        "ada": "<p>We test the charger and the charging port, then the battery, the power path, the memory and "
               "the health of the drive. That tells us which part has failed, and you get the finding and the "
               "repair price before anything is replaced.</p><p>" + DIAG_LINE + " BIOS or firmware recovery "
               "starts from N$449.</p>",
        "faq": [FILES_FAQ,
                ("Is an old laptop worth repairing?",
                 "<p>It depends on the fault and the age of the machine. A charger or a battery is usually worth "
                 "replacing. A failed motherboard on an old laptop often is not. You get the repair price before "
                 "you commit, and our guide on <a href=\"/guides/repair-or-replace-laptop\">repairing or "
                 "replacing a laptop</a> sets out how to decide.</p>"),
                TIME_FAQ],
        "rel": [("/problems/windows-black-screen", "Black screen but the power is on", "When it runs but shows nothing."),
                ("/problems/laptop-battery-draining-fast", "Battery drains fast or will not charge", "How to read the battery's real condition."),
                ("/services/computer-repair", "Computer and laptop repair", "What the diagnostic covers.")],
    },
    # ------------------------------------------------------------------ F-02
    {
        "slug": "windows-black-screen", "code": "F-02", "icon": "screen", "area": "Display and startup",
        "short": "The screen is black but the power is on",
        "blurb": "Power light on, fan running, nothing on the screen.",
        "title": "Laptop Screen Black but Power Is On? Fixes to Try | ADA Tech",
        "desc": "Laptop or PC on but the screen is black? Keyboard shortcuts that often bring it back, how to tell "
                "a screen fault from a Windows fault, and when to get it diagnosed.",
        "h1": "Why is my laptop screen black when the power is on?",
        "lead": "If the power light is on, the computer is often running normally and only the picture is "
                "missing. Three keyboard shortcuts fix a large share of these.",
        "answer": "A black screen with the power on usually means one of four things: the graphics driver has "
                  "crashed, Windows is stuck while signing in or updating, the picture is being sent to a "
                  "different display, or the screen or its cable has failed. Try the keyboard shortcuts below "
                  "first. If an external screen shows a picture, the laptop itself is fine and the fault is in "
                  "its screen.",
        "causes": "Graphics driver, Windows sign-in, display output, screen or cable",
        "where": "Remote or workshop",
        "clues": [
            ("Black screen with a mouse pointer you can move", "Windows has started but the desktop has not loaded. Common after an update."),
            ("The logo shows, then black, every time", "A graphics driver or a startup fault."),
            ("You hear Windows sounds, and a torch shows a faint picture", "The screen backlight has failed."),
            ("An external monitor or TV shows the picture", "The laptop's own screen or screen cable."),
            ("Nothing on either screen, but the fan spins", "Memory, graphics hardware or firmware. See <a href=\"/problems/laptop-not-turning-on\">laptop will not turn on</a>."),
        ],
        "checks": [
            ("Restart the graphics driver",
             "<p>Press <kbd>Windows</kbd> + <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd>. The screen blinks "
             "and you may hear a beep. This restarts the graphics driver without closing anything.</p>"),
            ("Switch the display output",
             "<p>Press <kbd>Windows</kbd> + <kbd>P</kbd>, then <kbd>P</kbd> again, then <kbd>Enter</kbd>. Repeat "
             "up to four times. This cycles through the display modes, in case Windows is sending the picture to "
             "a second screen that is not there.</p>"),
            ("Restart the desktop",
             "<p>Press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Delete</kbd>. If a menu appears, open Task Manager, "
             "choose <em>Run new task</em>, type <code>explorer.exe</code> and press Enter.</p>"),
            ("Connect another screen",
             "Plug in a TV or monitor with an HDMI cable. If the picture appears there, the laptop is working and "
             "the fault is in its screen."),
            ("Turn it fully off and start clean",
             "Hold the power button for 10 seconds until it is off. Unplug every USB device, then start it again."),
            ("Start in Safe Mode",
             "<p>Turn the computer off as Windows begins to load, three times in a row. Windows then opens its "
             "recovery screen. Choose <em>Troubleshoot</em>, <em>Advanced options</em>, <em>Startup Settings</em>, "
             "<em>Restart</em>, then press <kbd>4</kbd>. If the screen works in Safe Mode, a driver or a startup "
             "program is the cause.</p>"),
        ],
        "stop": [
            "It began after a drop or after liquid got in.",
            "It went black in the middle of an update and the drive light is still busy. Give it an hour before forcing it off.",
            "You have had to force it off several times. Each forced shutdown risks damaging files.",
            "Neither the laptop screen nor an external screen shows anything.",
        ],
        "ada": "<p>We work out which of the four it is: the display, Windows, the drive or the hardware. A driver "
               "or software fault can often be fixed the same day, and sometimes remotely. A failed screen or "
               "cable is quoted with the part.</p><p>" + DIAG_LINE + " Driver and software faults start from "
               "N$179.</p>",
        "faq": [("Is a black screen the same as a blue screen?",
                 "<p>No. A <a href=\"/problems/windows-blue-screen\">blue screen</a> shows an error message and a "
                 "stop code. A black screen shows nothing, and the computer may still be running behind it.</p>"),
                FILES_FAQ, TIME_FAQ],
        "rel": [("/problems/windows-blue-screen", "Blue screen errors", "When Windows shows a stop code instead."),
                ("/problems/windows-update-not-working", "Windows Update fails or gets stuck", "A common trigger for black screens."),
                ("/services/remote-support", "Remote support", "When it can be fixed without bringing it in.")],
    },
    # ------------------------------------------------------------------ F-03
    {
        "slug": "windows-blue-screen", "code": "F-03", "icon": "alert", "area": "Windows",
        "short": "It keeps showing a blue screen",
        "blurb": "Windows stops with an error and a stop code, then restarts.",
        "title": "Blue Screen on Windows 10 or 11: What the Stop Code Means | ADA Tech",
        "desc": "Laptop or PC keeps showing a blue screen? What common stop codes point to, eight checks you can "
                "run yourself, and when the cause is failing hardware.",
        "h1": "Why does my laptop keep showing a blue screen?",
        "lead": "A blue screen means Windows stopped itself because carrying on could have damaged something. "
                "One crash can be ignored. Repeated crashes have a cause, and the stop code points to it.",
        "answer": "Repeated blue screens are most often caused by a faulty driver, failing memory (RAM), a "
                  "failing drive, overheating or damaged Windows files. Write down the stop code on the screen, "
                  "because it narrows the cause. Back up your files while the computer still starts, then work "
                  "through the checks below. Reinstalling Windows only helps when the cause is software.",
        "causes": "Drivers, memory, drive, heat, damaged Windows files",
        "where": "Remote or workshop",
        "clues_head": ("Stop code on the screen", "Where to look first"),
        "clues": [
            ("<code>MEMORY_MANAGEMENT</code><br><code>PAGE_FAULT_IN_NONPAGED_AREA</code>", "Memory (RAM), or a driver misusing memory."),
            ("<code>CRITICAL_PROCESS_DIED</code><br><code>UNEXPECTED_STORE_EXCEPTION</code>", "The drive, or damaged Windows system files."),
            ("<code>DRIVER_IRQL_NOT_LESS_OR_EQUAL</code><br><code>SYSTEM_THREAD_EXCEPTION_NOT_HANDLED</code>", "A driver. If the screen names a file ending in <code>.sys</code>, that file belongs to the driver at fault."),
            ("<code>INACCESSIBLE_BOOT_DEVICE</code>", "The drive, a storage setting in the BIOS, or an update that failed part-way."),
            ("<code>WHEA_UNCORRECTABLE_ERROR</code>", "Hardware: heat, the processor, memory or power."),
            ("<code>VIDEO_TDR_FAILURE</code>", "The graphics driver or the graphics hardware."),
        ],
        "clues_note": "These are the usual first suspects for each code, not a diagnosis. The same code can have more than one cause.",
        "checks": [
            ("Record the stop code", "Photograph the blue screen. Note the stop code and any line that says “What failed”."),
            ("Think about what changed", "A new device, driver, program or Windows update just before the crashes started is the first suspect. Unplug new USB devices and uninstall what was added."),
            ("Back up your files now", "If Windows still starts, copy your important files to an external drive or cloud storage before doing anything else."),
            ("Check for heat", "If the laptop is very hot or the fan is loud before each crash, read <a href=\"/problems/laptop-overheating\">laptop overheating</a>."),
            ("Test the memory",
             "<p>Press the <kbd>Windows</kbd> key, type <em>Windows Memory Diagnostic</em> and choose "
             "<em>Restart now and check for problems</em>. Any error it reports means the memory needs attention.</p>"),
            ("Repair Windows system files",
             "<p>Right-click the Start button and open <em>Terminal (Admin)</em> or <em>Command Prompt (Admin)</em>. "
             "Run this, and wait for it to finish:</p><code class=\"cmd\">sfc /scannow</code>"
             "<p>If it reports problems it could not fix, run this and then run the first command again:</p>"
             "<code class=\"cmd\">DISM /Online /Cleanup-Image /RestoreHealth</code>"),
            ("Look at the crash history", "Press the <kbd>Windows</kbd> key, type <em>reliability</em> and open <em>View reliability history</em>. It shows each crash by date and what failed."),
            ("Update properly", "Install pending Windows updates, and get drivers from your laptop maker's support page for your exact model. Avoid “driver updater” programs."),
        ],
        "stop": [
            "The same stop code keeps coming back after the checks.",
            "Windows will not stay running long enough to back up your files.",
            "The memory test reports errors.",
            "The drive clicks, or files have started to go missing or will not open.",
        ],
        "ada": "<p>We read the crash records Windows keeps, test the memory and the drive, measure temperatures "
               "under load and repair Windows if the files are damaged. You are told whether the cause is "
               "software or a part, and what each option costs.</p><p>" + DIAG_LINE + "</p>",
        "faq": [("Will reinstalling Windows fix a blue screen?",
                 "<p>Only if the cause is software. If the memory or the drive is failing, the blue screens "
                 "return on the fresh installation. That is why the hardware is tested first.</p>"),
                ("Can a blue screen damage my files?",
                 "<p>The crash itself rarely does. But a failing drive is one of the causes of blue screens, and "
                 "a failing drive does lose files. Back up as soon as the crashes start.</p>"),
                ("Is a blue screen a virus?",
                 "<p>Rarely. Drivers, memory, the drive and heat are far more common causes. If you also see "
                 "pop-ups or programs you did not install, read "
                 "<a href=\"/problems/computer-virus-or-pop-ups\">virus and pop-up warnings</a>.</p>")],
        "rel": [("/problems/windows-black-screen", "Black screen but the power is on", "No error message, just nothing."),
                ("/problems/laptop-overheating", "Laptop overheating", "Heat is a common cause of crashes."),
                ("/guides/back-up-your-files", "How to back up your files", "Do this before any repair.")],
    },
    # ------------------------------------------------------------------ F-04
    {
        "slug": "slow-laptop", "code": "F-04", "icon": "gauge", "area": "Performance",
        "short": "My laptop is very slow",
        "blurb": "Slow to start, slow to open programs, freezes when busy.",
        "title": "Laptop Is Slow or Slow to Start Up? Find the Cause | ADA Tech",
        "desc": "Laptop is slow, slow to start up or hanging on Windows 10 or 11? Use Task Manager to find the real "
                "cause and what to do. Tune-up from N$249 in Rundu.",
        "h1": "Why is my laptop slow?",
        "lead": "A laptop that is slow, slow to start up or hanging has four common causes. Task Manager shows "
                "which one you have in about two minutes, and that decides whether the fix is free, cheap or a part.",
        "extra": [
            ("Laptop is slow to start up",
             "<p>If the laptop is slow to start up but fine once it is running, the usual causes are a "
             "mechanical hard drive and too many programs starting with Windows. Restart rather than shut "
             "down, switch off startup programs in Task Manager, and check whether the drive is an HDD or an "
             "SSD. A change from an HDD to an SSD is the biggest single improvement on an older laptop.</p>"),
            ("Laptop is slow and hanging: what to do",
             "<p>If the laptop is slow and hanging, with the cursor frozen or windows stuck, see whether the "
             "disk sits at 100% in Task Manager and whether the fan is loud. A drive that is failing also "
             "freezes the laptop, usually with clicking or files that will not open. If that is the case, "
             "copy your files off before trying anything else, and read "
             "<a href=\"/guides/data-recovery-deleted-files-dead-drive\">what can be recovered from a failing "
             "drive</a>.</p>"),
        ],
        "answer": "Most slow laptops have one of four causes: a mechanical hard drive instead of an SSD, too "
                  "little memory (RAM) for what is open, too many programs starting with Windows, or a drive "
                  "that is nearly full. Open Task Manager with Ctrl + Shift + Esc and look at the Performance "
                  "tab. A disk at 100% points to the drive, and memory above about 85% points to RAM.",
        "causes": "Hard drive, memory, startup programs, full drive, heat, malware",
        "where": "Remote or workshop",
        "clues": [
            ("Laptop is slow to start up: disk shows 100% in Task Manager, mostly after starting up", "A mechanical hard drive (HDD), or a drive that is failing."),
            ("Memory is above about 85% with only a few programs open", "Not enough RAM for how you use it."),
            ("Slow for the first few minutes, then fine", "Too many programs starting with Windows."),
            ("It slows down when it gets hot and the fan is loud", "Heat. The processor slows itself to cool down. See <a href=\"/problems/laptop-overheating\">overheating</a>."),
            ("Less than about 15% of drive C: is free", "The drive is too full for Windows to work properly."),
            ("It became slow suddenly, with pop-ups or unknown programs", "Unwanted software. See <a href=\"/problems/computer-virus-or-pop-ups\">virus and pop-ups</a>."),
        ],
        "checks": [
            ("Restart, do not just shut down", "Choose <em>Restart</em> from the power menu. On Windows 10 and 11, <em>Shut down</em> saves part of the system to start faster next time, so only Restart gives a clean start."),
            ("Read Task Manager",
             "<p>Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Esc</kbd> and open the <em>Performance</em> tab. "
             "Look at <em>Memory</em> and <em>Disk</em>. Under Disk, Windows shows whether the drive is an "
             "<em>SSD</em> or an <em>HDD</em>.</p>"),
            ("Turn off startup programs", "In Task Manager, open <em>Startup apps</em>. Disable anything you do not need the moment the laptop starts. Nothing is uninstalled by doing this."),
            ("Free up space", "Open <em>Settings</em>, <em>System</em>, <em>Storage</em> and follow the clean-up recommendations. Aim to keep at least 15% of the drive free."),
            ("Remove what you do not use", "Uninstall programs you no longer use, and keep only one antivirus. Windows Security is already built in."),
            ("Scan for unwanted software", "Open <em>Windows Security</em>, <em>Virus &amp; threat protection</em>, <em>Scan options</em> and run a <em>Full scan</em>."),
            ("Install pending updates", "A laptop that is part-way through updates can be slow until they finish."),
        ],
        "stop": [
            "The drive clicks or grinds.",
            "Files will not open, or go missing.",
            "It freezes completely for a minute or more at a time.",
        ],
        "stop_after": "<p>These point to a failing drive. Copy your important files off it before trying anything else.</p>",
        "ada": "<p>We find the bottleneck before recommending anything. If it is software, a tune-up clears "
               "startup programs, checks updates and reviews the health of the system. If it is the drive or the "
               "memory, we check what your model supports and quote the part.</p>"
               "<p>PC tune-up and optimisation costs N$249. Fitting RAM or an SSD starts from N$179 for labour, "
               "with the part quoted separately. Moving your files to a new drive starts from N$249 for up to "
               "50GB.</p>",
        "faq": [("Will an SSD or more RAM make it faster?",
                 "<p>Usually one of them will, but which one depends on the bottleneck. See "
                 "<a href=\"/problems/ssd-ram-upgrade\">RAM or SSD: which upgrade first?</a></p>"),
                ("Will reinstalling Windows make it faster?",
                 "<p>It helps when the cause is years of software clutter. It does not change a mechanical hard "
                 "drive or too little memory, so check those first.</p>"),
                ("Do I need a new laptop?",
                 "<p>Often not. A laptop that has a mechanical hard drive and 4GB of memory usually improves a "
                 "great deal with an SSD and more RAM, if the processor is reasonably recent. See "
                 "<a href=\"/guides/repair-or-replace-laptop\">repair or replace</a>.</p>")],
        "rel": [("/problems/ssd-ram-upgrade", "RAM or SSD: which upgrade first?", "How to choose the right part."),
                ("/problems/laptop-overheating", "Laptop overheating", "Heat makes a laptop slow itself down."),
                ("/pricing", "Pricing", "Tune-up, upgrade and Windows package prices.")],
    },
    # ------------------------------------------------------------------ F-05
    {
        "slug": "laptop-overheating", "code": "F-05", "icon": "heat", "area": "Cooling",
        "short": "It overheats or the fan is always loud",
        "blurb": "Hot to touch, loud fan, slows down or switches itself off.",
        "title": "Laptop Overheating or Fan Always Loud? Causes and Checks | ADA Tech",
        "desc": "Laptop overheating, fan always loud or shutting down by itself? The common causes, safe checks "
                "you can do, and the signs that mean you should stop using it.",
        "h1": "Why is my laptop overheating?",
        "lead": "A warm laptop under heavy work is normal. Constant heat, a fan that never slows, or sudden "
                "shutdowns are not, and they shorten the life of the machine.",
        "answer": "Laptops overheat for three main reasons: dust blocking the vents and the cooling fins, a "
                  "program keeping the processor busy in the background, or a cooling fan that has failed. Use "
                  "it on a hard flat surface, check Task Manager for a program using the processor, and clear "
                  "the vents. If it shuts down by itself from heat, stop using it until the cooling has been "
                  "cleaned and tested.",
        "causes": "Dust, blocked vents, background programs, failed fan, old thermal compound",
        "where": "Workshop in Rundu",
        "clues": [
            ("The fan is loud all the time, even when you are doing nothing", "Dust in the vents and cooling fins, or a program using the processor in the background."),
            ("It gets hot and switches itself off", "The processor's heat protection. The cooling is not coping."),
            ("Hot only during games, video editing or many browser tabs", "Normal under load, though the cooling may be partly blocked."),
            ("It gets hot and the fan makes no sound at all", "The fan has failed or is jammed."),
            ("Hot while charging, and the base or touchpad is bulging", "A swollen battery. Stop using it."),
        ],
        "checks": [
            ("Give it air", "Use it on a table, not on a bed, a cushion or your lap. Soft surfaces block the vents underneath."),
            ("Find what is using the processor", "<p>Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Esc</kbd>, open <em>Processes</em> and click the <em>CPU</em> column to sort. A program sitting high on the list while you are doing nothing is the cause.</p>"),
            ("Clear the vents", "With the laptop switched off, look at the vents for dust. Short bursts of compressed air through the vents can clear loose dust."),
            ("Lower the power mode", "Open <em>Settings</em>, <em>System</em>, <em>Power &amp; battery</em> and choose <em>Balanced</em> or <em>Best power efficiency</em>."),
            ("Compare before and after", "Note whether the heat started suddenly or built up over months. Sudden heat points to a fan or a program. Slow build-up points to dust."),
        ],
        "stop": [
            "You smell burning.",
            "The battery looks swollen, or the case is bending out of shape.",
            "It shuts down within minutes of starting.",
            "The case is too hot to keep a hand on.",
        ],
        "ada": "<p>We open the laptop, clean the fan and the cooling fins, test the fan, and replace the thermal "
               "compound between the processor and the cooler where it has dried out. Temperatures are measured "
               "under load before and after, so the result is a number and not an opinion.</p><p>" + DIAG_LINE +
               " The cleaning work is quoted after the diagnostic, because it depends on the model.</p>",
        "faq": [("Is it safe to keep using a laptop that overheats?",
                 "<p>Not for long. Heat ages the battery and the motherboard, and sudden shutdowns can damage "
                 "files. If it shuts itself down, stop using it until it has been checked.</p>"),
                ("Does a cooling pad fix overheating?",
                 "<p>It can lower the temperature a little. It does not remove dust from inside or fix a failed "
                 "fan, so it treats the symptom.</p>"),
                TIME_FAQ],
        "rel": [("/problems/slow-laptop", "Laptop is very slow", "Heat is one of the causes."),
                ("/problems/windows-blue-screen", "Blue screen errors", "Overheating can crash Windows."),
                ("/services/computer-repair", "Computer and laptop repair", "What the diagnostic covers.")],
    },
    # ------------------------------------------------------------------ F-06
    {
        "slug": "windows-update-not-working", "code": "F-06", "icon": "update", "area": "Windows",
        "short": "Windows Update fails or gets stuck",
        "blurb": "Stuck on a percentage, fails with a code, or keeps undoing changes.",
        "title": "Windows Update Stuck or Failing? How to Fix It | ADA Tech",
        "desc": "Windows Update stuck, failing with an error code or undoing changes? The usual causes, eight "
                "checks including the built-in repair commands, and repair from N$249.",
        "h1": "Why is Windows Update failing or stuck?",
        "lead": "An update that fails again and again is usually telling you about something else: not enough "
                "free space, damaged update files or an unstable connection.",
        "answer": "Windows Update usually fails for one of four reasons: too little free space on the drive, "
                  "damaged update files, an unstable or metered internet connection, or a driver the update "
                  "cannot work with. Free at least 20GB, run the Windows Update troubleshooter, then run the two "
                  "repair commands below. Never switch the computer off while it says it is working on updates.",
        "causes": "Low disk space, damaged update files, connection, drivers",
        "where": "Remote or workshop",
        "clues": [
            ("Stuck on the same percentage for hours", "A slow or interrupted download, or damaged update files."),
            ("Error <code>0x80070070</code>", "Not enough free space on the drive."),
            ("Error <code>0x80073712</code>", "Windows update files are damaged and need repair."),
            ("“Undoing changes made to your computer”, every time", "The update installs, fails and rolls back. Usually a driver or damaged system files."),
            ("“This PC can't run Windows 11”", "Not a fault. The hardware does not meet Windows 11's requirements. See our <a href=\"/guides/windows-10-end-of-support\">Windows 10 guide</a>."),
        ],
        "checks": [
            ("Restart and try once more", "Restart the computer, then open <em>Settings</em>, <em>Windows Update</em> and choose <em>Check for updates</em>."),
            ("Check the date and time", "A wrong date or time stops Windows from trusting the update servers. Set it to automatic in <em>Settings</em>, <em>Time &amp; language</em>."),
            ("Free up space", "Large updates need room to unpack. Free at least 20GB in <em>Settings</em>, <em>System</em>, <em>Storage</em>."),
            ("Check your data", "Updates are large, often several gigabytes. On prepaid mobile data, make sure there is enough, and check that the connection is not set as <em>metered</em>, which pauses downloads."),
            ("Run the troubleshooter",
             "<p>Windows 11: <em>Settings</em>, <em>System</em>, <em>Troubleshoot</em>, <em>Other troubleshooters</em>, "
             "<em>Windows Update</em>. Windows 10: <em>Settings</em>, <em>Update &amp; Security</em>, "
             "<em>Troubleshoot</em>, <em>Additional troubleshooters</em>.</p>"),
            ("Unplug what you do not need", "Remove USB drives, printers and other accessories before installing a large update."),
            ("Repair the update files",
             "<p>Right-click the Start button and open <em>Terminal (Admin)</em> or <em>Command Prompt (Admin)</em>. "
             "Run these one after the other, waiting for each to finish:</p>"
             "<code class=\"cmd\">DISM /Online /Cleanup-Image /RestoreHealth</code>"
             "<code class=\"cmd\">sfc /scannow</code>"),
            ("Read the update history", "<em>Settings</em>, <em>Windows Update</em>, <em>Update history</em> shows which update failed and the error code. Keep the code: it speeds up a diagnosis."),
        ],
        "stop": [
            "The computer restarts in a loop and never reaches the desktop.",
            "The same error code returns after all the checks.",
            "Windows has become unstable since the failed update.",
        ],
        "stop_after": "<p>Do not switch the computer off while it says “Working on updates”. Interrupting an update is one of the ways Windows gets damaged.</p>",
        "ada": "<p>We find out why the update fails, repair the update components and the system files, and "
               "install the update. A reinstall of Windows is recommended only when repair is not possible, "
               "and you are told before it is done.</p>"
               "<p>Windows Update repair starts from N$249. Much of this work can be done by "
               "<a href=\"/services/remote-support\">remote support</a> if the computer still starts.</p>",
        "faq": [("Can I just turn Windows updates off?",
                 "<p>You can pause them for a few weeks, but leaving them off leaves known security holes open. "
                 "It is better to fix the reason they fail.</p>"),
                ("My PC still runs Windows 10. Does it still get updates?",
                 "<p>Standard support for Windows 10 ended on 14 October 2025. Microsoft offers Extended "
                 "Security Updates for eligible home PCs until 12 October 2027. See "
                 "<a href=\"/guides/windows-10-end-of-support\">what to do about Windows 10</a>.</p>"),
                ("Will I lose my files if the update is repaired?",
                 "<p>A repair keeps your files and programs. If a reinstall turns out to be necessary, backing "
                 "up comes first and is agreed with you before anything is erased.</p>")],
        "rel": [("/guides/windows-10-end-of-support", "Windows 10 support has ended", "Your options, with dates."),
                ("/problems/windows-black-screen", "Black screen but the power is on", "Sometimes follows a failed update."),
                ("/services/windows-setup", "Windows and software setup", "Clean installation packages from N$649.")],
    },
    # ------------------------------------------------------------------ F-07
    {
        "slug": "wifi-keeps-disconnecting", "code": "F-07", "icon": "wifi", "area": "Network",
        "short": "The Wi-Fi keeps disconnecting",
        "blurb": "Drops out, reconnects, or says connected with no internet.",
        "title": "Wi-Fi Not Working or Keeps Disconnecting? Fixes | ADA Tech",
        "desc": "Wi-Fi not working on a laptop or PC, or keeps dropping? Tell a router fault from a laptop fault, "
                "check after a power outage. Setup from N$349 in Rundu.",
        "h1": "Why is my Wi-Fi not working or disconnecting?",
        "extra": [
            ("Wi-Fi not working after a power outage",
             "<p>When the power comes back, the router and the modem start in the wrong order or not at all. "
             "Switch the router off at the wall, wait 30 seconds and switch it on, then give it three "
             "minutes. If you have a separate modem or fibre box, start that first. Look at the lights: if none "
             "come on at all, check the power adapter and try another socket, because a surge can kill the "
             "adapter or the router. If the lights are normal and every device says no internet, the fault is "
             "on the provider's side, and it is worth calling them before changing any settings.</p>"),
            ("Wi-Fi not working on one laptop or on a PC",
             "<p>If phones connect and one laptop does not, follow the laptop checks above: forget the network, "
             "turn off the power saving on the adapter, update the driver and reset the network settings. A "
             "desktop PC that has no Wi-Fi adapter cannot join Wi-Fi at all. It needs a network cable to the "
             "router or a plug-in Wi-Fi adapter, and a desktop with an adapter can lose it after a Windows "
             "update.</p>"),
        ],
        "lead": "One question splits this problem in half: does every device drop at the same moment, or only "
                "one laptop?",
        "answer": "If every device loses the connection together, the fault is in the router, its position or "
                  "the internet line. If only one laptop drops while phones stay connected, the fault is in "
                  "that laptop: its Wi-Fi driver, its power-saving setting or its saved network profile. "
                  "Compare two devices side by side first, then follow the checks for whichever half applies.",
        "causes": "Router, signal, internet line, power cut, Wi-Fi driver, power saving",
        "where": "On site in Rundu, or remote",
        "clues": [
            ("Every device drops at the same time", "The router, the internet line or the power to the router."),
            ("Only one laptop drops, phones stay connected", "That laptop's Wi-Fi adapter, driver or power-saving setting."),
            ("It works near the router and drops in other rooms", "Signal strength. Walls, distance and where the router sits."),
            ("It drops at the same time each day, often evenings", "Congestion, either on your provider's network or on the Wi-Fi channel."),
            ("“Connected, no internet”", "The Wi-Fi itself is fine. The fault is between the router and the internet."),
        ],
        "checks": [
            ("Compare two devices", "When the laptop drops, look at a phone on the same Wi-Fi. This one check tells you whether to look at the router or the laptop."),
            ("Restart the router properly", "Switch the router off at the wall, wait 30 seconds, switch it on and give it three minutes."),
            ("Move closer", "Test beside the router. If it is stable there, the problem is coverage, and the router's position matters more than its settings."),
            ("Forget the network and rejoin", "<em>Settings</em>, <em>Network &amp; internet</em>, <em>Wi-Fi</em>, <em>Manage known networks</em>. Choose the network, select <em>Forget</em>, then connect again with the password."),
            ("Stop Windows switching the adapter off",
             "<p>Right-click the Start button and open <em>Device Manager</em>. Under <em>Network adapters</em>, "
             "open the Wi-Fi adapter, go to <em>Power Management</em> and untick <em>Allow the computer to turn "
             "off this device to save power</em>.</p>"),
            ("Update the Wi-Fi driver", "Download the wireless driver for your exact model from the laptop maker's support page."),
            ("Choose the right band", "If the router offers 2.4GHz and 5GHz, 5GHz is faster over a short distance and 2.4GHz reaches further through walls."),
            ("Reset the network settings", "<em>Settings</em>, <em>Network &amp; internet</em>, <em>Advanced network settings</em>, <em>Network reset</em>. You will need to enter your Wi-Fi passwords again afterwards."),
        ],
        "stop": [
            "The router is old, runs hot or restarts by itself.",
            "An office or lodge needs coverage across several rooms or buildings.",
            "The connection has to be reliable for card machines, cameras or bookings.",
        ],
        "stop_title": "Get the network assessed if",
        "ada": "<p>For one laptop, we test the adapter and the driver. For a home or an office, we check the "
               "router's settings and position, measure where the signal falls away and recommend the smallest "
               "change that fixes it, which is sometimes moving the router and sometimes an extra access "
               "point.</p><p>Router and Wi-Fi setup starts from N$349. Cabling, extra equipment and coverage "
               "across several rooms are assessed and quoted.</p>",
        "faq": [("Is it my internet provider or my router?",
                 "<p>If the router's internet light goes out or changes colour when the connection drops, the "
                 "fault is on the provider's side or the line. If the lights stay normal and devices still drop, "
                 "look at the router and the Wi-Fi.</p>"),
                ("Will a Wi-Fi extender fix it?",
                 "<p>Sometimes. An extender repeats the signal it receives, so if it is placed where the signal "
                 "is already weak it repeats a weak signal. A cabled access point is usually more reliable for "
                 "an office.</p>"),
                ("Can you fix Wi-Fi remotely?",
                 "<p>Laptop settings and drivers, often yes. Router position, cabling and coverage need a visit, "
                 "which we do in Rundu.</p>")],
        "rel": [("/services/networking", "Wi-Fi and networking", "Router setup, coverage and office networks."),
                ("/services/business-it", "Business IT setup", "When the whole office depends on it."),
                ("/problems/printer-not-printing", "Printer will not print", "Often a Wi-Fi problem in disguise.")],
    },
    # ------------------------------------------------------------------ F-08
    {
        "slug": "laptop-battery-draining-fast", "code": "F-08", "icon": "battery", "area": "Power",
        "short": "The battery drains fast or will not charge",
        "blurb": "An hour of use, “plugged in, not charging”, or it dies at 30%.",
        "title": "Laptop Battery Draining Fast or Not Charging? How to Check | ADA Tech",
        "desc": "Laptop battery drains fast, dies suddenly or says plugged in, not charging? How to run the "
                "built-in Windows battery report and read the battery's real condition.",
        "h1": "Why is my laptop battery draining so fast?",
        "lead": "Windows can tell you exactly how worn the battery is. One command produces a report that "
                "separates a worn battery from a setting or a charger fault.",
        "answer": "Laptop batteries wear out with use. To see how worn yours is, open Command Prompt and run "
                  "powercfg /batteryreport, then compare “Full charge capacity” with “Design capacity” in the "
                  "report. If the battery now holds much less than it was designed to, it needs replacing. If "
                  "the capacity is healthy, look at screen brightness, background programs and the charger.",
        "causes": "Worn battery, charger, charging port, background programs, settings",
        "where": "Workshop in Rundu",
        "clues": [
            ("It used to last four hours and now lasts one", "The battery has worn. Check the capacity in the battery report."),
            ("It switches off suddenly at 20% or 30%", "Worn cells. The percentage shown is no longer accurate."),
            ("“Plugged in, not charging”", "The charger's wattage, the charging port, the battery, or a charge limit set by the maker's own app."),
            ("It stops charging at 60% or 80% every time", "Usually a battery-care setting from the manufacturer, which is deliberate and protects the battery."),
            ("The battery drains while the lid is closed", "The laptop is waking up in sleep. Use <em>Hibernate</em> or <em>Shut down</em> instead."),
            ("The case bulges, or the touchpad is lifting", "A swollen battery. Stop using and charging it."),
        ],
        "checks": [
            ("Run the battery report",
             "<p>Press the <kbd>Windows</kbd> key, type <em>cmd</em> and press Enter. Run:</p>"
             "<code class=\"cmd\">powercfg /batteryreport</code>"
             "<p>Windows saves a file called <code>battery-report.html</code> and shows where. Open it and "
             "compare <em>Design capacity</em> with <em>Full charge capacity</em>.</p>"),
            ("See what is using the battery", "<em>Settings</em>, <em>System</em>, <em>Power &amp; battery</em>, <em>Battery usage</em> lists the programs that used the most power."),
            ("Lower the screen brightness", "The screen is usually the largest drain. Lower it, and choose <em>Best power efficiency</em> as the power mode."),
            ("Check the charger", "Use the original charger or one with the same wattage. A lower-wattage charger can run the laptop without charging the battery."),
            ("Look for a charge limit", "Lenovo, ASUS, Dell, HP and others include a battery-care option in their own app that stops charging at 60% or 80% on purpose."),
        ],
        "stop": [
            "The battery is swollen. Do not charge it, press on it or pierce it.",
            "The charger or the charging port gets very hot or sparks.",
            "You smell burning near the charging port.",
        ],
        "ada": "<p>We test the battery, the charger and the charging port separately, so you replace the part "
               "that has actually failed. A replacement battery is quoted for your exact model before it is "
               "ordered.</p><p>" + DIAG_LINE + "</p>",
        "faq": [("How long should a laptop battery last?",
                 "<p>A battery wears a little with every charge. After a few years of daily use, holding "
                 "noticeably less than when new is normal. The battery report shows the real figure for yours.</p>"),
                ("Is it bad to leave the laptop plugged in all the time?",
                 "<p>Modern laptops stop charging when full, so it is safe. If you mostly work plugged in, the "
                 "maker's battery-care setting, which holds the charge at about 80%, slows the wear.</p>"),
                ("Can I keep using a swollen battery?",
                 "<p>No. A swollen battery can catch fire. Switch the laptop off, do not charge it, and have "
                 "the battery removed.</p>")],
        "rel": [("/problems/laptop-not-turning-on", "Laptop will not turn on", "When there is no power at all."),
                ("/problems/laptop-overheating", "Laptop overheating", "Heat wears a battery faster."),
                ("/guides/repair-or-replace-laptop", "Repair or replace?", "When a new battery is worth it.")],
    },
    # ------------------------------------------------------------------ F-09
    {
        "slug": "printer-not-printing", "code": "F-09", "icon": "printer", "area": "Printers",
        "short": "The printer will not print",
        "blurb": "Shows offline, jobs stuck in the queue, or prints nothing.",
        "title": "Printer Offline or Not Printing? How to Fix It | ADA Tech",
        "desc": "Printer says offline, jobs stuck in the queue or nothing prints? Seven checks for Windows, "
                "including how to clear a stuck print queue. Printer setup from N$179 in Rundu.",
        "h1": "Why will my printer not print?",
        "lead": "Most printing faults are connection or software faults, not a broken printer. The printer and "
                "the computer have stopped talking to each other.",
        "answer": "A printer that will not print is usually offline (the computer cannot reach it), blocked by "
                  "a stuck job in the print queue, or using a driver that an update has broken. Check that the "
                  "printer is on the same Wi-Fi network as the computer, clear the print queue, and restart the "
                  "Print Spooler service. If a new router was installed, the printer still has the old Wi-Fi "
                  "details and must be reconnected.",
        "causes": "Connection, stuck queue, driver, Wi-Fi change, ink or toner",
        "where": "On site in Rundu, or remote",
        "clues": [
            ("The printer shows as “Offline”", "The computer cannot reach it: a different Wi-Fi network, a changed router or a loose cable."),
            ("Documents sit in the queue and nothing happens", "A stuck job is blocking everything behind it."),
            ("It stopped after a Windows update", "The printer driver."),
            ("It stopped after a new router or a new Wi-Fi password", "The printer still has the old Wi-Fi details."),
            ("One computer prints and another does not", "The setup on the computer that fails, not the printer."),
            ("Pages come out blank, faded or streaked", "Ink, toner or the print heads. Run the printer's own cleaning cycle."),
        ],
        "checks": [
            ("Restart the printer and read its panel", "Switch it off and on. Look for a warning light or a message about paper, ink or a jam."),
            ("Check both are on the same network", "Print the network report from the printer's own menu. The Wi-Fi name on it must match the one the computer is using."),
            ("Check it is not set to offline", "<em>Settings</em>, <em>Bluetooth &amp; devices</em>, <em>Printers &amp; scanners</em>. Open the printer, open the print queue, and in the <em>Printer</em> menu make sure <em>Use Printer Offline</em> is not ticked."),
            ("Clear the queue", "In the print queue, cancel every document."),
            ("Restart the Print Spooler", "<p>Press the <kbd>Windows</kbd> key, type <em>services</em> and open it. Find <em>Print Spooler</em>, right-click it and choose <em>Restart</em>.</p>"),
            ("Remove the printer and add it again", "Remove it in <em>Printers &amp; scanners</em>, then add it again. Install the driver from the printer maker's support page for your exact model."),
            ("Try a USB cable", "If it prints over USB but not over Wi-Fi, the printer is fine and the network is the problem."),
        ],
        "stop": [
            "The printer makes grinding noises or jams on every page.",
            "It shows a hardware error code that returns after a restart.",
        ],
        "stop_title": "It is a printer repair, not a setup problem, if",
        "ada": "<p>We set up printers and fix connection, driver and sharing problems, including printers shared "
               "by a whole office. If the fault is mechanical, inside the printer itself, we tell you so "
               "rather than charge for setup work that will not fix it.</p>"
               "<p>Printer setup starts from N$179 and covers installation on a computer or a network and "
               "basic troubleshooting.</p>",
        "faq": [("Why does my printer keep going offline?",
                 "<p>Usually because the router gives it a different address each time it reconnects, or because "
                 "the printer drops off the Wi-Fi when it sleeps. Giving the printer a fixed address in the "
                 "router normally stops it.</p>"),
                ("Can several computers share one printer?",
                 "<p>Yes. A printer on the office network can be added to every computer and phone that needs "
                 "it. That is part of a normal <a href=\"/services/business-it\">office setup</a>.</p>"),
                ("Can you fix a printer remotely?",
                 "<p>Driver, queue and sharing problems, often yes. Anything that needs the printer's own panel "
                 "or a cable needs someone in the room.</p>")],
        "rel": [("/problems/wifi-keeps-disconnecting", "Wi-Fi keeps disconnecting", "The network behind the printer."),
                ("/services/business-it", "Business IT setup", "Printers, devices and accounts for an office."),
                ("/services/remote-support", "Remote support", "Software faults fixed over the internet.")],
    },
    # ------------------------------------------------------------------ F-10
    {
        "slug": "computer-virus-or-pop-ups", "code": "F-10", "icon": "threat", "area": "Security",
        "short": "Pop-ups, virus warnings or strange behaviour",
        "blurb": "Warnings that will not close, new toolbars, programs you did not install.",
        "title": "Virus Removal: Warnings, Pop-Ups and Real Infections | ADA Tech",
        "desc": "Virus removal for a Windows PC: tell a fake warning from a real infection, clean it yourself, "
                "or get virus removal in Rundu or remotely.",
        "h1": "Virus removal: does my computer have a virus?",
        "extra": [
            ("Virus removal near me: in Rundu or remotely",
             "<p>If you searched for a virus removal service near you and you are in Rundu, bring the "
             "computer to the workshop. We check what is on it, remove it, and make sure Windows Security and "
             "the updates are working again. If the computer still starts and you are elsewhere in Namibia, "
             "software-related faults can often be handled by "
             "<a href=\"/services/remote-support\">remote support</a>, with your permission and after we "
             "confirm the scope. Do not let anyone who phones you unasked do it.</p>"),
        ],
        "lead": "Most “virus warnings” that fill the screen and give a phone number are not viruses. They are web "
                "pages built to frighten you into calling. Real infections are quieter.",
        "answer": "A full-screen warning that tells you to call a number is a scam web page, not a virus. Close "
                  "the browser and never call the number or give anyone remote access. Real infections show up "
                  "as programs you did not install, a browser that redirects, or security software that has "
                  "been switched off. Run a full scan with Windows Security, remove unknown browser extensions "
                  "and change your passwords from another device.",
        "causes": "Scam web pages, browser notifications, unwanted extensions, malware",
        "where": "Remote or workshop",
        "clues": [
            ("A full-screen warning with a phone number to call", "A scam web page. Microsoft's own error messages never include a phone number."),
            ("Pop-ups in the corner of the screen, even with the browser closed", "A website was allowed to send notifications."),
            ("The browser opens pages you did not ask for, or the home page changed", "An unwanted browser extension."),
            ("Programs you did not install, or the antivirus has been switched off", "Malware on the computer."),
            ("Files renamed, with a note demanding payment", "Ransomware. Disconnect from the network and switch off."),
            ("Friends receive messages you did not send", "A stolen password. The computer may be clean."),
        ],
        "checks": [
            ("Close a fake warning", "<p>Press <kbd>Alt</kbd> + <kbd>F4</kbd>, or press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Esc</kbd> and end the browser in Task Manager. Do not call the number and do not click inside the page.</p>"),
            ("Remove notification permissions", "In Chrome or Edge, open <em>Settings</em>, <em>Privacy and security</em>, <em>Site settings</em>, <em>Notifications</em> and remove every site you do not recognise."),
            ("Remove unknown extensions", "Open the browser's <em>Extensions</em> page and remove anything you did not choose to install."),
            ("Run a full scan", "<em>Windows Security</em>, <em>Virus &amp; threat protection</em>, <em>Scan options</em>, <em>Full scan</em>. Then run <em>Microsoft Defender Antivirus (offline scan)</em>, which restarts the PC and scans before Windows loads."),
            ("Uninstall what you do not recognise", "<em>Settings</em>, <em>Apps</em>, <em>Installed apps</em>, sorted by install date. Remove programs that appeared around the time the trouble started."),
            ("Change your passwords from another device", "Use a phone or a different computer. Start with email and banking, and turn on two-step verification."),
            ("Install pending updates", "Updates close the holes that malware uses."),
        ],
        "stop": [
            "Files have been encrypted or renamed and there is a ransom note. Switch off, disconnect from the network, and get advice before paying anyone.",
            "Someone you phoned was given remote access to the computer. Treat it as compromised: disconnect it and tell your bank.",
            "The computer is used for banking or holds client records.",
        ],
        "ada": "<p>We check what is actually on the machine, remove it, and check that security updates and "
               "Windows Security are working again. Where an infection has gone deep, a clean installation of "
               "Windows is the only result that can be trusted, and we say so.</p><p>" + DIAG_LINE +
               " If a clean installation is the right answer, the Complete Device Refresh (N$1,049) includes "
               "backup and restore of up to 50GB, a malware scan and clean-up, and a fresh Windows setup.</p>",
        "faq": [("Do I need to buy antivirus software?",
                 "<p>Windows Security is built into Windows 10 and 11 and is enough for most people when it is "
                 "switched on and Windows is kept up to date. Running two antivirus programs together slows the "
                 "computer and causes conflicts.</p>"),
                ("I called the number on the warning. What now?",
                 "<p>If you gave remote access, disconnect the computer from the internet. If you gave card "
                 "details, call your bank straight away. Change your passwords from another device, then have "
                 "the computer checked.</p>"),
                ("Does ADA Tech ever phone people to say their computer has a virus?",
                 "<p>No. Nobody legitimate does. A call or a pop-up that arrives unasked and offers to fix your "
                 "computer is a scam.</p>")],
        "rel": [("/services/security", "Security and backups", "Two-step verification, backups and device protection."),
                ("/guides/back-up-your-files", "How to back up your files", "The only real protection against ransomware."),
                ("/services/windows-setup", "Windows and software setup", "Clean installation packages.")],
    },
    # ------------------------------------------------------------------ F-11
    {
        "slug": "liquid-spilled-on-laptop", "code": "F-11", "icon": "drop", "area": "Emergency",
        "short": "I spilled liquid on my laptop",
        "blurb": "Water, tea, a soft drink or beer went into the keyboard.",
        "title": "Spilled Water or a Drink on Your Laptop? Do This First | ADA Tech",
        "desc": "Liquid spilled on a laptop? Switch it off now. The first five minutes, what not to do, why rice "
                "does not help, and why it should be opened and cleaned even if it still works.",
        "h1": "I spilled liquid on my laptop. What do I do?",
        "lead": "Switch it off now. Hold the power button down until it is off, then unplug the charger. Read "
                "the rest afterwards.",
        "answer": "Switch the laptop off immediately by holding the power button, and unplug the charger. Do not "
                  "switch it back on to check whether it still works. Turn it upside down, open like a tent, "
                  "over a towel so the liquid drains away from the motherboard. Then have it opened and cleaned "
                  "as soon as possible, because the residue left behind corrodes the board over the following "
                  "days.",
        "answer_label": "Do this now",
        "causes": "Short circuits while powered, then corrosion from residue",
        "where": "Workshop in Rundu",
        "clues_title": "What was spilled matters",
        "clues_head": ("What was spilled", "What to expect"),
        "clues": [
            ("Clean water", "The best odds. The danger is a short circuit while the power is on, so speed matters most."),
            ("Tea or coffee with sugar, soft drinks, juice", "Sticky residue that conducts electricity and corrodes. It needs cleaning inside even if the laptop works."),
            ("Beer, wine, milk", "The same as sugary drinks, with corrosion starting sooner."),
            ("Salt water or soup", "The most corrosive. Treat as urgent."),
            ("A few drops on the keys, wiped at once", "Often no damage, but watch for keys that stick or type the wrong letter."),
        ],
        "checks_title": "The first five minutes", "checks_word": "first steps",
        "checks": [
            ("Switch it off", "Hold the power button down until the laptop is completely off. Do not wait to save your work."),
            ("Unplug everything", "Take out the charger and every USB device. If the battery comes out, remove it."),
            ("Drain it", "Open the laptop as far as it goes and stand it upside down like a tent, on a towel. Liquid then runs out through the keyboard instead of down onto the board."),
            ("Wipe what you can reach", "Dry the outside and the keyboard with a cloth or paper towel. Do not shake the laptop."),
            ("Leave it off", "Do not switch it on “just to check”. Power plus liquid is what causes the damage."),
        ],
        "stop_title": "Do not",
        "stop": [
            "Switch it on to see if it still works.",
            "Use a hair dryer or leave it in the sun. Heat warps parts and pushes liquid further in.",
            "Put it in rice. Rice does not draw liquid out from inside a laptop, and it does nothing about the residue.",
            "Charge it.",
        ],
        "stop_after": "<p>If the files matter more than the laptop, say so first. The drive can often be removed and copied before anything else is attempted.</p>",
        "ada": "<p>We open the laptop, disconnect the battery, find where the liquid went and clean the affected "
               "areas, then test it part by part. A keyboard often needs replacing after a spill.</p>"
               "<p>Liquid damage is uncertain, and some of it cannot be repaired at a sensible cost. You are "
               "told what we find before you spend more than the diagnostic.</p><p>" + DIAG_LINE + "</p>",
        "faq": [("It still works after the spill. Is it fine?",
                 "<p>Not necessarily. Residue inside keeps corroding the board, and faults often appear days or "
                 "weeks later. If anything other than a few drops of clean water went in, have it opened and "
                 "cleaned.</p>"),
                ("How long should I leave it to dry?",
                 "<p>Drying alone is not the fix, because the residue stays behind. Keep it switched off and "
                 "bring it in as soon as you can, ideally within a day.</p>"),
                FILES_FAQ],
        "rel": [("/problems/laptop-not-turning-on", "Laptop will not turn on", "If it no longer starts."),
                ("/guides/back-up-your-files", "How to back up your files", "So a spill costs a laptop, not your work."),
                ("/services/computer-repair", "Computer and laptop repair", "What the diagnostic covers.")],
    },
    # ------------------------------------------------------------------ F-12
    {
        "slug": "ssd-ram-upgrade", "code": "F-12", "icon": "chip", "area": "Upgrades",
        "short": "Should I upgrade the RAM or the SSD?",
        "blurb": "Which upgrade makes an older laptop faster, and which is wasted money.",
        "title": "RAM or SSD: Which Upgrade First for a Slow Laptop? | ADA Tech",
        "desc": "Should you upgrade RAM or SSD first? What each one fixes, how to check which your laptop needs "
                "in Task Manager, and what your model can take. Fitting from N$179 in Rundu.",
        "h1": "Should I upgrade the RAM or the SSD first?",
        "lead": "The right upgrade is the one that removes the bottleneck. Buying both without checking can "
                "waste money, and some laptops cannot take one of them at all.",
        "answer": "If the laptop still has a mechanical hard drive (HDD), replace it with an SSD first: that "
                  "gives the biggest improvement in start-up and loading times. If it already has an SSD and "
                  "memory use sits above about 85% in Task Manager during normal work, add RAM. Check what the "
                  "model supports before buying, because some laptops have memory soldered in place.",
        "causes": "Not a fault. A choice between two parts",
        "where": "Workshop in Rundu",
        "clues_title": "Which upgrade fits which symptom",
        "clues_head": ("What you notice", "Upgrade that helps"),
        "clues": [
            ("Takes minutes to start, and programs are slow to open", "SSD, if the laptop still has a hard drive (HDD)."),
            ("Task Manager shows Disk at 100% for long periods", "SSD."),
            ("Slows down with many browser tabs or several programs open", "RAM."),
            ("Task Manager shows Memory above about 85% in normal use", "RAM."),
            ("Already has an SSD and 8GB or more, and is still slow", "Neither. Look for another cause on the <a href=\"/problems/slow-laptop\">slow laptop</a> page."),
        ],
        "checks_title": "How to check your own laptop",
        "checks": [
            ("See what drive you have", "<p>Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Esc</kbd>, open <em>Performance</em> and select <em>Disk</em>. Windows shows <em>SSD</em> or <em>HDD</em> under the drive's name.</p>"),
            ("See how much memory is in use", "In the same window select <em>Memory</em>. Note the total, how much is in use during your normal work, and <em>Slots used</em>, which shows whether there is a free slot."),
            ("Find your exact model", "The model number is on a label underneath, or in <em>Settings</em>, <em>System</em>, <em>About</em>. It decides which parts fit."),
            ("Check what the model supports", "The maker's specification page lists the maximum memory, whether it is soldered, and whether the drive bay takes a 2.5-inch SATA drive, an M.2 SATA drive or an M.2 NVMe drive. These are not interchangeable."),
            ("Check the drive's health first", "If the old drive is already failing, copy your files off it before anything else."),
        ],
        "stop_title": "An upgrade may not be worth it if",
        "stop": [
            "The processor is very old, so the laptop will stay slow whatever is added.",
            "The laptop cannot run a supported version of Windows.",
            "The battery, the screen and the hinges are also failing.",
        ],
        "stop_after": "<p>In those cases, putting the money towards a replacement can be the better decision. See <a href=\"/guides/repair-or-replace-laptop\">repair or replace</a>.</p>",
        "ada": "<p>We check the bottleneck, the model's limits and the health of the existing drive, then "
               "recommend one part. If you want your files and programs moved to the new drive, that is done "
               "and tested before the laptop is handed back.</p>"
               "<p>Fitting RAM or an SSD starts from N$179 for labour. The part is quoted separately. Moving "
               "your data starts from N$249 for up to 50GB.</p>",
        "faq": [("How much RAM do I need?",
                 "<p>Windows 11 needs at least 4GB to run at all. For everyday work with a browser and Office, "
                 "8GB is comfortable. Heavy use, such as large spreadsheets, design work or many programs at "
                 "once, benefits from 16GB.</p>"),
                ("Will I lose my files when the drive is replaced?",
                 "<p>Not if the old drive is healthy and you ask for the data to be moved. The old drive is "
                 "copied to the new one, or Windows is installed fresh and your files are copied across.</p>"),
                ("Can every laptop be upgraded?",
                 "<p>No. Many thin laptops have the memory soldered to the motherboard, and a few have soldered "
                 "storage too. We check your model before you buy anything.</p>")],
        "rel": [("/problems/slow-laptop", "Laptop is very slow", "Find the bottleneck first."),
                ("/guides/repair-or-replace-laptop", "Repair or replace?", "When an upgrade is not worth it."),
                ("/pricing", "Pricing", "Labour prices for upgrades and data transfer.")],
    },
]

HOME_FAULTS = ["laptop-not-turning-on", "slow-laptop", "windows-blue-screen", "windows-black-screen",
               "laptop-overheating", "wifi-keeps-disconnecting", "windows-update-not-working",
               "liquid-spilled-on-laptop"]

KEYWORDS = {
    "laptop-not-turning-on": "dead no power wont start not starting not booting boot charger charging light no bootable device beep "
                             "laptop not turning on when plugged in laptop not turning on black screen laptop not turning on but power light is on "
                             "laptop not turning on but charging computer wont start computer wont start after power outage "
                             "computer wont start after windows update computer wont start black screen",
    "windows-black-screen": "black screen blank no display no picture dark screen cursor",
    "windows-blue-screen": "blue screen bsod stop code crash restarting error memory management critical process died",
    "slow-laptop": "slow lagging lag hanging freezing freeze speed up faster 100% disk laptop is slow laptop is slow what to do "
                   "laptop is slow to start up laptop is slow and hanging",
    "laptop-overheating": "hot heat overheating fan loud noisy shutting down shuts off temperature dust",
    "windows-update-not-working": "update stuck failing failed error 0x undoing changes windows 11 upgrade",
    "wifi-keeps-disconnecting": "wifi wi-fi internet network disconnecting dropping no internet router signal wifi not working "
                                "wifi not working on laptop wifi not working after power outage wifi not working on pc",
    "laptop-battery-draining-fast": "battery draining drain not charging plugged in charger dies swollen",
    "printer-not-printing": "printer offline not printing print queue spooler stuck hp canon epson",
    "computer-virus-or-pop-ups": "virus malware pop-up popup scam warning hacked ransomware antivirus adware virus removal "
                                 "virus removal near me virus removal service near me",
    "liquid-spilled-on-laptop": "water spill spilled liquid wet coffee tea drink rice keyboard",
    "ssd-ram-upgrade": "ssd ram memory upgrade hdd hard drive storage faster nvme",
}


def by_slug(slug):
    return next(p for p in PROBLEMS if p["slug"] == slug)


def fault_cards(slugs=None, swipe=False):
    items = [by_slug(s) for s in slugs] if slugs else PROBLEMS
    out = []
    for p in items:
        out.append(f'<a class="card card--link fault" href="/problems/{p["slug"]}">{icon(p["icon"])}'
                   f'<span class="tag">{p["code"]} / {e(p["area"])}</span><h3 class="h3">{e(p["short"])}</h3>'
                   f'<p>{e(p["blurb"])}</p><span class="more">Causes and checks</span></a>')
    return f'<div class="grid g3{" swipe" if swipe else ""}">' + "".join(out) + "</div>"


def hub():
    body = hero(
        "What is wrong with the device?",
        "Start from the symptom. Each page says what it usually means, what you can safely check yourself, "
        "when to stop, and what a repair costs.",
        [PRB], [("/support", "Not listed? Describe it"), (wa(), "Ask on WhatsApp", "line")],
        code=("Fault index", f"{len(PROBLEMS)} entries"))
    body += sec(answer(
        "These are the faults ADA Tech is asked about most: a laptop that will not turn on, black and blue "
        "screens, slow or overheating laptops, Windows Update failures, Wi-Fi that drops, worn batteries, "
        "printers that will not print, virus warnings and liquid spills. You do not need to know the cause "
        f"before asking for help. A standard diagnostic costs {DIAG} and comes off the repair if you go ahead.")
        + fault_cards())
    body += sec(head_block(
        "Questions people type into Google",
        "Each one goes to the page that answers it.", label="Quick lookup") + '<ul class="signs">' + "".join(
        f'<li><a href="{h}">{e(t)}</a></li>' for h, t in [
            ("/problems/windows-blue-screen", "How do I fix a blue screen on Windows 11?"),
            ("/problems/windows-black-screen", "Why is my laptop screen black but the power light is on?"),
            ("/problems/slow-laptop", "Why is my laptop slow even after restarting?"),
            ("/problems/laptop-overheating", "Why does my laptop get hot and shut down?"),
            ("/problems/windows-update-not-working", "Why does Windows Update keep failing?"),
            ("/problems/laptop-not-turning-on", "Why will my laptop not start after a BIOS update?"),
            ("/problems/wifi-keeps-disconnecting", "Why does Wi-Fi disconnect only on my laptop?"),
            ("/problems/ssd-ram-upgrade", "Should I upgrade RAM or SSD first?"),
            ("/problems/laptop-battery-draining-fast", "Why does my laptop say plugged in, not charging?"),
            ("/problems/printer-not-printing", "Why does my printer say offline?"),
            ("/problems/computer-virus-or-pop-ups", "Is the virus warning on my screen real?"),
            ("/problems/liquid-spilled-on-laptop", "What do I do if I spill water on my laptop?"),
        ]) + "</ul>", "sec--light")
    page("problems", "Computer and Laptop Problems: Causes and Fixes | ADA Tech",
         "Laptop will not turn on, blue or black screen, slow, overheating, Wi-Fi dropping, Windows Update "
         "failing, printer offline, virus warnings, liquid spills: causes, safe checks and repair costs.",
         body, active="/problems", crumbs=[PRB])


def build():
    hub()
    for p in PROBLEMS:
        path = "problems/" + p["slug"]
        crumbs = [PRB, (path, p["short"])]
        body = hero(p["h1"], p["lead"], crumbs,
                    [("/support", "Get it diagnosed"),
                     (wa(f"Hello ADA Tech, I need help with this problem: {p['short']}. "), "Ask on WhatsApp", "line")],
                    code=(f"Fault {p['code']}", p["area"]), ico=p["icon"])
        n = len(p["checks"])
        sh = sheet("Fault sheet", p["code"], [
            ("Symptom", e(p["short"])),
            ("Usual causes", e(p["causes"])),
            ("Self-checks", f"{n} {p.get('checks_word', 'checks')} on this page"),
            ("Diagnostic", f"<strong>{DIAG}</strong>, deducted from the repair if you go ahead"),
            ("Handled", e(p["where"])),
        ], ("/support", "Get it diagnosed"))
        body += sec('<div class="intro">' + answer(p["answer"], p.get("answer_label", "In short")) + sh + "</div>",
                    "sec--tight")
        head = p.get("clues_head", ("What you see", "What it usually means"))
        body += sec(head_block(p.get("clues_title", "What you see, and what it usually means"), label="Read the symptom")
                    + table(list(head), p["clues"], caption=p.get("clues_note", ""), first_th=True), "sec--light")
        body += sec(head_block(p.get("checks_title", "What you can check yourself"),
                               "These are safe to try, cost nothing and do not need tools.", label="Self-checks")
                    + checks(p["checks"]))
        for h2, inner in p.get("extra", []):
            body += sec(head_block(h2) + '<div class="prose">' + inner + "</div>", "sec--light")
        body += sec('<div class="split"><div>'
                    + stop(p["stop"], p.get("stop_title", "Stop and get it looked at if"), p.get("stop_after", ""))
                    + '</div><div><span class="label">On the bench</span><h2 class="h2">What ADA Tech does</h2>'
                    + '<div class="mt2">' + p["ada"] + '</div>'
                    + '<p><a class="more" href="/pricing">See all prices</a></p></div></div>', "sec--light")
        body += sec(head_block("Common questions", label="Questions") + faq(p["faq"]))
        body += related(p["rel"], "Related")
        schema = [faq_schema(p["faq"]),
                  howto_schema(p.get("checks_title", "What you can check yourself") + ": " + p["short"],
                               p["answer"], p["checks"])]
        page(path, p["title"], p["desc"], body, active="/problems", crumbs=crumbs, schema=schema)
