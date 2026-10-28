# Per-page link preview images: each page gets a 1200x630 JPEG cut from its most representative content photo,
# with a soft bottom shade and the DEVCON 17 logo. Pages without a usable photo keep the default (og-devcon-17.jpg).
import re, os, io, json, base64, html, sys
from PIL import Image, ImageDraw, ImageOps
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, 'scripts')
import build_og_default as dflt
SITE = 'https://devcon.ph'
W, H = 1200, 630
SKIP_ALT = re.compile(r'logo|icon|badge|qr|wordmark|sticker', re.I)
# pages whose first photo is not the best one: pick a better source by file name (optional overrides)
PREFER = {'/case-studies/microbit/': 'Students working together', '/case-studies/zoho-creator/': 'Photo collage'}
FORCE_DEFAULT = {'/case-studies/'}  # the hub represents every story, so it keeps the brand image
LOGO = None

def load(src, page_dir):
    if src.startswith('data:image/svg'): return None
    if src.startswith('data:'):
        try: return Image.open(io.BytesIO(base64.b64decode(src.split(',', 1)[1])))
        except Exception: return None
    if src.startswith('http') or src.endswith('.svg'): return None
    p = os.path.normpath(os.path.join(page_dir, src.split('#')[0].split('?')[0]))
    try: return Image.open(p)
    except Exception: return None

def candidates(f):
    s = open(f, encoding='utf-8').read()
    a = s.find('<div class="page" data-page'); b = s.find('</main>', a)
    if a < 0: return []
    main = s[a:b]
    main = re.sub(r'<(ul|div) class="[^"]*(?:logo|marquee|lgo|tm-people|kai-people|sa-quotes|sa-person|tools-strip|acc-logos)[^"]*".*?</\1>', ' ', main, flags=re.S)
    out = []
    for m in re.finditer(r'<img\b([^>]*)>', main):
        attrs = m.group(1); src = re.search(r'src="([^"]+)"', attrs); alt = re.search(r'alt="([^"]*)"', attrs)
        if not src: continue
        src = src.group(1); alt = html.unescape(alt.group(1)) if alt else ''
        if SKIP_ALT.search(alt) or SKIP_ALT.search(src.split('/')[-1] if not src.startswith('data:') else ''): continue
        out.append((src, alt))
    return out

def pick(f, p=None):
    d = os.path.dirname(f)
    cands = candidates(f)
    if p in PREFER: cands = [c for c in cands if PREFER[p] in c[1]] + [c for c in cands if PREFER[p] not in c[1]]
    for src, alt in cands:
        im = load(src, d)
        if im is None: continue
        w, h = im.size
        if w < 700 or h < 340: continue
        r = w / h
        if r < 1.0 or r > 3.4: continue
        return im.convert('RGB'), src, alt
    # stories: fall back to the story's card photo on Partner Success Stories
    m = re.match(r'/case-studies/([^/]+)/$', p or '')
    if m:
        t = os.path.join('docs/case-studies/thumbs', m.group(1) + '.webp')
        if os.path.isfile(t): return Image.open(t).convert('RGB'), t, 'card photo'
    return None


def faces(im):
    """Face boxes (x, y, w, h) in source pixels, found with OpenCV's Haar cascades."""
    try:
        import cv2, numpy as np
    except Exception:
        return []
    s = min(1.0, 1600 / max(im.size)); small = im.resize((int(im.width * s), int(im.height * s))) if s < 1 else im
    g = cv2.cvtColor(np.array(small.convert('RGB')), cv2.COLOR_RGB2GRAY); g = cv2.equalizeHist(g)
    found = []
    for name in ('haarcascade_frontalface_alt2.xml', 'haarcascade_frontalface_default.xml'):
        c = cv2.CascadeClassifier(cv2.data.haarcascades + name)
        mn = max(14, int(min(g.shape) * 0.018))
        for (x, y, w, h) in c.detectMultiScale(g, scaleFactor=1.08, minNeighbors=6, minSize=(mn, mn)):
            found.append((x / s, y / s, w / s, h / s))
    # merge overlaps
    out = []
    for f in sorted(found, key=lambda b: -b[2]):
        if not any(abs(f[0] - o[0]) < o[2] * .5 and abs(f[1] - o[1]) < o[3] * .5 for o in out): out.append(f)
    return out

def focus_crop(im):
    """Crop to 1200x630 without cutting heads: keep every face (with headroom) or, if they cannot all fit, the top row of heads."""
    W0, H0 = im.size; R = W / H; fs = faces(im)
    if W0 / H0 >= R:  # wider than the card: full height, slide sideways
        cw = int(H0 * R); ch = H0
        if fs:
            l = min(f[0] for f in fs); r = max(f[0] + f[2] for f in fs); cx = (l + r) / 2
        else:
            cx = W0 / 2
        x0 = int(max(0, min(W0 - cw, cx - cw / 2))); y0 = 0
    else:  # taller than the card: full width, slide vertically
        cw = W0; ch = int(W0 / R); x0 = 0
        if fs:
            fh = sorted(f[3] for f in fs)[len(fs) // 2]
            top = max(0, min(f[1] for f in fs) - fh * .9); bottom = max(f[1] + f[3] for f in fs) + fh * .5
            if bottom - top <= ch: y0 = top - (ch - (bottom - top)) * .35
            else: y0 = top
        else:
            y0 = (H0 - ch) * .3
        y0 = int(max(0, min(H0 - ch, y0)))
    return im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.LANCZOS), len(fs)

def compose(im):
    global LOGO
    if LOGO is None:
        lg = dflt.logo_cut(); lh = 46; LOGO = lg.resize((int(lg.width * lh / lg.height), lh), Image.LANCZOS)
    c, _n = focus_crop(im)
    shade = Image.new('L', (W, H), 0); sd = ImageDraw.Draw(shade)
    for y in range(H):
        t = max(0, (y - H * .70) / (H * .30)); sd.line([(0, y), (W, y)], fill=int(190 * t ** 1.6))
    c = Image.composite(Image.new('RGB', (W, H), (8, 6, 36)), c, shade)
    c.paste(LOGO, (40, H - LOGO.height - 34), LOGO)
    return c

def page_title(s):
    t = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1)).strip()
    return re.split(r'\s+\|\s+', t)[0]

if __name__ == '__main__':
    pages = json.load(open('docs/url-map.json'))['pages']
    os.makedirs('docs/og', exist_ok=True)
    report = []
    for p in pages:
        f = 'docs' + p + 'index.html'
        if p == '/' or not os.path.isfile(f): continue
        s = open(f, encoding='utf-8').read()
        got = None if p in FORCE_DEFAULT else pick(f, p)
        slug = p.strip('/').replace('/', '--')
        if got:
            im, src, alt = got
            out = compose(im); path = f'docs/og/{slug}.jpg'; q = 84
            while True:
                out.save(path, 'JPEG', quality=q, optimize=True, progressive=True)
                if os.path.getsize(path) < 280_000 or q <= 60: break
                q -= 4
            url = f'{SITE}/og/{slug}.jpg'; alt_txt = page_title(s)
            report.append((p, 'own', alt[:60], os.path.getsize(path) // 1024))
        else:
            url = f'{SITE}/og-devcon-17.jpg'; alt_txt = 'DEVCON Philippines: Engineering an AI-Ready Nation'
            report.append((p, 'default', '', 0))
        s2 = re.sub(r'(<meta property="og:image" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), s)
        s2 = re.sub(r'(<meta name="twitter:image" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), s2)
        s2 = re.sub(r'(<meta property="og:image:alt" content=")[^"]*(")', lambda m: m.group(1) + html.escape(alt_txt, quote=True) + m.group(2), s2)
        s2 = re.sub(r'(<meta name="twitter:image:alt" content=")[^"]*(")', lambda m: m.group(1) + html.escape(alt_txt, quote=True) + m.group(2), s2)
        s2 = s2.replace('<meta property="og:image:type" content="image/png"/>', '<meta property="og:image:type" content="image/jpeg"/>')
        if s2 != s: open(f, 'w', encoding='utf-8').write(s2)
    json.dump([{'page': p, 'image': k, 'source_alt': a, 'kb': kb} for p, k, a, kb in report], open('/tmp/og_report.json', 'w'), indent=1)
    own = [r for r in report if r[1] == 'own']; print(f'{len(own)} pages got their own image, {len(report) - len(own)} keep the default')
