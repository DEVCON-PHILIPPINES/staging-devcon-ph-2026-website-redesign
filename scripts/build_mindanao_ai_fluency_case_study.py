# Case study: three AI Fluency Masterclass and Hackathon days in Mindanao (Bukidnon, Iligan, Davao).
# Narrative: bring frontier AI to leaders and IT students where they are.
import re, glob, json, os, base64, sys
from urllib.parse import quote
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, 'scripts')
import build_sheisdevcon_aba_case_study as aba
PATH = 'case-studies/mindanao-ai-fluency-hackathons'
SPA = 'mindanao-ai-fluency'
MEDIA = f'docs/{PATH}/media/'
TITLE = 'Frontier AI, Where Mindanao&#8217;s Builders Are: AI Fluency Masterclass and Hackathons | Case Study'
DESC = ('Three AI Fluency Masterclass and Hackathon days in Bukidnon, Iligan, and Davao brought frontier AI to Mindanao&#8217;s chapter leaders and IT students '
        'on their own campuses: learn in the morning, build and pitch by the afternoon.')
SCALE = 'mailto:hello@devcon.ph?subject=' + quote('Bring the AI Fluency Masterclass and Hackathon to our city')
NT = '<span class="sr-only"> (opens in a new tab)</span>'

def yt(v, title):
    return (f'<div class="yt-frame"><iframe src="https://www.youtube-nocookie.com/embed/{v}?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0&amp;modestbranding=1" title="{title}" loading="lazy" '
            f'allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
            f'<p class="yt-link"><a href="https://www.youtube.com/watch?v={v}" target="_blank" rel="noopener">Watch on YouTube{NT}</a></p>')

def page_html(mode):
    M = (lambda f: f'media/{f}.webp') if mode == 'docs' else (lambda f: 'data:image/webp;base64,' + base64.b64encode(open(f'{MEDIA}{f}.webp', 'rb').read()).decode())
    K = {'cs': ('../', 'case-studies'), 'partner': ('../../partner/', 'partner'), 'caravan': ('../mindanao-ai-caravan/', 'mindanao-ai-caravan'),
         'aba': ('../sheisdevcon-aba/', 'sheisdevcon-aba'), 'fluency': ('../../programs/ai-fluency-agentic-training/', 'ai-fluency'),
         'guide': ('../../playbook/hackathon-best-practice/', 'hackathon-best-practice'), 'bukidnon': ('../../locations/bukidnon/', 'chapter-bukidnon'),
         'iligan': ('../../locations/iligan/', 'chapter-iligan'), 'davao': ('../../locations/davao/', 'chapter-davao'), 'invite': ('../../invite/', 'invite'),
         'hermes': ('../hermes-agentic-code-camp/', 'hermes-camp'), 'codecamps': ('../../programs/ai-code-camps/', 'ai-code-camps'), 'orin': ('../devcon-studios-nvidia-orin-nano/', 'orin-nano')}
    L = (lambda k: K[k][0]) if mode == 'docs' else (lambda k: '#/' + K[k][1])
    home = '../../' if mode == 'docs' else '#/'
    fig = lambda f, alt, cap=None, cls='': f'<figure class="cs-fig {cls}"><img src="{M(f)}" alt="{alt}" loading="lazy"/>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
    stat = lambda b, s, c: f'<li class="num-item" style="--c:{c}"><b>{b}</b><span>{s}</span></li>'
    disc = [('aba', '#SHEISDEVCON × Austrian Business Agency', 'Two years of women in tech code camps, Manila to Mindanao'),
            ('caravan', 'Mindanao AI Caravan', 'Free AI education for kids, teachers, and builders in Mindanao'),
            ('hermes', 'Hermes Agentic Code Camp and Hackathon', 'First in the Philippines: builders shipped agents in one night'),
            ('orin', 'DEVCON Studios × NVIDIA Jetson Orin Nano', 'Kai, an edge offline AI robot built in public')]
    disc_html = ''.join(f'<li><a class="disc-card" href="{L(k)}"><b>{t}</b><span>{r}</span><em>Read the story</em></a></li>' for k, t, r in disc)
    hidden = ' hidden' if mode == 'spa' else ''
    day = [('#F2C500', 'Morning: the masterclass', 'Hands-on AI Fluency with frontier tools: prompting, building with AI assistants, and thinking responsibly about AI.'),
           ('#EA641D', 'Afternoon: the hackathon', 'Teams turn what they just learned into a working prototype for a local problem, against the clock.'),
           ('#71B405', 'Closing: demo and pitch', 'Every team demos to mentors, partners, and local leaders, and the best builds are recognized.'),
           ('#A57BFF', 'All day: leaders learn too', 'Chapter leaders train alongside students, so the skills stay in the city after the visiting mentors leave.')]
    day_html = ''.join(f'<li class="pp" style="--c:{c}"><h3>{h}</h3><p>{d}</p></li>' for c, h, d in day)
    return f'''<div class="page" data-page="{SPA}"{hidden}>
  <header class="page-hero page-hero--apc">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">Home</a><span aria-hidden="true">/</span><a href="{L('cs')}">Partner Success Stories</a><span aria-hidden="true">/</span><span aria-current="page">Mindanao AI Fluency</span></nav>
      <span class="eyebrow" style="color:var(--y)">Case study · AI Fluency Masterclass and Hackathons · Mindanao</span>
      <h1 id="{SPA}-title">Frontier AI, where Mindanao&#8217;s builders are</h1>
      <p class="cs-years"><span>2026 · Bukidnon · Iligan · Davao</span></p>
      <p class="page-lead">Frontier AI usually reaches Manila first. So instead of asking Mindanao&#8217;s chapter leaders and IT students to travel to it, DEVCON brought it to them: an AI Fluency Masterclass in the morning and a hackathon by the afternoon, on three campuses across Mindanao.</p>
      <div class="hero-btns"><a class="btn-primary btn-xl" href="{L('partner')}">Sponsor the next one</a><a class="btn-outline" href="{SCALE}">Help scale this program nationally</a></div>
    </div>
  </header>

  <section class="section" style="padding-top:28px"><div class="wrap">{fig('bukidnon-celebrate', 'Students, chapter leaders, mentors, and partners cheering together after the Bukidnon AI Fluency Masterclass and Hackathon', 'Bukidnon, after a full day of learning and building.', 'cs-fig--wide')}</div></section>

  <section class="numbers" aria-labelledby="maf-num"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">At a glance</span><h2 id="maf-num">Three cities, three campuses, one format</h2></header>
    <ul class="numbers-grid" role="list">{stat('3', 'Cities: Bukidnon, Iligan, and Davao', 'var(--y)')}{stat('3', 'Campuses: Central Mindanao University, MSU-IIT, and the University of Mindanao', 'var(--o)')}{stat('1 day', 'From first prompt to a working demo, in each city', 'var(--g)')}{stat('3 hours', 'To build and pitch a prototype at the Davao hackathon', 'var(--p2)')}</ul>
  </div></section>

  <section class="section" aria-labelledby="maf-idea"><div class="wrap cs-split">
    <div>
      <span class="eyebrow" style="color:var(--y)">The idea</span>
      <h2 class="cs-h2">Bring the frontier to them</h2>
      <p class="lead-p">Mindanao has no shortage of talent. What it often lacks is access: frontier AI tools, the people who use them every day, and the time and fare to travel to where those people are.</p>
      <p>So the format travels instead. DEVCON HQ brings the curriculum and mentors; each local chapter brings the campus, the students, and the local problems worth solving. Leaders and students learn the same frontier tools on the same day, in their own city, and leave with something they built.</p>
      <p>The challenges stay close to home: farms, clinics, small food businesses, and construction sites. That is the point of the Nexus AI key visual, a farmer, a builder, and a doctor, each with AI in hand.</p>
    </div>
    {fig('kv-nexus', 'Nexus AI Hackathon key visual: a young builder wearing AR glasses between a farmer with an agriculture dashboard and a doctor with a health dashboard', 'Built around local problems, from farms to clinics.')}
  </div></section>

  <section class="section" aria-labelledby="maf-day"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">The format</span><h2 id="maf-day">How a day runs</h2>
      <p>The same one-day format in every city, adapted by the local chapter.</p></header>
    <ul class="pp-grid pp-grid--4" role="list">{day_html}</ul>
    <p class="kai-links">Run one in your city with the <a class="pp-link" href="{L('guide')}">Masterclass and Hackathon Best Practice and Checklist</a>, built from the lessons of these runs.</p>
  </div></section>

  <section class="section" aria-labelledby="maf-bukidnon"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Stop 1 · Bukidnon</span><h2 id="maf-bukidnon">Aral ngayon, AI trabaho bukas</h2>
      <p>&#8220;Learn today, AI work tomorrow.&#8221; At Central Mindanao University, DEVCON Bukidnon and DOST Northern Mindanao ran the Nexus AI Fluency Masterclass and Hackathon as a stop of the DEVCON AI Mindanao Caravan, with students, faculty, and regional leaders in one hall.</p></header>
    <div class="cs-split maf-stop">
      <div>{yt('O4mID3-PvA8', 'DEVCON AI Mindanao Caravan: Aral Ngayon, AI Trabaho Bukas (Nexus AI, Bukidnon)')}</div>
      <div class="maf-pair">{fig('bukidnon-group', 'Partners, regional leaders, and students lined up for a group photo at the Bukidnon masterclass')}{fig('bukidnon-build', 'Two students building with an AI coding assistant on a laptop during the hackathon')}</div>
    </div>
    <p class="kai-links">Hosted by <a class="pp-link" href="{L('bukidnon')}">DEVCON Bukidnon</a>.</p>
  </div></section>

  <section class="section" aria-labelledby="maf-iligan"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Stop 2 · Iligan</span><h2 id="maf-iligan">The final stop of the AI Angat Mindanao Caravan</h2>
      <p>At MSU-Iligan Institute of Technology, DEVCON Iligan closed the caravan with the same format: a masterclass on the podium, then teams of IT students building and demoing in the same room.</p></header>
    <div class="cs-split maf-stop">
      <div>{yt('V3wjPqwkbBg', 'NEXUS AI Fluency Masterclass and Hackathon, final stop of the AI Angat Mindanao Caravan (Iligan)')}</div>
      <div class="maf-pair">{fig('iligan-masterclass', 'A mentor leading the AI Fluency Masterclass from the MSU-IIT podium')}{fig('iligan-team', 'A smiling hackathon team with laptops, giving thumbs up in Iligan')}</div>
    </div>
    <p class="kai-links">Hosted by <a class="pp-link" href="{L('iligan')}">DEVCON Iligan</a>.</p>
  </div></section>

  <section class="section" aria-labelledby="maf-davao"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Stop 3 · Davao · October 14, 2026</span><h2 id="maf-davao">SUBAY: navigating the technical and ethical path in AI</h2>
      <p>At the University of Mindanao, Matina Campus, DEVCON Davao and #SHEISDEVCON ran the masterclass and a 3-hour hackathon, co-presented by the Austrian Business Agency. Teams pitched AI for real local needs.</p></header>
    <div class="cs-split maf-stop">
      <div>{yt('1N98Cw_rFHQ', 'Recap from SUBAY: DEVCON Davao AI Fluency Masterclass and Hackathon, University of Mindanao')}</div>
      <div class="maf-pair">{fig('davao-timer', 'Hackathon participants at their laptops with a 3-hour countdown on the screen behind them')}{fig('davao-halal', 'A student pitching Halal Keeps, AI-assisted halal readiness guidance for small food businesses')}</div>
    </div>
    <ul class="maf-builds" role="list">
      <li><b>Halal Keeps</b><span>AI-assisted halal readiness guidance for small food businesses, by a team from Davao Central College.</span></li>
      <li><b>BantayBuild</b><span>AI-powered construction loss prevention and financial intelligence.</span></li>
      <li><b>Champion: Girl, Boy, Bakla, Hapon</b><span>The hackathon champion team, from Ateneo de Davao University.</span></li>
    </ul>
    <div class="maf-trio">{fig('davao-keynote', 'The ABA keynote on Indonesian and Filipina women in IT and tech')}{fig('davao-builders', 'Women participants smiling at their workstations')}{fig('davao-sdg', 'A student presenting a project aligned with good health and well-being')}</div>
    <p class="kai-links">Hosted by <a class="pp-link" href="{L('davao')}">DEVCON Davao</a>. Read the <a class="pp-link" href="{L('aba')}">#SHEISDEVCON × ABA story</a> for the women in tech side of the day.</p>
  </div></section>

  <section class="section" aria-labelledby="maf-why"><div class="wrap cs-split">
    <div>
      <span class="eyebrow" style="color:var(--y)">Why it matters</span>
      <h2 class="cs-h2">The same frontier, closer to home</h2>
      <ul class="doc-list">
        <li><b>Access, not just awareness:</b> students build with the same frontier AI tools used in Manila, without the trip.</li>
        <li><b>Leaders who stay:</b> chapter leaders learn alongside students, so the skills keep working after the event.</li>
        <li><b>Local problems first:</b> farms, clinics, halal food, and construction, solved by the people who know them.</li>
        <li><b>A format that travels:</b> one day, one playbook, repeatable in any city with a chapter and a campus.</li>
      </ul>
      <p>Part of <a class="pp-link" href="{L('fluency')}">AI Fluency &amp; Agentic Training</a>, alongside the <a class="pp-link" href="{L('codecamps')}">Open-Source AI Code Camps</a>.</p>
    </div>
    {fig('davao-group', 'A packed University of Mindanao auditorium after the SUBAY masterclass and hackathon', 'Davao, at the end of SUBAY.')}
  </div></section>

  <section class="section" aria-labelledby="maf-thanks"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Made possible together</span><h2 id="maf-thanks">Partners and hosts</h2></header>
    <p class="sa-chips"><b>Bukidnon and Iligan</b><span>DOST Northern Mindanao</span><span>DICT</span><span>Amihan</span><span>Monheim</span><span>Tutorials Dojo</span><span>Sui</span><span>Central Mindanao University</span><span>MSU-Iligan Institute of Technology</span></p>
    <p class="sa-chips"><b>Davao</b><span>Austrian Business Agency</span><span>Amihan</span><span>Avtica</span><span>Tutorials Dojo</span><span>Cowork Mugna</span><span>Mugna</span><span>Monde Nissin</span><span>Tiger</span><span>The Bloom</span><span>Davies</span><span>P&amp;G Printing Services</span><span>University of Mindanao</span><span>DICT</span></p>
    <p class="sa-chips"><b>Chapters</b><span>DEVCON Bukidnon</span><span>DEVCON Iligan</span><span>DEVCON Davao</span><span>#SHEISDEVCON</span></p>
  </div></section>

  <section class="section cs-discover" aria-labelledby="{SPA}-discover"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">More stories</span><h2 id="{SPA}-discover">Discover other partner success stories</h2></header>
    <ul class="disc-grid" role="list">{disc_html}</ul>
    <p style="margin-top:18px"><a class="pp-link" href="{L('cs')}">See all partner success stories</a></p>
  </div></section>

  <section class="page-cta">
    <div class="wrap">
      <h2>Sponsor the next one</h2>
      <p>Help bring the AI Fluency Masterclass and Hackathon to more cities and campuses in 2027.</p>
      <div class="programs-cta"><a class="btn-primary btn-xl" href="{L('partner')}">Sponsor the next one</a><a class="btn-outline" href="{SCALE}">Help scale this program nationally</a></div>
    </div>
  </section>
</div>
'''

def page(mode):
    P = page_html(mode)
    idx = [m.start() for m in re.finditer(r'\n  <section class="(?:section[^"]*|page-cta|numbers)"', P)]
    last = P.rindex('</section>') + len('</section>'); rows = [P[a:(idx[n + 1] if n + 1 < len(idx) else last)] for n, a in enumerate(idx)]
    k = next(n for n, r in enumerate(rows) if 'class="numbers"' in r[:80]); out = []
    for n, r in enumerate(rows):
        if n <= k or 'page-cta' in r[:60]: out.append(r); continue
        band = ((n - k - 1) % 2 == 1); o = re.match(r'\s*<section class="([^"]*)"', r); cls = re.sub(r'\s*\bband2\b', '', o.group(1))
        out.append(r.replace(f'class="{o.group(1)}"', f'class="{cls.replace("section", "section band2", 1) if band else cls}"', 1))
    return P[:idx[0]] + ''.join(out) + P[last:]

CSS = aba.CSS + ('.maf-stop{align-items:start}.maf-pair{display:grid;grid-template-columns:minmax(0,1fr);gap:12px}.maf-pair .cs-fig{margin:0}'
                 '.maf-builds{list-style:none;margin:18px 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}'
                 '.maf-builds li{padding:16px;border-radius:16px;background:rgba(255,255,255,.04);border:1px solid var(--line);border-top:3px solid var(--y)}.maf-builds b{display:block;color:#fff;font-weight:900;margin-bottom:4px}.maf-builds span{color:var(--text-secondary);font-size:.92rem;line-height:1.5}'
                 '.maf-trio{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.maf-trio .cs-fig{margin:0}'
                 '@media (max-width:900px){.maf-builds,.maf-trio{grid-template-columns:minmax(0,1fr)}}')

CARD = lambda href, thumb: (f'<article class="case" id="{SPA}-card" data-cats="ai camps events" style="--c:#71B405">\n'
    f'        <a class="case-thumb" href="{href}" tabindex="-1" aria-hidden="true"><img src="{thumb}" alt="" loading="lazy" width="1400" height="440"/></a>\n'
    f'        <div class="case-main">\n          <div class="case-top"><span class="case-ic" aria-hidden="true"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l2.5 5.5L20 11l-5.5 2.5L12 19l-2.5-5.5L4 11l5.5-2.5z"/></svg></span><span class="prog-tag">AI Fluency &amp; Agentic Training · Mindanao</span></div>\n'
    f'          <h2><a class="case-title-link" href="{href}">Frontier AI, where Mindanao&#8217;s builders are: AI Fluency Masterclass and Hackathons</a></h2>'
    f'<ul class="cs-tags" role="list"><li class="cs-tag cs-tag--cat">AI and agentic</li><li class="cs-tag cs-tag--cat">Code camps</li><li class="cs-tag cs-tag--cat">Events and summits</li><li class="cs-tag">Mindanao</li><li class="cs-tag">Hackathon</li><li class="cs-tag">IT students</li></ul>'
    f'<p class="cs-years"><span>2026 · Bukidnon · Iligan · Davao</span></p>\n'
    f'          <div class="case-block"><h3>The goal</h3><p>Bring frontier AI to Mindanao&#8217;s chapter leaders and IT students where they are, instead of asking them to travel to it.</p></div>\n'
    f'          <div class="case-block"><h3>What we did</h3><p>A one-day AI Fluency Masterclass and hackathon on three campuses: Central Mindanao University, MSU-IIT, and the University of Mindanao.</p><p><a class="pp-link" href="{href}">Read the full story</a></p></div>\n'
    f'        </div>\n        <aside class="case-results" aria-label="Results"><p class="case-results-h">Results</p><ul role="list"><li><b>3 cities</b><span>Bukidnon, Iligan, Davao</span></li><li><b>3 campuses</b><span>One format, adapted locally</span></li><li><b>1 day</b><span>From first prompt to demo</span></li></ul></aside>\n      </article>\n      ')

if __name__ == '__main__':
    src = open('docs/case-studies/devcon-studios-nvidia-orin-nano/index.html', encoding='utf-8').read()
    ot = re.search(r'<title>([^<]*)</title>', src).group(1); od = re.search(r'<meta name="description" content="([^"]*)"', src).group(1)
    a = src.index('<div class="page" data-page="orin-nano"'); b = src.index('</main>')
    out = src[:a] + page('docs') + src[b:]
    out = out.replace(f'<title>{ot}</title>', f'<title>{TITLE}</title>').replace(od, DESC).replace('https://devcon.ph/case-studies/devcon-studios-nvidia-orin-nano/', f'https://devcon.ph/{PATH}/')
    out = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + TITLE + m.group(2), out)
    out = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', lambda m: m.group(1) + TITLE + m.group(2), out)
    out = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + DESC + m.group(2), out)
    out = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', lambda m: m.group(1) + DESC + m.group(2), out)
    out = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', out, flags=re.S)
    if CSS not in out: out = out.replace('</style>', CSS + '</style>', 1)
    os.makedirs(f'docs/{PATH}', exist_ok=True); open(f'docs/{PATH}/index.html', 'w', encoding='utf-8').write(out)
    from PIL import Image, ImageOps
    ImageOps.fit(Image.open(f'{MEDIA}bukidnon-celebrate.webp').convert('RGB'), (1400, 440), Image.LANCZOS, centering=(0.5, 0.45)).save('docs/case-studies/thumbs/mindanao-ai-fluency-hackathons.webp', quality=72, method=6)
    f = 'docs/case-studies/index.html'; h = open(f, encoding='utf-8').read()
    h = re.sub(rf'<article class="case" id="{SPA}-card".*?</article>\s*', '', h, flags=re.S)
    i = h.index('</article>', h.index('<article class="case"')) + len('</article>'); i = h.index('<article class="case"', i)
    h = h[:i] + CARD('mindanao-ai-fluency-hackathons/', 'thumbs/mindanao-ai-fluency-hackathons.webp') + h[i:]
    open(f, 'w', encoding='utf-8').write(h)
    c = glob.glob('combined/*.html')[0]; t = open(c, encoding='utf-8').read()
    def drop(t, key):
        a = t.find(f'<div class="page" data-page="{key}"')
        if a < 0: return t
        b = t.find('<div class="page"', a + 10); m = t.find('</main>', a); b = m if b < 0 or m < b else b
        return t[:a] + t[b:]
    t = drop(t, SPA); t = re.sub(rf'<article class="case" id="{SPA}-card".*?</article>\s*', '', t, flags=re.S)
    i = t.index('</main>'); t = t[:i] + page('spa') + t[i:]
    a = t.index('<div class="page" data-page="case-studies"'); j = t.index('</article>', t.index('<article class="case"', a)) + len('</article>'); j = t.index('<article class="case"', j)
    thumb = 'data:image/webp;base64,' + base64.b64encode(open('docs/case-studies/thumbs/mindanao-ai-fluency-hackathons.webp', 'rb').read()).decode()
    t = t[:j] + CARD('#/' + SPA, thumb) + t[j:]
    if CSS not in t: t = t.replace('</style>', CSS + '</style>', 1)
    open(c, 'w', encoding='utf-8').write(t)
    sm = open('docs/sitemap.xml').read()
    if PATH not in sm: open('docs/sitemap.xml', 'w').write(sm.replace('</urlset>', f'  <url><loc>https://devcon.ph/{PATH}/</loc><lastmod>2026-10-26</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n</urlset>'))
    um = json.load(open('docs/url-map.json'))
    if f'/{PATH}/' not in um['pages']: um['pages'] = sorted(um['pages'] + [f'/{PATH}/'])
    json.dump(um, open('docs/url-map.json', 'w'), indent=1)
    ll = open('docs/llms.txt').read()
    if PATH not in ll: open('docs/llms.txt', 'w').write(ll.rstrip('\n') + f'\n- [Frontier AI, where Mindanao&#8217;s builders are](https://devcon.ph/{PATH}/): AI Fluency Masterclass and Hackathons in Bukidnon, Iligan, and Davao\n')
    print('built', PATH)
