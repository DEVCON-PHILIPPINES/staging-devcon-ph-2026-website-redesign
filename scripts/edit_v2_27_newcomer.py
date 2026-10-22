# v2.27: newcomer review. Chapter team and contact, featured events, consistent chapter counts, clear labels,
# Programs menu by audience, province coverage, plainer words, and a Start here page.
import re, glob, os, json
from urllib.parse import quote
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
COMBINED = glob.glob('combined/*.html')[0]
DOCS = glob.glob('docs/**/*.html', recursive=True)
NT = '<span class="sr-only"> (opens in a new tab)</span>'
DPLUS = 'https://www.devcon.plus/events'
ACTIVE = ['manila', 'laguna', 'legazpi', 'pampanga', 'cebu', 'iloilo', 'davao', 'iligan', 'bukidnon']
VC = ['bohol', 'bacolod', 'tacloban', 'cagayandeoro']
NAME = {'manila': 'Manila', 'laguna': 'Laguna', 'legazpi': 'Legazpi', 'pampanga': 'Pampanga', 'cebu': 'Cebu', 'iloilo': 'Iloilo', 'bohol': 'Bohol', 'bacolod': 'Bacolod',
        'tacloban': 'Tacloban', 'davao': 'Davao', 'cagayandeoro': 'Cagayan de Oro', 'iligan': 'Iligan', 'bukidnon': 'Bukidnon'}
PROVINCE = {'manila': 'Metro Manila', 'laguna': 'Laguna', 'legazpi': 'Albay', 'pampanga': 'Pampanga', 'cebu': 'Cebu', 'iloilo': 'Iloilo', 'bohol': 'Bohol',
            'bacolod': 'Negros Occidental', 'tacloban': 'Leyte', 'davao': 'Davao del Sur', 'cagayandeoro': 'Misamis Oriental', 'iligan': 'Lanao del Norte', 'bukidnon': 'Bukidnon'}
FB = {'manila': 'devconmanila', 'laguna': 'DEVCONLAGUNA', 'legazpi': 'devconlegazpi', 'pampanga': 'devconpampanga', 'cebu': 'devconcebu', 'iloilo': 'devconiloilo',
      'bohol': 'devconbohol', 'bacolod': 'devconbacolod', 'tacloban': 'DevConPH', 'davao': 'devcondavao', 'cagayandeoro': 'DEVCONCDO', 'iligan': 'devconiligan', 'bukidnon': 'devconbukidnon'}
log = {}
def bump(k, n=1): log[k] = log.get(k, 0) + n
def rd(f): return open(f, encoding='utf-8').read()
def wr(f, s): open(f, 'w', encoding='utf-8').write(s)
def addcss(s, css): return s.replace('</style>', css + '</style>', 1) if css not in s else s
def prefix(f):  # relative path from a folder page to the site root
    if f == COMBINED: return None
    d = os.path.relpath('docs', os.path.dirname(f)).replace('\\', '/')
    return '' if d == '.' else d + '/'
def link(f, path, spa):
    p = prefix(f); return ('#/' + spa) if p is None else p + path

# ---------- 2) chapter pages: drop the non-renewal sentence; it moves to Start a chapter ----------
OLD_Q = 'As a volunteer community, we can only support so many chapters well, and we have not renewed a total of 4 chapters for non-compliance and inactivity to date.'
NEW_Q = 'As a volunteer community, we can only support so many chapters well.'
# ---------- 3) featured events on chapter pages ----------
DP_BTN = f'<a class="btn-outline ch-dplus" href="{DPLUS}" target="_blank" rel="noopener">See upcoming events on DEVCON+{NT}</a>'
# ---------- 1) Meet the team, with a direct contact ----------
def team(c, pres):
    n = NAME[c]; fb = FB[c]
    msg = f'<a class="btn-primary" href="https://m.me/{fb}" target="_blank" rel="noopener">Message DEVCON {n if fb.lower() != "devconph" else "Philippines"} on Messenger{NT}</a>'
    fbl = f'<a class="btn-outline" href="https://www.facebook.com/{fb}" target="_blank" rel="noopener">Follow on Facebook{NT}</a>'
    mail = f'<a class="pp-link" href="mailto:hello@devcon.ph?subject={quote(f"Partnership with DEVCON {n}")}">Partnerships and school invites: hello@devcon.ph</a>'
    if pres:
        img, role, name = pres
        people = f'<li class="tm-card"><img src="{img}" alt="{name}" width="120" height="120" loading="lazy"/><b>{name}</b><span>{role}</span></li>'
        intro = f'The volunteer officers who run DEVCON {n} day to day. Message the chapter directly for events, volunteering, or local partnerships.'
    else:
        people = ''
        intro = f'DEVCON {n} is a volunteer community without active chapter officers yet. Message the volunteers directly, or reach DEVCON HQ for partnerships.'
    return (f'\n  <section class="section ch-team" id="{c}-team" aria-labelledby="{c}-team-t"><div class="wrap">'
            f'<header class="sec-head"><span class="eyebrow" style="color:var(--y)">The team</span><h2 id="{c}-team-t">Meet the DEVCON {n} team</h2><p>{intro}</p></header>'
            f'<div class="tm-grid">' + (f'<ul class="tm-people" role="list">{people}</ul>' if people else '') +
            f'<div class="tm-contact"><h3>Contact DEVCON {n}</h3><p>The fastest way to reach the local team is Messenger.</p><div class="hero-btns">{msg}{fbl}</div><p>{mail}</p></div></div>'
            f'</div></section>')
TEAM_CSS = ('.tm-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:20px;align-items:start}.tm-grid:has(>.tm-contact:only-child){grid-template-columns:minmax(0,1fr)}'
            '.tm-people{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px}'
            '.tm-card{display:flex;flex-direction:column;align-items:center;text-align:center;gap:4px;padding:18px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}'
            '.tm-card img{width:110px;height:110px;border-radius:50%;object-fit:cover;border:3px solid var(--c,#F2C500);margin-bottom:6px}.tm-card b{color:#fff;font-weight:900}.tm-card span{color:var(--y);font-size:.85rem;font-weight:800}'
            '.tm-contact{padding:20px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}.tm-contact h3{margin:0 0 4px;color:#fff;font-weight:900}.tm-contact p{color:var(--text-secondary)}'
            '.ch-dplus{margin-top:12px}.ch-chips .chip-covers{background:rgba(242,197,0,.12);border-color:rgba(242,197,0,.45);color:var(--y)}'
            '.dcc-row-l{flex:1 1 0;min-width:0}.dcc-row-r{flex:none}.dcc-row-l{flex-wrap:wrap;row-gap:2px}.dcc-row-l .dcc-tag{flex-basis:100%;max-width:max-content;margin:2px 0 0 18px}'
            '@media (max-width:760px){.tm-grid{grid-template-columns:minmax(0,1fr)}}')

def chapter_edit(P, c):
    if OLD_Q in P: P = P.replace(OLD_Q, NEW_Q); bump('2 chapter note removed')
    # featured events: rename the card and add the DEVCON+ button
    if 'aria-label="Notable events"><p class="chip-label">Notable events</p>' in P:
        P = P.replace('aria-label="Notable events"><p class="chip-label">Notable events</p>', 'aria-label="Featured events"><p class="chip-label">Featured events</p>', 1)
        P = re.sub(r'(aria-label="Featured events"><p class="chip-label">Featured events</p><ul class="loc-chips" role="list">.*?</ul>)', lambda m: m.group(1) + DP_BTN, P, count=1, flags=re.S)
        bump('3 chapter featured events')
    # province coverage chip
    if 'chip-covers' not in P:
        lab = f'Covers: {PROVINCE[c]}' if c in ACTIVE else f'Area: {PROVINCE[c]}'
        P, k = re.subn(r'(<ul class="ch-chips" role="list">.*?)(</ul>)', lambda m: m.group(1) + f'<li class="chip-covers">{lab}</li>' + m.group(2), P, count=1, flags=re.S); bump('8 coverage chips', k)
        if c in VC and 'Volunteer community</li>' not in P:
            P = re.sub(r'(<ul class="ch-chips" role="list"><li><b>[^<]*</b>[^<]*</li>)', lambda m: m.group(1) + '<li>Volunteer community</li>', P, count=1)
    # team section after the About section
    if 'ch-team' not in P:
        m = re.search(r'<span class="[^"]*"><img src="([^"]+)" alt="([^"]+)" width="240" height="240"/></span><p class="bcard-role"[^>]*>([^<]+)</p><h3>([^<]+)</h3>', P)
        pres = (m.group(1), m.group(3), m.group(4)) if m else None
        a = P.find('<section class="section ch-about'); a = P.find('<section', a + 10) if a >= 0 else -1
        if a < 0: a = P.find('<section class="section', P.find('</header>'))
        P = P[:a] + team(c, pres).lstrip('\n') + '\n  ' + P[a:]; bump('1 team sections')
    return P

# ---------- 5) and 6) consistent counts and clear labels on the map, menu, and Locations ----------
REGION = {'Luzon': ('4 locations', '4 active chapters'), 'Visayas': ('5 locations', '2 active chapters · 3 volunteer communities'),
          'Mindanao': ('4 locations', '3 active chapters · 1 volunteer community')}
def map_edit(s, f):
    for r, (cnt, sub) in REGION.items():
        s, k = re.subn(rf'<span class="dcc-region">{r}</span><span class="dcc-count">\d+ Chapters?</span></div>',
                       f'<span class="dcc-region">{r}</span><span class="dcc-count">{cnt}</span></div><p class="dcc-sub">{sub}</p>', s); bump('5 map region counts', k)
    s, k = re.subn(r'<sup class="dcc-ast">\*</sup>', '<span class="dcc-tag dcc-tag--vc">Volunteer community</span>', s); bump('6 map volunteer labels', k)
    s, k = re.subn(r'(<a class="dcc-row" data-name="[^"]+"[^>]*>\s*<span class="dcc-row-l"><i class="dcc-dot2"></i>[^<]+)(</span>)', lambda m: m.group(1) + '<span class="dcc-tag dcc-tag--ch">Active chapter</span>' + m.group(2), s); bump('6 map active labels', k)
    inv = link(f, 'invite/', 'invite')
    s, k = re.subn(r'<span><i class="lg lg-grow"></i>Strategic growth area \(no local partners yet, not in the 13\)</span>',
                   f'<span><i class="lg lg-grow"></i>Growth area: no chapter yet. <a class="dcc-invite" href="{inv}">Invite DEVCON here</a></span>', s); bump('6 growth legend', k)
    # menu: the asterisk becomes a word
    s, k = re.subn(r'<span class="dd-name">([^<]+)<sup>\*</sup></span>', r'<span class="dd-name">\1<em class="dd-vc">Community</em></span>', s); bump('6 menu labels', k)
    s = s.replace('<p class="dd-note"><sup>*</sup> Local tech community network, no active chapter officers.</p>',
                  '<p class="dd-note"><em class="dd-vc">Community</em> Volunteer community: a local tech network without active chapter officers yet. 13 locations: 9 active chapters and 4 volunteer communities.</p>')
    return s
MAP_CSS = ('.dcc-sub{margin:-2px 0 8px;color:var(--text-secondary);font-size:.82rem}'
           '.dcc-tag{display:inline-flex;align-items:center;margin-left:8px;padding:1px 8px;border-radius:999px;font-size:.66rem;font-weight:800;letter-spacing:.02em;vertical-align:middle;white-space:nowrap}'
           '.dcc-tag--ch{background:rgba(113,180,5,.16);color:#B8E86A;border:1px solid rgba(113,180,5,.45)}.dcc-tag--vc{background:rgba(255,255,255,.06);color:#d6d3ef;border:1px dashed rgba(255,255,255,.4)}'
           '.dcc-growth b{background:rgba(255,255,255,.05)!important;color:#a7a4c4!important;border:1px dashed rgba(255,255,255,.35)!important;box-shadow:none!important}'
           '.dcc-invite{color:var(--y);font-weight:800;text-decoration:underline}'
           '.dd-vc{font-style:normal;margin-left:6px;padding:0 6px;border-radius:999px;border:1px dashed rgba(255,255,255,.4);font-size:.62rem;font-weight:800;color:#d6d3ef;vertical-align:middle}')

# ---------- 7) Programs menu by audience, each program once ----------
GROUPS = [('For kids and teachers', '#F2C500', [('programs/kids/', 'devcon-kids', 'DEVCON Kids'), ('programs/#hour-of-ai', 'programs', 'Hour of AI for Kids'), ('programs/educators/', 'educators', 'DEVCON for Educators')]),
          ('For students', '#A57BFF', [('programs/campus/', 'campus', 'Campus DEVCON'), ('programs/jumpstart-internships/', 'internships', 'AI Engineering Internships (Jumpstart)'),
                                        ('programs/ai-scholarships/', 'ai', 'AI Scholarships'), ('programs/ai-code-camps/', 'ai-code-camps', 'Open-Source AI Code Camps'),
                                        ('case-studies/sui/', 'sui', 'Smart Contracts Code Camps (Sui)')]),
          ('For professionals', '#4DA2FF', [('programs/ai-fluency-agentic-training/', 'ai-fluency', 'AI Fluency &amp; Agentic Training'), ('programs/pro-summit/', 'pro-summit', 'PRO Developers Summit'),
                                             ('programs/sheisdevcon/', 'sheisdevcon', '#SHEISDEVCON: women in tech'), ('programs/crest/', 'crest', 'DEVCON CREST: climate tech')]),
          ('For chapter leaders', '#71B405', [('playbook/', 'playbook', 'Community Playbook'), ('volunteer/#chapter-officer', 'volunteer', 'Become a chapter officer'), ('invite/#start-a-chapter', 'invite', 'Start a chapter')])]
def menu_html(f):
    def col(groups):
        out = ''
        for h, c, items in groups:
            lis = ''.join(f'<li><a href="{link(f, p, k)}" style="--c:{c}"><i class="dd-dot"></i><span class="dd-name">{t}</span></a></li>' for p, k, t in items)
            out += f'<p class="dd-region" style="--c:{c}">{h}</p><ul role="list">{lis}</ul>'
        return out
    dplus = f'<p class="dd-region" style="--c:#B99BFF">Events</p><ul role="list"><li><a href="https://www.devcon.plus" target="_blank" rel="noopener" style="--c:#71B405"><i class="dd-dot"></i><span class="dd-name">DEVCON+: find events</span>{NT}</a></li></ul>'
    return f'<div class="ddp-cols">\n            <div class="dd-col">{col(GROUPS[:2])}</div>\n            <div class="dd-col">{col(GROUPS[2:])}{dplus}</div>\n          </div>'
def menu_edit(s, f):
    a = s.find('<div class="nav-dd-panel" id="dd-programs">')
    if a < 0: return s
    b = s.find('<div class="ddp-cols">', a); e = s.find('\n          </div>\n        </div>', b)
    if b < 0 or e < 0: return s
    bump('7 programs menu'); return s[:b] + menu_html(f) + s[e + len('\n          </div>'):]

# ---------- 9) plainer words, and Partner Results instead of DevRel Case Studies ----------
WORDS = [('>DevRel Case Studies<', '>Partner Results<'), ('See all DevRel case studies', 'See all partner results'), ('See DevRel case studies', 'See partner results'),
         ('Read the DevRel case studies', 'Read the partner results'), ('Read our DevRel case studies', 'Read our partner results'), ("'case-studies':'DevRel case studies'", "'case-studies':'Partner results'"),
         ('"name": "DevRel Case Studies"', '"name": "Partner Results"'), ('Guidelines, loopers, and the Playbook AI', 'Guidelines, event videos, and the Playbook AI assistant'),
         ('Standard event loopers for pre-show and background visuals.', 'Standard looping event videos (loopers) for pre-show and background visuals.'),
         ('Ask your Chapter President for your chapter&#8217;s Notebook AI.', 'Ask your Chapter President for your chapter&#8217;s Notebook AI, the Playbook AI assistant built on Google NotebookLM.'),
         ('turns chapter leaders into AI orchestrators.', 'turns chapter leaders into AI orchestrators: leaders who direct AI tools to get real work done.'),
         ('follow the BIR invoice guideline for tax compliance.', 'follow the BIR invoice guideline, which explains how to issue official receipts to sponsors for tax compliance.'),
         ('Chapters Playbook and Notebook AI', 'Chapters Playbook and Notebook AI assistant')]

# ---------- run ----------
for f in DOCS + [COMBINED]:
    s = rd(f); o = s
    s = map_edit(s, f); s = menu_edit(s, f)
    for a, b in WORDS:
        if a in s: s = s.replace(a, b); bump('9 words')
    if f == COMBINED:
        for c in NAME:
            a = s.find(f'<div class="page" data-page="chapter-{c}"')
            if a < 0: continue
            b = s.find('<div class="page"', a + 10); b = s.index('</main>', a) if b < 0 or s.find('</main>', a) < b else b
            s = s[:a] + chapter_edit(s[a:b], c) + s[b:]
    else:
        m = re.match(r'docs/locations/([a-z]+)/index\.html$', f)
        if m and m.group(1) in NAME: s = chapter_edit(s, m.group(1))
    if s != o:
        s = addcss(s, MAP_CSS)
        if 'ch-team' in s: s = addcss(s, TEAM_CSS)
        wr(f, s)

# ---------- 3) and 4) Attend: featured events, DEVCON+ button, honest step 2 ----------
for f in ['docs/attend/index.html', COMBINED]:
    s = rd(f)
    s = s.replace('<span class="eyebrow" style="color:var(--y)">Recent events</span><h2 id="recent-ev">What you missed this year</h2>',
                  '<span class="eyebrow" style="color:var(--y)">Featured events</span><h2 id="recent-ev">Featured events from across the country</h2><p>A few signature events from our chapters. For the latest schedule, check DEVCON+.</p>')
    s, k = re.subn(r'(<ol class="ev-list" role="list">.*?</ol>)', lambda m: re.sub(r'<time>[^<]*</time>', '', m.group(1)) + f'\n      <div class="programs-cta"><a class="btn-primary btn-xl" href="{DPLUS}" target="_blank" rel="noopener">See upcoming events on DEVCON+{NT}</a></div>', s, count=1, flags=re.S)
    bump('3 attend featured', k)
    s = s.replace('<h3>Pick an event near you</h3><p>Browse by chapter or region, online or on-site.</p>', '<h3>Pick an event near you</h3><p>Browse upcoming events on DEVCON+, online or on-site. Each chapter page below also shows its featured events.</p>')
    s = addcss(s, '.ev-list li{grid-template-columns:minmax(0,1fr)!important}')
    wr(f, s)

# ---------- 2) and 8) Invite: the non-renewal note on Start a chapter; province coverage ----------
for f in ['docs/invite/index.html', COMBINED]:
    s = rd(f)
    s = s.replace('<p class="ch-req-lead"><b>Limited capacity as a volunteer community.</b> We can only support so many chapters well, so we approve new chapters carefully and review every chapter each year. We will always prioritize',
                  '<p class="ch-req-lead"><b>Limited capacity as a volunteer community.</b> We can only support so many chapters well, so we approve new chapters carefully and review every chapter each year. To date, we have not renewed a total of <b>4 chapters</b> for non-compliance and inactivity. We will always prioritize')
    s = s.replace('<p>Every item needs an owner, you or a partner, before we can confirm. This is required outside our chapter locations:',
                  '<p class="inv-cover"><b>Who covers speaker costs?</b> Each active chapter covers its entire province. If your province has no active DEVCON chapter, the host covers the volunteer speakers&#8217; costs. Provinces with a volunteer community but no active chapter are treated as not covered for now. <a class="pp-link" href="LOCLINK">See which provinces are covered</a>.</p>\n          <p>Every item needs an owner, you or a partner, before we can confirm. This is required outside our chapter provinces:')
    s = s.replace('href="LOCLINK"', 'href="' + ('../locations/' if f != COMBINED else '#/chapters') + '"')
    s = addcss(s, '.inv-cover{margin:14px 0;padding:12px 16px;border-radius:14px;background:rgba(242,197,0,.08);border:1px solid rgba(242,197,0,.45);color:#fff}.inv-cover b{color:var(--y)}')
    wr(f, s); bump('8 invite coverage line')

# ---------- 5) one statement of the totals on Locations ----------
for f in ['docs/locations/index.html', COMBINED]:
    s = rd(f)
    s = s.replace('and <a class="pp-link reg-link" href="#mindanao">Mindanao</a>, with 120+ free events every year,',
                  'and <a class="pp-link reg-link" href="#mindanao">Mindanao</a>: 9 active chapters and 4 volunteer communities, with 120+ free events every year,')
    wr(f, s)
print(json.dumps(log, indent=1))
