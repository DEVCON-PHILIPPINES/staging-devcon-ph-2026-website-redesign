# v2.20: AI Code Camps Barangay AI feature; case study filters and tags; chapter president as event director; Hermes Shorts
import re, glob, base64, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
COMBINED = glob.glob('combined/*.html')[0]
def seg(s, key):
    a = s.index(f'<div class="page" data-page="{key}"'); b = s.find('<div class="page"', a + 10)
    if b < 0 or s.find('</main>', a) < b: b = s.index('</main>', a)
    return a, b
def reband(P):
    idx = [m.start() for m in re.finditer(r'\n  <section class="(?:section[^"]*|page-cta|numbers)"', P)]
    last = P.rindex('</section>') + len('</section>'); rows = [P[a:(idx[n + 1] if n + 1 < len(idx) else last)] for n, a in enumerate(idx)]
    k = next(n for n, r in enumerate(rows) if 'class="numbers"' in r[:80]); out = []
    for n, r in enumerate(rows):
        if n <= k or 'page-cta' in r[:60]: out.append(r); continue
        band = ((n - k - 1) % 2 == 1); o = re.match(r'\s*<section class="([^"]*)"', r); cls = re.sub(r'\s*\bband2\b', '', o.group(1))
        out.append(r.replace(f'class="{o.group(1)}"', f'class="{cls.replace("section", "section band2", 1) if band else cls}"', 1))
    return P[:idx[0]] + ''.join(out) + P[last:]
def edit(path, key, fn, css=''):
    for f, mode in [(path, 'docs'), (COMBINED, 'spa')]:
        s = open(f, encoding='utf-8').read(); a, b = seg(s, key)
        s = s[:a] + fn(s[a:b], mode) + s[b:]
        if css and css not in s: s = s.replace('</style>', css + '</style>', 1)
        open(f, 'w', encoding='utf-8').write(s)
    print('edited', key)

# 1) AI Code Camps: Barangay AI as the major feature, right after the results
IMG = 'docs/programs/ai-code-camps/media/barangay-ai-models.webp'
def acc(P, mode):
    if 'acc-feature' in P: return P
    src = 'media/barangay-ai-models.webp' if mode == 'docs' else 'data:image/webp;base64,' + base64.b64encode(open(IMG, 'rb').read()).decode()
    sec = ('<section class="section acc-feature" aria-labelledby="acc-feature-t"><div class="wrap">'
           '<header class="sec-head yt-head"><span class="eyebrow" style="color:var(--y)">DEVCON Barangay AI · Free, open source, community-owned</span>'
           '<h2 id="acc-feature-t">Today you&#8217;re going to build your own AI</h2>'
           '<p>Not use someone else&#8217;s. Not pay for a subscription. Build one: name it, shape its personality, and deploy it live, in an afternoon.</p></header>'
           f'<figure class="acc-visual"><img src="{src}" alt="DEVCON Barangay AI: open-source models Qwen by Alibaba, Gemma by Google, Llama by Meta, Phi by Microsoft, Mistral, GPT-OSS by OpenAI, and Granite by IBM all connect through Ollama into the DEVCON chat app" width="862" height="522" loading="lazy"/></figure>'
           '<p class="acc-private"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/></svg>'
           '<span>The AI runs entirely on <b>your own computer</b>. No cloud, no API fees, no data leaving the room. It&#8217;s yours.</span></p>'
           '<p class="acc-models-cap">The app connects to any open-source model, served through Ollama or any OpenAI-compatible endpoint, all running free and offline.</p>'
           '</div></section>')
    j = P.index('</section>', P.index('<section class="numbers"')) + len('</section>')
    return reband(P[:j] + '\n  ' + sec + P[j:])
ACC_CSS = ('.acc-visual{max-width:960px;margin:0 auto;border-radius:24px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 80px rgba(0,0,0,.5)}.acc-visual img{display:block;width:100%;height:auto}'
           '.acc-private{display:flex;align-items:flex-start;gap:12px;max-width:960px;margin:18px auto 0;padding:16px 20px;border-radius:16px;background:rgba(165,123,255,.10);border:1px solid rgba(165,123,255,.45);color:#fff;line-height:1.55}'
           '.acc-private svg{flex:none;width:22px;height:22px;margin-top:2px;color:#C9B2FF}.acc-models-cap{max-width:760px;margin:14px auto 0;text-align:center;color:var(--text-secondary)}')
edit('docs/programs/ai-code-camps/index.html', 'ai-code-camps', acc, ACC_CSS)

# 2) DevRel Case Studies: categories, filters, tags
CATS = [('ai', 'AI and agentic'), ('kids', 'Kids and educators'), ('hardware', 'Hardware and edge AI'), ('web3', 'Web3 and blockchain'),
        ('camps', 'Code camps'), ('events', 'Events and summits'), ('lowcode', 'Low-code')]
CARDS = {'orin-nano-card': (['hardware', 'ai'], ['NVIDIA Jetson', 'Edge AI', 'Robotics', 'Build in public']),
         'hermes-camp-card': (['ai', 'camps', 'events'], ['Hermes Agent', 'MCP', 'Hackathon']),
         'educators-csta-card': (['kids'], ['Teacher training', 'micro:bit', 'CSTA']),
         'microbit-card': (['kids', 'hardware', 'camps'], ['micro:bit', 'Robotics', 'Schools']),
         'ai-physical-computing-card': (['kids', 'ai', 'hardware'], ['Teachable Machine', 'micro:bit', 'Educators']),
         'mindanao-ai-caravan-card': (['ai', 'kids', 'events'], ['Mindanao', 'Hour of AI', 'Hackathon']),
         'sui-devrel': (['web3', 'camps'], ['Sui Move', 'Smart contracts', 'Nationwide']),
         'icp-code-camps': (['web3', 'camps'], ['ICP', 'Smart contracts', 'Nationwide']),
         'hour-of-ai-card': (['kids', 'ai'], ['Hour of AI', 'DEVCON Kids', 'Schools']),
         'ai-code-camps': (['ai', 'camps'], ['Ollama', 'Open source', 'Local AI']),
         'zoho-creator-card': (['lowcode', 'camps'], ['Zoho Creator', 'Students']),
         'campus-summit-card': (['events'], ['Campus DEVCON', 'Student leaders']),
         'pro-summit-card': (['events'], ['Professionals', 'Tech for impact'])}
LABEL = dict(CATS)
BAR = ('<div class="cs-filter" role="group" aria-label="Filter case studies by category">'
       '<button type="button" class="cs-chip" data-filter="all" aria-pressed="true">All</button>' +
       ''.join(f'<button type="button" class="cs-chip" data-filter="{k}" aria-pressed="false">{v}</button>' for k, v in CATS) +
       '</div><p class="cs-count" aria-live="polite">Showing all case studies</p>')
JS = ('<script>(function(){var bar=document.querySelector(".cs-filter");if(!bar)return;var cards=[].slice.call(document.querySelectorAll(".case[data-cats]"));'
      'var out=document.querySelector(".cs-count");function set(f){var n=0;cards.forEach(function(c){var on=f==="all"||(" "+c.getAttribute("data-cats")+" ").indexOf(" "+f+" ")>-1;c.hidden=!on;if(on)n++;});'
      '[].forEach.call(bar.querySelectorAll(".cs-chip"),function(b){b.setAttribute("aria-pressed",b.getAttribute("data-filter")===f?"true":"false");});'
      'if(out)out.textContent=f==="all"?"Showing all "+n+" case studies":"Showing "+n+" of "+cards.length+" case studies";}'
      'bar.addEventListener("click",function(e){var b=e.target.closest(".cs-chip");if(b)set(b.getAttribute("data-filter"));});set("all");})();</script>')
def hub(P, mode):
    if 'cs-filter' in P: return P
    def rep(m):
        cid = m.group(1)
        if cid not in CARDS: return m.group(0)
        cats, tags = CARDS[cid]
        tag = m.group(0).replace(f'id="{cid}"', f'id="{cid}" data-cats="{" ".join(cats)}"', 1)
        return tag
    P = re.sub(r'<article class="case" id="([^"]+)"[^>]*>', rep, P)
    # tags under each card's results label
    for cid, (cats, tags) in CARDS.items():
        i = P.find(f'id="{cid}"')
        if i < 0: continue
        j = P.find('</h2>', i) + len('</h2>')
        chips = '<ul class="cs-tags" role="list">' + ''.join(f'<li class="cs-tag cs-tag--cat">{LABEL[c]}</li>' for c in cats) + ''.join(f'<li class="cs-tag">{t}</li>' for t in tags) + '</ul>'
        P = P[:j] + chips + P[j:]
    # filter bar before the first card
    k = P.index('<article class="case"'); w = P.rfind('<div', 0, k)
    P = P[:k] + BAR + '\n      ' + P[k:]
    return P.replace('</div>\n', '</div>\n', 1)
HUB_CSS = ('.cs-filter{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 6px}.cs-chip{display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border-radius:999px;border:1px solid var(--line);background:rgba(255,255,255,.04);color:#fff;font:inherit;font-weight:800;font-size:.9rem;cursor:pointer}'
           '.cs-chip:hover{border-color:var(--y)}.cs-chip[aria-pressed="true"]{background:var(--y);border-color:var(--y);color:#0b0840}.cs-chip:focus-visible{outline:3px solid var(--y);outline-offset:2px}'
           '.cs-count{margin:6px 0 18px;color:var(--text-secondary);font-size:.9rem}'
           '.cs-tags{list-style:none;margin:10px 0 4px;padding:0;display:flex;flex-wrap:wrap;gap:6px}.cs-tag{padding:3px 10px;border-radius:999px;background:rgba(255,255,255,.05);border:1px solid var(--line);color:var(--text-secondary);font-size:.78rem;font-weight:700}'
           '.cs-tag--cat{background:rgba(242,197,0,.12);border-color:rgba(242,197,0,.45);color:var(--y)}.case[hidden]{display:none!important}')
def hub_js(f):
    s = open(f, encoding='utf-8').read()
    if 'cs-filter")' not in s: s = s.replace('</body>', JS + '\n</body>', 1); open(f, 'w', encoding='utf-8').write(s)
edit('docs/case-studies/index.html', 'case-studies', hub, HUB_CSS)
hub_js('docs/case-studies/index.html'); hub_js(COMBINED)

# 3) Hackathon best practice: the chapter president is the event director
def guide(P, mode):
    R = [('<li class="mh-role" style="--c:#F2C500"><h3>Event director</h3>', '<li class="mh-role" style="--c:#F2C500"><h3>Event director: the chapter president</h3>'),
         ('<li><b>Form the core team</b><span>Name an event director and every lead in the roles section.</span></li>', '<li><b>Form the core team</b><span>The chapter president serves as event director and names every lead in the roles section.</span></li>'),
         ('DEVCON HQ sets the guardrails; the local team runs the day. One name per role, and every lead also names a backup.', 'DEVCON HQ sets the guardrails, and the chapter president leads the day as event director. One name per role, and every lead also names a backup.')]
    for o, n in R:
        if o in P: P = P.replace(o, n, 1)
    return P
edit('docs/playbook/hackathon-best-practice/index.html', 'hackathon-best-practice', guide)
b = open('scripts/build_masterclass_hackathon_guide.py').read()
b = b.replace("('Event director', '#F2C500',", "('Event director: the chapter president', '#F2C500',").replace("'Name an event director and every lead in the roles section.'", "'The chapter president serves as event director and names every lead in the roles section.'").replace('DEVCON HQ sets the guardrails; the local team runs the day.', 'DEVCON HQ sets the guardrails, and the chapter president leads the day as event director.')
open('scripts/build_masterclass_hackathon_guide.py', 'w').write(b)

# 4) Hermes case study: two Shorts, autoplay muted
def shorts(P, mode):
    if 'cr-shorts' in P: return P
    fr = lambda v, t: (f'<li><div class="yt-frame yt-frame--short"><iframe src="https://www.youtube-nocookie.com/embed/{v}?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0&amp;modestbranding=1" title="{t}" loading="lazy" '
                       f'allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
                       f'<b>{t}</b><a href="https://www.youtube.com/shorts/{v}" target="_blank" rel="noopener">Watch on YouTube<span class="sr-only"> (opens in a new tab)</span></a></li>')
    sec = ('<section class="section cr-shorts" aria-labelledby="cr-shorts-t"><div class="wrap">'
           '<header class="sec-head yt-head"><span class="eyebrow" style="color:var(--y)">Watch</span><h2 id="cr-shorts-t">The night, in under a minute</h2>'
           '<p>The first Hermes Agent hackathon in the Philippines, and what it opens up for Filipino builders.</p></header>'
           '<ul class="cr-shortgrid" role="list">' + fr('9gR-vHVfEUk', 'The first ever Hermes Agent hackathon in the Philippines') + fr('eZ5_JyFjUo8', 'Global opportunities for Filipino builders') + '</ul></div></section>')
    j = P.index('</section>', P.index('<section class="numbers"')) + len('</section>')
    return reband(P[:j] + '\n  ' + sec + P[j:])
SH_CSS = ('.cr-shortgrid{list-style:none;margin:0 auto;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,300px));justify-content:center;gap:24px}'
          '.cr-shortgrid li{display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center}.cr-shortgrid .yt-frame--short{width:100%;max-width:300px}'
          '.cr-shortgrid b{color:#fff;font-weight:900}.cr-shortgrid a{display:inline-flex;align-items:center;min-height:44px;color:var(--y);font-weight:800;text-decoration:underline}'
          '@media (max-width:640px){.cr-shortgrid{grid-template-columns:minmax(0,300px)}}')
edit('docs/case-studies/hermes-agentic-code-camp/index.html', 'hermes-camp', shorts, SH_CSS)
