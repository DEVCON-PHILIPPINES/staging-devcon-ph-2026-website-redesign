# Site search: a header search button on every page, a keyword index of every page (docs/search-index.json),
# and a small client script (docs/assets/search.js). No third-party services.
import re, glob, os, json, html
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SECTION = {'': 'Home', 'about': 'About', 'programs': 'Programs', 'locations': 'Locations', 'case-studies': 'Partner Results', 'playbook': 'Community Playbook',
           'attend': 'Attend', 'invite': 'Invite DEVCON', 'partner': 'Partner', 'volunteer': 'Volunteer', 'start-here': 'Start here'}
EXTRA = {  # extra keywords so plain words and provinces find the right page
 '/locations/manila/': 'metro manila ncr makati ortigas intramuros', '/locations/legazpi/': 'albay bicol', '/locations/bacolod/': 'negros occidental negros',
 '/locations/tacloban/': 'leyte eastern visayas', '/locations/cagayandeoro/': 'cdo misamis oriental northern mindanao', '/locations/iligan/': 'lanao del norte',
 '/locations/davao/': 'davao del sur davao city', '/locations/laguna/': 'calabarzon los banos', '/locations/pampanga/': 'central luzon angeles clark',
 '/locations/bohol/': 'tagbilaran', '/locations/bukidnon/': 'malaybalay valencia', '/locations/cebu/': 'central visayas', '/locations/iloilo/': 'western visayas panay',
 '/programs/kids/': 'children kids school elementary hour of ai codey', '/programs/jumpstart-internships/': 'intern internship ojt practicum jumpstart',
 '/programs/ai-scholarships/': 'scholarship certification claude free certification', '/programs/sheisdevcon/': 'women girls she ladies gender',
 '/programs/campus/': 'students university college campus ambassador', '/programs/educators/': 'teachers educators deped',
 '/programs/crest/': 'climate environment resilience', '/programs/pro-summit/': 'professionals summit conference',
 '/programs/ai-code-camps/': 'ollama local ai open source llm qwen llama gemma code camp', '/case-studies/sui/': 'web3 blockchain move smart contracts sui',
 '/case-studies/icp/': 'web3 blockchain smart contracts internet computer', '/attend/': 'events calendar schedule devcon+ register tickets meetup',
 '/volunteer/': 'volunteer help sign up officer join', '/invite/': 'invite speaker school host chapter start apply', '/partner/': 'sponsor partner donate fund support',
 '/start-here/': 'glossary new beginner basics what is', '/case-studies/': 'case studies results devrel partners', '/about/leadership/': 'leaders board president team officers',
 '/playbook/hackathon-best-practice/': 'hackathon masterclass checklist plan event guide', '/playbook/volunteers-guide/': 'volunteer basics guide',
 '/locations/': 'chapters chapter locations map luzon visayas mindanao near me', '/about/17years/': 'manifesto anniversary devcon 17 ai-ready nation'}

def clean(t): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t))).strip()
def build_index():
    pages = json.load(open('docs/url-map.json'))['pages']; out = []
    for p in pages:
        f = 'docs' + p + 'index.html'
        if not os.path.isfile(f): continue
        s = open(f, encoding='utf-8').read()
        title = clean(re.search(r'<title>(.*?)</title>', s, re.S).group(1)); title = re.split(r'\s+\|\s+', title)[0]
        desc = re.search(r'<meta name="description" content="([^"]*)"', s); desc = html.unescape(desc.group(1)) if desc else ''
        a = s.find('<div class="page" data-page'); b = s.find('</main>', a); main = s[a:b] if a >= 0 else ''
        main = re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>|<nav class="crumbs".*?</nav>', ' ', main, flags=re.S)
        main = re.sub(r'data:[^"]+', '', main)
        h1 = clean(re.search(r'<h1[^>]*>(.*?)</h1>', main, re.S).group(1)) if re.search(r'<h1', main) else title
        heads = [clean(h) for h in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', main, re.S)][:30]
        text = clean(main)[:2600]
        sec = SECTION.get(p.strip('/').split('/')[0] if p != '/' else '', 'DEVCON')
        out.append({'u': p.lstrip('/'), 't': title, 'h': h1, 'd': desc, 'hs': heads, 'x': text, 's': sec, 'k': EXTRA.get(p, '')})
    os.makedirs('docs/assets', exist_ok=True)
    json.dump(out, open('docs/search-index.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    return len(out)

JS = r'''/* DEVCON site search: keyword search over search-index.json, no third parties */
(function () {
  var HR='hr'+'ef="', ROOT = new URL(window.__ssRoot || './', location.href).href, idx = null, loading = null, ui = null, sel = -1, hits = [];
  var SYN = {kid:'kids children',kids:'children school',intern:'internship jumpstart ojt',internship:'jumpstart intern ojt',ojt:'internship jumpstart',
    scholarship:'certification claude',web3:'blockchain smart contracts sui icp',blockchain:'web3 smart contracts',crypto:'blockchain web3',
    women:'sheisdevcon she girls',girls:'sheisdevcon women',she:'sheisdevcon women',sponsor:'partner',donate:'partner sponsor',
    event:'events attend devcon+',events:'attend devcon+ calendar',volunteer:'volunteer sign up',chapter:'chapters locations',near:'locations chapters',
    teacher:'educators teachers',teachers:'educators',student:'students campus',students:'campus',ai:'ai artificial intelligence',llm:'ai ollama',
    contact:'contact messenger email hello@devcon.ph',email:'contact hello@devcon.ph',cdo:'cagayan de oro',ncr:'manila metro manila',hq:'devcon hq ortigas national office'};
  var PIN=[[/^(events?|attend|find (an )?events?|upcoming( events)?|calendar|schedule)$/,'attend/','Attend: find your next DEVCON event'],[/^(start|open|new|apply)( a| for a)? chapter$/,'invite/#start-a-chapter','Start a chapter: requirements and how to apply'],[/^(become|join)( a| as a)? (chapter )?officer$|^chapter officer$/,'volunteer/#chapter-officer','Become a chapter officer'],[/^(volunteer|volunteering|sign up)$/,'volunteer/','Volunteer with DEVCON'],[/^(invite|speaker|invite (a )?speaker|host)$/,'invite/','Invite DEVCON to your school or city'],[/^(sponsor|partner|partnership|donate)$/,'partner/','Partner with DEVCON'],[/^(contact|email|hello)$/,'start-here/','Start here: how to reach DEVCON'],[/^(chapters?|locations?|near me)$/,'locations/','All 13 DEVCON locations'],[/^(glossary|start here|new)$/,'start-here/#glossary','Glossary of DEVCON words']];
  function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9+@.\s-]/g,' ').replace(/\s+/g,' ').trim()}
  function lev(a,b,max){if(Math.abs(a.length-b.length)>max)return max+1;var p=[],i,j;for(j=0;j<=b.length;j++)p[j]=j;for(i=1;i<=a.length;i++){var c=[i],m=i;for(j=1;j<=b.length;j++){c[j]=Math.min(p[j]+1,c[j-1]+1,p[j-1]+(a[i-1]===b[j-1]?0:1));if(c[j]<m)m=c[j]}if(m>max)return max+1;p=c}return p[b.length]}
  var VOCAB=null;function vocab(){if(VOCAB)return VOCAB;var s={};idx.forEach(function(d){d._w.forEach(function(w){if(w.length>3)s[w]=(s[w]||0)+1})});VOCAB=s;return s}
  function fix(t){if(t.length<5)return t;var v=vocab();if(v[t])return t;var lim=t.length>=8?2:1,best=t,bd=lim+1,bc=0;for(var w in v){var d=lev(t,w,lim);if(d<bd||(d===bd&&v[w]>bc)){bd=d;best=w;bc=v[w]}}return bd<=lim?best:t}
  function lev1(a,b){if(Math.abs(a.length-b.length)>1)return false;var i=0,j=0,e=0;while(i<a.length&&j<b.length){if(a[i]===b[j]){i++;j++;continue}if(++e>1)return false;if(a.length>b.length)i++;else if(b.length>a.length)j++;else{i++;j++}}return e+(a.length-i)+(b.length-j)<=1}
  function prep(d){d._p=norm(d.u.replace(/[\/-]/g,' '));d._f=[[norm(d.t),8],[norm(d.h),6],[norm(d.hs.join(' ')),4],[norm(d.k),4],[norm(d.d),3],[norm(d.x),1]];d._w=(d._f.map(function(f){return f[0]}).join(' ')).split(/\s+/);return d}
  function load(){if(idx)return Promise.resolve(idx);if(!loading)loading=fetch(ROOT+'search-index.json').then(function(r){return r.json()}).then(function(j){idx=j.map(prep);return idx});return loading}
  function score(d,toks,phrase){var total=0,all=true;toks.forEach(function(t){var best=0;d._f.forEach(function(f){var s=f[0],w=f[1];if(!s)return;var re=new RegExp('(^|\\s)'+t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'));if(re.test(s))best=Math.max(best,w*2);else if(s.indexOf(t)>-1)best=Math.max(best,w)});
      if(!best&&t.length>=5&&d._w.some(function(x){return lev1(x,t)}))best=1;if(!best&&SYN[t]){SYN[t].split(' ').forEach(function(sy){d._f.forEach(function(f){if(f[0].indexOf(sy)>-1)best=Math.max(best,f[1]*.6)})})}
      if(!best)all=false;else if((' '+d._p+' ').indexOf(' '+t)>-1)best+=10;total+=best});if(all&&phrase){var t0=d._f[0][0],h0=d._f[1][0];if(t0===phrase||h0===phrase)total+=40;else if(t0.indexOf(phrase)===0||h0.indexOf(phrase)===0)total+=14;if(phrase.indexOf(' ')>0&&d._f[2][0].indexOf(phrase)>-1)total+=18;if(phrase.indexOf(' ')<0&&d._p.split(' ').indexOf(phrase)>-1)total+=6}return all?total:total*.25}
  function snippet(d,toks){var src=d.d&&toks.some(function(t){return norm(d.d).indexOf(t)>-1})?d.d:d.x,n=norm(src),pos=-1;toks.some(function(t){pos=n.indexOf(t);return pos>-1});
    var a=Math.max(0,pos-60),s=(a>0?'… ':'')+src.slice(a,a+170)+(src.length>a+170?' …':'');return esc(s).replace(new RegExp('('+toks.map(function(t){return t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}).join('|')+')','gi'),'<mark>$1</mark>')}
  function esc(s){return s.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  var POP=[['Find an event','attend/'],['Volunteer','volunteer/'],['Find your chapter','locations/'],['Programs','programs/'],['Start here','start-here/'],['Partner Results','case-studies/'],['Invite DEVCON','invite/'],['Partner with us','partner/']];
  function build(){ui=document.createElement('div');ui.className='ss';ui.hidden=true;ui.innerHTML=
    '<div class="ss-back" data-ss-close></div><div class="ss-box" role="dialog" aria-modal="true" aria-label="Search DEVCON"><div class="ss-bar"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>'+
    '<input class="ss-in" type="search" placeholder="Search programs, chapters, events, guides…" aria-label="Search the site" autocomplete="off" role="combobox" aria-expanded="true" aria-controls="ss-list"/>'+
    '<button class="ss-x" type="button" data-ss-close aria-label="Close search">Esc</button></div><div class="ss-body"><p class="ss-hint"></p><ul class="ss-list" id="ss-list" role="listbox"></ul></div>'+
    '<p class="ss-foot"><span><kbd>↑</kbd><kbd>↓</kbd> to move</span><span><kbd>Enter</kbd> to open</span><span><kbd>/</kbd> or <kbd>Ctrl</kbd><kbd>K</kbd> to search</span></p></div>';
    document.body.appendChild(ui);var inp=ui.querySelector('.ss-in');inp.addEventListener('input',function(){run(inp.value)});
    inp.addEventListener('keydown',function(e){if(e.key==='ArrowDown'){move(1);e.preventDefault()}else if(e.key==='ArrowUp'){move(-1);e.preventDefault()}else if(e.key==='Enter'){var a=ui.querySelectorAll('.ss-list a')[Math.max(sel,0)];if(a){location.href=a.href}e.preventDefault()}});
    ui.addEventListener('click',function(e){if(e.target.closest('[data-ss-close]'))close()});ui.addEventListener('keydown',function(e){if(e.key==='Escape')close();if(e.key==='Tab'){var f=[].slice.call(ui.querySelectorAll('input,a,button'));var i=f.indexOf(document.activeElement);if(e.shiftKey&&i<=0){f[f.length-1].focus();e.preventDefault()}else if(!e.shiftKey&&i===f.length-1){f[0].focus();e.preventDefault()}}})}
  function move(d){var a=ui.querySelectorAll('.ss-list a');if(!a.length)return;sel=(sel+d+a.length)%a.length;a.forEach(function(x,i){x.setAttribute('aria-selected',i===sel)});a[sel].scrollIntoView({block:'nearest'})}
  function popular(){ui.querySelector('.ss-hint').textContent='Popular';ui.querySelector('.ss-list').innerHTML=POP.map(function(p){return '<li><a class="ss-pop" '+HR+ROOT+p[1]+'" role="option">'+p[0]+'</a></li>'}).join('')}
  function run(q){var toks=norm(q).split(/\s+/).filter(function(t){return t.length>1});sel=-1;if(!toks.length){popular();return}
    load().then(function(ix){var orig=toks.slice();toks=toks.map(fix);var fixed=toks.join(' ')!==orig.join(' ');var phrase=toks.join(' ');hits=ix.map(function(d){return [score(d,toks,phrase),d]}).filter(function(x){return x[0]>0}).sort(function(a,b){return b[0]-a[0]}).slice(0,10);
      var list=ui.querySelector('.ss-list'),hint=ui.querySelector('.ss-hint');
      if(!hits.length){hint.textContent='No results for “'+q+'”';list.innerHTML='<li class="ss-none">Try a program, a city, or a word like <b>volunteer</b>, <b>events</b>, or <b>internship</b>. Or <a '+HR+ROOT+'start-here/">start here</a>, or email <a '+HR+'mailto:hello@devcon.ph">hello@devcon.ph</a>.</li>';return}
      var pin=PIN.filter(function(x){return x[0].test(phrase)})[0];if(pin){var pu=pin[1].split('#')[0];hits=hits.filter(function(h){return h[1].u!==pu||pin[1].indexOf('#')>-1});hits.unshift([999,{u:pin[1],t:pin[2],s:'Top match',d:'',x:'',_pin:1}]);hits=hits.slice(0,10)}
      hint.textContent=(fixed?'Showing results for “'+toks.join(' ')+'” · ':'')+hits.length+(hits.length===1?' result':' results');
      list.innerHTML=hits.map(function(h,i){var d=h[1];return '<li><a '+HR+ROOT+d.u+'" role="option" aria-selected="false"><span class="ss-sec">'+esc(d.s)+'</span><b>'+esc(d.t)+'</b><span class="ss-snip">'+snippet(d,toks)+'</span></a></li>'}).join('')})}
  function open(){if(!ui)build();ui.hidden=false;document.documentElement.classList.add('ss-open');var inp=ui.querySelector('.ss-in');inp.value='';popular();setTimeout(function(){inp.focus()},20);load()}
  function close(){if(!ui)return;ui.hidden=true;document.documentElement.classList.remove('ss-open');var b=document.querySelector('[data-search-open]');if(b)b.focus()}
  document.addEventListener('click',function(e){if(e.target.closest('[data-search-open]')){e.preventDefault();open()}});
  document.addEventListener('keydown',function(e){var t=e.target,typing=t&&(t.tagName==='INPUT'||t.tagName==='TEXTAREA'||t.isContentEditable);
    if((e.key==='/'&&!typing)||((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k')){e.preventDefault();open()}});
})();
'''
BTN = ('<button class="nav-search" type="button" data-search-open aria-label="Search the site" title="Search (/)">'
       '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg></button>')
CSS = ('.nav-search{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;margin-left:8px;border-radius:12px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.06);color:#fff;cursor:pointer;flex:none}'
       '.nav-search:hover{border-color:var(--y);color:var(--y)}.nav-search:focus-visible{outline:3px solid var(--y);outline-offset:2px}.nav-search svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round}'
       '.nav .wrap{display:flex;align-items:center}.nav .nav-links{order:2}.nav-search{order:3;margin-left:12px}'
       '@media (max-width:1100px){.nav-search{margin-left:auto;margin-right:8px;order:2}.nav .burger{order:3}}'
       '.ss{position:fixed;inset:0;z-index:9999;display:flex;justify-content:center;align-items:flex-start;padding:min(12vh,96px) 16px 16px}.ss[hidden]{display:none}html.ss-open{overflow:hidden}'
       '.ss-back{position:absolute;inset:0;background:rgba(5,3,30,.72);backdrop-filter:blur(4px)}'
       '.ss-box{position:relative;width:min(720px,100%);max-height:calc(100vh - 2*min(12vh,96px));display:flex;flex-direction:column;border-radius:20px;background:#120d4a;border:1px solid rgba(255,255,255,.14);box-shadow:0 40px 100px rgba(0,0,0,.6);overflow:hidden}'
       '.ss-bar{display:flex;align-items:center;gap:10px;padding:14px 16px;border-bottom:1px solid rgba(255,255,255,.1)}.ss-bar svg{width:22px;height:22px;fill:none;stroke:var(--y);stroke-width:2.2;stroke-linecap:round;flex:none}'
       '.ss-in{flex:1;min-width:0;min-height:44px;border:0;background:transparent;color:#fff;font:inherit;font-size:1.1rem;outline:none}.ss-in::placeholder{color:#a9a5d0}'
       '.ss-x{min-height:44px;min-width:44px;padding:0 10px;border-radius:10px;border:1px solid rgba(255,255,255,.18);background:transparent;color:#d6d3ef;font:inherit;font-size:.8rem;cursor:pointer}'
       '.ss-body{overflow:auto;padding:10px 10px 6px}.ss-hint{margin:4px 8px 8px;color:#a9a5d0;font-size:.8rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase}'
       '.ss-list{list-style:none;margin:0;padding:0;display:grid;gap:4px}.ss-list a{display:flex;flex-direction:column;gap:2px;padding:12px 14px;border-radius:12px;color:#fff;text-decoration:none;min-height:44px}'
       '.ss-list a:hover,.ss-list a[aria-selected="true"]{background:rgba(242,197,0,.12);outline:1px solid rgba(242,197,0,.45)}.ss-list b{font-weight:900}'
       '.ss-sec{color:var(--y);font-size:.72rem;font-weight:900;letter-spacing:.06em;text-transform:uppercase}.ss-snip{color:#c9c5e6;font-size:.88rem;line-height:1.45}.ss-snip mark{background:rgba(242,197,0,.3);color:#fff;border-radius:3px;padding:0 2px}'
       '.ss-list .ss-pop{display:inline-flex;flex-direction:row;align-items:center;font-weight:800}.ss-none{padding:12px 14px;color:#c9c5e6}.ss-none a{color:var(--y)}'
       '.ss-foot{display:flex;flex-wrap:wrap;gap:14px;margin:0;padding:10px 16px;border-top:1px solid rgba(255,255,255,.1);color:#a9a5d0;font-size:.78rem}.ss-foot kbd{display:inline-block;min-width:20px;margin-right:3px;padding:1px 5px;border-radius:5px;border:1px solid rgba(255,255,255,.25);font:inherit;font-size:.74rem;text-align:center}'
       '@media (max-width:560px){.ss{padding:10px}.ss-box{max-height:calc(100vh - 20px)}.ss-foot{display:none}}')

if __name__ == '__main__':
    n = build_index()
    pages = 0
    for f in glob.glob('docs/**/*.html', recursive=True):
        s = open(f, encoding='utf-8').read()
        if 'http-equiv="refresh"' in s or '<header class="nav">' not in s: continue
        d = os.path.relpath('docs', os.path.dirname(f)).replace('\\', '/'); pre = '' if d == '.' else d + '/'
        if 'data-search-open' not in s:
            s = s.replace('    <button class="burger" data-nav-toggle>', '    ' + BTN + '\n    <button class="burger" data-nav-toggle>', 1)
        s = re.sub(r'<script src="[^"]*assets/search\.js" defer></script>\n', '', s)
        s = re.sub(r'<script>window\.__ssRoot=.*?</script>\n', '', s, flags=re.S)
        s = s.replace('</body>', '<script>window.__ssRoot=' + json.dumps(pre or './') + ';' + JS + '</script>\n</body>', 1)
        if CSS not in s: s = s.replace('</style>', CSS + '</style>', 1)
        open(f, 'w', encoding='utf-8').write(s); pages += 1
    print(f'search index: {n} pages, {os.path.getsize("docs/search-index.json")//1024} KB; search added to {pages} pages')
