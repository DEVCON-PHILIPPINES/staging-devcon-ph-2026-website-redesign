# Community Playbook: whole-day AI Masterclass (morning) and Hackathon (afternoon) planning guide.
# Generic by design: no sponsor, venue, chapter, or person names, and no budget figures.
import re, glob, json, os
from urllib.parse import quote
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
PATH = 'playbook/hackathon-best-practice'
SPA = 'hackathon-best-practice'
TITLE = 'DEVCON Masterclass and Hackathon Best Practice and Checklist | DEVCON Community Playbook'
DESC = ('DEVCON Masterclass and Hackathon Best Practice and Checklist: run a whole-day AI event with a morning masterclass and an afternoon rapid hackathon. '
        'Overview, tools, a 3-month plan, a sample program, duties per lead, risk management, and a readiness checklist.')
TALK = 'mailto:hello@devcon.ph?subject=' + quote('Planning a whole-day AI Masterclass and Hackathon')

import re as _re
def _icon(n, label):
    s = open(f'/tmp/acc/{n}.svg').read(); d = _re.search(r'<path d="([^"]+)"', s).group(1)
    return f'<svg class="tlogo" viewBox="0 0 24 24" role="img" aria-label="{label}"><path fill="currentColor" d="{d}"/></svg>'
_CODE = '<svg class="tlogo" viewBox="0 0 24 24" role="img" aria-label="{l}"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>'
_ROUTE = '<svg class="tlogo" viewBox="0 0 24 24" role="img" aria-label="{l}"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M4 6h6l4 6-4 6H4M14 12h6M17 9l3 3-3 3"/></svg>'
_HEART = '<svg class="tlogo" viewBox="0 0 24 24" role="img" aria-label="{l}"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>'
TOOLS = [
 ('Think and orchestrate', [
   (_icon('claude','Claude'), 'Claude', 'https://claude.ai', 'AI assistant for reasoning, coding, and content'),
   (_ROUTE.format(l='OpenRouter'), 'OpenRouter', 'https://openrouter.ai', 'One API for many AI models, with usage limits'),
   (_icon('google','Google AI Studio'), 'Google AI Studio', 'https://aistudio.google.com', 'Gemini API and fast prototyping'),
   (_icon('ollama','Ollama'), 'Ollama', 'https://ollama.com', 'Run open models locally, no cloud needed')]),
 ('Build', [
   (_CODE.format(l='OpenCode'), 'OpenCode', 'https://opencode.ai', 'Open-source AI coding agent'),
   (_icon('google','Google Antigravity'), 'Google Antigravity', 'https://antigravity.google', 'AI-powered development platform'),
   (_HEART.format(l='Lovable'), 'Lovable', 'https://lovable.dev', 'AI app builder, from prompt to app')]),
 ('Ship and demo', [
   (_icon('github','GitHub'), 'GitHub', 'https://github.com', 'Share your code and fork starter kits'),
   (_icon('vercel','Vercel'), 'Vercel', 'https://vercel.com', 'Deploy a live demo link in minutes')]),
]
CHECK = [
 ('Four weeks out', ['Venue, rooms, and date confirmed in writing', 'Speakers, facilitators, and judges confirmed', 'Registration open, with separate masterclass and hackathon sign-ups', 'Prints and merch ordered']),
 ('One week out', ['Volunteer training done; every lead has a backup', 'Pre-install session held for participants', 'Hackathon kit, rubric, and per-team usage caps ready', 'Headcount locked with the venue and caterer']),
 ('Day before', ['Stage, sound, screens, and livestream tested at the venue', 'Backup internet, power, and offline slides ready', 'Registration desk, QR check-in, and signage set up', 'Weather checked and go or no-go decided']),
 ('Event day', ['Team briefing at call time', 'Run of show, script, and timer with the host', 'Partners recognized at opening and closing', 'Speaker tokens handed over, debrief held, venue cleared']),
]
PLAN = [
 ('Month 1 · Weeks 12 to 9', 'Set the foundation', '#71B405', [
   ('Define the goal and audience', 'Who is it for, what should they leave with, and how many seats.'),
   ('Pick the date and shortlist venues', 'Check academic calendars, holidays, and weather season.'),
   ('Form the core team', 'Name an event director and every lead in the roles section.'),
   ('Draft the budget and funding plan', 'List costs, confirmed support, and who to approach.'),
   ('Open the event page', 'One official registration page for every attendee.')]),
 ('Month 2 · Weeks 8 to 5', 'Lock the essentials', '#A57BFF', [
   ('Confirm the venue in writing', 'Main hall, breakout rooms for the build, power, and internet.'),
   ('Confirm speakers and facilitators', 'Morning modules, parallel afternoon talks, and judges.'),
   ('Prepare the hackathon kit', 'Challenge brief, tools list, sandbox, rubric, and usage caps.'),
   ('Brand the event', 'Slides, key visual, and print files in one shared folder.'),
   ('Launch registration and promotion', 'Separate sign-ups for the masterclass and the hackathon.'),
   ('Order prints early', 'Tarps and printed materials need two to three weeks to arrive.')]),
 ('Month 3 · Weeks 4 to 1', 'Rehearse and run', '#F2C500', [
   ('Train every volunteer', 'A mandatory online session on the program flow and each role.'),
   ('Run a pre-install session', 'Help participants set up tools and accounts on their own laptops.'),
   ('Lock the headcount', 'Confirm numbers with the venue and caterer five days before.'),
   ('Do two full dry runs', 'Host, program lead, and tech lead walk the whole run of show.'),
   ('Ingress the day before', 'Set up the stage, sound, screens, registration, and signage.'),
   ('Make the go or no-go call', 'At least 24 hours before, based on weather and safety advisories.')]),
 ('After · Week +1', 'Close the loop', '#EA641D', [
   ('Debrief the same day', 'What worked, what to fix, while it is fresh.'),
   ('Thank everyone publicly', 'Speakers, mentors, partners, volunteers, and participants.'),
   ('Publish the recap', 'Photos, winners, and a short video.'),
   ('Write the impact report', 'Attendance, projects shipped, survey results, and lessons.')]),
]
RUN = [('7:30 AM', 'Volunteer call time and team briefing', 'Event director'), ('8:00 AM', 'Registration and check-in', 'Registration lead'),
       ('8:30 AM', 'Welcome and opening remarks', 'Host, partner representative'), ('8:45 AM', 'Keynote', 'Keynote speaker'),
       ('9:15 AM', 'Messages of support', 'Partners and guests'), ('9:45 AM', 'Masterclass module 1: AI fundamentals and orchestration', 'Lead facilitator'),
       ('10:45 AM', 'Masterclass module 2: AI tools, live demo', 'Facilitators'), ('12:00 PM', 'Lunch break', 'Food lead'),
       ('12:30 PM', 'Hackathon briefing: mechanics, teams, tools, rubric', 'Hackathon lead'), ('1:00 PM', 'Rapid hackathon build, with parallel talks for non-builders', 'Hackathon lead, mentors'),
       ('3:00 PM', 'Build freeze, then project demos and pitching', 'Teams, judges'), ('4:00 PM', 'Awarding and closing remarks', 'Host, event director'),
       ('4:30 PM', 'Group photo and team debrief', 'All'), ('Evening', 'Optional community dinner with partners and leaders', 'VIP and ushers lead')]
TRANSITIONS = [('8:00 to 9:00 AM', 'Registration rush. Fully staff the desk and don’t pull anyone away.'),
               ('12:00 to 12:30 PM', 'Lunch and room split. The host clearly directs builders, attendees, and guests to the right rooms.'),
               ('12:30 to 1:00 PM', 'The highest-risk handoff. Confirm teams and tool access before the clock starts.'),
               ('3:00 PM', 'Pitching. Judges briefed and seated, scoring sheet ready, timer visible.'),
               ('4:00 PM onward', 'Awarding and close. Recognize partners, end on time, then pack up.')]
ROLES = [
 ('Event director', '#F2C500', ['Owns the plan, the budget, and every final decision', 'Assigns leads and runs weekly check-ins', 'Makes the go or no-go call', 'Single point of escalation on the day; arrives first for ingress']),
 ('Program lead', '#A57BFF', ['Writes the run of show and host script', 'Confirms speakers, facilitators, parallel talks, and judges', 'Orders speaker tokens and hands them over right after each session', 'Leads the two dry runs and keeps the day on time']),
 ('Hackathon lead', '#71B405', ['Prepares the challenge brief, kit, rubric, and tool list', 'Sets per-team AI usage caps and sandboxed accounts', 'Runs the briefing, the build clock, the freeze, and the demo order', 'Briefs mentors and judges on the scoring']),
 ('Tech lead', '#4DA2FF', ['Tests projectors, screens, sound, and livestream the day before', 'Keeps a backup laptop, adapters, and offline copies of every slide', 'Confirms backup internet and power at key stations', 'Sets up check-in, scoring, and voting tools']),
 ('Registration lead', '#EA641D', ['Sets up separate sign-ups for the masterclass and the hackathon', 'Confirms the final headcount with the venue five days before', 'Prepares QR check-in, name tags, attendance sheets, and signage', 'Writes the welcome-desk script, from the gate to the seat']),
 ('Logistics lead', '#EC4899', ['Books rooms, tables, chairs, power strips, and cable management', 'Orders tarps, prints, lanyards, and stickers early, with extras', 'Checks aircon and ventilation, and sets up a quiet call room', 'Leads ingress and pack-up']),
 ('Food lead', '#F2C500', ['Locks the caterer and menu early', 'Orders 10 to 15% buffer food and water for everyone', 'Plans drinks and snacks for the volunteer team', 'Confirms dinner numbers if there is a community dinner']),
 ('VIP and ushers lead', '#A57BFF', ['Confirms guest travel, pickup, and accommodation', 'Prepares each VIP’s itinerary and remarks timing', 'Assigns an usher to every VIP on the day', 'Makes sure partners are recognized at opening and closing']),
 ('Documentation and social lead', '#71B405', ['Assigns a photographer and videographer', 'Schedules pre-event teasers and speaker spotlights', 'Covers the day live with approved captions only', 'Delivers the recap album, reel, and case study material']),
 ('Volunteers lead', '#4DA2FF', ['Recruits, assigns, and trains every volunteer', 'Shares the contact list and call time', 'Rotates breaks so no post is left unattended', 'Collects volunteer feedback for the debrief']),
 ('Finance and admin', '#EA641D', ['Tracks the budget and approves spending', 'Handles partner agreements and paperwork', 'Keeps receipts and liquidates after the event', 'Reports actuals in the impact report']),
]
RISKS = [
 ('Severe weather or flooding', 'High', 'Monitor official weather and disaster advisories 48 hours out. Name a backup indoor venue. Decide go or no-go at least 24 hours before and tell everyone.'),
 ('Venue rooms or capacity fall through', 'Medium', 'Get rooms confirmed in writing. Keep an alternative room or layout on standby.'),
 ('AV, internet, or power failure', 'Medium', 'Test everything the day before. Keep a backup laptop, offline slides, backup internet, and power backup at key stations.'),
 ('AI tool costs run over', 'Medium', 'Set per-team usage caps and use sandboxed or pre-funded accounts, never personal cards.'),
 ('Low hackathon turnout', 'Medium', 'Use a separate sign-up, promote early, and plan a minimum viable number of teams.'),
 ('Speaker or VIP delayed', 'Medium', 'Confirm travel the day before. Have a local backup speaker or a panel fallback ready.'),
 ('Wrong headcount', 'Medium', 'Lock numbers five days before with the venue and caterer. Order buffer food.'),
 ('Late start or overrun', 'Medium', 'Strict start time, short focused talks, buffers in the run of show, and a host who enforces time.'),
 ('Budget shortfall', 'Medium', 'Line up partners early and track spending weekly. Keep a priority list of what to cut first.'),
 ('Safety and conduct', 'Always on', 'Brief everyone on the Code of Conduct and the Privacy and Safe Space standard. Follow the Child Protection Policy if minors attend.'),
]
DECISIONS = [('Go or no-go on weather', '24 hours before', 'Postpone if official advisories warn of severe weather'),
             ('Final hackathon team count', '3 days before', 'Proceed with confirmed teams'),
             ('Headcount and dinner lock', '5 days before', 'Cap at the confirmed number'),
             ('Speaker backup plan', '4 days before', 'Switch to a panel format')]
PROVEN = ['A mandatory briefing for every volunteer before the day', 'Pre-event hype posts and speaker spotlights', 'Tokens for every speaker and guest',
          'A livestream, tested at the venue', 'Water for every attendee, and buffer food', 'Backup internet and power at key stations',
          'Short, focused talks and an early end time', 'Prizes shown quietly, so the focus stays on learning', 'Diverse speakers and inclusive teams',
          'Government, academe, and local partners invited', 'QR check-in for fast registration', 'Two full dry runs before the day',
          'Local design and branding that feels like the city']
WATCH = [('Wrong headcount', 'Confirm with the venue five days before.'), ('Prints arriving late', 'Order everything two to three weeks out.'),
         ('Too few lanyards and stickers', 'Order 20 to 30% more than expected.'), ('No gate or arrival instructions', 'A welcome-desk script from the gate to the seat.'),
         ('Livestream not tested', 'Test it at the venue the day before.'), ('Hot rooms', 'Check the aircon during ingress.'),
         ('An empty afternoon for non-builders', 'Schedule parallel talks during the build.'), ('Role confusion on the day', 'Volunteer training and a checklist per lead.')]

def page_html(mode):
    L = (lambda k: {'volunteers-guide': '../volunteers-guide/', 'code-of-conduct': '../code-of-conduct/', 'privacy': '../privacy-and-safe-space/',
                    'child': '../child-protection-policy/', 'playbook': '../', 'brand': '../brand-kit/', 'hermes': '../../case-studies/hermes-agentic-code-camp/'}[k]) if mode == 'docs' else \
        (lambda k: '#/' + {'volunteers-guide': 'volunteers-guide', 'code-of-conduct': 'code-of-conduct-for-national-and-chapter-officers-and-volunteers', 'privacy': 'standard-privacy-and-safespace-consent', 'child': 'child-protection-policy',
                           'playbook': 'playbook', 'brand': 'brand-kit', 'hermes': 'hermes-camp'}[k])
    home = '../../' if mode == 'docs' else '#/'
    plan = ''.join(f'<li class="tl-phase" style="--c:{c}"><span class="mh-when">{when}</span><h3>{h}</h3><ul role="list">' +
                   ''.join(f'<li><b>{t}</b><span>{d}</span></li>' for t, d in tasks) + '</ul></li>' for when, h, c, tasks in PLAN)
    run = ''.join(f'<tr><th scope="row">{t}</th><td>{a}</td><td>{w}</td></tr>' for t, a, w in RUN)
    trans = ''.join(f'<li><span>{t}</span><b>{d}</b></li>' for t, d in TRANSITIONS)
    roles = ''.join(f'<li class="mh-role" style="--c:{c}"><h3>{n}</h3><ul role="list">' + ''.join(f'<li>{x}</li>' for x in b) + '</ul></li>' for n, c, b in ROLES)
    lvl = lambda l: {'High': 'mh-lvl--high', 'Medium': 'mh-lvl--med'}.get(l, 'mh-lvl--on')
    risks = ''.join(f'<tr><th scope="row">{r}</th><td><span class="mh-lvl {lvl(l)}">{l}</span></td><td>{m}</td></tr>' for r, l, m in RISKS)
    dec = ''.join(f'<tr><th scope="row">{d}</th><td>{w}</td><td>{x}</td></tr>' for d, w, x in DECISIONS)
    proven = ''.join(f'<li>{p}</li>' for p in PROVEN)
    watch = ''.join(f'<li><b>{w}</b><span>{f}</span></li>' for w, f in WATCH)
    tools = ''.join(f'<h3 class="sub-h mh-tgroup">{g}</h3><ul class="tool-logos" role="list">' + ''.join(
        f'<li>{svg}<b><a href="{u}" target="_blank" rel="noopener">{n}<span class="sr-only"> (opens in a new tab)</span></a></b><span>{d}</span></li>' for svg, n, u, d in items) + '</ul>' for g, items in TOOLS)
    checks = ''.join(f'<div class="mh-checkcol"><h3 class="sub-h">{h}</h3><ul class="mh-checklist" role="list">' + ''.join(f'<li><span class="mh-box" aria-hidden="true"></span>{x}</li>' for x in items) + '</ul></div>' for h, items in CHECK)
    hidden = ' hidden' if mode == 'spa' else ''
    return f'''<div class="page" data-page="{SPA}"{hidden}>
  <header class="page-hero page-hero--playbook">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">Home</a><span aria-hidden="true">/</span><a href="{L('playbook')}">Community Playbook</a><span aria-hidden="true">/</span><span aria-current="page">Masterclass and Hackathon Best Practice and Checklist</span></nav>
      <span class="eyebrow" style="color:var(--y)">Community Playbook · Best practice and checklist</span>
      <h1 id="{SPA}-title">DEVCON Masterclass and Hackathon Best Practice and Checklist</h1>
      <p class="page-lead">Learn in the morning, build in the afternoon. The best practices we&#8217;ve learned running these days across the country: the tools to use, a 3-month plan, a sample program, clear duties for every lead, a risk plan, and a readiness checklist.</p>
      <div class="hero-btns"><a class="btn-primary btn-xl" href="#mh-plan">See the 3-month plan</a><a class="btn-outline" href="#mh-check">Go to the checklist</a></div>
    </div>
  </header>

  <section class="numbers" aria-labelledby="mh-glance"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Overview</span><h2 id="mh-glance">One day, learn then build</h2>
      <p>A morning masterclass gives everyone the same foundation. An afternoon rapid hackathon turns it into working projects, demoed live.</p></header>
    <ul class="numbers-grid" role="list"><li class="num-item" style="--c:var(--y)"><b>1 day</b><span>Morning masterclass, afternoon hackathon</span></li><li class="num-item" style="--c:var(--p2)"><b>3 months</b><span>Of planning, from goal to debrief</span></li><li class="num-item" style="--c:var(--o)"><b>2 hours</b><span>Rapid build, with mentors on hand</span></li><li class="num-item" style="--c:var(--g)"><b>5 minutes</b><span>Per team demo, live</span></li></ul>
  </div></section>

  <section class="section" aria-labelledby="mh-what"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">What makes it work</span><h2 id="mh-what">Four principles behind every run</h2></header>
    <ul class="kids-worked mh-principles" role="list" style="list-style:none;padding:0">
      <li><article><h3>Inclusive by design</h3><p>Women in tech, students from many schools, and people from every discipline, in the room and on stage.</p></article></li>
      <li><article><h3>Open source first</h3><p>Open, reproducible tools, so nobody needs expensive licenses to take part.</p></article></li>
      <li><article><h3>Multi-model</h3><p>Participants learn to orchestrate several AI models and platforms together.</p></article></li>
      <li><article><h3>Bring your own device</h3><p>Builders use their own laptops, set up in a pre-install session before the day.</p></article></li>
    </ul>
  </div></section>

  <section class="section band2" aria-labelledby="mh-tools"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Tools</span><h2 id="mh-tools">Tools participants can use</h2>
      <p>Builders bring their own laptops with these set up before the day. Open-source tools are encouraged, and any stack is welcome.</p></header>
    {tools}
  </div></section>

  <section class="section" id="mh-plan" aria-labelledby="mh-plan-t"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">3-month plan</span><h2 id="mh-plan-t">From first idea to impact report</h2>
      <p>Start 12 weeks out. Every task has one owner and a deadline, reviewed in a short weekly check-in.</p></header>
    <ol class="tl-grid mh-plan" role="list">{plan}</ol>
  </div></section>

  <section class="section band2" id="mh-program" aria-labelledby="mh-program-t"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Sample program</span><h2 id="mh-program-t">A whole-day run of show</h2>
      <p>Adjust the times to your venue. Keep the shape: learn, eat, brief, build, demo, celebrate, and end on time.</p></header>
    <div class="tbl-wrap"><table class="reach-tbl mh-tbl"><caption>Sample run of show</caption><thead><tr><th scope="col">Time</th><th scope="col">Segment</th><th scope="col">Lead</th></tr></thead><tbody>{run}</tbody></table></div>
    <div class="merge-block">
      <h3 class="sub-h">Critical transition points</h3>
      <ul class="cr-run mh-trans" role="list">{trans}</ul>
    </div>
  </div></section>

  <section class="section" aria-labelledby="mh-roles"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Roles</span><h2 id="mh-roles">Clear duties for every lead</h2>
      <p>One name per role. Every role is load-bearing, so each lead also names a backup.</p></header>
    <ul class="mh-roles" role="list">{roles}</ul>
  </div></section>

  <section class="section band2" aria-labelledby="mh-risk"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Risk management</span><h2 id="mh-risk">Plan for what can go wrong</h2>
      <p>Review this list at every weekly check-in and again during the dry runs.</p></header>
    <div class="tbl-wrap"><table class="reach-tbl mh-tbl mh-risks"><caption>Risks and how to manage them</caption><thead><tr><th scope="col">Risk</th><th scope="col">Level</th><th scope="col">How to manage it</th></tr></thead><tbody>{risks}</tbody></table></div>
    <div class="merge-block">
      <h3 class="sub-h">Key decisions, with a default if no one decides</h3>
      <div class="tbl-wrap"><table class="reach-tbl mh-tbl"><caption>Decision points</caption><thead><tr><th scope="col">Decision</th><th scope="col">Deadline</th><th scope="col">Default</th></tr></thead><tbody>{dec}</tbody></table></div>
    </div>
  </div></section>

  <section class="section" id="mh-check" aria-labelledby="mh-check-t"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Checklist</span><h2 id="mh-check-t">Readiness checklist</h2>
      <p>Tick these off as you go. If a box is still empty the day before, raise it with the event director.</p></header>
    <div class="mh-checks">{checks}</div>
  </div></section>

  <section class="section band2" aria-labelledby="mh-best"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Best practices</span><h2 id="mh-best">Lessons from past runs</h2></header>
    <div class="kai-road">
      <div><h3 class="sub-h">Proven practices to carry forward</h3><ul class="doc-list mh-proven">{proven}</ul></div>
      <div><h3 class="sub-h">Watch-outs to avoid</h3><ul class="mh-watch" role="list">{watch}</ul></div>
    </div>
    <div class="merge-block mh-dos">
      <div><h3 class="sub-h">Dos for volunteers</h3><ul class="doc-list"><li>Arrive at call time, before doors open</li><li>Wear the team shirt so attendees can find you</li><li>Follow your lead; the event director has the final call</li><li>Save every coordinator&#8217;s number before the day</li><li>Post only approved content, and send press questions to the event director</li></ul></div>
      <div><h3 class="sub-h">Don&#8217;ts for volunteers</h3><ul class="doc-list"><li>Don&#8217;t promise hackathon slots to walk-ins</li><li>Don&#8217;t post unconfirmed details</li><li>Don&#8217;t leave your post without a replacement</li><li>Don&#8217;t ignore weather warnings; escalate them right away</li></ul></div>
    </div>
  </div></section>

  <section class="section" aria-labelledby="mh-more"><div class="wrap">
    <header class="sec-head"><span class="eyebrow" style="color:var(--y)">Keep these handy</span><h2 id="mh-more">Related playbook guides</h2></header>
    <ul class="pp-grid pp-grid--4" role="list">
      <li class="pp" style="--c:#F2C500"><h3>Volunteering Basics</h3><p>How volunteering works across DEVCON.</p><a class="pp-link" href="{L('volunteers-guide')}">Read Volunteering Basics</a></li>
      <li class="pp" style="--c:#A57BFF"><h3>Code of Conduct</h3><p>Standards for officers and volunteers.</p><a class="pp-link" href="{L('code-of-conduct')}">Read the Code of Conduct</a></li>
      <li class="pp" style="--c:#EA641D"><h3>Privacy and Safe Space</h3><p>Keeping every event inclusive and secure.</p><a class="pp-link" href="{L('privacy')}">Read the consent standard</a></li>
      <li class="pp" style="--c:#EC4899"><h3>Child Protection Policy</h3><p>For any event where minors attend.</p><a class="pp-link" href="{L('child')}">Read the policy</a></li>
    </ul>
    <p class="kai-links">See this format in action in the <a class="pp-link" href="{L('hermes')}">Hermes Agentic Code Camp case study</a>, and keep your materials on brand with the <a class="pp-link" href="{L('brand')}">Brand Kit</a>.</p>
  </div></section>

  <section class="page-cta">
    <div class="wrap">
      <h2>Planning one in your city?</h2>
      <p>Talk to DEVCON HQ early. We&#8217;ll help you shape the program, train your volunteers, and connect you with facilitators.</p>
      <div class="programs-cta"><a class="btn-primary btn-xl" href="{TALK}">Talk to DEVCON HQ</a><a class="btn-outline" href="{L('volunteers-guide')}">Start with Volunteering Basics</a></div>
    </div>
  </section>
</div>
'''

CSS = ('.tool-logos{list-style:none;margin:0 0 8px;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}'
       '.tool-logos li{display:grid;grid-template-columns:44px minmax(0,1fr);grid-template-rows:auto auto;column-gap:12px;align-items:center;padding:14px 16px;border-radius:16px;background:rgba(255,255,255,.04);border:1px solid var(--line)}'
       '.tool-logos .tlogo{grid-row:span 2;width:36px;height:36px;color:#fff}.tool-logos b a{color:#fff;font-weight:900;text-decoration:underline;text-decoration-color:var(--y);text-underline-offset:3px;display:inline-flex;align-items:center;min-height:44px}.tool-logos b a:hover{color:var(--y)}.tool-logos span{color:var(--text-secondary);font-size:.86rem;line-height:1.4}'
       '.mh-tgroup{margin:18px 0 10px}.mh-tgroup:first-of-type{margin-top:0}'
       '.mh-checks{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}.mh-checkcol{padding:16px 18px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}.mh-checkcol .sub-h{margin-top:0}'
       '.mh-checklist{list-style:none;margin:0;padding:0;display:grid;gap:10px}.mh-checklist li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:10px;color:#fff;line-height:1.45;font-size:.93rem}'
       '.mh-box{width:18px;height:18px;margin-top:2px;border-radius:5px;border:2px solid var(--y)}'
       '@media (max-width:1000px){.tool-logos,.mh-checks{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:560px){.tool-logos,.mh-checks{grid-template-columns:minmax(0,1fr)}}'
       '@media print{.mh-box{border-color:#000}}'
       '.mh-when{display:block;color:var(--text-secondary);font-size:.78rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;margin-bottom:4px}'
       '.mh-plan{grid-template-columns:repeat(4,minmax(0,1fr))}'
       '.mh-tbl td,.mh-tbl th{text-align:left!important;vertical-align:top}.mh-tbl tbody th{white-space:nowrap;color:var(--y)}.mh-risks tbody th{white-space:normal;color:#fff}'
       '.mh-trans li{grid-template-columns:150px minmax(0,1fr)!important}'
       '.mh-roles{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}'
       '.mh-role{padding:18px 20px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line);border-top:4px solid var(--c)}'
       '.mh-role h3{margin:0 0 10px;color:#fff;font-weight:900;font-size:1.05rem}'
       '.mh-role ul{margin:0;padding-left:18px;display:grid;gap:6px}.mh-role li{color:var(--text-secondary);line-height:1.5;font-size:.93rem}'
       '.mh-lvl{display:inline-flex;padding:3px 10px;border-radius:999px;font-size:.78rem;font-weight:900;white-space:nowrap}'
       '.mh-lvl--high{background:rgba(234,68,68,.18);color:#FF9A9A;border:1px solid rgba(234,68,68,.5)}'
       '.mh-lvl--med{background:rgba(242,197,0,.14);color:var(--y);border:1px solid rgba(242,197,0,.5)}'
       '.mh-lvl--on{background:rgba(113,180,5,.16);color:#B8E86A;border:1px solid rgba(113,180,5,.5)}'
       '.mh-watch{list-style:none;margin:0;padding:0;display:grid;gap:8px}.mh-watch li{padding:10px 14px;border-radius:12px;background:rgba(255,255,255,.04);border:1px solid var(--line)}'
       '.mh-watch b{display:block;color:#fff}.mh-watch span{color:var(--text-secondary);font-size:.9rem}'
       '.mh-dos{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}'
       '@media (max-width:1000px){.mh-plan{grid-template-columns:repeat(2,minmax(0,1fr))}.mh-roles{grid-template-columns:repeat(2,minmax(0,1fr))}}'
       '@media (max-width:640px){.mh-plan,.mh-roles,.mh-dos{grid-template-columns:minmax(0,1fr)}.mh-trans li{grid-template-columns:minmax(0,1fr)!important}}')

CARD = lambda href: (f'<li class="pp" style="--c:#4DA2FF"><span class="pp-ic" aria-hidden="true"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M7 14h4M7 17h7"/></svg></span>'
                     f'<h3>DEVCON Masterclass and Hackathon Best Practice and Checklist</h3><p>Tools, a 3-month plan, sample program, roles, risks, and a readiness checklist.</p><a class="pp-link" href="{href}">Open the best practice and checklist</a></li>')

# 1) folder page from the Volunteers Guide template
src = open('docs/playbook/volunteers-guide/index.html', encoding='utf-8').read()
old_title = re.search(r'<title>([^<]*)</title>', src).group(1); old_desc = re.search(r'<meta name="description" content="([^"]*)"', src).group(1)
a = src.index('<div class="page" data-page="volunteers-guide"'); b = src.index('</main>')
out = src[:a] + page_html('docs') + src[b:]
out = out.replace(old_title, TITLE).replace(old_desc, DESC).replace('https://devcon.ph/playbook/volunteers-guide/', f'https://devcon.ph/{PATH}/')
if CSS not in out: out = out.replace('</style>', CSS + '</style>', 1)
os.makedirs(f'docs/{PATH}', exist_ok=True); open(f'docs/{PATH}/index.html', 'w', encoding='utf-8').write(out)
# 2) playbook hub card (after the Brand Kit card)
f = 'docs/playbook/index.html'; h = open(f, encoding='utf-8').read()
h = re.sub(r'<li class="pp" style="--c:#4DA2FF"><span class="pp-ic" aria-hidden="true"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5".*?</a></li>\s*', '', h, flags=re.S)
if True:
    i = h.index('</a></li>', h.index('href="brand-kit/"')) + len('</a></li>'); h = h[:i] + '\n        ' + CARD('hackathon-best-practice/') + h[i:]
open(f, 'w', encoding='utf-8').write(h)
# 3) single-file build
c = glob.glob('combined/*.html')[0]; t = open(c, encoding='utf-8').read()
t = re.sub(r'<div class="page" data-page="masterclass-hackathon-guide".*?</div>\n(?=</main>)', '', t, flags=re.S); t = re.sub(r'<li class="pp" style="--c:#4DA2FF"><span class="pp-ic" aria-hidden="true"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5".*?</a></li>\s*', '', t, flags=re.S)
if True:
    i = t.index('</main>'); t = t[:i] + page_html('spa') + t[i:]
    a = t.index('<div class="page" data-page="playbook"'); j = t.index('</a></li>', t.index('href="#/brand-kit"', a)) + len('</a></li>')
    t = t[:j] + '\n        ' + CARD(f'#/{SPA}') + t[j:]
    if CSS not in t: t = t.replace('</style>', CSS + '</style>', 1)
open(c, 'w', encoding='utf-8').write(t)
# 4) sitemap, url map, llms
sm = open('docs/sitemap.xml').read()
if PATH not in sm: open('docs/sitemap.xml', 'w').write(sm.replace('</urlset>', f'  <url><loc>https://devcon.ph/{PATH}/</loc><lastmod>2026-10-13</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>\n</urlset>'))
um = json.load(open('docs/url-map.json'))
if f'/{PATH}/' not in um['pages']: um['pages'] = sorted(um['pages'] + [f'/{PATH}/'])
json.dump(um, open('docs/url-map.json', 'w'), indent=1)
ll = open('docs/llms.txt').read()
ll = '\n'.join(l for l in ll.split('\n') if PATH not in l) + ('\n' if not ll.endswith('\n') else '')
if True:
    k = ll.find('- [Brand Kit]')
    line = f'- [DEVCON Masterclass and Hackathon Best Practice and Checklist](https://devcon.ph/{PATH}/): tools, plan, program, roles, risks, and checklist\n'
    ll = ll[:k] + line + ll[k:] if k >= 0 else ll + line
    open('docs/llms.txt', 'w').write(ll)
print('built', PATH)
