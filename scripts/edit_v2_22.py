# v2.22: region anchors, volunteer-capacity message, working preview image URL, large chapter names
import re, glob, os, json
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
PROD = 'https://devcon.ph'
FILES = [f for f in glob.glob('docs/**/*.html', recursive=True)] + glob.glob('combined/*.html')
CITIES = {'bacolod': 'Bacolod', 'bohol': 'Bohol', 'bukidnon': 'Bukidnon', 'cagayandeoro': 'Cagayan de Oro', 'cebu': 'Cebu', 'davao': 'Davao', 'iligan': 'Iligan',
          'iloilo': 'Iloilo', 'laguna': 'Laguna', 'legazpi': 'Legazpi', 'manila': 'Manila', 'pampanga': 'Pampanga', 'tacloban': 'Tacloban'}
TEXT = [
 # homepage: inside the existing "not an events company" paragraph
 ('Every program we run is a public good, free and open to the Filipino tech community.</p>',
  'Every program we run is a public good, free and open to the Filipino tech community. Because we are volunteer-run, our capacity to accept every invitation or open new chapters depends on our volunteer leaders, partner resources, and strategic national priorities.</p>'),
 # locations: inside "We grow chapters, not pins on a map"
 ('long-term alignment with DEVCON as a non-profit, beyond seed funds and tech hype.</p>',
  'long-term alignment with DEVCON as a non-profit, beyond seed funds and tech hype. As a volunteer-run community, how many chapters we can open is limited by our volunteer leaders&#8217; capacity, partner resources, and strategic national priorities.</p>'),
 # invite: inside the volunteer-led line
 ('Our speakers are volunteers who share their time and expertise for free to pay it forward.</p>',
  'Our speakers are volunteers who share their time and expertise for free to pay it forward. As such, we can&#8217;t accept every invitation: what we can take on depends on our volunteer leaders&#8217; capacity, partner resources, and strategic national priorities.</p>'),
]
CSS = ('.dcc-card[id]{scroll-margin-top:96px}'
       '.ch-h1 .ch-meet{display:block;font-size:clamp(20px,2.4vw,32px);line-height:1.2;letter-spacing:0;color:var(--y);margin-bottom:4px}'
       '.ch-h1 .ch-name{display:block;font-size:clamp(46px,10vw,128px);line-height:.95;letter-spacing:-.02em}'
       '.ft-regions h3 a{color:inherit;text-decoration:none;display:inline-flex;align-items:center;min-height:44px;min-width:44px;padding-right:6px}.ft-regions h3 a:hover{color:var(--y);text-decoration:underline}')
stats = {'og': 0, 'text': 0, 'chapter_line': 0, 'h1': 0, 'anchors': 0, 'footer': 0}
for f in FILES:
    s = open(f, encoding='utf-8').read(); o = s
    # preview image: working absolute URL on production (devcon.ph still serves the old site)
    n = s.count('https://devcon.ph/og-devcon-17.png'); s = s.replace('https://devcon.ph/og-devcon-17.png', f'{PROD}/og-devcon-17.png'); stats['og'] += n
    for a, b in TEXT:
        if a in s and b not in s: s = s.replace(a, b); stats['text'] += 1
    # chapter pages: one short clause in the existing volunteer-led line
    def line(m):
        stats['chapter_line'] += 1
        return f'{m.group(1)} is run entirely by volunteers who pay it forward, so what the chapter can take on depends on its volunteer leaders and partner resources.'
    s = re.sub(r'(DEVCON (?:Bacolod|Bohol|Bukidnon|Cagayan de Oro|Cebu|Davao|Iligan|Iloilo|Laguna|Legazpi|Manila|Pampanga|Tacloban)) is run entirely by volunteers who pay it forward\.(?! so)', line, s)
    # chapter headline: "Meet DEVCON" small, the location name large
    def h1(m):
        stats['h1'] += 1
        return f'<h1 id="chapter-{m.group(1)}-title" class="ch-h1"><span class="ch-meet">Meet DEVCON</span> <span class="ch-name">{m.group(2)}</span></h1>'
    s = re.sub(r'<h1 id="chapter-([a-z]+)-title">Meet DEVCON ([^<]+)</h1>', h1, s)
    # region anchors on the Locations cards, and links from the intro
    for r in ('luzon', 'visayas', 'mindanao'):
        s, k = re.subn(rf'<div class="dcc-card dcc-{r}" style=', f'<div class="dcc-card dcc-{r}" id="{r}" style=', s, count=1) if f'id="{r}"' not in s and ('data-page="chapters"' in s) else (s, 0)
        stats['anchors'] += k
    if f == 'docs/locations/index.html':
        s = s.replace('13 locations across Luzon, Visayas, and Mindanao,', '13 locations across <a class="pp-link reg-link" href="#luzon">Luzon</a>, <a class="pp-link reg-link" href="#visayas">Visayas</a>, and <a class="pp-link reg-link" href="#mindanao">Mindanao</a>,', 1)
    # footer region headings link to the anchors (folder pages only; the single file uses hash routing)
    if f.startswith('docs'):
        m = re.search(r'href="([^"]*)locations/manila/"', s[s.find('ft-regions'):]) if 'ft-regions' in s else None
        if m:
            pre = m.group(1)
            for r, name in (('luzon', 'Luzon'), ('visayas', 'Visayas'), ('mindanao', 'Mindanao')):
                if f'<h3>{name}</h3>' in s:
                    s = s.replace(f'<h3>{name}</h3>', f'<h3><a href="{pre}locations/#{r}">{name}</a></h3>', 1); stats['footer'] += 1
    if s != o:
        if '<style' in s and CSS not in s: s = s.replace('</style>', CSS + '</style>', 1)
        open(f, 'w', encoding='utf-8').write(s)
print(stats)
# short region addresses -> Locations anchors (Cloudflare 301 rules plus redirect pages)
lines = open('docs/_redirects').read().rstrip('\n').split('\n')
add = []
for r in ('luzon', 'visayas', 'mindanao'):
    for src in (f'/{r}', f'/{r}/', f'/locations/{r}', f'/locations/{r}/'):
        if not any(l.split(' ')[0] == src for l in lines): add.append(f'{src} /locations/#{r} 301')
i = next(n for n, l in enumerate(lines) if l.startswith('/index.html')); lines[i:i] = add
open('docs/_redirects', 'w').write('\n'.join(lines) + '\n')
stub = open('docs/cebu/index.html', encoding='utf-8').read()
for r in ('luzon', 'visayas', 'mindanao'):
    for d, rel in ((f'docs/{r}', f'../locations/#{r}'), (f'docs/locations/{r}', f'../#{r}')):
        os.makedirs(d, exist_ok=True)
        open(f'{d}/index.html', 'w', encoding='utf-8').write(stub.replace('../locations/cebu/', rel).replace('https://devcon.ph/locations/cebu/', f'https://devcon.ph/locations/#{r}'))
print('region redirects added:', len(add))
