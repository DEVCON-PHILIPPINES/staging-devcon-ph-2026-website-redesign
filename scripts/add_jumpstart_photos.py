# Jumpstart Internships: event photos distributed through the page (docs folder page and single-file build)
import re, glob, json, base64, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ALT = json.load(open('/tmp/js_alts.json')) if os.path.exists('/tmp/js_alts.json') else {}
MEDIA = 'docs/programs/jumpstart-internships/media/'
def src(k, mode):
    return f'media/{k}.webp' if mode == 'docs' else 'data:image/webp;base64,' + base64.b64encode(open(f'{MEDIA}{k}.webp', 'rb').read()).decode()
def gal(keys, mode, cls='', cap=None):
    lis = ''.join(f'<li><img src="{src(k, mode)}" alt="{ALT[k]}" loading="lazy"/></li>' for k in keys)
    c = f'<p class="js-cap">{cap}</p>' if cap else ''
    return f'<div class="merge-block js-photos"><ul class="js-gal {cls}" role="list">{lis}</ul>{c}</div>'
LIFE = lambda mode: (f'<section class="section js-life" aria-labelledby="js-life-t"><div class="wrap">'
    f'<header class="sec-head"><span class="eyebrow" style="color:var(--y)">Life at Jumpstart</span><h2 id="js-life-t">Real builds, real mentors, real teammates</h2>'
    f'<p>Five months at the DEVCON HQ main office in Ortigas and our AI events space in Makati: building with hardware and AI, learning from mentors, and shipping work the community uses.</p></header>'
    f'<ul class="js-gal js-gal--lead" role="list">' + ''.join(f'<li><img src="{src(k, mode)}" alt="{ALT[k]}" loading="lazy"/></li>' for k in ['js-cohort', 'js-focus', 'js-rover', 'js-demo']) + '</ul></div></section>')
PLACE = [('Build AI that the country can actually use', ['js-hardware', 'js-kits', 'js-mars'], 'js-gal--3', 'Hands-on with robotics kits, micro:bit, and AI.'),
         ('A portfolio you&#8217;ll be proud of', ['js-present', 'js-cohort1'], 'js-gal--2', 'Interns present their work to mentors, partners, and the community.'),
         ('More than an internship', ['js-launchpad', 'js-security', 'js-claude', 'js-mentoring', 'js-planning', 'js-reading'], 'js-gal--3', 'Sessions on AI, security, product, and leadership, with mentors from the industry.'),
         ('In their words', ['js-booth', 'js-interview', 'js-team'], 'js-gal--3', 'Out in the community, from event booths to the main stage.')]
CSS = ('.js-photos{grid-column:1/-1;width:100%}.js-gal{list-style:none;margin:0;padding:0;display:grid;gap:12px}.js-gal li{margin:0}'
       '.js-gal img{display:block;width:100%;height:100%;aspect-ratio:4/3;object-fit:cover;object-position:50% 50%;border-radius:16px;border:1px solid var(--line)}'
       '.js-gal--2{grid-template-columns:repeat(2,minmax(0,1fr))}.js-gal--3{grid-template-columns:repeat(3,minmax(0,1fr))}'
       '.js-gal--lead{grid-template-columns:repeat(3,minmax(0,1fr))}.js-gal--lead li:first-child{grid-column:1/-1}.js-gal--lead li:first-child img{aspect-ratio:21/9}'
       '.js-cap{margin:10px 0 0;color:var(--text-secondary);font-size:.9rem}'
       '@media (max-width:760px){.js-gal--2,.js-gal--3,.js-gal--lead{grid-template-columns:repeat(2,minmax(0,1fr))}.js-gal--lead li:first-child img{aspect-ratio:16/9}}'
       '@media (max-width:480px){.js-gal--2,.js-gal--3,.js-gal--lead{grid-template-columns:minmax(0,1fr)}}')
def edit(P, mode):
    if 'js-life' in P: return P
    # 1) photo row right after the numbers
    j = P.index('</section>', P.index('<section class="numbers"')) + len('</section>')
    P = P[:j] + '\n  ' + LIFE(mode) + P[j:]
    # 2) photos inside themed sections
    for h2, keys, cls, cap in PLACE:
        i = P.index(h2); k = P.index('</div></section>', i) if P.find('</div></section>', i) != -1 and P.find('</div></section>', i) < P.find('<section', i + 10) else None
        if k is None:
            k = P.rindex('</div>', i, P.find('</section>', i)); k = P.rfind('</div>', i, P.find('</section>', i))
        P = P[:k] + gal(keys, mode, cls, cap) + P[k:]
    # 3) keep background bands alternating after the numbers row
    idx = [m.start() for m in re.finditer(r'\n  <section class="(?:section[^"]*|page-cta|numbers)"', P)]
    last = P.rindex('</section>') + len('</section>'); rows = [P[a:(idx[n + 1] if n + 1 < len(idx) else last)] for n, a in enumerate(idx)]
    kk = next(n for n, r in enumerate(rows) if 'class="numbers"' in r[:80]); out = []
    for n, r in enumerate(rows):
        if n <= kk or 'page-cta' in r[:60]: out.append(r); continue
        band = ((n - kk - 1) % 2 == 1); o = re.match(r'\s*<section class="([^"]*)"', r); cls = re.sub(r'\s*\bband2\b', '', o.group(1))
        out.append(r.replace(f'class="{o.group(1)}"', f'class="{cls.replace("section", "section band2", 1) if band else cls}"', 1))
    return P[:idx[0]] + ''.join(out) + P[last:]
for f, mode in [('docs/programs/jumpstart-internships/index.html', 'docs')] + [(c, 'spa') for c in glob.glob('combined/*.html')]:
    s = open(f, encoding='utf-8').read()
    a = s.index('<div class="page" data-page="internships"'); b = s.find('<div class="page"', a + 10); b = s.index('</main>') if b < 0 else b
    s = s[:a] + edit(s[a:b], mode) + s[b:]
    if CSS not in s: s = s.replace('</style>', CSS + '</style>', 1)
    open(f, 'w', encoding='utf-8').write(s); print('photos added in', 'docs page' if mode == 'docs' else 'single file')
