# Bacolod: six coherent sections, with the reopening status (team reapplying, DEVCON HQ vetting)
import re, glob, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSczVxZPmHIRPphNJNgbuRVzEC5QTponVzjDPPMmkSxP0cIdrg/viewform'
def rows(P):
    idx = [m.start() for m in re.finditer(r'\n  <(?:section|header) class="', P)]
    end = P.rindex('</section>') + len('</section>')
    return idx, [P[a:(idx[n + 1] if n + 1 < len(idx) else end)] for n, a in enumerate(idx)], end
def pick(R, key): return next(r for r in R if key in r[:160])
def edit(P, mode):
    if 'bacolod-status' in P: return P
    idx, R, end = rows(P)
    hero, about, involved, high, video, upcoming, cta = pick(R, 'page-hero'), pick(R, 'ch-about'), pick(R, 'ch-involved'), pick(R, 'Past highlights') if False else next(r for r in R if 'Past highlights' in r), pick(R, 'ch-video'), pick(R, 'ch-upcoming'), pick(R, 'page-cta')
    # hero: status note and button targets
    hero = hero.replace('No active events right now', 'Reopening under review')
    hero = re.sub(r'On the path to a full chapter\s*(</[^>]+>\s*<[^>]+>)\s*DEVCON Bacolod needs active local officers before it can run chapter events again\.',
                  lambda m: 'Reapplying to reopen' + m.group(1) + 'The Bacolod team is reapplying to reopen the chapter, and DEVCON HQ is vetting the application.', hero, count=1)
    hero = hero.replace('href="#bacolod-qoq">How chapters grow', 'href="#bacolod-status">See the reopening status')
    status = f'''
  <section class="section bac-status" id="bacolod-status" aria-labelledby="bacolod-status-t"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Reopening status</span><h2 id="bacolod-status-t">DEVCON Bacolod is reapplying to reopen</h2>
      <p>The Bacolod team has reapplied to bring the chapter back, and DEVCON HQ is vetting the application now. Chapters reopen only when a committed officer team is ready to run regular, free programs for the long term.</p></header>
    <ol class="bac-steps" role="list">
      <li class="bac-step bac-step--done"><span class="bac-dot" aria-hidden="true">1</span><b>The team reapplies</b><span>Local volunteers step up as the future officer team.</span><em>In progress</em></li>
      <li class="bac-step bac-step--now"><span class="bac-dot" aria-hidden="true">2</span><b>DEVCON HQ vets the application</b><span>A careful review of commitment, readiness, and long-term fit with DEVCON as a non-profit.</span><em>Ongoing</em></li>
      <li class="bac-step"><span class="bac-dot" aria-hidden="true">3</span><b>The chapter reopens</b><span>Officers are confirmed and the first chapter events return to Bacolod.</span><em>Next</em></li>
    </ol>
    <div class="hero-btns"><a class="btn-primary btn-xl" href="{FORM}" target="_blank" rel="noopener" data-volunteer>Join the reopening team<span class="sr-only"> (opens in a new tab)</span></a><a class="btn-outline" href="#bacolod-nearby">Find events nearby</a></div>
  </div></section>'''
    # highlights + video in one section
    vid = re.search(r'<div class="yt-frame.*?</div>\s*(?:<p class="yt-link">.*?</p>)?', video, re.S).group(0)
    high = high.replace('</div></section>', f'<div class="merge-block"><h3 class="sub-h">A spotlight on the DEVCON Bacolod OGs who started it all</h3>{vid}</div></div></section>', 1) if '</div></section>' in high else high[:high.rindex('</div>')] + f'<div class="merge-block"><h3 class="sub-h">A spotlight on the DEVCON Bacolod OGs who started it all</h3>{vid}</div>' + high[high.rindex('</div>'):]
    # one "until events return" section: message, actions, nearby chapters
    nearby = re.search(r'<ul class="ch-others" role="list">.*?</ul>', upcoming, re.S)
    near = nearby.group(0) if nearby else ''
    until = f'''
  <section class="section ch-upcoming" id="bacolod-nearby" aria-labelledby="bacolod-until-t"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Until events return</span><h2 id="bacolod-until-t">Geeks of Bacolod, this is your sign</h2>
      <p>There are no DEVCON Bacolod events while the chapter is under review. Help the team reopen it, stay in the loop, or join free events at active Visayas chapters nearby.</p></header>
    <div class="hero-btns"><a class="btn-primary btn-xl" href="{FORM}" target="_blank" rel="noopener" data-volunteer>Volunteer<span class="sr-only"> (opens in a new tab)</span></a><a class="btn-outline" href="https://www.facebook.com/devconbacolod" target="_blank" rel="noopener">Follow DEVCON Bacolod<span class="sr-only"> (opens in a new tab)</span></a><a class="btn-outline" href="https://www.devcon.plus" target="_blank" rel="noopener">Get updates on DEVCON+<span class="sr-only"> (opens in a new tab)</span></a></div>
    <div class="merge-block"><h3 class="sub-h">Free events at nearby chapters</h3>{near}</div>
  </div></section>'''
    cta = re.sub(r'<h2>Help grow DEVCON Bacolod into a full chapter</h2>\s*<p>[^<]*</p>', '<h2>Help reopen DEVCON Bacolod</h2>\n      <p>The team is reapplying and the application is under review. Volunteer now and you could be one of the officers who brings the chapter back.</p>', cta, count=1)
    new = [hero, status, about, high, until, cta]
    out = ''.join(r if r.startswith('\n') else '\n' + r for r in new)
    # alternate bands after the hero
    parts = re.split(r'(?=\n  <section class=")', out); first = parts[0]; body = parts[1:]; fixed = []
    for n, r in enumerate(body):
        if 'page-cta' in r[:60]: fixed.append(r); continue
        o = re.match(r'\s*<section class="([^"]*)"', r); cls = re.sub(r'\s*\bband2\b', '', o.group(1))
        fixed.append(r.replace(f'class="{o.group(1)}"', f'class="{cls.replace("section", "section band2", 1) if n % 2 == 1 else cls}"', 1))
    return P[:idx[0]] + first + ''.join(fixed) + P[end:]
CSS = ('.bac-steps{list-style:none;margin:0 0 20px;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}'
       '.bac-step{position:relative;display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}'
       '.bac-dot{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:rgba(255,255,255,.08);color:#fff;font-weight:900}'
       '.bac-step b{color:#fff;font-weight:900}.bac-step span{color:var(--text-secondary);font-size:.92rem;line-height:1.5}'
       '.bac-step em{font-style:normal;align-self:flex-start;margin-top:auto;padding:3px 10px;border-radius:999px;font-size:.78rem;font-weight:900;background:rgba(255,255,255,.06);color:var(--text-secondary)}'
       '.bac-step--done .bac-dot{background:#71B405}.bac-step--done em{background:rgba(113,180,5,.18);color:#B8E86A}'
       '.bac-step--now{border-color:rgba(242,197,0,.6);box-shadow:0 0 0 1px rgba(242,197,0,.35)}.bac-step--now .bac-dot{background:var(--y);color:#0b0840}.bac-step--now em{background:rgba(242,197,0,.18);color:var(--y)}'
       '@media (max-width:760px){.bac-steps{grid-template-columns:minmax(0,1fr)}}')
for f in ['docs/locations/bacolod/index.html'] + glob.glob('combined/*.html'):
    s = open(f, encoding='utf-8').read(); a = s.index('<div class="page" data-page="chapter-bacolod"'); b = s.find('<div class="page"', a + 10)
    if b < 0 or s.find('</main>', a) < b: b = s.index('</main>', a)
    s = s[:a] + edit(s[a:b], 'docs' if f.startswith('docs') else 'spa') + s[b:]
    if CSS not in s: s = s.replace('</style>', CSS + '</style>', 1)
    open(f, 'w', encoding='utf-8').write(s); print('simplified Bacolod in', 'docs page' if f.startswith('docs') else 'single file')
