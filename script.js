const boot=document.querySelector('.boot');if(boot)boot.remove();

/* ADA family visual theme */
if(!document.querySelector('link[data-ada-brand-refresh]')){const theme=document.createElement('link');theme.rel='stylesheet';theme.href='/ada-brand-refresh.css?v=20260824-1';theme.dataset.adaBrandRefresh='1';document.head.appendChild(theme)}

/* ADA Tech mobile-first compatibility layer.
   Kept here so every public page receives the same phone/tablet behaviour,
   including older pages that use site-header/main-nav class names. */
const responsiveStyle=document.createElement('style');
responsiveStyle.id='ada-tech-responsive-v1';
responsiveStyle.textContent=`
html,body{max-width:100%;overflow-x:hidden}img,video{max-width:100%;height:auto}a,button{-webkit-tap-highlight-color:transparent}input,select,textarea{max-width:100%}.header .wrap,.site-header .wrap,.header-inner{position:relative}
@media(max-width:1020px){
  .header,.site-header{height:76px;position:sticky;top:0;z-index:100;background:rgba(255,255,255,.97);backdrop-filter:blur(18px)}
  .header .wrap,.site-header .wrap,.header-inner{height:100%;display:flex;align-items:center;justify-content:space-between;gap:14px}
  .identity img,.brand img{width:132px!important}.division{font-size:7px!important;padding-left:9px!important}.brand span{min-width:auto}
  .nav,.main-nav{gap:9px!important;margin-left:auto}.nav a:not(.cta),.main-nav a:not(.cta){display:none!important}.mobileMenu{display:inline-flex!important;align-items:center;justify-content:center;width:46px;height:46px;border:1px solid #d8e0e7;border-radius:14px;background:#fff;color:#080a0d;font-size:22px;line-height:1;cursor:pointer;user-select:none}
  .nav.open,.main-nav.open{position:absolute;top:calc(100% + 8px);left:0;right:0;display:flex!important;flex-direction:column;align-items:stretch;gap:4px!important;background:#fff;border:1px solid #dfe5eb;border-radius:18px;padding:10px;box-shadow:0 22px 60px rgba(8,10,13,.16);z-index:120}
  .nav.open a,.main-nav.open a{display:flex!important;width:100%;min-height:48px;align-items:center;padding:12px 14px;border-radius:11px;font-size:14px!important;font-weight:750}.nav.open a:not(.cta):hover,.main-nav.open a:not(.cta):hover{background:#f3f6f9}.nav.open .cta,.main-nav.open .cta{justify-content:center;margin-top:4px}.nav.open .mobileMenu,.main-nav.open .mobileMenu{position:absolute;right:10px;top:-62px}
  .hero{min-height:auto!important;padding:64px 0 58px!important}.heroGrid,.pageHeroGrid,.serviceIntro{grid-template-columns:1fr!important;gap:36px!important}.hero h1,.pageHero h1{font-size:clamp(50px,8vw,72px)!important}.visual{height:420px!important}.pageHero{padding:60px 0!important}.pageHero .heroImage{height:320px!important}.section{padding:78px 0!important}.sectionHead{gap:30px!important}.cards,.priceGrid{grid-template-columns:repeat(2,minmax(0,1fr))!important}.card{min-width:0}.imageSplit{grid-template-columns:1fr!important}.imageSplit .media{order:-1;min-height:430px!important}.footerTop{grid-template-columns:repeat(2,minmax(0,1fr))!important}.footerTop>div:first-child{grid-column:1/-1}.routeStrip .wrap{grid-template-columns:repeat(3,minmax(0,1fr))}.tableWrap{max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}.tableWrap table{min-width:720px}.support-layout,.reviewLayout,.faqGrid{grid-template-columns:1fr!important}.support-intro,.faqAside{position:static!important}
}
@media(max-width:780px){
  .routeStrip .wrap{grid-template-columns:1fr!important}.route{min-height:auto!important;padding:22px!important}.route strong{margin:14px 0 7px!important}.cards,.priceGrid{grid-template-columns:1fr!important}.sectionHead{display:block!important}.sectionHead p{margin-top:16px!important;max-width:620px!important}.visualCaption{gap:14px}.visualCaption strong{font-size:16px!important}.waGrid{grid-template-columns:1fr!important}.whatsappBand .btn{width:100%}.footerTop{grid-template-columns:1fr 1fr!important}
}
@media(max-width:680px){
  html{scroll-padding-top:76px}body{font-size:15.5px;line-height:1.58}.wrap{width:calc(100% - 28px)!important;max-width:1220px}.utility,.topbar{display:none!important}
  .header,.site-header{height:70px!important}.identity img,.brand img{width:118px!important}.division{font-size:6.5px!important;letter-spacing:.13em!important}.nav .cta,.main-nav .cta{display:none!important}.nav.open .cta,.main-nav.open .cta{display:flex!important}.mobileMenu{width:44px;height:44px;border-radius:13px;font-size:21px}
  .hero{padding:46px 0 48px!important}.heroGrid{gap:28px!important}.hero h1,.pageHero h1,.proof-hero h1,.reviewHero h1,.desk-hero h1{font-size:clamp(40px,12vw,50px)!important;line-height:.96!important;letter-spacing:-.055em!important;overflow-wrap:normal;word-break:normal}.lede,.hero p,.pageHero p{font-size:16px!important;line-height:1.6!important}.kicker{font-size:11px;flex-wrap:wrap}.eyebrow{font-size:9px!important;letter-spacing:.14em!important}
  .actions,.hero-actions{display:grid!important;grid-template-columns:1fr!important;gap:9px!important;width:100%}.actions .btn,.hero-actions .btn,.btn.full{width:100%!important;min-height:52px!important;padding:0 16px!important}.btn{min-height:48px;font-size:9.5px!important;letter-spacing:.065em!important;text-align:center}
  .trustline{gap:10px 15px!important;font-size:11px!important}.visual{height:320px!important;border-radius:20px!important}.visualCaption{left:16px!important;right:16px!important;bottom:15px!important}.visualCaption small:last-child{display:none}.label{font-size:7px!important;padding:6px 7px!important}
  .section{padding:58px 0!important}.sectionHead{margin-bottom:28px!important}.sectionHead h2,.imageSplit .copy h2,.support-intro h2{font-size:clamp(35px,10vw,43px)!important;line-height:1!important;letter-spacing:-.05em!important}.card{min-height:auto!important;padding:20px!important;border-radius:16px!important}.card h3{font-size:22px!important;margin:27px 0 10px!important}.card p{font-size:14px!important}.card .link{padding-top:18px!important}.priceCard{padding:21px!important}.price{font-size:39px!important}
  .pageHero{padding:42px 0 44px!important}.pageHeroGrid{gap:26px!important}.pageHero .heroImage{height:230px!important;border-radius:18px!important}.breadcrumbs{font-size:10px!important;margin-bottom:13px!important}.serviceIntro{gap:30px!important}.serviceIntro .content{font-size:16px!important}.checklist{grid-template-columns:1fr!important}
  .imageSplit .copy{padding:48px 18px!important}.imageSplit .media{min-height:300px!important}.whatsappBand{padding:46px 0!important}.waGrid h3{font-size:32px!important}.waGrid p{font-size:14px!important}
  .footer{padding:52px 0 24px!important}.footerTop{gap:28px 20px!important}.footerLogo{width:155px!important}.footer a,.footer p{font-size:13px!important}.footerBottom{margin-top:34px!important;gap:9px!important;font-size:11px!important}
  .floatingWA{right:14px!important;bottom:max(14px,env(safe-area-inset-bottom))!important;width:52px!important;height:52px!important;padding:0!important;justify-content:center!important;border-radius:50%!important}.floatingWA span{display:none!important}.floatingWA:before{font-size:14px!important}
  input,select,textarea{font-size:16px!important}
  .support-form,.reviewCard,.case-card,.desk-card,.faqItem{max-width:100%!important}.form-grid{grid-template-columns:1fr!important}.support-form{padding:18px!important;border-radius:18px!important}.form-field input,.form-field select{min-height:52px!important}.form-field textarea{min-height:145px!important}.support-form .btn.full{min-height:56px!important}
  .reviewGrid,.case-grid,.desk-grid{grid-template-columns:1fr!important}.case-flow{grid-template-columns:1fr!important}.faqItem button{font-size:16px!important;padding:18px!important}.faqAnswer{padding:0 18px 18px!important}.faqSearch{font-size:16px!important;min-height:50px}.tableWrap{margin-left:0;margin-right:0;border-radius:14px!important}.tableWrap:after{content:'Swipe table →';display:block;padding:9px 12px;font-size:10px;color:#6c7884;background:#f5f7f9}
  h1,h2,h3,p,a,span,strong{overflow-wrap:break-word}.footer a,.footer p,.card p{word-break:normal}.footerContact p{overflow-wrap:anywhere}
}
@media(max-width:520px){
  .footerTop{grid-template-columns:1fr!important}.footerTop>div:first-child{grid-column:auto!important}.footerBottom{flex-direction:column!important}.hero h1,.pageHero h1,.proof-hero h1,.reviewHero h1,.desk-hero h1{font-size:clamp(38px,12vw,46px)!important}.visual{height:285px!important}.pageHero .heroImage{height:205px!important}.section{padding:52px 0!important}.route{padding:20px!important}.floatingWA{width:50px!important;height:50px!important}
}
@media(max-width:390px){
  .wrap{width:calc(100% - 22px)!important}.identity img,.brand img{width:108px!important}.division{display:none!important}.hero h1,.pageHero h1,.proof-hero h1,.reviewHero h1,.desk-hero h1{font-size:38px!important}.sectionHead h2,.imageSplit .copy h2,.support-intro h2{font-size:34px!important}.visual{height:260px!important}.card{padding:18px!important}.btn{font-size:9px!important}.support-form{padding:15px!important}
}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{scroll-behavior:auto!important;animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important}}
`;
document.head.appendChild(responsiveStyle);

const ADA_FAVICON='https://andreas-digital-agency.vercel.app/brand/ADA-favicon.png?v=4';let favicon=document.querySelector("link[rel~='icon']");if(!favicon){favicon=document.createElement('link');favicon.rel='icon';favicon.type='image/png';document.head.appendChild(favicon)}favicon.href=ADA_FAVICON;let touch=document.querySelector("link[rel='apple-touch-icon']");if(!touch){touch=document.createElement('link');touch.rel='apple-touch-icon';document.head.appendChild(touch)}touch.href=ADA_FAVICON;
const path=location.pathname.replace(/\/$/,'')||'/';
const isAdmin=path==='/tech-publisher';
if(!isAdmin){
  const navMarkup='<a href="/services">Services</a><a href="/problems">Problems</a><a href="/work">Work</a><a href="/pricing">Pricing</a><a href="/about">About</a><a class="cta nav-support" href="/support">Get Support</a><span class="mobileMenu" role="button" tabindex="0" aria-label="Open navigation" aria-expanded="false">☰</span>';
  document.querySelectorAll('nav.nav, nav.main-nav').forEach(n=>n.innerHTML=navMarkup);
  if(path.startsWith('/problems/')&&!document.querySelector('[data-problem-conversion]')){const f=document.querySelector('footer');if(f){const s=document.createElement('section');s.className='whatsappBand';s.dataset.problemConversion='1';s.innerHTML='<div class="wrap waGrid"><div><div class="eyebrow" style="color:#dbe9ff">Still happening?</div><h3>Stop guessing at the cause.</h3><p>Standard device diagnosis starts at N$120 and can be waived when approved repair/service of N$350+ follows.</p></div><a class="btn" href="/support">Request diagnostic →</a></div>';f.before(s)}}
  const toggleMenu=m=>{const n=m.closest('nav');if(!n)return;const open=!n.classList.contains('open');n.classList.toggle('open',open);m.setAttribute('aria-expanded',String(open));m.setAttribute('aria-label',open?'Close navigation':'Open navigation');m.textContent=open?'×':'☰'};
  document.querySelectorAll('.mobileMenu').forEach(m=>{m.addEventListener('click',()=>toggleMenu(m));m.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();toggleMenu(m)}});const n=m.closest('nav');n?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{n.classList.remove('open');m.setAttribute('aria-expanded','false');m.textContent='☰'}))});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')document.querySelectorAll('nav.open').forEach(n=>{n.classList.remove('open');const m=n.querySelector('.mobileMenu');if(m){m.setAttribute('aria-expanded','false');m.textContent='☰'}})});
  window.addEventListener('resize',()=>{if(innerWidth>1020)document.querySelectorAll('nav.open').forEach(n=>n.classList.remove('open'))},{passive:true});
}
const vids=[...document.querySelectorAll('video')];if('IntersectionObserver'in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.play().catch(()=>{});else e.target.pause()}),{threshold:.12});vids.forEach(v=>io.observe(v))}
