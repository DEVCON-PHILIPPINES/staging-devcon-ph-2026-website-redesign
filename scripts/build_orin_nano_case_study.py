# DEVCON Studios x NVIDIA Jetson Orin Nano case study (v2.08): new page, hub card, sitemap, url map, llms, single-file build
import re, glob, json, os
from urllib.parse import quote
os.chdir('/home/claude/repo')
SLUG_PATH = 'case-studies/devcon-studios-nvidia-orin-nano'
SPA = 'orin-nano'
TITLE = 'DEVCON Studios x NVIDIA Jetson Orin Nano: Building Kai in Public | Case Study'
DESC = ('How DEVCON Studios and Cohort 4 AI Engineering Interns turned an NVIDIA Jetson Orin Nano Developer Kit into Kai, a fully offline edge AI robot, '
        'and built it in public from unboxing to R&D showcase. A model for telling builder stories with partner technology.')
COLLAB = 'mailto:hello@devcon.ph?subject=' + quote('Collaborate with DEVCON Studios: build in public with our tech')

def page_html(mode):
    """mode 'docs' = folder page links; 'spa' = single-file hash links"""
    def L(key):
        docs = {'partner': '../../partner/', 'internships': '../../programs/jumpstart-internships/', 'hermes-camp': '../hermes-agentic-code-camp/',
                'case-studies': '../', 'devcon-kids': '../../programs/kids/', '17years': '../../about/17years/', 'educators': '../../programs/educators/',
                'mindanao-ai-caravan': '../mindanao-ai-caravan/', 'sui': '../sui/', 'microbit': '../microbit/', 'ai-physical-computing': '../ai-physical-computing-educators/',
                'hour-of-ai': '../hour-of-ai/'}
        return docs[key] if mode == 'docs' else '#/' + key
    import base64 as _b
    def M(f):
        if mode == 'docs': return f'media/{f}'
        path = f'docs/{SLUG_PATH}/media/{f}'
        if f.endswith(('.mp4','.webm')): return f'https://prod-devcon-ph-2026-website-redesign.pages.dev/{SLUG_PATH}/media/{f}'
        mime = 'image/webp' if f.endswith('.webp') else 'image/jpeg'
        return f'data:{mime};base64,' + _b.b64encode(open(path, 'rb').read()).decode()
    def fig(f, alt, cap=None, cls='', credit=None):
        c = f'<figcaption>{cap or ""}{" <span class=\'kai-credit\'>" + credit + "</span>" if credit else ""}</figcaption>' if (cap or credit) else ''
        return f'<figure class="cs-fig {cls}"><img src="{M(f)}" alt="{alt}" loading="lazy"/>{c}</figure>'
    def short(vid, title, step, h, p):
        return (f'<li class="kai-ep"><span class="kai-step">{step}</span><div class="yt-frame yt-frame--short"><iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0&amp;modestbranding=1" '
                f'title="{title}" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
                f'<b>{h}</b><span>{p}</span><a href="https://www.youtube.com/shorts/{vid}" target="_blank" rel="noopener">Watch on YouTube<span class="sr-only"> (opens in a new tab)</span></a></li>')
    def clip(f, h, p):
        return (f'<li><video poster="{M(f + ".jpg")}" muted loop playsinline autoplay preload="metadata" aria-label="{h}"><source src="{M(f + ".webm")}" type="video/webm"/><source src="{M(f + ".mp4")}" type="video/mp4"/></video>'
                f'<b>{h}</b><span>{p}</span></li>')
    stat = lambda b, s, c: f'<li class="num-item" style="--c:{c}"><b>{b}</b><span>{s}</span></li>'
    disc = [('hermes-camp', 'Hermes Agentic Code Camp and Hackathon', 'First in the Philippines: two weeks to national beta, 30+ builders shipped agents'),
            ('mindanao-ai-caravan', 'Mindanao AI Caravan', 'Free AI education for kids, teachers, and builders in Bukidnon and Iligan'),
            ('microbit', 'micro:bit case study', '44 code camps; 86% of students more confident in coding'),
            ('ai-physical-computing', 'AI and Physical Computing for Educators', '95 educators from 32 schools built AI models and micro:bit prototypes'),
            ('sui', 'Sui × DEVCON: Build Beyond', '330+ Move smart contracts verified on mainnet'),
            ('hour-of-ai', 'Hour of AI for Kids', '3.8k kids introduced to AI and coding, nationwide')]
    disc_html = ''.join(f'<li><a class="disc-card" href="{L(k)}"><b>{t}</b><span>{r}</span><em>Read the case study</em></a></li>' for k, t, r in disc)
    hidden = ' hidden' if mode == 'spa' else ''
    return f'''<div class="page" data-page="{SPA}"{hidden}>
  <header class="page-hero page-hero--apc">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{'../../' if mode == 'docs' else '#/'}">Home</a><span aria-hidden="true">/</span><a href="{L('case-studies')}">DevRel Case Studies</a><span aria-hidden="true">/</span><span aria-current="page">DEVCON Studios x NVIDIA</span></nav>
      <span class="eyebrow" style="color:var(--y)">Partner case study · DEVCON Studios x NVIDIA Jetson Orin Nano</span>
      <h1 id="{SPA}-title">From unboxing to R&amp;D showcase: building Kai in public on NVIDIA Jetson Orin Nano</h1>
      <p class="cs-years"><span>2026 · Beta at DEVCON 17</span></p>
      <p class="cr-built"><span>Built on</span><b class="kai-chip">NVIDIA Jetson Orin Nano</b><b class="kai-chip kai-chip--g">Google Gemma</b></p>
      <p class="page-lead">Our founder Winston Damarillo brought home an NVIDIA Jetson Orin Nano Developer Kit. Here&#8217;s what the DEVCON Studios team and our Cohort 4 AI Engineering Interns built with it, in public, and how we can tell builder stories with your tech.</p>
      <div class="hero-btns"><a class="btn-primary btn-xl" href="{COLLAB}">Collaborate with DEVCON Studios</a><a class="btn-outline" href="{L('partner')}">Sponsor the next one</a></div>
    </div>
  </header>

  <section class="section kai-open" style="padding-top:28px"><div class="wrap kai-duo">
    {fig('nvidia-devkit-box.webp', 'The NVIDIA Jetson Orin Nano Developer Kit board beside its retail box', 'Where it started: the NVIDIA Jetson Orin Nano Developer Kit.', credit='Image: NVIDIA')}
    {fig('kai-beta.webp', 'Kai, a cardboard robot with googly eyes and purple yarn pigtails, mirroring a face on the DEVCON 17 stage', 'Where it landed: Kai, the edge offline AI robot, at its DEVCON 17 beta launch.')}
  </div></section>

  <section class="numbers" aria-labelledby="kai-num"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">What your tech gets with DEVCON Studios</span><h2 id="kai-num">Built for real, built in public</h2>
      <p>One developer kit became a working robot, a content series, and a showcase at our 17th anniversary.</p></header>
    <ul class="numbers-grid" role="list">{stat('20+', 'Capabilities running on-device, from vision to voice', 'var(--y)')}{stat('100%', 'Offline: no cloud, no internet, no data leaving the room', 'var(--g)')}{stat('11', 'Face parameters tracked every frame', 'var(--p2)')}{stat('4', 'Build-in-public Shorts, from unboxing to showcase', 'var(--o)')}</ul>
  </div></section>

  <section class="section" aria-labelledby="kai-watch"><div class="wrap">
    <header class="sec-head yt-head"><span class="eyebrow" style="color:var(--y)">Build in public</span><h2 id="kai-watch">From unboxing to R&amp;D showcase, in four Shorts</h2>
      <p>DEVCON Studios filmed the journey as it happened, so the community followed the build, not just the launch.</p></header>
    <ol class="kai-eps" role="list">
      {short('VIEh8Wy3oEA', 'We are exploring the NVIDIA Jetson Orin Nano', '01', 'Unboxing and first look', 'Exploring the NVIDIA Jetson Orin Nano for the first time.')}
      {short('6WFQfZ0RLDk', 'This is what Edge AI engineering actually looks like', '02', 'Edge AI engineering, for real', 'What building on-device AI actually looks like day to day.')}
      {short('XkiajuFTPbQ', 'We surprised our AI Engineering Interns with a quick interview', '03', 'Meet the builders', 'A surprise interview with our AI Engineering Interns.')}
      {short('zQSmjp5M90k', 'When studying AI engineering feels like a celebration', '04', 'The showcase', 'When studying AI engineering feels like a celebration.')}
    </ol>
  </div></section>

  <section class="section band2" aria-labelledby="kai-meet"><div class="wrap cs-split kai-meet">
    {fig('meet-kai.webp', 'Meet Kai infographic: powered by Jetson Orin Nano for edge offline AI and Google Gemma for open-source LLM; a chest camera scans you; turn your head and open your mouth and she mirrors your face; works offline, faster, more private, uses less power', None, 'kai-poster')}
    <div>
      <span class="eyebrow" style="color:var(--y)">Meet Kai</span>
      <h2 class="cs-h2">An edge offline AI robot that sees, listens, and responds</h2>
      <p class="lead-p">Kai thinks, sees, and responds entirely on the device. No cloud, no internet, and no data leaving the room. Turn your head, open your mouth, and Kai mirrors your face in real time.</p>
      <ul class="doc-list">
        <li><b>Sees you:</b> a chest camera tracks 11 face parameters per frame, plus gestures (nod, shake, proximity) and a lightweight emotion read.</li>
        <li><b>Talks with you:</b> Google Gemma runs locally as Kai&#8217;s conversational layer, with speech-to-text in Tagalog and English and a spoken reply synced to a moving jaw.</li>
        <li><b>Knows your documents:</b> offline document Q&amp;A over text, Markdown, and PDF files.</li>
        <li><b>Private by design:</b> facial data is processed in memory only, never stored or sent, and people are told before tracking starts.</li>
      </ul>
    </div>
  </div></section>

  <section class="section" aria-labelledby="kai-log"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Build log</span><h2 id="kai-log">From one servo to a robot with a personality</h2>
      <p>Three moments from the R&amp;D, straight from the team&#8217;s phones.</p></header>
    <ol class="kai-clips" role="list">
      {clip('01-servo-test', 'First servo test', 'Face tracking on the Jetson drives a single servo for the first time.')}
      {clip('02-cardboard-prototype', 'Cardboard prototype', 'The head turns and the mouth opens, mirroring a face on screen.')}
      {clip('03-kai-beta', 'Kai, beta', 'Eyes, pigtails, and all: smooth head and jaw movement, ready for the stage.')}
    </ol>
  </div></section>

  <section class="section band2" aria-labelledby="kai-stack"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Technical depth</span><h2 id="kai-stack">What the NVIDIA Jetson Orin Nano made possible</h2>
      <p>The Jetson&#8217;s NVIDIA Ampere GPU, with 1,024 CUDA cores and 32 Tensor Cores, and 8 GB of memory, carried vision, language, voice, and robotics at once, fully offline.</p></header>
    <div class="cs-split kai-stack-top">
      {fig('nvidia-devkit-board.webp', 'Close-up of the NVIDIA Jetson Orin Nano Developer Kit board with its cooling fan', None, credit='Image: NVIDIA')}
      <ul class="kai-stack" role="list">
        <li><b>Vision</b><span>GPU face detection, YOLOv8 object detection, an 11-parameter face-tracking pipeline, gestures, and emotion.</span></li>
        <li><b>Language</b><span>Google Gemma and Qwen3 running locally through Ollama, plus offline document Q&amp;A.</span></li>
        <li><b>Voice</b><span>faster-whisper speech-to-text in Tagalog and English, and spoken replies with jaw sync.</span></li>
        <li><b>Robotics</b><span>An Arduino Uno and servos over local Wi-Fi at 30+ updates a second, smoothed for natural movement.</span></li>
        <li><b>Reliability</b><span>Tuned for the 8 GB board, with a camera fallback chain so Kai degrades gracefully instead of crashing.</span></li>
      </ul>
    </div>
    <div class="merge-block">
      <h3 class="sub-h">Why edge offline AI</h3>
      <ul class="kai-why" role="list"><li><b>Works offline</b><span>Anywhere, even without internet</span></li><li><b>Faster responses</b><span>No round trip to the cloud</span></li><li><b>More privacy</b><span>Faces never leave the device</span></li><li><b>Uses less power</b><span>A compact edge computer</span></li><li><b>Better for our planet</b><span>Efficient models, local compute</span></li></ul>
    </div>
  </div></section>

  <section class="section" aria-labelledby="kai-next"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">What&#8217;s next</span><h2 id="kai-next">From face tracking to a robot that moves on its own</h2>
      <p>Kai launched as a beta at DEVCON&#8217;s 17th anniversary. The roadmap goes deeper into the NVIDIA stack.</p></header>
    <div class="kai-road">
      <div><h3 class="sub-h">Next up</h3><ul class="doc-list"><li><b>Untethered:</b> battery power, so Kai runs anywhere.</li><li><b>Face-aware conversation:</b> Kai turns toward whoever is speaking.</li><li><b>TensorRT:</b> faster, leaner face tracking on the Jetson&#8217;s deep learning accelerator.</li></ul></div>
      <div><h3 class="sub-h">On the wishlist</h3><ul class="doc-list"><li><b>NVIDIA Isaac Sim:</b> train and test Kai in a simulated world first.</li><li><b>NVIDIA Omniverse:</b> a real-time digital twin of Kai.</li><li><b>Multi-face tracking, ROS 2, and a &#8220;Hey Kai&#8221; wake word.</b></li></ul></div>
    </div>
  </div></section>

  <section class="section band2" aria-labelledby="kai-partner"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">For hardware and platform partners</span><h2 id="kai-partner">How we tell builder stories with your tech</h2>
      <p>DEVCON Studios pairs your hardware or platform with real builders, then tells the story as it happens, to a community in 13 locations nationwide.</p></header>
    <ol class="cr-how" role="list"><li><b>Send us your tech</b><span>A developer kit, a board, a platform, or an API.</span></li><li><b>Our builders go hands-on</b><span>AI Engineering Interns run real R&amp;D, documented as they go.</span></li><li><b>DEVCON Studios tells the story</b><span>Build-in-public Shorts, from unboxing to showcase.</span></li><li><b>We showcase it nationwide</b><span>Live demos at DEVCON events, and workshops for students and educators.</span></li></ol>
    <p class="kai-links">Our builders come from <a class="pp-link" href="{L('internships')}">Jumpstart Internships</a>, and the same hands-on model powers our <a class="pp-link" href="{L('hermes-camp')}">Hermes Agentic Code Camp</a>.</p>
  </div></section>

  <section class="section cr-partner-call" aria-labelledby="kai-pc"><div class="wrap" style="text-align:center;max-width:980px">
    <span class="eyebrow" style="color:var(--y)">Collaborate with DEVCON Studios</span><h2 id="kai-pc">Put your tech in builders&#8217; hands, and let us tell the story</h2>
    <p>Hardware makers, AI labs, and platforms: send us your tech and our builders will build with it in public, from unboxing to showcase, in front of the country&#8217;s largest volunteer tech community.</p>
    <div class="hero-btns" style="justify-content:center"><a class="btn-primary btn-xl" href="{COLLAB}">Collaborate with DEVCON Studios</a><a class="btn-outline" href="{L('partner')}">See partnership options</a></div>
  </div></section>

  <section class="section band2 cs-discover" aria-labelledby="{SPA}-discover"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">More results</span><h2 id="{SPA}-discover">Discover other case studies and impactful results</h2></header>
    <ul class="disc-grid" role="list">{disc_html}</ul>
    <p style="margin-top:18px"><a class="pp-link" href="{L('case-studies')}">See all DevRel case studies</a></p>
  </div></section>

  <section class="page-cta">
    <div class="wrap">
      <h2>Sponsor the next one</h2>
      <p>Help scale build-in-public hardware R&amp;D nationally, across 13 locations and beyond the capital.</p>
      <div class="programs-cta"><a class="btn-primary btn-xl" href="{L('partner')}">Sponsor the next one</a><a class="btn-outline" href="mailto:hello@devcon.ph?subject={quote('Help scale build-in-public hardware R&D nationally')}">Help scale this program nationally</a></div>
    </div>
  </section>
</div>
'''

CSS = ('.kai-duo{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:16px;align-items:stretch}.kai-duo .cs-fig{margin:0;height:100%}.kai-duo .cs-fig img{width:100%;height:100%;max-height:520px;object-fit:cover}'
       '.kai-credit{opacity:.7;font-size:.78rem;margin-left:6px}'
       '.kai-chip{display:inline-flex;align-items:center;min-height:30px;padding:3px 12px;border-radius:999px;background:rgba(118,185,0,.16);border:1px solid rgba(118,185,0,.6);color:#B8E86A;font-size:.85rem}.kai-chip--g{background:rgba(77,162,255,.14);border-color:rgba(77,162,255,.55);color:#9DCBFF}'
       '.kai-eps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}'
       '.kai-ep{display:flex;flex-direction:column;gap:8px;text-align:center}.kai-ep .yt-frame--short{max-width:none;width:100%}'
       '.kai-step{color:var(--y);font-weight:900;letter-spacing:.08em}.kai-ep b{color:#fff;font-weight:900}.kai-ep span{color:var(--text-secondary);font-size:.9rem;line-height:1.45}'
       '.kai-ep a{display:inline-flex;align-items:center;justify-content:center;min-height:44px;color:var(--y);font-weight:800;text-decoration:underline}'
       '.kai-meet{grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr)}.kai-poster{margin:0}.kai-poster img{border-radius:20px}'
       '.kai-clips{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}'
       '.kai-clips li{display:flex;flex-direction:column;gap:6px}.kai-clips video{width:100%;aspect-ratio:9/16;object-fit:cover;border-radius:18px;border:1px solid var(--line);background:#000}'
       '.kai-clips b{color:#fff;font-weight:900}.kai-clips span{color:var(--text-secondary);font-size:.9rem;line-height:1.45}'
       '.kai-stack-top{align-items:center}.kai-stack-top .cs-fig{margin:0}'
       '.kai-stack{list-style:none;margin:0;padding:0;display:grid;gap:10px}.kai-stack li{padding:14px 16px;border-radius:14px;background:rgba(255,255,255,.04);border:1px solid var(--line);border-left:4px solid #76B900}'
       '.kai-stack b{display:block;color:#fff}.kai-stack span{color:var(--text-secondary);font-size:.92rem;line-height:1.5}'
       '.kai-why{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}.kai-why li{padding:14px;border-radius:14px;background:rgba(255,255,255,.04);border:1px solid var(--line);text-align:center}'
       '.kai-why b{display:block;color:var(--y)}.kai-why span{color:var(--text-secondary);font-size:.86rem}'
       '.kai-road{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}.kai-links{margin-top:18px;color:var(--text-secondary)}'
       '@media (max-width:1000px){.kai-eps{grid-template-columns:repeat(2,minmax(0,1fr))}.kai-why{grid-template-columns:repeat(2,minmax(0,1fr))}}'
       '@media (max-width:760px){.kai-duo,.kai-meet,.kai-road{grid-template-columns:minmax(0,1fr)}.kai-clips{grid-template-columns:minmax(0,1fr);max-width:360px;margin:0 auto}}'
       '@media (max-width:520px){.kai-eps{grid-template-columns:minmax(0,1fr);max-width:320px;margin:0 auto}}')

CARD = lambda href: f'''<article class="case" id="{SPA}-card" style="--c:#76B900">
        <div class="case-main">
          <div class="case-top"><span class="case-ic" aria-hidden="true"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="5" width="14" height="14" rx="2"/><path d="M9 9h6v6H9zM9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></svg></span><span class="prog-tag">DEVCON Studios · NVIDIA Jetson Orin Nano</span></div>
          <h2><a class="case-title-link" href="{href}">From unboxing to R&amp;D showcase: building Kai in public on NVIDIA Jetson Orin Nano</a></h2><p class="cs-years"><span>2026 · Beta at DEVCON 17</span></p>
          <div class="case-block"><h3>The goal</h3><p>Show what one developer kit can become in builders&#8217; hands, and tell that story in public.</p></div>
          <div class="case-block"><h3>What we did</h3><p>Cohort 4 AI Engineering Interns turned an NVIDIA Jetson Orin Nano into Kai, a fully offline AI robot that sees, listens, and talks, while DEVCON Studios filmed the build from unboxing to showcase.</p><p><a class="pp-link" href="{href}">Read the full case study</a></p></div>
        </div>
        <aside class="case-results" aria-label="Results"><p class="case-results-h">Results</p><ul role="list"><li><b>20+</b><span>on-device capabilities</span></li><li><b>100%</b><span>offline, private by design</span></li><li><b>4</b><span>build-in-public Shorts</span></li></ul></aside>
      </article>
      '''

# ---------- 1) new folder page, from the Hermes page as the template ----------
src = open('docs/case-studies/hermes-agentic-code-camp/index.html', encoding='utf-8').read()
old_title = re.search(r'<title>([^<]*)</title>', src).group(1)
old_desc = re.search(r'<meta name="description" content="([^"]*)"', src).group(1)
a = src.index('<div class="page" data-page="hermes-camp"'); b = src.index('</main>')
out = src[:a] + page_html('docs') + src[b:]
out = out.replace(old_title, TITLE).replace(old_desc, DESC)
out = out.replace('https://devcon.ph/case-studies/hermes-agentic-code-camp/', f'https://devcon.ph/{SLUG_PATH}/')
out = out.replace('</style>', CSS + '</style>', 1)
open(f'docs/{SLUG_PATH}/index.html', 'w', encoding='utf-8').write(out)

# ---------- 2) hub card first ----------
f = 'docs/case-studies/index.html'; h = open(f, encoding='utf-8').read()
h = re.sub(r'<article class="case" id="orin-nano-card".*?</article>\s*', '', h, flags=re.S); h = h.replace(CSS, '')
if True:
    i = h.index('<article class="case"'); h = h[:i] + CARD('devcon-studios-nvidia-orin-nano/') + h[i:]
    h = h.replace('</style>', CSS + '</style>', 1)
open(f, 'w', encoding='utf-8').write(h)

# ---------- 3) single-file build: page + hub card + CSS ----------
c = glob.glob('combined/*.html')[0]; t = open(c, encoding='utf-8').read()
t = re.sub(r'<div class="page" data-page="orin-nano".*?</div>\n(?=</main>|<div class="page")', '', t, flags=re.S); t = re.sub(r'<article class="case" id="orin-nano-card".*?</article>\s*', '', t, flags=re.S); t = t.replace(CSS, '')
if True:
    i = t.index('</main>'); t = t[:i] + page_html('spa') + t[i:]
    a = t.index('<div class="page" data-page="case-studies"'); j = t.index('<article class="case"', a)
    t = t[:j] + CARD(f'#/{SPA}') + t[j:]
    t = t.replace('</style>', CSS + '</style>', 1)
    # copy media next to the single file so the download works offline too
open(c, 'w', encoding='utf-8').write(t)

# ---------- 4) sitemap, url map, llms ----------
sm = open('docs/sitemap.xml').read()
if SLUG_PATH not in sm:
    sm = sm.replace('</urlset>', f'  <url><loc>https://devcon.ph/{SLUG_PATH}/</loc><lastmod>2026-10-12</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n</urlset>')
    open('docs/sitemap.xml', 'w').write(sm)
um = json.load(open('docs/url-map.json'))
if f'/{SLUG_PATH}/' not in um['pages']: um['pages'] = sorted(um['pages'] + [f'/{SLUG_PATH}/'])
json.dump(um, open('docs/url-map.json', 'w'), indent=1)
ll = open('docs/llms.txt').read()
if SLUG_PATH not in ll:
    ll = ll.replace('- [Hermes Agentic Code Camp and Hackathon]', f'- [DEVCON Studios x NVIDIA Jetson Orin Nano](https://devcon.ph/{SLUG_PATH}/): Kai, an edge offline AI robot built in public\n- [Hermes Agentic Code Camp and Hackathon]', 1)
    open('docs/llms.txt', 'w').write(ll)
print('page, hub card, single-file build, sitemap, url map, llms updated')
