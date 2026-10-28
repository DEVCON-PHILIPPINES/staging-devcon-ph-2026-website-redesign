# Default and homepage link preview image: 1200x630, logo and text centered inside the middle square (safe for phone crops), under 300 KB.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FONT = os.environ.get('MONTSERRAT', '/tmp/fonts/Montserrat.ttf')
SUB = ['The country\u2019s largest volunteer tech community.', '13 locations nationwide.']
og = Image.open('docs/og-devcon-17.png').convert('RGB'); W, H = 1200, 630
def font(sz, w): f = ImageFont.truetype(FONT, sz); f.set_variation_by_axes([w]); return f
def logo_cut():
    reg = og.crop((0, 0, 520, 212)); px = reg.load()
    rows = [any(max(px[x, y]) > 120 for x in range(0, reg.width, 2)) for y in range(reg.height)]
    y0 = next(y for y, v in enumerate(rows) if v); y1 = y0
    while y1 < reg.height and (rows[y1] or any(rows[y1:y1 + 6])): y1 += 1
    xs = [x for y in range(y0, y1) for x in range(reg.width) if max(px[x, y]) > 120]
    lg = reg.crop((min(xs) - 6, y0 - 6, max(xs) + 6, y1 + 6)).convert('RGBA'); lp = lg.load()
    for y in range(lg.height):
        for x in range(lg.width):
            r, g, b, _ = lp[x, y]; lp[x, y] = (r, g, b, max(0, min(255, int((max(r, g, b) - 45) * 3.2))))
    return lg
def build():
    bg = Image.new('RGB', (W, H)); d = ImageDraw.Draw(bg)
    for y in range(H):
        for x in range(0, W, 4):
            t = x / W; u = y / H; d.line([(x, y), (x + 3, y)], fill=(int(12 + 40 * t), int(8 + 8 * u), int(58 + 70 * t)))
    art = og.crop((650, 0, 1200, 630)).resize((550, 630))
    def side(img, alpha, flip=False):
        a = img.transpose(Image.FLIP_LEFT_RIGHT) if flip else img
        m = Image.new('L', a.size, 0); md = ImageDraw.Draw(m)
        for x in range(a.width):
            t = x / a.width if not flip else 1 - x / a.width
            md.line([(x, 0), (x, a.height)], fill=int(alpha * max(0, min(1, (t - .15) / .6))))
        return a, m
    a, m = side(art, 170); bg.paste(a, (W - 550, 0), m)
    a, m = side(art, 110, True); bg.paste(a, (0, 0), m)
    ov = Image.new('L', (W, H), 0); ImageDraw.Draw(ov).ellipse((190, 30, 1010, 600), fill=160); ov = ov.filter(ImageFilter.GaussianBlur(70))
    bg = Image.composite(Image.new('RGB', (W, H), (10, 8, 40)), bg, ov)
    lg = logo_cut(); lh = 60; lg = lg.resize((int(lg.width * lh / lg.height), lh), Image.LANCZOS)
    d = ImageDraw.Draw(bg); safe = 540; size = 92
    while True:
        f = font(size, 800); lines = [[('Engineering an', 'white')], [('AI-Ready', '#F2C500'), (' Nation', 'white')]]
        widths = [sum(d.textlength(t, font=f) for t, _ in ln) for ln in lines]
        if max(widths) <= safe or size <= 50: break
        size -= 2
    ss = 28
    while max(d.textlength(s, font=font(ss, 600)) for s in SUB) > 600 and ss > 18: ss -= 1
    sub = font(ss, 600); lead = int(size * 1.14); sl = int(ss * 1.45)
    block = lh + 28 + lead * 2 + 22 + sl * len(SUB)
    y = (H - block) // 2; bg.paste(lg, ((W - lg.width) // 2, y), lg); y += lh + 28
    for ln, wid in zip(lines, widths):
        x = (W - wid) / 2
        for t, c in ln: d.text((x, y), t, font=f, fill=c); x += d.textlength(t, font=f)
        y += lead
    y += 22
    for s in SUB:
        tw = d.textlength(s, font=sub); d.text(((W - tw) / 2, y), s, font=sub, fill=(222, 218, 244)); y += sl
    q = 86
    while True:
        bg.save('docs/og-devcon-17.jpg', 'JPEG', quality=q, optimize=True, progressive=True)
        if os.path.getsize('docs/og-devcon-17.jpg') < 280_000 or q <= 60: break
        q -= 4
    return bg, size, ss, max(widths), max(d.textlength(s, font=sub) for s in SUB)
if __name__ == '__main__':
    bg, size, ss, hw, sw = build()
    print(f'og-devcon-17.jpg {bg.size} {os.path.getsize("docs/og-devcon-17.jpg")//1024} KB | headline {size}px, widest {int(hw)}px | subtitle {ss}px, widest {int(sw)}px | square-crop margin {int((630-max(hw,sw))/2)}px')
    sq = bg.crop(((W - H) // 2, 0, (W + H) // 2, H)).resize((315, 315)); th = bg.resize((300, 158))
    pv = Image.new('RGB', (600 + 10 + 315, 315 + 10 + 158), 'white'); pv.paste(bg.resize((600, 315)), (0, 0)); pv.paste(sq, (610, 0)); pv.paste(th, (0, 325)); pv.save('/tmp/og_home_prev.png')
