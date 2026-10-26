# /start-here/: "New to DEVCON? Start here": chapters, DEVCON+, volunteering, programs, and a glossary of insider words.
import re, glob, os, json
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
COMBINED = glob.glob('combined/*.html')[0]
NT = '<span class="sr-only"> (opens in a new tab)</span>'
TITLE = 'New to DEVCON? Start Here | DEVCON Philippines'
DESC = 'New to DEVCON Philippines? How chapters and volunteer communities work, where to find events on DEVCON+, how to volunteer, which program is for you, and what our insider words mean.'

def page(mode):
    L = (lambda k: {'home': '../', 'locations': '../locations/', 'volunteer': '../volunteer/', 'programs': '../programs/', 'invite': '../invite/', 'kids': '../programs/kids/',
                    'campus': '../programs/campus/', 'pro': '../programs/pro-summit/', 'playbook': '../playbook/', 'results': '../case-studies/', 'about': '../about/',
                    'fluency': '../programs/ai-fluency-agentic-training/', 'sui': '../case-studies/sui/'}[k]) if mode == 'docs' else \
        (lambda k: '#/' + {'home': '', 'locations': 'chapters', 'volunteer': 'volunteer', 'programs': 'programs', 'invite': 'invite', 'kids': 'devcon-kids', 'campus': 'campus',
                           'pro': 'pro-summit', 'playbook': 'playbook', 'results': 'case-studies', 'about': 'about', 'fluency': 'ai-fluency', 'sui': 'sui'}[k])
    hidden = ' hidden' if mode == 'spa' else ''
    basics = [('#F2C500', 'Chapters and volunteer communities', f'DEVCON has 13 locations: 9 active chapters, each covering its province, and 4 volunteer communities that are working toward becoming chapters. Every one is run by local volunteers.', L('locations'), 'See all 13 locations'),
              ('#A57BFF', 'DEVCON+, where events live', 'DEVCON+ is our member platform. Create a free account to find upcoming events, register, and earn points when you attend or volunteer.', 'https://www.devcon.plus/events', 'Find events on DEVCON+'),
              ('#71B405', 'Volunteering', 'Event volunteers, chapter officers, and national leaders are all DEVCON volunteers. Start by helping at one event.', L('volunteer'), 'See volunteer roles'),
              ('#4DA2FF', 'Programs for every stage', 'From kids and teachers to students and professionals. Each program is free and runs through our chapters.', L('programs'), 'Explore programs')]
    cards = ''.join(f'<li class="pp" style="--c:{c}"><h3>{h}</h3><p>{d}</p><a class="pp-link" href="{u}"' + (f' target="_blank" rel="noopener">{t}{NT}</a>' if u.startswith('http') else f'>{t}</a>') + '</li>' for c, h, d, u, t in basics)
    who = [('For kids and teachers', 'DEVCON Kids, Hour of AI for Kids, and DEVCON for Educators', L('kids')), ('For students', 'Campus DEVCON, AI Engineering Internships, AI Scholarships, and code camps', L('campus')),
           ('For professionals', 'AI Fluency &amp; Agentic Training, PRO Developers Summit, #SHEISDEVCON, and DEVCON CREST', L('pro')), ('For chapter leaders', 'The Community Playbook, becoming a chapter officer, and starting a chapter', L('playbook'))]
    who_html = ''.join(f'<li><b>{h}</b><span>{d}</span><a class="pp-link" href="{u}">Start here</a></li>' for h, d, u in who)
    terms = [('Chapter', 'A local DEVCON community with elected volunteer officers, covering its province.'),
             ('Volunteer community', 'A local DEVCON network without active chapter officers yet, working toward becoming a chapter.'),
             ('DEVCON HQ', 'The national office in Ortigas that sets standards, trains chapter leaders, and approves partnerships.'),
             ('DEVCON+', 'Our member platform for events, registration, and points.'),
             ('DevRel', 'Short for developer relations: how tech companies work with developer communities. Our <a class="pp-link" href="RESULTS">Partner Results</a> show what those partnerships achieved.'),
             ('Code camp', 'A hands-on coding workshop where you build something real in a day or less.'),
             ('Hackathon', 'A time-boxed build challenge where teams create a working project and demo it.'),
             ('Move smart contracts', 'Programs written in Move, the language of the Sui blockchain, that run on-chain. See the <a class="pp-link" href="SUI">Sui code camps</a>.'),
             ('AI orchestrator', 'Someone who directs AI tools to get real work done. Taught in <a class="pp-link" href="FLUENCY">AI Fluency &amp; Agentic Training</a>.'),
             ('Playbook AI (Notebook AI)', 'Each chapter&#8217;s AI assistant for the Community Playbook, built on Google NotebookLM. Ask your chapter president for access.'),
             ('Loopers', 'Standard looping event videos played before a session starts and in the background.'),
             ('BIR invoice guideline', 'How chapters issue official receipts to event sponsors so partnerships stay tax compliant.')]
    gl = ''.join(f'<div class="gl-item"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in terms).replace('RESULTS', L('results')).replace('SUI', L('sui')).replace('FLUENCY', L('fluency'))
    return f'''<div class="page" data-page="start-here"{hidden}>
  <header class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{L('home')}">Home</a><span aria-hidden="true">/</span><span aria-current="page">Start here</span></nav>
      <span class="eyebrow" style="color:var(--y)">New to DEVCON?</span>
      <h1 id="start-here-title">Start here</h1>
      <p class="page-lead">DEVCON Philippines is a credible, trusted, volunteer-led non-profit for developers, students, and educators. Here&#8217;s how it works, in two minutes.</p>
      <div class="hero-btns"><a class="btn-primary btn-xl" href="https://www.devcon.plus/events" target="_blank" rel="noopener">Find an event on DEVCON+{NT}</a><a class="btn-outline" href="{L('volunteer')}">Volunteer with us</a></div>
    </div>
  </header>

  <section class="section" aria-labelledby="sh-basics"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">The basics</span><h2 id="sh-basics">Four things to know</h2></header>
    <ul class="pp-grid pp-grid--4" role="list">{cards}</ul>
  </div></section>

  <section class="section band2" aria-labelledby="sh-who"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Programs</span><h2 id="sh-who">Which program is for you?</h2></header>
    <ul class="sh-who" role="list">{who_html}</ul>
  </div></section>

  <section class="section" id="glossary" aria-labelledby="sh-gl"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Glossary</span><h2 id="sh-gl">Words you&#8217;ll see on this site</h2><p>Plain-language meanings for the terms our community uses.</p></header>
    <dl class="gl-list">{gl}</dl>
  </div></section>

  <section class="page-cta">
    <div class="wrap">
      <h2>Ready for your first event?</h2>
      <p>Most events are free. Create a DEVCON+ account, pick an event near you, and say hello.</p>
      <div class="programs-cta"><a class="btn-primary btn-xl" href="https://www.devcon.plus/events" target="_blank" rel="noopener">See upcoming events on DEVCON+{NT}</a><a class="btn-outline" href="{L('locations')}">Find your chapter</a></div>
    </div>
  </section>
</div>
'''
CSS = ('.sh-who{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}'
       '.sh-who li{display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}.sh-who b{color:#fff;font-weight:900}.sh-who span{color:var(--text-secondary)}'
       '.gl-list{margin:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 20px}.gl-item{padding:14px 16px;border-radius:14px;background:rgba(255,255,255,.04);border:1px solid var(--line)}'
       '.gl-item dt{color:var(--y);font-weight:900;margin-bottom:4px}.gl-item dd{margin:0;color:var(--text-secondary);line-height:1.55}'
       '@media (max-width:760px){.sh-who,.gl-list{grid-template-columns:minmax(0,1fr)}}')

src = open('docs/attend/index.html', encoding='utf-8').read()
ot = re.search(r'<title>([^<]*)</title>', src).group(1); od = re.search(r'<meta name="description" content="([^"]*)"', src).group(1)
a = src.index('<div class="page" data-page="attend"'); b = src.index('</main>')
out = src[:a] + page('docs') + src[b:]
out = out.replace(ot, TITLE).replace(od, DESC).replace('https://devcon.ph/attend/', 'https://devcon.ph/start-here/').replace('</style>', CSS + '</style>', 1)
os.makedirs('docs/start-here', exist_ok=True); open('docs/start-here/index.html', 'w', encoding='utf-8').write(out)
c = open(COMBINED, encoding='utf-8').read()
if 'data-page="start-here"' not in c:
    i = c.index('</main>'); c = c[:i] + page('spa') + c[i:]; c = c.replace('</style>', CSS + '</style>', 1); open(COMBINED, 'w', encoding='utf-8').write(c)
# links: first item in the "Our Story" menu, and the footer Community column, on every page
n = 0
for f in glob.glob('docs/**/*.html', recursive=True) + [COMBINED]:
    s = open(f, encoding='utf-8').read(); o = s
    if f == COMBINED: pre = None
    else:
        d = os.path.relpath('docs', os.path.dirname(f)).replace('\\', '/'); pre = '' if d == '.' else d + '/'
    href = '#/start-here' if pre is None else pre + 'start-here/'
    if 'New to DEVCON? Start here' not in s:
        s = re.sub(r'(<div class="nav-dd-panel nav-dd-panel--sm" id="dd-story">\s*)', lambda m: m.group(1) + f'<a href="{href}" style="--c:#71B405"><b>New to DEVCON? Start here</b><span>Chapters, DEVCON+, volunteering, and programs</span></a>\n          ', s, count=1)
        s = re.sub(r'(<li><a href="[^"]*">Attend an event</a></li>)', lambda m: f'<li><a href="{href}">New to DEVCON? Start here</a></li>' + m.group(1), s, count=1)
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1
m = json.load(open('docs/url-map.json'))
if '/start-here/' not in m['pages']: m['pages'] = sorted(m['pages'] + ['/start-here/'])
json.dump(m, open('docs/url-map.json', 'w'), indent=1)
sm = open('docs/sitemap.xml').read()
if 'devcon.ph/start-here/' not in sm: open('docs/sitemap.xml', 'w').write(sm.replace('</urlset>', '  <url><loc>https://devcon.ph/start-here/</loc><lastmod>2026-10-22</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n</urlset>'))
ll = open('docs/llms.txt').read()
if 'start-here' not in ll: open('docs/llms.txt', 'w').write(ll.rstrip('\n') + '\n- [New to DEVCON? Start here](https://devcon.ph/start-here/): chapters, DEVCON+, volunteering, programs, and a glossary\n')
print('start here built; linked on', n, 'files')
