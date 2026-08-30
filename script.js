const boot=document.querySelector('.boot');if(boot)boot.remove();

/* ADA Tech navigation loading transition.
   Initial page loading is CSS-first so content never flashes before the loader. */
(()=>{
  const showNavigationState=(e)=>{
    const a=e.target.closest('a[href]');
    if(!a||e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey) return;
    const href=a.getAttribute('href')||'';
    if(!href||href.startsWith('#')||href.startsWith('mailto:')||href.startsWith('tel:')||a.target==='_blank'||a.hasAttribute('download')) return;
    let url;
    try{url=new URL(a.href,location.href)}catch{return}
    if(url.origin!==location.origin) return;
    if(url.pathname===location.pathname&&url.search===location.search) return;
    document.documentElement.classList.add('ada-navigating');
  };
  document.addEventListener('click',showNavigationState,{capture:true});
  window.addEventListener('pageshow',()=>document.documentElement.classList.remove('ada-navigating'));
})();

/* ADA family theme */
if(!document.querySelector('link[data-ada-brand-refresh]')){
  const theme=document.createElement('link');
  theme.rel='stylesheet';
  theme.href='/ada-brand-refresh.css?v=20260824-2';
  theme.dataset.adaBrandRefresh='1';
  document.head.appendChild(theme);
}

/* Favicons */
const ADA_FAVICON='https://andreas-digital-agency.vercel.app/brand/ADA-favicon.png?v=4';
let favicon=document.querySelector("link[rel~='icon']");
if(!favicon){favicon=document.createElement('link');favicon.rel='icon';favicon.type='image/png';document.head.appendChild(favicon)}
favicon.href=ADA_FAVICON;
let touch=document.querySelector("link[rel='apple-touch-icon']");
if(!touch){touch=document.createElement('link');touch.rel='apple-touch-icon';document.head.appendChild(touch)}
touch.href=ADA_FAVICON;

/* Global responsive + navigation system */
const globalStyle=document.createElement('style');
globalStyle.id='ada-tech-global-ui-v2';
globalStyle.textContent=`
html,body{max-width:100%;overflow-x:hidden}img,video{max-width:100%;height:auto}a,button{-webkit-tap-highlight-color:transparent}input,select,textarea{max-width:100%}
.header .wrap,.site-header .wrap,.header-inner{position:relative}.nav,.main-nav{display:flex;align-items:center;gap:4px!important;margin-left:auto;overflow:visible!important}.mobileMenu{display:none}
.ada-nav-group{position:relative}.ada-nav-trigger,.ada-nav-direct{appearance:none;border:0;background:transparent;color:#4f5f73;font:inherit;font-size:13px;font-weight:700;display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 10px;border-radius:10px;cursor:pointer;white-space:nowrap;text-decoration:none}.ada-nav-trigger:hover,.ada-nav-trigger:focus-visible,.ada-nav-direct:hover,.ada-nav-direct:focus-visible{background:#f3f6f9;color:#0f1b2d;outline:none}.ada-chevron{font-size:11px;transition:transform .18s ease}.ada-nav-group.open .ada-chevron{transform:rotate(180deg)}
.ada-nav-panel{position:absolute;top:calc(100% + 12px);left:0;width:340px;padding:12px;background:rgba(255,255,255,.985);border:1px solid #dbe4ee;border-radius:18px;box-shadow:0 24px 70px rgba(15,27,45,.16);opacity:0;visibility:hidden;transform:translateY(-6px);pointer-events:none;transition:.18s ease;z-index:300}.ada-nav-group:last-of-type .ada-nav-panel{left:auto;right:0}.ada-nav-group:hover>.ada-nav-panel,.ada-nav-group:focus-within>.ada-nav-panel,.ada-nav-group.open>.ada-nav-panel{opacity:1;visibility:visible;transform:none;pointer-events:auto}.ada-nav-panel.mega{width:min(720px,72vw)}.ada-nav-panel.wide{width:min(590px,65vw)}.ada-nav-panel-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px}.ada-nav-panel.mega .ada-nav-panel-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.ada-nav-item{display:block;padding:11px 12px!important;border-radius:12px!important;text-decoration:none!important;color:#21344c!important;min-height:0!important}.ada-nav-item:hover,.ada-nav-item:focus-visible{background:#f3f7fb!important;outline:none}.ada-nav-item strong{display:block;font-size:12px;line-height:1.2;color:#10243a}.ada-nav-item small{display:block;margin-top:4px;color:#718095;font-size:10px;line-height:1.35;font-weight:500}.ada-nav-item.all{background:#edf5ff!important;color:#174f8c!important}.ada-nav-item.all strong{color:#174f8c}.ada-nav-section-label{grid-column:1/-1;padding:6px 10px 2px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:#7a899b;font-weight:800}.nav .cta,.main-nav .cta{margin-left:4px!important;white-space:nowrap}.ada-current{color:#174f8c!important;background:#edf5ff!important}
.ada-utility-links{display:flex;align-items:center;gap:18px!important}.ada-utility-links a{font-size:11px!important;opacity:.88}.ada-utility-links a:hover{opacity:1}
.ada-global-footer{background:#081b33!important;color:#fff;padding:58px 0 24px}.ada-footer-grid{display:grid;grid-template-columns:1.35fr 1fr 1fr 1fr 1fr;gap:34px}.ada-footer-brand img{width:178px;max-width:100%;margin-bottom:18px}.ada-footer-brand p{color:#aebdcd!important;max-width:280px;font-size:13px;line-height:1.6}.ada-global-footer h3{font-size:12px;margin:0 0 14px;color:#fff;letter-spacing:.02em}.ada-global-footer a{display:block;color:#b7c3d0!important;font-size:12px;line-height:1.45;margin:8px 0;text-decoration:none}.ada-global-footer a:hover{color:#fff!important}.ada-footer-subhead{margin-top:20px!important;color:#7faee0!important;font-size:9px!important;letter-spacing:.12em!important;text-transform:uppercase}.ada-footer-bottom{display:flex;justify-content:space-between;gap:20px;align-items:center;margin-top:46px;padding-top:20px;border-top:1px solid rgba(255,255,255,.11);color:#7f91a5;font-size:11px}.ada-footer-bottom a{display:inline!important;font-size:11px!important;margin:0!important;color:#9fb0c2!important}

@media(max-width:1180px) and (min-width:1021px){.ada-nav-trigger,.ada-nav-direct{padding:0 7px;font-size:12px}.nav .cta,.main-nav .cta{padding-left:14px!important;padding-right:14px!important}.identity img,.brand img{width:132px!important}}
@media(max-width:1020px){
  .header,.site-header{height:76px!important;position:sticky;top:0!important;z-index:200;background:rgba(255,255,255,.97)!important;backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-bottom:1px solid rgba(8,27,51,.07)!important}.header .wrap,.site-header .wrap,.header-inner{height:100%!important;display:flex;align-items:center;justify-content:space-between;gap:14px}.header .wrap{width:min(1220px,calc(100% - 28px))!important;padding:0!important;border:0!important;border-radius:0!important;box-shadow:none!important;background:transparent!important}.identity img,.brand img{width:132px!important}.division{font-size:7px!important;padding-left:9px!important}.brand span{min-width:auto}
  .nav,.main-nav{gap:8px!important}.nav>.ada-nav-group,.main-nav>.ada-nav-group,.nav>.ada-nav-direct,.main-nav>.ada-nav-direct,.nav>.cta,.main-nav>.cta{display:none!important}.mobileMenu{display:inline-flex!important;align-items:center;justify-content:center;width:46px;height:46px;border:1px solid #d8e0e7;border-radius:14px;background:#fff;color:#0f1b2d;font-size:22px;line-height:1;cursor:pointer;user-select:none}
  .nav.open,.main-nav.open{position:absolute;top:calc(100% + 8px);left:0;right:0;display:flex!important;flex-direction:column;align-items:stretch;gap:4px!important;background:#fff;border:1px solid #dfe5eb;border-radius:20px;padding:10px;box-shadow:0 24px 70px rgba(15,27,45,.18);z-index:400;max-height:calc(100vh - 96px);overflow-y:auto!important;-webkit-overflow-scrolling:touch}.nav.open>.ada-nav-group,.main-nav.open>.ada-nav-group,.nav.open>.ada-nav-direct,.main-nav.open>.ada-nav-direct,.nav.open>.cta,.main-nav.open>.cta{display:block!important;width:100%!important}.nav.open>.ada-nav-direct,.main-nav.open>.ada-nav-direct{display:flex!important;min-height:50px;align-items:center;padding:12px 14px!important;font-size:14px!important}.nav.open>.cta,.main-nav.open>.cta{display:flex!important;align-items:center;justify-content:center;min-height:50px;margin:5px 0 0!important}.nav.open .mobileMenu,.main-nav.open .mobileMenu{position:absolute;right:10px;top:-64px}
  .ada-nav-trigger{width:100%;min-height:50px;justify-content:space-between;padding:12px 14px;font-size:14px}.ada-nav-panel,.ada-nav-panel.mega,.ada-nav-panel.wide{position:static;width:100%!important;padding:0 8px 8px;margin:0;border:0;border-radius:0;box-shadow:none;background:#f8fafc;opacity:1;visibility:visible;transform:none;pointer-events:auto;display:none}.ada-nav-group.open>.ada-nav-panel{display:block}.ada-nav-panel-grid,.ada-nav-panel.mega .ada-nav-panel-grid{grid-template-columns:1fr}.ada-nav-section-label{padding-top:13px}.ada-nav-item{padding:11px 12px!important}.ada-nav-item strong{font-size:13px}.ada-nav-item small{font-size:11px}.ada-global-footer{padding:52px 0 24px}.ada-footer-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:34px 28px}.ada-footer-brand{grid-column:1/-1}
  .hero{min-height:auto!important;padding:64px 0 58px!important}.heroGrid,.pageHeroGrid,.serviceIntro{grid-template-columns:1fr!important;gap:36px!important}.hero h1,.pageHero h1{font-size:clamp(50px,8vw,72px)!important}.visual{height:420px!important}.pageHero{padding:60px 0!important}.pageHero .heroImage{height:320px!important}.section{padding:78px 0!important}.sectionHead{gap:30px!important}.cards,.priceGrid{grid-template-columns:repeat(2,minmax(0,1fr))!important}.card{min-width:0}.imageSplit{grid-template-columns:1fr!important}.imageSplit .media{order:-1;min-height:430px!important}.routeStrip .wrap{grid-template-columns:repeat(3,minmax(0,1fr))}.tableWrap{max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}.tableWrap table{min-width:720px}.support-layout,.reviewLayout,.faqGrid{grid-template-columns:1fr!important}.support-intro,.faqAside{position:static!important}
}
@media(max-width:780px){.routeStrip .wrap{grid-template-columns:1fr!important}.route{min-height:auto!important;padding:22px!important}.route strong{margin:14px 0 7px!important}.cards,.priceGrid{grid-template-columns:1fr!important}.sectionHead{display:block!important}.sectionHead p{margin-top:16px!important}.waGrid{grid-template-columns:1fr!important}.whatsappBand .btn{width:100%}}
@media(max-width:680px){
  html{scroll-padding-top:76px}body{font-size:15.5px;line-height:1.58}.wrap{width:calc(100% - 28px)!important;max-width:1220px}.utility,.topbar{display:none!important}.header,.site-header{height:70px!important}.identity img,.brand img{width:118px!important}.division{font-size:6.5px!important;letter-spacing:.13em!important}.mobileMenu{width:44px;height:44px;border-radius:13px;font-size:21px}.nav.open,.main-nav.open{left:0;right:0;border-radius:16px;padding:8px}.nav.open .mobileMenu,.main-nav.open .mobileMenu{top:-60px}
  .hero{padding:46px 0 48px!important}.heroGrid{gap:28px!important}.hero h1,.pageHero h1,.proof-hero h1,.reviewHero h1,.desk-hero h1{font-size:clamp(40px,12vw,50px)!important;line-height:.96!important;letter-spacing:-.055em!important}.lede,.hero p,.pageHero p{font-size:16px!important;line-height:1.6!important}.actions,.hero-actions{display:grid!important;grid-template-columns:1fr!important;gap:9px!important;width:100%}.actions .btn,.hero-actions .btn,.btn.full{width:100%!important;min-height:52px!important;padding:0 16px!important}.btn{min-height:48px;font-size:9.5px!important;text-align:center}.visual{height:320px!important;border-radius:20px!important}.section{padding:58px 0!important}.sectionHead h2,.imageSplit .copy h2,.support-intro h2{font-size:clamp(35px,10vw,43px)!important}.card{min-height:auto!important;padding:20px!important;border-radius:16px!important}.priceCard{padding:21px!important}.pageHero{padding:42px 0 44px!important}.pageHero .heroImage{height:230px!important;border-radius:18px!important}.checklist{grid-template-columns:1fr!important}.imageSplit .copy{padding:48px 18px!important}.imageSplit .media{min-height:300px!important}.whatsappBand{padding:46px 0!important}.floatingWA{right:14px!important;bottom:max(14px,env(safe-area-inset-bottom))!important;width:52px!important;height:52px!important;padding:0!important;justify-content:center!important;border-radius:50%!important}.floatingWA span{display:none!important}input,select,textarea{font-size:16px!important}.form-grid,.reviewGrid,.case-grid,.desk-grid,.case-flow{grid-template-columns:1fr!important}.support-form{padding:18px!important;border-radius:18px!important}.ada-footer-grid{grid-template-columns:1fr;gap:28px}.ada-footer-brand{grid-column:auto}.ada-footer-bottom{flex-direction:column;align-items:flex-start;margin-top:34px}
}
@media(max-width:390px){.wrap{width:calc(100% - 22px)!important}.identity img,.brand img{width:108px!important}.division{display:none!important}.hero h1,.pageHero h1,.proof-hero h1,.reviewHero h1,.desk-hero h1{font-size:38px!important}.sectionHead h2,.imageSplit .copy h2,.support-intro h2{font-size:34px!important}.visual{height:260px!important}.card{padding:18px!important}.support-form{padding:15px!important}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{scroll-behavior:auto!important;animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important}}
`;
document.head.appendChild(globalStyle);

const path=location.pathname.replace(/\/$/,'')||'/';
const isAdmin=path==='/tech-publisher';

if(!isAdmin){
  /* Standard utility access */
  const utilityMarkup='<div class="ada-utility-links"><a href="/reviews">Reviews</a><a href="/client-desk">Client Desk</a><a href="/service-record">Service Record</a><a href="/directory">All Tech Pages</a><a href="https://andreas-digital-agency.vercel.app/">ADA Main</a></div>';
  document.querySelectorAll('.utility .wrap,.topbar .wrap').forEach(w=>w.innerHTML=utilityMarkup);

  const services=`
    <div class="ada-nav-group">
      <button class="ada-nav-trigger" type="button" aria-expanded="false">Services <span class="ada-chevron">⌄</span></button>
      <div class="ada-nav-panel mega"><div class="ada-nav-panel-grid">
        <a class="ada-nav-item all" href="/services"><strong>All Services</strong><small>Choose by problem or system.</small></a>
        <a class="ada-nav-item" href="/services/computer-repair"><strong>Computer Repair</strong><small>Diagnostics, hardware, SSD/RAM, heat and startup faults.</small></a>
        <a class="ada-nav-item" href="/services/windows-setup"><strong>Windows & Software</strong><small>Windows, drivers, updates, Office and licensed setup.</small></a>
        <a class="ada-nav-item" href="/services/bios-firmware"><strong>BIOS & Firmware</strong><small>Boot, UEFI, updates and recovery assessment.</small></a>
        <a class="ada-nav-item" href="/services/networking"><strong>Networking & Wi-Fi</strong><small>Routers, connectivity, cabling and office networks.</small></a>
        <a class="ada-nav-item" href="/services/remote-support"><strong>Remote Support</strong><small>Software and configuration help across Namibia.</small></a>
        <a class="ada-nav-item" href="/services/cctv"><strong>CCTV Systems</strong><small>Planning, setup, recorder and remote viewing.</small></a>
        <a class="ada-nav-item" href="/services/security"><strong>Security & Data</strong><small>MFA, backups, endpoint hygiene and hardening.</small></a>
        <a class="ada-nav-item" href="/services/server-infrastructure"><strong>Server & Infrastructure</strong><small>Technical infrastructure and server foundations.</small></a>
        <a class="ada-nav-item" href="/services/business-it"><strong>Business IT</strong><small>Users, devices, printers, accounts and office systems.</small></a>
      </div></div>
    </div>`;

  const help=`
    <div class="ada-nav-group">
      <button class="ada-nav-trigger" type="button" aria-expanded="false">Help <span class="ada-chevron">⌄</span></button>
      <div class="ada-nav-panel mega"><div class="ada-nav-panel-grid">
        <a class="ada-nav-item all" href="/problems"><strong>Common Problems</strong><small>Start with the symptom you are seeing.</small></a>
        <a class="ada-nav-item" href="/problems/windows-blue-screen"><strong>Blue Screen</strong><small>Stop codes, crashes and restart loops.</small></a>
        <a class="ada-nav-item" href="/problems/windows-black-screen"><strong>Black Screen</strong><small>Power on but no usable display.</small></a>
        <a class="ada-nav-item" href="/problems/slow-laptop"><strong>Slow Laptop</strong><small>Performance, storage, RAM or software bottlenecks.</small></a>
        <a class="ada-nav-item" href="/problems/laptop-overheating"><strong>Overheating</strong><small>Heat, loud fans and shutdowns.</small></a>
        <a class="ada-nav-item" href="/problems/laptop-not-turning-on"><strong>Won't Turn On</strong><small>Power, boot and startup symptoms.</small></a>
        <a class="ada-nav-item" href="/problems/windows-update-not-working"><strong>Windows Update</strong><small>Failed, stuck or repeating updates.</small></a>
        <a class="ada-nav-item" href="/problems/wifi-keeps-disconnecting"><strong>Wi-Fi Disconnecting</strong><small>Repeated drops and adapter issues.</small></a>
        <a class="ada-nav-item" href="/problems/ssd-ram-upgrade"><strong>RAM or SSD?</strong><small>Choose the upgrade that solves the actual bottleneck.</small></a>
        <a class="ada-nav-item" href="/faq"><strong>FAQ</strong><small>Pricing, licences, data safety, repairs and support.</small></a>
        <a class="ada-nav-item" href="/support"><strong>Request Support</strong><small>Describe the problem and send it to ADA Tech.</small></a>
      </div></div>
    </div>`;

  const plans=`
    <div class="ada-nav-group">
      <button class="ada-nav-trigger" type="button" aria-expanded="false">Plans <span class="ada-chevron">⌄</span></button>
      <div class="ada-nav-panel"><div class="ada-nav-panel-grid">
        <a class="ada-nav-item" href="/first-aid"><strong>ADA First Aid</strong><small>Recurring device care for individuals and families.</small></a>
        <a class="ada-nav-item" href="/managed-it"><strong>Managed IT</strong><small>Ongoing support for organisations, users and devices.</small></a>
      </div></div>
    </div>`;

  const work=`
    <div class="ada-nav-group">
      <button class="ada-nav-trigger" type="button" aria-expanded="false">Work <span class="ada-chevron">⌄</span></button>
      <div class="ada-nav-panel"><div class="ada-nav-panel-grid">
        <a class="ada-nav-item" href="/work"><strong>Tech Case Files</strong><small>Real issue → diagnosis → intervention → result.</small></a>
        <a class="ada-nav-item" href="/reviews"><strong>Client Reviews</strong><small>Approved feedback from real ADA Tech clients.</small></a>
      </div></div>
    </div>`;

  const about=`
    <div class="ada-nav-group">
      <button class="ada-nav-trigger" type="button" aria-expanded="false">About <span class="ada-chevron">⌄</span></button>
      <div class="ada-nav-panel"><div class="ada-nav-panel-grid">
        <a class="ada-nav-item" href="/about"><strong>How ADA Tech Works</strong><small>Assess, diagnose, recommend, implement and document.</small></a>
        <a class="ada-nav-item" href="/locations/rundu"><strong>Rundu IT Support</strong><small>Local on-site support in Rundu.</small></a>
        <a class="ada-nav-item" href="/contact"><strong>Contact ADA Tech</strong><small>Route a technical, quote or business enquiry.</small></a>
        <a class="ada-nav-item" href="/directory"><strong>Site Directory</strong><small>Browse every public ADA Tech page.</small></a>
        <a class="ada-nav-item" href="https://andreas-digital-agency.vercel.app/"><strong>ADA Main Website</strong><small>Company, divisions, projects, careers and news.</small></a>
      </div></div>
    </div>`;

  const navMarkup=services+help+plans+work+'<a class="ada-nav-direct" href="/pricing">Pricing</a>'+about+'<a class="cta nav-support" href="/support">Get Support</a><span class="mobileMenu" role="button" tabindex="0" aria-label="Open navigation" aria-expanded="false">☰</span>';
  document.querySelectorAll('nav.nav,nav.main-nav').forEach(n=>n.innerHTML=navMarkup);

  /* Mark current page */
  document.querySelectorAll('.ada-nav-item,.ada-nav-direct').forEach(a=>{
    const href=a.getAttribute('href');
    if(href&&href.startsWith('/')&&(path===href||(href!=='/'&&path.startsWith(href+'/'))))a.classList.add('ada-current');
  });

  /* Professional full site footer */
  const footerMarkup=`<footer class="ada-global-footer"><div class="wrap"><div class="ada-footer-grid">
    <div class="ada-footer-brand"><img src="https://andreas-digital-agency.vercel.app/brand/logos/ada-primary-white.png" alt="Andreas Digital Agency"><p>Practical computer, network and business IT support from Rundu, with remote support across Namibia.</p><a href="/support">Get Support →</a><a href="https://wa.me/264818032641" target="_blank" rel="noopener">WhatsApp +264 81 803 2641 →</a></div>
    <div><h3>Services</h3><a href="/services">All Services</a><a href="/services/computer-repair">Computer Repair</a><a href="/services/windows-setup">Windows & Software</a><a href="/services/bios-firmware">BIOS & Firmware</a><a href="/services/networking">Networking & Wi-Fi</a><a href="/services/remote-support">Remote Support</a><a href="/services/cctv">CCTV</a><a href="/services/security">Security & Data</a><a href="/services/server-infrastructure">Server & Infrastructure</a><a href="/services/business-it">Business IT</a></div>
    <div><h3>Help & Problems</h3><a href="/problems">All Common Problems</a><a href="/problems/windows-blue-screen">Blue Screen</a><a href="/problems/windows-black-screen">Black Screen</a><a href="/problems/slow-laptop">Slow Laptop</a><a href="/problems/laptop-overheating">Overheating</a><a href="/problems/laptop-not-turning-on">Won't Turn On</a><a href="/problems/windows-update-not-working">Windows Update</a><a href="/problems/wifi-keeps-disconnecting">Wi-Fi Disconnecting</a><a href="/problems/ssd-ram-upgrade">RAM or SSD Upgrade</a><a href="/faq">FAQ</a></div>
    <div><h3>Plans & Proof</h3><a href="/first-aid">ADA First Aid</a><a href="/managed-it">Managed IT</a><a href="/work">Tech Case Files</a><a href="/reviews">Client Reviews</a><a href="/pricing">Pricing</a><span class="ada-footer-subhead">Existing Clients</span><a href="/client-desk">Client Desk</a><a href="/service-record">Service Record</a></div>
    <div><h3>ADA Tech</h3><a href="/about">How ADA Tech Works</a><a href="/locations/rundu">Rundu IT Support</a><a href="/contact">Contact</a><a href="/support">Request Support</a><a href="/directory">Site Directory</a><span class="ada-footer-subhead">ADA Company</span><a href="https://andreas-digital-agency.vercel.app/">ADA Main</a><a href="https://ada-web-division.vercel.app/">ADA Web Division</a></div>
  </div><div class="ada-footer-bottom"><span>© 2026 Andreas Digital Agency. Built in Namibia. Designed for Africa.</span><span><a href="/directory">All Tech Pages</a> · <a href="/contact">Contact</a> · <a href="/support">Support</a></span></div></div></footer>`;
  document.querySelectorAll('footer.footer,footer.site-footer,footer').forEach((f,i)=>{if(i===0)f.outerHTML=footerMarkup;else f.remove()});

  /* Problem pages always end with a conversion action */
  if(path.startsWith('/problems/')&&!document.querySelector('[data-problem-conversion]')){
    const f=document.querySelector('.ada-global-footer');
    if(f){const s=document.createElement('section');s.className='whatsappBand';s.dataset.problemConversion='1';s.innerHTML='<div class="wrap waGrid"><div><div class="eyebrow" style="color:#dbe9ff">Still happening?</div><h3>Stop guessing at the cause.</h3><p>Standard device diagnosis starts at N$120 and can be waived when approved repair/service of N$350+ follows.</p></div><a class="btn" href="/support">Request diagnostic →</a></div>';f.before(s)}
  }

  const closeAllGroups=()=>document.querySelectorAll('.ada-nav-group.open').forEach(g=>{g.classList.remove('open');g.querySelector('.ada-nav-trigger')?.setAttribute('aria-expanded','false')});
  const closeMobile=()=>document.querySelectorAll('nav.open').forEach(n=>{n.classList.remove('open');const m=n.querySelector('.mobileMenu');if(m){m.setAttribute('aria-expanded','false');m.setAttribute('aria-label','Open navigation');m.textContent='☰'}});

  document.querySelectorAll('.mobileMenu').forEach(m=>{
    const toggle=()=>{const n=m.closest('nav');if(!n)return;const open=!n.classList.contains('open');n.classList.toggle('open',open);m.setAttribute('aria-expanded',String(open));m.setAttribute('aria-label',open?'Close navigation':'Open navigation');m.textContent=open?'×':'☰';if(!open)closeAllGroups()};
    m.addEventListener('click',toggle);
    m.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();toggle()}});
  });

  document.querySelectorAll('.ada-nav-trigger').forEach(btn=>{
    btn.addEventListener('click',e=>{
      const group=btn.closest('.ada-nav-group');if(!group)return;
      if(innerWidth<=1020){e.preventDefault();const open=!group.classList.contains('open');group.parentElement.querySelectorAll('.ada-nav-group.open').forEach(g=>{if(g!==group){g.classList.remove('open');g.querySelector('.ada-nav-trigger')?.setAttribute('aria-expanded','false')}});group.classList.toggle('open',open);btn.setAttribute('aria-expanded',String(open));}
      else{const open=!group.classList.contains('open');closeAllGroups();group.classList.toggle('open',open);btn.setAttribute('aria-expanded',String(open));}
    });
  });

  document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{closeMobile();closeAllGroups()}));
  document.addEventListener('click',e=>{if(innerWidth>1020&&!e.target.closest('nav'))closeAllGroups()});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeAllGroups();closeMobile()}});
  window.addEventListener('resize',()=>{if(innerWidth>1020)closeMobile();closeAllGroups()},{passive:true});
}

/* Pause off-screen videos to save phone battery/data */
const vids=[...document.querySelectorAll('video')];
if('IntersectionObserver'in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.play().catch(()=>{});else e.target.pause()}),{threshold:.12});vids.forEach(v=>io.observe(v))}


/* ADA unified division path bridge */
(() => {
  const prefix = "/divisions/tech";
  const onUnifiedPath =
    window.location.pathname === prefix ||
    window.location.pathname.startsWith(prefix + "/");

  if (!onUnifiedPath) return;

  const toUnifiedPath = (value) => {
    if (!value || !value.startsWith("/") || value.startsWith("//")) return value;
    if (value === prefix || value.startsWith(prefix + "/")) return value;
    return prefix + value;
  };

  const rewriteLinks = (root = document) => {
    root.querySelectorAll("a[href]").forEach((link) => {
      const href = link.getAttribute("href");
      const next = toUnifiedPath(href);
      if (next !== href) link.setAttribute("href", next);
    });

    root.querySelectorAll("form[action]").forEach((form) => {
      const action = form.getAttribute("action");
      const next = toUnifiedPath(action);
      if (next !== action) form.setAttribute("action", next);
    });
  };

  rewriteLinks();

  const observer = new MutationObserver(() => rewriteLinks());
  observer.observe(document.documentElement, {
    childList: true,
    subtree: true,
  });
})();
