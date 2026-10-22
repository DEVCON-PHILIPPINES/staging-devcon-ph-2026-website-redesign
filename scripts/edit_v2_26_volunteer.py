# v2.26: /volunteer/ page (roles, time commitment, what happens after sign-up, becoming a chapter officer),
# sign-up buttons, chapter application, softer capacity wording.
import re, glob, os, json
from urllib.parse import quote
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSczVxZPmHIRPphNJNgbuRVzEC5QTponVzjDPPMmkSxP0cIdrg/viewform'
COMBINED = glob.glob('combined/*.html')[0]
NT = '<span class="sr-only"> (opens in a new tab)</span>'
SIGNUP = lambda cls='btn-primary btn-xl': f'<a class="{cls}" href="{FORM}" target="_blank" rel="noopener" data-volunteer>Sign up to volunteer{NT}</a>'
TITLE = 'Volunteer with DEVCON: Roles, Time Commitment, and How to Join | DEVCON Philippines'
DESC = ('Volunteer with DEVCON Philippines: event volunteer, mentor or speaker, chapter officer, or national volunteer at DEVCON HQ. '
        'See the time each role takes, what happens after you sign up, and how to become a chapter officer.')

def volunteer_page(mode):
    L = (lambda k: {'basics': '../playbook/volunteers-guide/', 'coc': '../playbook/code-of-conduct/', 'locations': '../locations/', 'start': '../invite/#start-a-chapter',
                    'leaders': '../about/leadership/', 'home': '../'}[k]) if mode == 'docs' else \
        (lambda k: {'basics': '#/volunteers-guide', 'coc': '#/code-of-conduct-for-national-and-chapter-officers-and-volunteers', 'locations': '#/chapters',
                    'start': '#/invite', 'leaders': '#/leadership', 'home': '#/'}[k])
    hidden = ' hidden' if mode == 'spa' else ''
    roles = [('#F2C500', 'Event volunteer', 'Help run a free event: registration, ushering, tech and AV, hosting, or photos and social.', 'Per event: a short briefing, then the event day. Join as your schedule allows.'),
             ('#A57BFF', 'Mentor or speaker', 'Share what you know at code camps, talks, workshops, and hackathons.', 'Per session: preparation, then the talk or camp.'),
             ('#71B405', 'Chapter officer', 'Help lead an existing chapter and plan its programs with the chapter president.', 'Ongoing: a few hours a week, for a one-year term.'),
             ('#4DA2FF', 'National volunteer at DEVCON HQ', 'Support national programs, partnerships, communications, or design with the DEVCON HQ national office.', 'Project-based, coordinated with DEVCON HQ.')]
    role_html = ''.join(f'<li class="pp" style="--c:{c}"><h3>{t}</h3><p>{d}</p><p class="vol-time"><b>Time:</b> {tm}</p></li>' for c, t, d, tm in roles)
    steps = [('Sign up', 'A short form: your nearest chapter, the roles you&#8217;re interested in, and when you&#8217;re free.'),
             ('We reach out', 'Your nearest chapter or DEVCON HQ contacts you when there&#8217;s a role that fits. We match volunteers to what each chapter needs, so it may take a little while.'),
             ('Get briefed', 'A volunteer briefing before your first event. Read Volunteering Basics and the Code of Conduct ahead of time.'),
             ('Show up and grow', 'Start at an event, then take on more: lead a team, mentor, or join your chapter&#8217;s officer team.')]
    step_html = ''.join(f'<li><span class="vol-n" aria-hidden="true">{i}</span><b>{t}</b><span>{d}</span></li>' for i, (t, d) in enumerate(steps, 1))
    return f'''<div class="page" data-page="volunteer"{hidden}>
  <header class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{L('home')}">Home</a><span aria-hidden="true">/</span><span aria-current="page">Volunteer</span></nav>
      <span class="eyebrow" style="color:var(--y)">Volunteer with DEVCON</span>
      <h1 id="volunteer-title">Pay it forward with DEVCON</h1>
      <p class="page-lead">Event volunteers, chapter officers, and national leaders are all DEVCON volunteers paying it forward. Pick a role, give the time you can, and grow with the community.</p>
      <div class="hero-btns">{SIGNUP()}<a class="btn-outline" href="{L('basics')}">Read Volunteering Basics</a></div>
    </div>
  </header>

  <section class="section" aria-labelledby="vol-roles"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Roles</span><h2 id="vol-roles">Find a role that fits your time</h2>
      <p>Most volunteers start at an event. Many go on to mentor, speak, or lead.</p></header>
    <ul class="pp-grid pp-grid--4" role="list">{role_html}</ul>
  </div></section>

  <section class="section band2" aria-labelledby="vol-next"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">After you sign up</span><h2 id="vol-next">What happens next</h2></header>
    <ol class="vol-steps" role="list">{step_html}</ol>
    <p class="vol-note"><b>Good to know:</b> volunteering is about paying it forward. Merch isn&#8217;t guaranteed: stocks are limited and shared with volunteers when available.</p>
    <div class="hero-btns">{SIGNUP()}</div>
  </div></section>

  <section class="section" id="chapter-officer" aria-labelledby="vol-officer"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Become a chapter officer</span><h2 id="vol-officer">Join an existing chapter&#8217;s officer team</h2>
      <p>Chapter officers lead their local chapter day to day, with support and training from the DEVCON HQ national office.</p></header>
    <ol class="vol-steps vol-steps--3" role="list">
      <li><span class="vol-n" aria-hidden="true">1</span><b>Volunteer locally first</b><span>Help at your nearest chapter&#8217;s events so the team gets to know you.</span></li>
      <li><span class="vol-n" aria-hidden="true">2</span><b>Tell your chapter president</b><span>Let them know you&#8217;d like to serve, or say so in the sign-up form.</span></li>
      <li><span class="vol-n" aria-hidden="true">3</span><b>Join for the next term</b><span>Officers are chosen locally for each one-year term and follow the Playbook and Code of Conduct.</span></li>
    </ol>
    <div class="hero-btns"><a class="btn-primary" href="{L('locations')}">Find your chapter</a><a class="btn-outline" href="{L('leaders')}">Meet the chapter presidents</a></div>
    <p class="vol-note">No chapter near you? <a class="pp-link" href="{L('start')}">See how to start one</a>.</p>
  </div></section>

  <section class="page-cta">
    <div class="wrap">
      <h2>Ready to pay it forward?</h2>
      <p>Sign up once, and your nearest chapter or DEVCON HQ will reach out when there&#8217;s a role that fits.</p>
      <div class="programs-cta">{SIGNUP()}<a class="btn-outline" href="{L('coc')}">Read the Code of Conduct</a></div>
    </div>
  </section>
</div>
'''
CSS = ('.vol-time{margin-top:auto;padding-top:8px;color:#fff;font-size:.9rem}.vol-time b{color:var(--y)}'
       '.vol-steps{list-style:none;margin:0 0 18px;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}.vol-steps--3{grid-template-columns:repeat(3,minmax(0,1fr))}'
       '.vol-steps li{display:flex;flex-direction:column;gap:6px;padding:18px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}'
       '.vol-n{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:var(--y);color:#0b0840;font-weight:900}'
       '.vol-steps b{color:#fff;font-weight:900}.vol-steps span:not(.vol-n){color:var(--text-secondary);font-size:.92rem;line-height:1.5}'
       '.vol-note{margin:0 0 16px;padding:12px 16px;border-radius:14px;background:rgba(255,255,255,.04);border:1px solid var(--line);color:var(--text-secondary)}.vol-note b{color:#fff}'
       '@media (max-width:900px){.vol-steps,.vol-steps--3{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:560px){.vol-steps,.vol-steps--3{grid-template-columns:minmax(0,1fr)}}')

APPLY_BODY = ('Hi DEVCON HQ,\n\nWe would like to apply to start a DEVCON chapter.\n\nCity or province:\nProposed officer team (names, roles, contact details):\n'
              'Our track record (volunteer events we have run, with dates and photos):\nCommunity size and who we serve:\nSchools or partners supporting us:\nWhy now:\n\nThank you!')
APPLY = lambda: ('<div class="ch-apply"><h3>Ready to apply?</h3><p>Email DEVCON HQ with your city, your proposed officer team, and your track record of volunteer events. '
                 'We review every application against the requirements above and reply by email.</p>'
                 f'<div class="hero-btns"><a class="btn-primary btn-xl" href="mailto:hello@devcon.ph?subject={quote("Chapter application: [your city]")}&amp;body={quote(APPLY_BODY)}">Apply to start a chapter</a>'
                 f'<a class="btn-outline" href="{FORM}" target="_blank" rel="noopener" data-volunteer>Start as a volunteer{NT}</a></div></div>')
APPLY_CSS = ('.ch-apply{margin:22px 0;padding:20px 22px;border-radius:18px;background:rgba(242,197,0,.08);border:1px solid rgba(242,197,0,.45)}'
             '.ch-apply h3{margin:0 0 6px;color:#fff;font-weight:900}.ch-apply p{margin:0 0 14px;color:var(--text-secondary);line-height:1.55}')

def write(f, s): open(f, 'w', encoding='utf-8').write(s)
log = {}
def edit_all(files, a, b, key):
    n = 0
    for f in files:
        s = open(f, encoding='utf-8').read()
        if a in s: write(f, s.replace(a, b)); n += 1
    log[key] = n

ALL = glob.glob('docs/**/*.html', recursive=True) + [COMBINED]
# 5) Locations: the button opens the form, so it says so
edit_all(ALL, f'data-volunteer>Volunteer on DEVCON+</a>', f'data-volunteer>Sign up to volunteer{NT}</a>', '5 rename button')
# 6) Locations and Invite: drop the non-renewal count
edit_all(ALL, ' To date, we have not renewed a total of 4 chapters for non-compliance and inactivity.', '', '6 locations wording')
edit_all(ALL, ' To date, we have not renewed a total of <b>4 chapters</b> for non-compliance and inactivity.', '', '6 invite wording')
# 7) Chapter pages: a sign-up button in the Volunteer card
n = 0
for f in glob.glob('docs/locations/*/index.html') + [COMBINED]:
    s = open(f, encoding='utf-8').read()
    s2 = re.sub(r'(<li class="pp" style="--c:#A57BFF"><span class="pp-ic" aria-hidden="true">.*?</span><h3>Volunteer</h3><p>[^<]*</p>)(<a class="pp-link" href="([^"]*)">Read the volunteering basics</a></li>)',
                lambda m: m.group(1) + f'<a class="btn-primary pp-btn" href="{FORM}" target="_blank" rel="noopener" data-volunteer>Sign up to volunteer{NT}</a>' + m.group(2), s, flags=re.S)
    if s2 != s: n += s2.count('pp-btn') - s.count('pp-btn'); write(f, s2)
log['7 chapter sign-up buttons'] = n
# 8) Leadership: "Become a chapter officer" goes to the new officer section
edit_all(['docs/about/leadership/index.html'], 'href="../../invite/#start-a-chapter">Become a chapter officer</a>', 'href="../../volunteer/#chapter-officer">Become a chapter officer</a>', '8 leadership link')
edit_all([COMBINED], 'href="#start-a-chapter">Become a chapter officer</a>', 'href="#/volunteer">Become a chapter officer</a>', '8 leadership link (single file)')
# 9) Invite: an apply button after the requirements
n = 0
for f in ['docs/invite/index.html', COMBINED]:
    s = open(f, encoding='utf-8').read()
    if 'ch-apply' not in s:
        s, k = re.subn(r'(<div class="ch-req" id="chapter-requirements">.*?</ul>\s*</div>)', lambda m: m.group(1) + '\n        ' + APPLY(), s, count=1, flags=re.S)
        if k: s = s.replace('</style>', APPLY_CSS + '</style>', 1); write(f, s); n += 1
log['9 apply button'] = n
# chapter card button spacing
for f in glob.glob('docs/locations/*/index.html') + [COMBINED]:
    s = open(f, encoding='utf-8').read(); css = '.pp .pp-btn{align-self:flex-start;margin:10px 0 4px;min-height:44px}'
    if 'pp-btn' in s and css not in s: write(f, s.replace('</style>', css + '</style>', 1))

# 10) /volunteer/: a real page instead of a redirect
src = open('docs/attend/index.html', encoding='utf-8').read()
ot = re.search(r'<title>([^<]*)</title>', src).group(1); od = re.search(r'<meta name="description" content="([^"]*)"', src).group(1)
a = src.index('<div class="page" data-page="attend"'); b = src.index('</main>')
page = src[:a] + volunteer_page('docs') + src[b:]
page = page.replace(ot, TITLE).replace(od, DESC).replace('https://devcon.ph/attend/', 'https://devcon.ph/volunteer/')
page = page.replace('</style>', CSS + '</style>', 1)
write('docs/volunteer/index.html', page)
c = open(COMBINED, encoding='utf-8').read()
if 'data-page="volunteer"' not in c:
    i = c.index('</main>'); c = c[:i] + volunteer_page('spa') + c[i:]; c = c.replace('</style>', CSS + '</style>', 1); write(COMBINED, c)
r = [l for l in open('docs/_redirects').read().split('\n') if l.split(' ')[0] not in ('/volunteer', '/volunteer/')]
write('docs/_redirects', '\n'.join(r).rstrip('\n') + '\n')
m = json.load(open('docs/url-map.json')); m['redirects'].pop('/volunteer/', None)
if '/volunteer/' not in m['pages']: m['pages'] = sorted(m['pages'] + ['/volunteer/'])
json.dump(m, open('docs/url-map.json', 'w'), indent=1)
sm = open('docs/sitemap.xml').read()
if 'devcon.ph/volunteer/' not in sm: write('docs/sitemap.xml', sm.replace('</urlset>', '  <url><loc>https://devcon.ph/volunteer/</loc><lastmod>2026-10-21</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n</urlset>'))
rs = open('scripts/restructure.py').read(); write('scripts/restructure.py', rs.replace("'volunteer': 'volunteers-guide', ", ''))
log['10 volunteer page'] = 'built'
print(log)
