import re,glob
from urllib.parse import quote
def icon(n,label):
    s=open(f'/tmp/acc/{n}.svg').read()
    path=re.search(r'<path d="([^"]+)"',s).group(1)
    return f'<svg class="tlogo" viewBox="0 0 24 24" role="img" aria-label="{label}"><path fill="currentColor" d="{path}"/></svg>'
CODE='<svg class="tlogo" viewBox="0 0 24 24" role="img" aria-label="OpenCode"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>'
TOOLS=[(icon('ollama','Ollama'),'Ollama','Runs open models locally'),(icon('alibabacloud','Alibaba Cloud'),'Qwen','by Alibaba Cloud'),
       (icon('meta','Meta'),'Llama','by Meta'),(icon('google','Google'),'Gemma','by Google'),(icon('anthropic','Anthropic'),'Claude','by Anthropic'),
       (CODE,'OpenCode','Open-source coding agent'),(icon('github','GitHub'),'GitHub','Fork and ship'),(icon('vercel','Vercel'),'Vercel','Deploy live')]
tiles=''.join(f'<li>{svg}<b>{n}</b><span>{d}</span></li>' for svg,n,d in TOOLS)
TOOLS_SEC=('<section class="section" aria-labelledby="bai-tools"><div class="wrap">'
  '<header class="sec-head"><span class="eyebrow" style="color:var(--y)">The models and tools</span><h2 id="bai-tools">Built on open models and open tools</h2>'
  '<p>Every builder picked an open-weight model, ran it locally with Ollama, and shipped it live. These are the models and tools across our AI camps.</p></header>'
  f'<ul class="tool-logos" role="list">{tiles}<li class="tool-logos-more"><b>and more</b></li></ul></div></section>')
MODEL_ICON={'qwen':icon('alibabacloud','Qwen by Alibaba Cloud'),'llama':icon('meta','Llama by Meta'),'gemma':icon('google','Gemma by Google')}
SCALE='mailto:hello@devcon.ph?subject='+quote('Help scale Open-Source AI Code Camps nationwide')
CSS=('.tool-logos{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}'
     '.tool-logos li{display:grid;grid-template-columns:44px minmax(0,1fr);grid-template-rows:auto auto;column-gap:12px;align-items:center;padding:16px 18px;border-radius:16px;background:rgba(255,255,255,.04);border:1px solid var(--line)}'
     '.tool-logos .tlogo{grid-row:span 2;width:40px;height:40px;color:#fff}.tool-logos b{color:#fff;font-weight:900;font-size:1.05rem}.tool-logos span{color:var(--text-secondary);font-size:.86rem}'
     '.tool-logos .tool-logos-more{display:flex;justify-content:center;border-style:dashed}.tool-logos-more b{color:var(--text-secondary)}'
     '.bar-name .tlogo{width:16px;height:16px;margin-right:8px;vertical-align:-3px;color:#fff}'
     '.acc-moments .acc-lead img{width:100%;border-radius:20px;border:1px solid var(--line)}'
     '@media (max-width:900px){.tool-logos{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:520px){.tool-logos{grid-template-columns:minmax(0,1fr)}}')
def top_sections(P):
    idx=[m.start() for m in re.finditer(r'\n  <(?:section|header) class="(?:page-hero[^"]*|numbers|section[^"]*|page-cta)"',P)]
    out=[]
    for i,j in enumerate(idx):
        e=idx[i+1] if i+1<len(idx) else P.rindex('</section>')+len('</section>')
        out.append((j,e))
    return out
def edit(P):
    # 1) hero: main CTA
    P=re.sub(r'<div class="hero-btns"><a class="btn-primary btn-xl" href="https://barangay-ai-showcase.vercel.app/"[^>]*>See the AI showcase<span class="sr-only"> \(opens in a new tab\)</span></a><a class="btn-outline" href="https://barangay-ai.vercel.app/"[^>]*>Explore the platform<span class="sr-only"> \(opens in a new tab\)</span></a></div>',
             f'<div class="hero-btns"><a class="btn-primary btn-xl" href="{SCALE}">Help scale this nationwide</a><a class="btn-outline" href="https://barangay-ai-showcase.vercel.app/" target="_blank" rel="noopener">See the AI showcase<span class="sr-only"> (opens in a new tab)</span></a></div>',P,count=1)
    assert 'Help scale this nationwide' in P
    # 2) tools strip -> logo feature section
    P,k=re.subn(r'<section class="section" aria-label="Tools we teach">.*?</section>',TOOLS_SEC,P,count=1,flags=re.S); assert k==1
    # 3) model logos in the bar chart
    P=re.sub(r'<span class="bar-name">(qwen|llama|gemma)([^<]*)</span>',lambda m:f'<span class="bar-name">{MODEL_ICON[m.group(1)]}{m.group(1)}{m.group(2)}</span>',P)
    # 4) closing CTA
    P,k=re.subn(r'<section class="page-cta">.*?</section>',
        '<section class="page-cta">\n    <div class="wrap">\n      <h2>Help scale this nationwide</h2>\n      <p>19 builders finished, and every one would come back. Help us bring Open-Source AI Code Camps to all 13 DEVCON locations, beyond the capital.</p>\n'
        f'      <div class="programs-cta"><a class="btn-primary btn-xl" href="{SCALE}">Help scale this nationwide</a><a class="btn-outline" href="PARTNER">Sponsor the next camp</a></div>\n    </div>\n  </section>',P,count=1,flags=re.S); assert k==1
    # 5) move "Moments from the camp" up, right after the results, with a lead photo
    secs=top_sections(P); rows=[P[j:e] for j,e in secs]; start=secs[0][0]; end=secs[-1][1]
    mi=next(i for i,r in enumerate(rows) if 'aria-label="Moments from the camp"' in r[:200])
    ni=next(i for i,r in enumerate(rows) if 'class="numbers"' in r[:120])
    mom=rows.pop(mi).replace('aria-label="Moments from the camp"','aria-label="Moments from the camp" class-placeholder',1)
    mom=re.sub(r'<section class="section[^"]*" aria-label="Moments from the camp" class-placeholder>','<section class="section acc-moments" aria-label="Moments from the camp">',mom,count=1)
    mom=mom.replace('Moments from the camp</span>','In the room</span>',1) if 'Moments from the camp</span>' in mom else mom
    rows.insert(ni+1,mom)
    # alternate bands after the numbers row
    k=next(i for i,r in enumerate(rows) if 'class="numbers"' in r[:120]); fixed=[]
    for i,r in enumerate(rows):
        if i<=k or 'page-cta' in r[:60]: fixed.append(r); continue
        band=((i-k-1)%2==1); o=re.match(r'\s*<section class="([^"]*)"',r)
        cls=re.sub(r'\s*\bband2\b','',o.group(1)); cls=cls.replace('section','section band2',1) if band else cls
        fixed.append(r.replace(f'class="{o.group(1)}"',f'class="{cls}"',1))
    return P[:start]+''.join(fixed)+P[end:]
for f,partner in [('docs/programs/ai-code-camps/index.html','../../partner/')]+[(c,'#/partner') for c in glob.glob('combined/*.html')]:
    s=open(f,encoding='utf-8').read()
    if f.startswith('docs'): a=s.index('<div class="page" data-page'); b=s.index('</main>')
    else:
        a=s.index('<div class="page" data-page="ai-code-camps"') if 'data-page="ai-code-camps"' in s else s.index('<div class="page" data-page="aicamps"'); b=s.find('<div class="page"',a+10)
    seg=edit(s[a:b]).replace('href="PARTNER"',f'href="{partner}"')
    s=s[:a]+seg+s[b:]
    s=s.replace('</style>',CSS+'</style>',1); open(f,'w',encoding='utf-8').write(s); print('edited',f)
