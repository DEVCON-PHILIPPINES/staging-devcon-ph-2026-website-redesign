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

def _page_html(mode):
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
        return (f'<li class="kai-ep"><span class="kai-step">{step}</span><div class="yt-frame yt-frame--short"><iframe src="https://www.youtube-nocookie.com/embed/{vid}?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0&amp;modestbranding=1" '
                f'title="{title}" loading="lazy" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
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
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{'../../' if mode == 'docs' else '#/'}">Home</a><span aria-hidden="true">/</span><a href="{L('case-studies')}">Partner Success Stories</a><span aria-hidden="true">/</span><span aria-current="page">DEVCON Studios x NVIDIA</span></nav>
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
    <ul class="numbers-grid" role="list">{stat('Up to 67', 'TOPS of AI compute on JetPack 6.2, in the palm of your hand', 'var(--y)')}{stat('8 GB', 'Shared memory for vision, voice, and the LLM at once', 'var(--g)')}{stat('10–15 W', 'Power draw: runs off a powerbank, untethered', 'var(--p2)')}{stat('1,300+', 'Tests in the open-source repo, no hardware needed', 'var(--o)')}</ul>
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
        <li><b>Sees you:</b> MediaPipe FaceMesh tracks 11 facial parameters in real time, from a 320 by 240 camera feed.</li>
        <li><b>Follows you:</b> a PD controller glides the head to whoever is in front of it, at 15 updates a second.</li>
        <li><b>Talks with you:</b> wakes on &#8220;Hey Kai&#8221;, turns speech to text with Whisper, answers from its own documents with Google Gemma, and speaks with Piper, jaw in sync.</li>
        <li><b>Private by design:</b> every workload runs on the device, with no cloud and no API keys on the path. Facial data is processed in memory only, and people are told before tracking starts.</li>
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
    <div class="merge-block">
      <h3 class="sub-h">Behind the scenes: what the highlight reel doesn&#8217;t show</h3>
      <div class="kai-bts">
        {fig('bts-tracker.webp', 'Debugging the face tracker: a servo in hand in front of a laptop running the tracking code', 'Debugging the tracker.')}
        {fig('bts-servos.webp', 'Fitting servos by hand into the cardboard prototype in front of a laptop', 'Fitting servos by hand.')}
      </div>
      <ul class="kai-chal" role="list">
        <li><b>3.3 V won&#8217;t drive a servo</b><span>Jetson GPIO tops out at 3.3 V and SG90s need about 5 V, so an Arduino became the bridge.</span></li>
        <li><b>A dead servo mid-build</b><span>A faulty servo can buzz but not turn, leaving only one working servo.</span></li>
        <li><b>Missing wires, day one</b><span>The first hardware test moved a day because parts weren&#8217;t checked beforehand.</span></li>
        <li><b>Brownouts drop the link</b><span>Servos share the USB 5 V rail, and commands that are too fast can drop the connection.</span></li>
      </ul>
    </div>
  </div></section>

  <section class="section" aria-labelledby="kai-platform"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">The platform</span><h2 id="kai-platform">What is the Jetson Orin Nano?</h2>
      <p>NVIDIA&#8217;s smallest edge-AI developer kit: a full computer the size of a paperback that runs modern neural networks locally, on the same CUDA, cuDNN, and TensorRT stack used in production edge deployments.</p></header>
    <div class="cs-split kai-plat">
      <ul class="kai-specs" role="list">
        <li><b>1,024-core Ampere GPU</b><span>Plus 32 Tensor Cores and a dedicated deep learning accelerator (DLA).</span></li>
        <li><b>Up to 67 TOPS (INT8)</b><span>Vision, speech, and an LLM at once. Full performance needs JetPack 6.2; earlier releases cap at 40.</span></li>
        <li><b>8 GB LPDDR5, 102 GB/s</b><span>One shared pool for the CPU and GPU: the real ceiling for what fits.</span></li>
        <li><b>6-core Arm Cortex-A78AE</b><span>The regular computer half, running Linux and the app code.</span></li>
        <li><b>7 to 25 W, 5 nm</b><span>Sips power: Kai runs off a powerbank, no wall socket needed.</span></li>
      </ul>
      {fig('devkit-layout.webp', 'Labeled layout of the Jetson Orin Nano Developer Kit: cooling fan, power button, CSI camera interfaces, USB, DisplayPort, Ethernet, 40-pin GPIO, and M.2 slots', 'The developer kit, port by port.', credit='Diagram: NVIDIA')}
    </div>
    <p class="kai-stackline"><span>The NVIDIA compute stack, all on one 8 GB module:</span><b>Ampere GPU</b><b>DLA</b><b>CUDA</b><b>TensorRT</b><b>cuDNN</b></p>
  </div></section>

  <section class="section" aria-labelledby="kai-edge"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Why edge</span><h2 id="kai-edge">Edge offline AI versus the cloud</h2></header>
    <div class="tbl-wrap"><table class="reach-tbl kai-tbl"><caption>Cloud AI compared with edge AI on the Orin Nano</caption><thead><tr><th scope="col">Cloud AI</th><th scope="col">Edge AI on the Orin Nano</th></tr></thead><tbody>
      <tr><td>Needs constant internet</td><td>Works fully offline, anywhere</td></tr>
      <tr><td>Latency from network round trips</td><td>Real time, with no network hop</td></tr>
      <tr><td>Data leaves the room</td><td>Nothing ever leaves the device</td></tr>
      <tr><td>Fails where connectivity is poor</td><td>Works from a smart city to a far barangay</td></tr></tbody></table></div>
    <p class="kai-builders"><b>For builders:</b> ship into venues, clinics, and far barangays with no per-call cost and no data leaving the room. The deployment target is a box you own, not an API you rent.</p>
  </div></section>

  <section class="section" aria-labelledby="kai-arch"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Architecture</span><h2 id="kai-arch">How it all runs on 8 GB</h2>
      <p>Two independent pipelines run in one process, seeing and moving, and hearing and answering, sharing the jaw servo and the dashboard.</p></header>
    <div class="kai-pipes">
      <div><h3 class="sub-h">Seeing and moving</h3><ol class="kai-flow" role="list"><li><b>Camera</b><span>CSI or USB, 320 by 240</span></li><li><b>FaceMesh</b><span>15 fps, 11 parameters</span></li><li><b>PD control</b><span>Glides at 15 Hz</span></li><li><b>Servos</b><span>Pan and jaw, via Arduino</span></li></ol></div>
      <div><h3 class="sub-h">Hearing and answering</h3><ol class="kai-flow" role="list"><li><b>Mic and wake word</b><span>&#8220;Hey Kai&#8221;, voice detection</span></li><li><b>Whisper</b><span>Speech to text</span></li><li><b>RAG and Gemma</b><span>Answers from its documents</span></li><li><b>Piper TTS</b><span>Speaks, jaw in sync</span></li></ol></div>
    </div>
    <p class="kai-builders"><b>Why an Arduino?</b> It acts only as a 5 V bridge. The Jetson&#8217;s GPIO pins top out at 3.3 V, which SG90 servos can&#8217;t reliably read.</p>
  </div></section>

  <section class="section" aria-labelledby="kai-mem"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">The real constraint</span><h2 id="kai-mem">8 GB of shared memory is the ceiling</h2>
      <p>GPU memory comes out of the same 7.6 GB the operating system and every process use. It&#8217;s the tightest constraint in the system, and the one you discover by crashing into it.</p></header>
    <div class="cs-split kai-mem">
      <div><h3 class="sub-h">Memory budget, 7.6 GB total</h3><ul class="kai-bars" role="list">
        <li style="--w:32%;--c:#76B900"><b>Gemma 2 (2B) via Ollama</b><span>2.4 GB</span></li>
        <li style="--w:18%;--c:#4DA2FF"><b>Face tracking</b><span>1.4 GB</span></li>
        <li style="--w:4%;--c:#EA641D"><b>Compressed swap</b><span>0.3 GB</span></li>
        <li style="--w:28%;--c:#A57BFF"><b>Free, at steady state</b><span>2.1 GB</span></li></ul></div>
      <div><h3 class="sub-h">What it forces</h3><ul class="doc-list">
        <li><b>A 2B model, not bigger:</b> a 2 GB model stays resident; larger models push out the camera.</li>
        <li><b>Context capped at 2,048 tokens:</b> raising it to 4,096 crashes the model runner.</li>
        <li><b>Whisper on the CPU:</b> kept off CUDA to leave GPU memory for the LLM and vision.</li>
        <li><b>Embeddings on the CPU:</b> retrieval runs on the CPU so it can&#8217;t compete for the GPU.</li></ul></div>
    </div>
  </div></section>

  <section class="section" aria-labelledby="kai-expect"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Why it matters</span><h2 id="kai-expect">Expectations versus reality</h2>
      <p>Edge AI on 8 GB is a systems problem, not a model problem. Almost every win came from measuring what the hardware actually did, not from what the datasheet promised.</p></header>
    <div class="tbl-wrap"><table class="reach-tbl kai-tbl"><caption>What the team expected, and what actually happened</caption><thead><tr><th scope="col">What we expected</th><th scope="col">What actually happened</th></tr></thead><tbody>
      <tr><td>A bigger LLM would give smarter replies</td><td>A 4B model pushed out the camera. A 2B model is the largest that fits alongside vision in 8 GB.</td></tr>
      <tr><td>A longer context window would give longer memory</td><td>Going past 2,048 tokens crashes the runner. GPU residency, not RAM, is the wall.</td></tr>
      <tr><td>Voice noise settings would make Kai sound livelier</td><td>Measured: they changed intonation less than the noise floor. Hypothesis dropped and logged.</td></tr>
      <tr><td>The wake-word matcher was the weak link</td><td>Three bugs, none in the matcher. A 0.35-second floor was silently eating the word &#8220;hey&#8221;.</td></tr></tbody></table></div>
    <p class="kai-builders"><b>For builders:</b> don&#8217;t trust the datasheet; measure on your board. The project changelog records the dropped ideas too, so you inherit the dead ends instead of repeating them.</p>
  </div></section>

  <section class="section" aria-labelledby="kai-journey"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">The journey</span><h2 id="kai-journey">From first servo to a shipping robot</h2>
      <p>Built in eight weeks on one Orin Nano, then hardened live at events.</p></header>
    <ol class="tl-grid kai-journey" role="list">
      <li class="tl-phase" style="--c:#76B900"><span class="mh-when">Jun 2026 · Shipped</span><h3>Face tracking</h3><ul role="list"><li><b>FaceMesh pipeline and PD control</b><span>On a 15 Hz thread, with automatic USB driver loading.</span></li></ul></li>
      <li class="tl-phase" style="--c:#4DA2FF"><span class="mh-when">Jul 2026 · Shipped</span><h3>Voice and RAG</h3><ul role="list"><li><b>Push-to-talk speech to text</b><span>Gemma 2 (2B) with offline document Q&amp;A and an editable persona.</span></li></ul></li>
      <li class="tl-phase" style="--c:#A57BFF"><span class="mh-when">Late Jul 2026 · Shipped</span><h3>Hands-free</h3><ul role="list"><li><b>Piper voice and a &#8220;Hey Kai&#8221; wake word</b><span>An always-open mic, with the jaw synced to real audio.</span></li></ul></li>
      <li class="tl-phase" style="--c:#F2C500"><span class="mh-when">Aug 2026 · Ongoing</span><h3>Hardening</h3><ul role="list"><li><b>Crash relaunch and fixes</b><span>Idle loop cut from 185 to 22 Hz, jaw timing and dialect fixes, 1,300+ tests.</span></li></ul></li>
      <li class="tl-phase" style="--c:#EA641D"><span class="mh-when">Next · Planned</span><h3>CUDA and TensorRT</h3><ul role="list"><li><b>Move inference onto the GPU</b><span>To reclaim headroom for bigger workloads.</span></li></ul></li>
      <li class="tl-phase" style="--c:#EC4899"><span class="mh-when">Future</span><h3>Level 2 autonomy</h3><ul role="list"><li><b>From reacting to acting</b><span>Multi-face awareness and richer on-device reasoning.</span></li></ul></li>
    </ol>
  </div></section>

  <section class="section" aria-labelledby="kai-next"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">The handoff</span><h2 id="kai-next">Ideas for Cohort 5</h2>
      <p>Same board, same offline-first constraint, new problems worth solving. Each idea builds on something Kai already proved.</p></header>
    <ul class="pp-grid pp-grid--4" role="list">
      <li class="pp" style="--c:#76B900"><h3>Self-driving bot</h3><p>A line- and obstacle-following rover, with a micro:bit handling motors and sensors and the Jetson doing the vision.</p><span class="kai-builds">Builds on: the servo bridge and PD control</span></li>
      <li class="pp" style="--c:#4DA2FF"><h3>Taglish conversation</h3><p>Natural switching between Tagalog and English in one conversation, not two separate language modes.</p><span class="kai-builds">Builds on: RAG, persona, and delivery shaping</span></li>
      <li class="pp" style="--c:#F2C500"><h3>Bisaya voice</h3><p>Cebuano and Bisaya understanding tuned per chapter, beyond canned filler lines.</p><span class="kai-builds">Builds on: the dialect-aware filler bank</span></li>
      <li class="pp" style="--c:#EA641D"><h3>A Filipino voice</h3><p>Train a custom Filipino text-to-speech voice, since none ships for Tagalog, Filipino, or Cebuano today.</p><span class="kai-builds">Builds on: the Piper TTS pipeline</span></li>
    </ul>
    <p class="kai-links">Further out: NVIDIA Isaac Sim to train Kai in simulation first, and NVIDIA Omniverse for a real-time digital twin.</p>
  </div></section>

  <section class="section" aria-labelledby="kai-team"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">The team</span><h2 id="kai-team">Who built Kai, and how to build on it</h2>
      <p>Cohort 4 AI Engineering Interns, DEVCON Philippines.</p></header>
    <div class="kai-team">
      <ul class="kai-people" role="list">
        <li><img src="{M('team-rhea.webp')}" alt="Rhea Perocho" loading="lazy"/><b>Rhea Perocho</b><span class="kai-role">Design and build</span><span>Designed and built Kai&#8217;s physical form: the cardboard body, the head, and the look that gives Kai its character.</span></li>
        <li><img src="{M('team-jhondel.webp')}" alt="Jhondel Mellomida" loading="lazy"/><b>Jhondel Mellomida</b><span class="kai-role">Developer and hardware</span><span>Handled the electronics and code: wiring, servos, the Arduino bridge, and the software that makes Kai see, listen, and talk.</span></li>
      </ul>
      <div class="kai-oss">
        <span class="eyebrow" style="color:var(--y)">Open source</span>
        <h3 class="sub-h">Clone it, fork it, ship it</h3>
        <ul class="doc-list"><li><b>Apache-2.0 licensed</b></li><li><b>1,300+ tests</b>, runnable with no hardware</li><li>Every constant annotated with the measurement behind it</li><li>Full wiring, pinouts, and parts list in the docs</li></ul>
        <p><a class="btn-primary" href="https://github.com/Kai-Devcon/kai" target="_blank" rel="noopener">View Kai on GitHub<span class="sr-only"> (opens in a new tab)</span></a></p>
        <p class="kai-builders"><b>For builders:</b> reproduce this exact build, read why every number is what it is, and stand on the dead ends instead of repeating them.</p>
      </div>
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
    <p style="margin-top:18px"><a class="pp-link" href="{L('case-studies')}">See all partner success stories</a></p>
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

def page_html(mode):
    P = _page_html(mode)
    idx = [m.start() for m in re.finditer(r'\n  <section class="(?:section[^"]*|page-cta|numbers)"', P)]
    last = P.rindex('</section>') + len('</section>'); rows = [P[a:(idx[n + 1] if n + 1 < len(idx) else last)] for n, a in enumerate(idx)]
    k = next(n for n, r in enumerate(rows) if 'class="numbers"' in r[:80]); out = []
    for n, r in enumerate(rows):
        if n <= k or 'page-cta' in r[:60]: out.append(r); continue
        band = ((n - k - 1) % 2 == 1); o = re.match(r'\s*<section class="([^"]*)"', r); cls = re.sub(r'\s*\bband2\b', '', o.group(1))
        out.append(r.replace(f'class="{o.group(1)}"', f'class="{cls.replace("section", "section band2", 1) if band else cls}"', 1))
    return P[:idx[0]] + ''.join(out) + P[last:]

CSS = ('.kai-specs{list-style:none;margin:0;padding:0;display:grid;gap:10px}.kai-specs li{padding:14px 16px;border-radius:14px;background:rgba(255,255,255,.04);border:1px solid var(--line);border-left:4px solid #76B900}.kai-specs b{display:block;color:#fff}.kai-specs span{color:var(--text-secondary);font-size:.92rem;line-height:1.5}'
       '.kai-plat{align-items:center}.kai-plat .cs-fig{margin:0;background:#fff;border-radius:18px;padding:12px}.kai-plat .cs-fig img{border-radius:10px}.kai-plat figcaption{color:#333}'
       '.kai-stackline{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:20px;color:var(--text-secondary)}.kai-stackline b{display:inline-flex;align-items:center;min-height:32px;padding:3px 12px;border-radius:999px;background:rgba(118,185,0,.16);border:1px solid rgba(118,185,0,.55);color:#B8E86A;font-size:.85rem}'
       '.kai-tbl td,.kai-tbl th{text-align:left!important;vertical-align:top}.kai-tbl td:first-child{color:var(--text-secondary)}.kai-tbl td:last-child{color:#fff}'
       '.kai-builders{margin-top:16px;padding:14px 18px;border-radius:14px;background:rgba(118,185,0,.08);border:1px solid rgba(118,185,0,.4);color:#fff}.kai-builders b{color:#B8E86A}'
       '.kai-pipes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}.kai-flow{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;counter-reset:f}'
       '.kai-flow li{position:relative;padding:12px;border-radius:12px;background:rgba(255,255,255,.04);border:1px solid var(--line)}.kai-flow b{display:block;color:#fff;font-size:.92rem}.kai-flow span{color:var(--text-secondary);font-size:.8rem;line-height:1.4}'
       '.kai-bars{list-style:none;margin:0;padding:0;display:grid;gap:10px}.kai-bars li{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 10px;align-items:center}.kai-bars li::after{content:"";grid-column:1/-1;height:12px;border-radius:999px;background:linear-gradient(90deg,var(--c) var(--w),rgba(255,255,255,.08) var(--w))}.kai-bars b{color:#fff;font-size:.92rem}.kai-bars span{color:var(--text-secondary);font-weight:800;font-size:.86rem}'
       '.kai-journey{grid-template-columns:repeat(3,minmax(0,1fr))}'
       '.kai-bts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-bottom:14px}.kai-bts .cs-fig{margin:0}'
       '.kai-chal{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}.kai-chal li{padding:14px;border-radius:14px;background:rgba(255,255,255,.04);border:1px solid var(--line);border-top:3px solid #EC4899}.kai-chal b{display:block;color:#fff;margin-bottom:4px}.kai-chal span{color:var(--text-secondary);font-size:.88rem;line-height:1.45}'
       '.kai-builds{display:block;margin-top:auto;padding-top:8px;color:var(--y);font-size:.82rem;font-weight:800}'
       '.kai-team{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:24px;align-items:start}.kai-people{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}'
       '.kai-people li{display:flex;flex-direction:column;align-items:center;text-align:center;gap:6px;padding:20px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}.kai-people img{width:120px;height:120px;border-radius:50%;object-fit:cover;border:3px solid #76B900}'
       '.kai-people b{color:#fff;font-weight:900;font-size:1.05rem}.kai-role{color:var(--y);font-weight:800;font-size:.85rem}.kai-people span:last-child{color:var(--text-secondary);font-size:.9rem;line-height:1.5}'
       '.kai-oss{padding:20px;border-radius:18px;background:rgba(118,185,0,.06);border:1px solid rgba(118,185,0,.4)}'
       '@media (max-width:1000px){.kai-flow,.kai-chal{grid-template-columns:repeat(2,minmax(0,1fr))}.kai-journey{grid-template-columns:repeat(2,minmax(0,1fr))}.kai-pipes,.kai-team{grid-template-columns:minmax(0,1fr)}}'
       '@media (max-width:560px){.kai-flow,.kai-chal,.kai-journey,.kai-bts,.kai-people{grid-template-columns:minmax(0,1fr)}}'
       '.kai-duo{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:16px;align-items:stretch}.kai-duo .cs-fig{margin:0;height:100%}.kai-duo .cs-fig img{width:100%;height:100%;max-height:520px;object-fit:cover}'
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
