# v2.32: volunteer communities drop the 2025 impact report row, the numbers, and testimonies;
# active chapters get one concise, optimistic note on how chapters grow.
import re, glob, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
COMBINED = glob.glob('combined/*.html')[0]
ACTIVE = {'manila': 'Manila', 'laguna': 'Laguna', 'legazpi': 'Legazpi', 'pampanga': 'Pampanga', 'cebu': 'Cebu', 'iloilo': 'Iloilo', 'davao': 'Davao', 'iligan': 'Iligan', 'bukidnon': 'Bukidnon'}
VC = ['bohol', 'cagayandeoro', 'tacloban']
log = {}
def bump(k, n=1): log[k] = log.get(k, 0) + n
def reband(P):
    parts = re.split(r'(?=\n  <section class=")', P)
    head, body = parts[0], parts[1:]; out = []; n = 0
    for r in body:
        o = re.match(r'\s*<section class="([^"]*)"', r); cls = o.group(1)
        if 'page-cta' in cls or cls.startswith('numbers'): out.append(r); continue
        base = re.sub(r'\s*\bband2\b', '', cls); new = base.replace('section', 'section band2', 1) if n % 2 == 0 else base
        out.append(r.replace(f'class="{cls}"', f'class="{new}"', 1)); n += 1
    return head + ''.join(out)
def qoq(c, mode):
    link = '#/invite' if mode == 'spa' else '../../invite/#start-a-chapter'
    return (f'<header class="sec-head"><span class="eyebrow" style="color:var(--y)">How chapters grow</span><h3 class="sub-h" id="{c}-qoq">Built by volunteers, earned through impact</h3>\n'
            f'      <p>Every DEVCON chapter is led by local volunteer officers and earns its place through regular, free programs that meet shared standards. '
            f'We review each chapter yearly so its community can count on it, and we grow as committed leaders step up in new cities. <a class="pp-link" href="{link}">Start a chapter in your city</a></p></header>')
def active_edit(P, c, mode):
    P, k = re.subn(r'<header class="sec-head"><span class="eyebrow" style="color:var\(--y\)">Quality over quantity</span><h3 class="sub-h" id="' + c + r'-qoq">.*?</header>\s*<p class="qoq-note">.*?</p>', lambda m: qoq(c, mode), P, count=1, flags=re.S)
    bump('active: quality block rewritten', k)
    P, k = re.subn(r'(<p class="ethos-line ethos-line--cta"><span class="ethos-tag">Volunteer-led</span>)DEVCON ' + re.escape(ACTIVE[c]) + r' is run entirely by volunteers who pay it forward[^<]*</p>',
                   lambda m: m.group(1) + f'DEVCON {ACTIVE[c]} is run by volunteers who pay it forward. Every program is free and built for the public good.</p>', P, count=1)
    bump('active: closing line rewritten', k)
    return P
def vc_edit(P, c):
    # the 2025 impact report row: story text and featured events; the Moments photos stay
    def story(m):
        sec = m.group(0)
        sec = re.sub(r'<div class="ch-story-main">.*?</div>\s*(?=<aside class="ch-story-side")', '', sec, count=1, flags=re.S)
        sec = re.sub(r'<aside class="ch-story-side"[^>]*>.*?</aside>\s*', '', sec, count=1, flags=re.S)
        sec = sec.replace('<div class="wrap ch-story-grid">', '<div class="wrap">', 1)
        sec = re.sub(r' aria-labelledby="[^"]*-story"', '', sec, count=1)
        return sec
    if '2025 impact report' in P:
        P, k = re.subn(r'<section class="[^"]*ch-story[^"]*".*?</section>', story, P, count=1, flags=re.S); bump('vc: impact report row removed', k)
    P, k = re.subn(r'\n  <section class="numbers" aria-labelledby="[^"]*-num">.*?</section>', '', P, count=1, flags=re.S); bump('vc: numbers and testimonies removed', k)
    return reband(P)
for f in glob.glob('docs/locations/*/index.html') + [COMBINED]:
    s = open(f, encoding='utf-8').read(); o = s
    for c in list(ACTIVE) + VC:
        if f == COMBINED:
            a = s.find(f'<div class="page" data-page="chapter-{c}"')
            if a < 0: continue
            b = s.find('<div class="page"', a + 10); m = s.find('</main>', a); b = m if b < 0 or m < b else b
            seg = s[a:b]; seg = active_edit(seg, c, 'spa') if c in ACTIVE else vc_edit(seg, c); s = s[:a] + seg + s[b:]
        elif f == f'docs/locations/{c}/index.html':
            s = active_edit(s, c, 'docs') if c in ACTIVE else vc_edit(s, c)
    if s != o: open(f, 'w', encoding='utf-8').write(s)
print(log)
