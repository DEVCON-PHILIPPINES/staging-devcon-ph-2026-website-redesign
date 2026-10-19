# Case study: nationwide #SHEISDEVCON code camps and hackathons supported by the Austrian Business Agency (ABA)
import re, glob, json, os, base64
from urllib.parse import quote
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
PATH = 'case-studies/sheisdevcon-aba'
SPA = 'sheisdevcon-aba'
MEDIA = f'docs/{PATH}/media/'
TITLE = '#SHEISDEVCON x Austrian Business Agency: Nationwide Women in Tech Code Camps | Case Study'
DESC = ('For two years, the Austrian Business Agency has supported #SHEISDEVCON code camps and hackathons from Manila to Iloilo to Davao, '
        'connecting Filipina tech talent with global career paths in Austria.')
SCALE = 'mailto:hello@devcon.ph?subject=' + quote('Help scale #SHEISDEVCON nationally')

def page_html(mode):
    M = (lambda f: f'media/{f}.webp') if mode == 'docs' else (lambda f: 'data:image/webp;base64,' + base64.b64encode(open(f'{MEDIA}{f}.webp', 'rb').read()).decode())
    L = (lambda k: {'cs': '../', 'she': '../../programs/sheisdevcon/', 'partner': '../../partner/', 'orin': '../devcon-studios-nvidia-orin-nano/', 'hermes': '../hermes-agentic-code-camp/',
                    'sui': '../sui/', 'icp': '../icp/', 'caravan': '../mindanao-ai-caravan/', 'davao': '../../locations/davao/', 'iloilo': '../../locations/iloilo/',
                    'manila': '../../locations/manila/', 'cebu': '../../locations/cebu/'}[k]) if mode == 'docs' else \
        (lambda k: '#/' + {'cs': 'case-studies', 'she': 'sheisdevcon', 'partner': 'partner', 'orin': 'orin-nano', 'hermes': 'hermes-camp', 'sui': 'sui', 'icp': 'icp',
                           'caravan': 'mindanao-ai-caravan', 'davao': 'chapter-davao', 'iloilo': 'chapter-iloilo', 'manila': 'chapter-manila', 'cebu': 'chapter-cebu'}[k])
    home = '../../' if mode == 'docs' else '#/'
    fig = lambda f, alt, cap=None, cls='': f'<figure class="cs-fig {cls}"><img src="{M(f)}" alt="{alt}" loading="lazy"/>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
    stat = lambda b, s, c: f'<li class="num-item" style="--c:{c}"><b>{b}</b><span>{s}</span></li>'
    disc = [('orin', 'DEVCON Studios × NVIDIA Jetson Orin Nano', 'Kai, an edge offline AI robot built in public'),
            ('hermes', 'Hermes Agentic Code Camp and Hackathon', 'First in the Philippines: 30+ builders shipped agents'),
            ('sui', 'Sui × DEVCON: Build Beyond', '330+ Move smart contracts verified on mainnet'),
            ('icp', 'ICP × DEVCON code camps', 'The biggest smart contracts code camp series in the Philippines'),
            ('caravan', 'Mindanao AI Caravan', 'Free AI education for kids, teachers, and builders in Mindanao')]
    disc_html = ''.join(f'<li><a class="disc-card" href="{L(k)}"><b>{t}</b><span>{r}</span><em>Read the case study</em></a></li>' for k, t, r in disc)
    hidden = ' hidden' if mode == 'spa' else ''
    return f'''<div class="page" data-page="{SPA}"{hidden}>
  <header class="page-hero page-hero--apc">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">Home</a><span aria-hidden="true">/</span><a href="{L('cs')}">DevRel Case Studies</a><span aria-hidden="true">/</span><span aria-current="page">#SHEISDEVCON × ABA</span></nav>
      <span class="eyebrow" style="color:var(--y)">Partner case study · #SHEISDEVCON × Austrian Business Agency</span>
      <h1 id="{SPA}-title">Nationwide #SHEISDEVCON code camps and hackathons, supported by the Austrian Business Agency</h1>
      <p class="cs-years"><span>2025–2026 · Two years · Manila to Mindanao</span></p>
      <p class="page-lead">Women in tech remain an underrepresented but highly skilled talent pool. For two years, the Austrian Business Agency has met them where they are: at #SHEISDEVCON code camps, summits, and hackathons from Manila to Iloilo to Davao, opening doors to global tech careers in Austria.</p>
      <div class="hero-btns"><a class="btn-primary btn-xl" href="{L('partner')}">Sponsor the next one</a><a class="btn-outline" href="{SCALE}">Help scale this program nationally</a></div>
    </div>
  </header>

  <section class="section" style="padding-top:28px"><div class="wrap">{fig('davao-group', 'More than a hundred students, mentors, and partners pose together under a giant THANK YOU at the #SHEISDEVCON Davao event', 'Students, mentors, and partners at #SHEISDEVCON Davao.', 'cs-fig--wide')}</div></section>

  <section class="numbers" aria-labelledby="sa-num"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">At a glance</span><h2 id="sa-num">Two years, four cities, one movement</h2></header>
    <ul class="numbers-grid" role="list">{stat('2 years', 'Of ABA support for #SHEISDEVCON', 'var(--y)')}{stat('4 cities', 'Manila, Iloilo, Cebu, and Davao', 'var(--p2)')}{stat('1st', 'Mindanao stop for ABA, in Davao', 'var(--o)')}{stat('100%', 'Free relocation and career guidance from ABA', 'var(--g)')}</ul>
  </div></section>

  <section class="section" aria-labelledby="sa-partner"><div class="wrap cs-split sa-partner">
    <div>
      <span class="eyebrow" style="color:var(--y)">The partner</span>
      <h2 class="cs-h2">Austria&#8217;s official location agency, in the room with Filipina builders</h2>
      <p class="lead-p">The Austrian Business Agency (ABA) is Austria&#8217;s official location agency under the Federal Ministry. Through WORK in AUSTRIA, it gives international IT professionals free, end-to-end relocation guidance, work permit advice, and global career matching.</p>
      <div class="sa-logo"><img src="{M('aba-logo')}" alt="Austrian Business Agency: Invest, Work, Film. Your easy access to Austria" loading="lazy"/></div>
      <div class="sa-person"><img src="{M('raphael')}" alt="Raphael Rey Bacolod speaking on stage" loading="lazy"/><div><b>Raphael Rey Bacolod</b><span>Director for Indonesia and the Philippines, Austrian Business Agency (WORK in AUSTRIA)</span><p>A steadfast champion of #SHEISDEVCON for two years, travelling from Manila to Iloilo, and in 2026 making ABA&#8217;s first stop in Mindanao to connect local talent directly with European tech opportunities.</p></div></div>
    </div>
    <div class="sa-video">
      <div class="yt-frame yt-frame--short"><iframe src="https://www.youtube-nocookie.com/embed/zqPUb6E7dX0?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0&amp;modestbranding=1" title="Career opportunities for Filipinos in Austria" loading="lazy" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
      <p class="yt-link"><a href="https://www.youtube.com/shorts/zqPUb6E7dX0" target="_blank" rel="noopener">Watch on YouTube<span class="sr-only"> (opens in a new tab)</span></a></p>
    </div>
  </div></section>

  <section class="section" aria-labelledby="sa-route"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">The route</span><h2 id="sa-route">From Manila to Mindanao</h2>
      <p>Great talent doesn&#8217;t only come from the capital. Each stop brought ABA closer to regional tech communities that traditional job fairs rarely reach.</p></header>
    <ul class="sa-stops" role="list">
      <li><img src="{M('manila-mentors')}" alt="Women mentors guiding students at a Move smart contracts code camp" loading="lazy"/><span class="sa-city">Manila</span><b>Move Smart Contracts Code Camp</b><span>Women mentors lead a full-day Web3 build with Sui.</span><a class="pp-link" href="{L('manila')}">DEVCON Manila</a></li>
      <li><img src="{M('iloilo-panel')}" alt="A panel of women tech leaders on stage at the She Builds Tech Summit in Iloilo" loading="lazy"/><span class="sa-city">Iloilo</span><b>She Builds Tech Summit</b><span>Panels, a pitch competition, and a community dinner.</span><a class="pp-link" href="{L('iloilo')}">DEVCON Iloilo</a></li>
      <li><img src="{M('cebu-ama')}" alt="Who run the world? Girls! Ask-us-anything session with women in tech from DEVCON Cebu" loading="lazy"/><span class="sa-city">Cebu</span><b>Who run the world? Girls!</b><span>An ask-us-anything with women in tech.</span><a class="pp-link" href="{L('cebu')}">DEVCON Cebu</a></li>
      <li><img src="{M('davao-champion')}" alt="The hackathon champion team holding certificates with mentors at SUBAY in Davao" loading="lazy"/><span class="sa-city">Davao</span><b>SUBAY: AI masterclass and hackathon</b><span>ABA&#8217;s first Mindanao stop, co-presenting the day.</span><a class="pp-link" href="{L('davao')}">DEVCON Davao</a></li>
    </ul>
  </div></section>

  <section class="section" aria-labelledby="sa-manila"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Manila · March 28, 2026</span><h2 id="sa-manila">Women mentors in action</h2>
      <p>At Colegio de San Juan de Letran in Intramuros, #SHEISDEVCON and the Move Smart Contracts Code Camp ran a full-day blockchain experience. Women mentors took the lead, guiding Letran students as they built their own smart contract portfolios on Sui, with hands-on coding support and real-time problem solving.</p></header>
    <div class="cs-split">
      {fig('manila-mentors', 'Four photos of women mentors helping students code and presenting a Git lesson', 'Women mentors guide students through their first smart contracts.')}
      {fig('manila-plenary', 'Raphael Bacolod giving the plenary talk From SheIsDevCon to Austria at a Letran podium', 'The plenary: From SheIsDevCon to Austria, pathways to an IT and tech career in the heart of Europe.')}
    </div>
  </div></section>

  <section class="section" aria-labelledby="sa-iloilo"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Iloilo</span><h2 id="sa-iloilo">She Builds Tech Summit</h2>
      <p>With Future Women Tech Founders, the Iloilo edition brought together female tech entrepreneurs, students, and regional IT leaders.</p></header>
    <ul class="sa-list" role="list"><li><b>A panel of women tech entrepreneurs:</b> Ilongga women on what it takes to thrive in tech and innovation.</li><li><b>A pitch competition</b> showcasing local startup ideas.</li><li><b>A community dinner with regional IT leaders:</b> the standout moment for ABA, a chance to exchange perspectives on the Iloilo ecosystem and talk openly about international career paths, including Austria.</li></ul>
    <div class="sa-trio">
      {fig('iloilo-panel', 'Women tech leaders on a panel at the She Builds Tech Summit')}
      {fig('iloilo-dinner', 'Organizers and regional tech leaders smiling at a long community dinner table')}
      {fig('iloilo-certificate', 'Raphael Bacolod receiving a certificate of appreciation on stage at the She Builds Tech Summit')}
    </div>
    <div class="sa-quotes">
      <blockquote><img src="{M('q-ted')}" alt="" loading="lazy"/><p>&#8220;In FWTF, we don&#8217;t just build technologies, we want to shape careers, develop confidence, and build a future where women lead in tech.&#8221;</p><footer><b>Ted Hyacinth T. Aspera</b><span>Founder, Future Women Tech Founders</span></footer></blockquote>
      <blockquote><img src="{M('q-ariessa')}" alt="" loading="lazy"/><p>&#8220;Innovation comes from the courage to be the &#8216;first&#8217; or the &#8216;only&#8217; until you are the &#8216;many&#8217;.&#8221;</p><footer><b>Marie Ariessa Lane C. Ko</b><span>Visayas Lead and Board Member, DEVCON Philippines</span></footer></blockquote>
    </div>
  </div></section>

  <section class="section" aria-labelledby="sa-davao"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Davao · October 14, 2026</span><h2 id="sa-davao">SUBAY: navigating the technical and ethical path in AI</h2>
      <p>DEVCON Davao and #SHEISDEVCON ran a full day at the University of Mindanao, Matina Campus, with ABA as co-presenter and major partner. It was ABA&#8217;s very first stop in Mindanao.</p></header>
    <div class="sa-mosaic">
      {fig('davao-keynote', 'Raphael Rey Bacolod delivering the keynote at the University of Mindanao podium', 'The keynote: connecting Mindanao talent with European tech opportunities.', 'sa-tall')}
      {fig('davao-austria-talk', 'A slide of quick facts about working in Austria: collective agreements, labour law, social security, and parental leave', 'Quick facts about working in Austria.')}
      {fig('davao-lab', 'Students coding at computers during the hackathon', 'The hackathon build.')}
      {fig('davao-pitch', 'Two students pitching BantayBuild, an AI-powered construction loss prevention and financial intelligence app', 'Pitching BantayBuild: AI for construction loss prevention.')}
    </div>
    <div class="sa-champ">
      {fig('davao-champion', 'The champion team and mentors holding certificates of excellence', None)}
      <div><span class="eyebrow" style="color:var(--y)">Hackathon champion</span><h3 class="sub-h">Girl, Boy, Bakla, Hapon</h3><p>From Ateneo de Davao University.</p>
        <h3 class="sub-h">Women leading the day</h3>
        <ul class="kai-people sa-people" role="list">
          <li><img src="{M('sp-altheae')}" alt="Altheae Owe" loading="lazy"/><b>Altheae Owe</b><span class="kai-role">#SHEISDEVCON Coordinator, DEVCON Davao</span><span>Lecturer at the University of Mindanao, bridging academic learning with industry exposure.</span></li>
          <li><img src="{M('sp-glyrhiz')}" alt="Glyrhiz Marhiel Tabamo" loading="lazy"/><b>Glyrhiz Marhiel Tabamo</b><span class="kai-role">President, DEVCON Bukidnon</span><span>Faculty at Central Mindanao University and founder of QuantumHive Innovations.</span></li>
        </ul></div>
    </div>
  </div></section>

  <section class="section" aria-labelledby="sa-why"><div class="wrap cs-split">
    <div>
      <span class="eyebrow" style="color:var(--y)">Why it matters</span>
      <h2 class="cs-h2">Trusted connections, early and local</h2>
      <p class="lead-p">ABA builds trusted connections with regional tech communities in markets where traditional job fairs can&#8217;t reach. Connecting early, locally, and through networks like #SHEISDEVCON makes a real difference.</p>
      <ul class="doc-list"><li><b>An underrepresented, highly skilled talent pool:</b> women in tech, from students to founders.</li><li><b>Beyond the capital:</b> Iloilo, Cebu, and Davao, not just Manila.</li><li><b>Global careers, made practical:</b> free relocation guidance, work permit advice, and career matching.</li></ul>
      <p><a class="pp-link" href="https://www.workinaustria.com/en/about-us/event-calendar/sheisdevcon-x-aba-manila-2026-smart-contracts-code-camp" target="_blank" rel="noopener">See the event on WORK in AUSTRIA<span class="sr-only"> (opens in a new tab)</span></a></p>
    </div>
    {fig('davao-attendees', 'Smiling students seated in an auditorium at the Davao event', 'Students at #SHEISDEVCON Davao.')}
  </div></section>

  <section class="section" aria-labelledby="sa-thanks"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Made possible together</span><h2 id="sa-thanks">Partners and collaborators</h2></header>
    <p class="sa-chips"><b>Supported by</b><span>Austrian Business Agency</span><span>Sui</span><span>Board of Investments</span></p>
    <p class="sa-chips"><b>Davao collaborators</b><span>Amihan</span><span>Avtica</span><span>Tutorials Dojo</span><span>Cowork Mugna</span><span>Mugna</span><span>Monde Nissin</span><span>Tiger</span><span>The Bloom</span><span>Davies</span><span>P&amp;G Printing Services</span></p>
    <p class="sa-chips"><b>Hosts and partners</b><span>University of Mindanao</span><span>DICT</span><span>Colegio de San Juan de Letran</span><span>Future Women Tech Founders</span></p>
    <p class="kai-links">Explore the program behind it all: <a class="pp-link" href="{L('she')}">#SHEISDEVCON</a>.</p>
  </div></section>

  <section class="section cs-discover" aria-labelledby="{SPA}-discover"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">More results</span><h2 id="{SPA}-discover">Discover other case studies and impactful results</h2></header>
    <ul class="disc-grid" role="list">{disc_html}</ul>
    <p style="margin-top:18px"><a class="pp-link" href="{L('cs')}">See all DevRel case studies</a></p>
  </div></section>

  <section class="page-cta">
    <div class="wrap">
      <h2>Sponsor the next one</h2>
      <p>Help scale #SHEISDEVCON code camps and hackathons nationally, across 13 locations and beyond the capital, in 2027.</p>
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

CSS = ('.sa-partner{align-items:start}.sa-logo{margin:16px 0;padding:16px 20px;border-radius:16px;background:#fff;max-width:340px}.sa-logo img{display:block;width:100%;height:auto}'
       '.sa-person{display:grid;grid-template-columns:110px minmax(0,1fr);gap:14px;align-items:start;margin-top:8px}.sa-person img{width:110px;height:110px;border-radius:16px;object-fit:cover;object-position:50% 20%}'
       '.sa-person b{display:block;color:#fff;font-weight:900}.sa-person span{display:block;color:var(--y);font-weight:800;font-size:.86rem}.sa-person p{margin:6px 0 0;color:var(--text-secondary);line-height:1.55}'
       '.sa-video{display:flex;flex-direction:column;align-items:center}.sa-video .yt-frame--short{width:100%;max-width:320px}'
       '.sa-stops{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}'
       '.sa-stops li{display:flex;flex-direction:column;gap:6px;padding-bottom:12px;border-radius:18px;overflow:hidden;background:rgba(255,255,255,.04);border:1px solid var(--line)}'
       '.sa-stops img{width:100%;aspect-ratio:4/3;object-fit:cover;object-position:50% 50%}.sa-stops li>*:not(img){margin:0 14px}'
       '.sa-city{color:var(--y);font-weight:900;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase}.sa-stops b{color:#fff;font-weight:900}.sa-stops span:not(.sa-city){color:var(--text-secondary);font-size:.9rem;line-height:1.45}'
       '.sa-list{list-style:none;margin:0 0 18px;padding:0;display:grid;gap:8px}.sa-list li{padding:12px 16px;border-radius:14px;background:rgba(255,255,255,.04);border:1px solid var(--line);color:var(--text-secondary)}.sa-list b{color:#fff}'
       '.sa-trio{display:grid;grid-template-columns:1.2fr 1.2fr .8fr;gap:12px}.sa-trio .cs-fig{margin:0}.sa-trio img{width:100%;height:100%;aspect-ratio:auto;object-fit:cover;max-height:300px}'
       '.sa-quotes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:18px}'
       '.sa-quotes blockquote{margin:0;display:grid;grid-template-columns:72px minmax(0,1fr);gap:4px 14px;padding:18px;border-radius:18px;background:rgba(236,72,153,.08);border:1px solid rgba(236,72,153,.4)}'
       '.sa-quotes img{grid-row:span 2;width:72px;height:72px;border-radius:50%;object-fit:cover}.sa-quotes p{margin:0;color:#fff;font-size:1.02rem;line-height:1.55}'
       '.sa-quotes footer b{display:block;color:#fff}.sa-quotes footer span{color:var(--text-secondary);font-size:.86rem}'
       '.sa-mosaic{display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:auto auto;gap:12px}.sa-mosaic .cs-fig{margin:0}.sa-mosaic .sa-tall{grid-row:span 2}.sa-mosaic img{width:100%;height:100%;object-fit:cover}'
       '.sa-champ{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:20px;align-items:start;margin-top:20px}.sa-champ .cs-fig{margin:0}.sa-people{margin-top:8px}'
       '.sa-chips{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:0 0 12px}.sa-chips b{color:#fff;margin-right:4px}.sa-chips span{padding:4px 12px;border-radius:999px;background:rgba(255,255,255,.05);border:1px solid var(--line);color:var(--text-secondary);font-size:.86rem;font-weight:700}'
       '@media (max-width:1000px){.sa-stops{grid-template-columns:repeat(2,minmax(0,1fr))}.sa-mosaic{grid-template-columns:1fr 1fr}.sa-mosaic .sa-tall{grid-row:auto;grid-column:1/-1}.sa-champ{grid-template-columns:minmax(0,1fr)}}'
       '@media (max-width:640px){.sa-stops,.sa-trio,.sa-quotes,.sa-mosaic{grid-template-columns:minmax(0,1fr)}.sa-person{grid-template-columns:80px minmax(0,1fr)}.sa-person img{width:80px;height:80px}}')

CARD = lambda href, thumb: (f'<article class="case" id="{SPA}-card" data-cats="events camps web3 ai" style="--c:#EC4899">\n'
    f'        <a class="case-thumb" href="{href}" tabindex="-1" aria-hidden="true"><img src="{thumb}" alt="" loading="lazy" width="1400" height="440"/></a>\n'
    f'        <div class="case-main">\n          <div class="case-top"><span class="case-ic" aria-hidden="true"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M12 12v9M8.5 17.5h7"/></svg></span><span class="prog-tag">#SHEISDEVCON · Austrian Business Agency</span></div>\n'
    f'          <h2><a class="case-title-link" href="{href}">Nationwide #SHEISDEVCON code camps and hackathons, supported by the Austrian Business Agency</a></h2>'
    f'<ul class="cs-tags" role="list"><li class="cs-tag cs-tag--cat">Events and summits</li><li class="cs-tag cs-tag--cat">Code camps</li><li class="cs-tag cs-tag--cat">Web3 and blockchain</li><li class="cs-tag cs-tag--cat">AI and agentic</li><li class="cs-tag">Women in tech</li><li class="cs-tag">Global careers</li><li class="cs-tag">Austria</li></ul>'
    f'<p class="cs-years"><span>2025–2026 · Two years</span></p>\n'
    f'          <div class="case-block"><h3>The goal</h3><p>Connect an underrepresented, highly skilled talent pool, women in tech, with global career paths, early and locally.</p></div>\n'
    f'          <div class="case-block"><h3>What we did</h3><p>#SHEISDEVCON code camps, summits, and hackathons from Manila to Iloilo, Cebu, and Davao, with ABA on stage at every stop and in Mindanao for the first time.</p><p><a class="pp-link" href="{href}">Read the full case study</a></p></div>\n'
    f'        </div>\n        <aside class="case-results" aria-label="Results"><p class="case-results-h">Results</p><ul role="list"><li><b>2 years</b><span>of ABA support</span></li><li><b>4 cities</b><span>Luzon, Visayas, Mindanao</span></li><li><b>1st</b><span>Mindanao stop for ABA</span></li></ul></aside>\n      </article>\n      ')

if __name__ == '__main__':
    # folder page from the Orin case study as the template (same depth, shared styles)
    src = open('docs/case-studies/devcon-studios-nvidia-orin-nano/index.html', encoding='utf-8').read()
    ot = re.search(r'<title>([^<]*)</title>', src).group(1); od = re.search(r'<meta name="description" content="([^"]*)"', src).group(1)
    a = src.index('<div class="page" data-page="orin-nano"'); b = src.index('</main>')
    out = src[:a] + page('docs') + src[b:]
    out = out.replace(ot, TITLE).replace(od, DESC).replace('https://devcon.ph/case-studies/devcon-studios-nvidia-orin-nano/', f'https://devcon.ph/{PATH}/')
    if CSS not in out: out = out.replace('</style>', CSS + '</style>', 1)
    open(f'docs/{PATH}/index.html', 'w', encoding='utf-8').write(out)
    # hub thumbnail and card (first)
    from PIL import Image, ImageOps
    ImageOps.fit(Image.open(f'{MEDIA}davao-group.webp').convert('RGB'), (1400, 440), Image.LANCZOS, centering=(0.5, 0.5)).save(f'docs/case-studies/thumbs/sheisdevcon-aba.webp', quality=72, method=6)
    f = 'docs/case-studies/index.html'; h = open(f, encoding='utf-8').read()
    h = re.sub(r'<article class="case" id="sheisdevcon-aba-card".*?</article>\s*', '', h, flags=re.S)
    i = h.index('<article class="case"'); h = h[:i] + CARD('sheisdevcon-aba/', 'thumbs/sheisdevcon-aba.webp') + h[i:]
    open(f, 'w', encoding='utf-8').write(h)
    # single-file build
    c = glob.glob('combined/*.html')[0]; t = open(c, encoding='utf-8').read()
    t = re.sub(r'<div class="page" data-page="sheisdevcon-aba".*?</div>\n(?=</main>|<div class="page")', '', t, flags=re.S)
    t = re.sub(r'<article class="case" id="sheisdevcon-aba-card".*?</article>\s*', '', t, flags=re.S)
    i = t.index('</main>'); t = t[:i] + page('spa') + t[i:]
    a = t.index('<div class="page" data-page="case-studies"'); j = t.index('<article class="case"', a)
    thumb = 'data:image/webp;base64,' + base64.b64encode(open('docs/case-studies/thumbs/sheisdevcon-aba.webp', 'rb').read()).decode()
    t = t[:j] + CARD('#/sheisdevcon-aba', thumb) + t[j:]
    if CSS not in t: t = t.replace('</style>', CSS + '</style>', 1)
    open(c, 'w', encoding='utf-8').write(t)
    # sitemap, url map, llms
    sm = open('docs/sitemap.xml').read()
    if PATH not in sm: open('docs/sitemap.xml', 'w').write(sm.replace('</urlset>', f'  <url><loc>https://devcon.ph/{PATH}/</loc><lastmod>2026-10-16</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n</urlset>'))
    um = json.load(open('docs/url-map.json'))
    if f'/{PATH}/' not in um['pages']: um['pages'] = sorted(um['pages'] + [f'/{PATH}/'])
    json.dump(um, open('docs/url-map.json', 'w'), indent=1)
    ll = open('docs/llms.txt').read()
    if PATH not in ll:
        k = ll.find('- [DEVCON Studios x NVIDIA'); line = f'- [#SHEISDEVCON x Austrian Business Agency](https://devcon.ph/{PATH}/): two years of women in tech code camps and hackathons, Manila to Mindanao\n'
        open('docs/llms.txt', 'w').write(ll[:k] + line + ll[k:] if k >= 0 else ll + line)
    print('built', PATH)
