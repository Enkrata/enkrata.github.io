#!/usr/bin/env python3
"""Assemble the Enkrata site pages from a shared head template and the brand
lockup, so head tags and the mark cannot drift between pages."""
import os

HEAD = open("_head.tmpl").read().strip()
LOCKUP = open("_lockup.frag").read().strip()

# The public TestFlight link. None until Kevin pastes it in from App Store
# Connect — the beta section then renders an email invitation instead of a
# button, because a dead "Join the beta" button is worse than none. The repo
# has never recorded this URL: docs/testflight.md carries it as the literal
# placeholder "[public link]".
TESTFLIGHT_URL = None

# The contact address, in ONE place. Undercrew is getting its own domain at
# Cloudflare with email routing to the Enkrata inbox, the way Rout already has
# — at which point this becomes something like hello@undercrew.<tld> and the
# switch is this line. Until then it is Kevin's POSH address, which is wrong on
# an Enkrata surface (POSH Social is a separate company) and is carried here as
# a placeholder rather than a decision.
#
# The privacy policy's copy of it is legally operative and referenced by App
# Store Connect, so changing that one is deliberate rather than incidental.
CONTACT = "kevin@poshsocialfl.com"

def beta_cta():
    if TESTFLIGHT_URL:
        return f'<p><a class="cta" href="{TESTFLIGHT_URL}">Join the beta on TestFlight</a></p>'
    return ('<p>Testing is invitation-only for the moment. Email '
            f'<a href="mailto:{CONTACT}">{CONTACT}</a> '
            'and I will send you a TestFlight invite.</p>')

def head(title, desc, path):
    return (HEAD.replace("{{TITLE}}", title)
                .replace("{{DESC}}", desc)
                .replace("{{PATH}}", path))

def page(title, desc, path, body, lockup_class="lockup"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(title, desc, path)}
</head>
<body>
<div class="page">
{body.strip()}
</div>
</body>
</html>
"""

lock = LOCKUP
lock_sm = LOCKUP.replace('class="lockup"', 'class="lockup lockup-sm"')

# ---------------------------------------------------------------- landing
index_body = f"""
<header class="masthead">
  {lock}
  <h1 class="sr-only">Enkrata</h1>
  <p class="tagline">Hard work on things that matter.</p>
</header>

<div class="prose">
  <p>Enkrata is Kevin Holloway's development studio — games, productivity apps,
  and fitness projects, built one at a time and shipped.</p>

  <p>The name comes from the Greek <em>enkrateia</em>: self-mastery, and the
  conviction that what you can control is enough to build something worth
  keeping.</p>
</div>

<section class="section">
  <h2>Now building</h2>
  <div class="now">
    <span class="status">In beta on TestFlight</span>
    <h3><a href="/undercrew/">Undercrew</a></h3>
    <p>A Terraria-deep 2D sandbox you never directly play. You run the crew of
    agents that plays it, from your phone.</p>
  </div>
</section>

<hr class="rule">
<footer>
  <p>&copy; 2026 Enkrata &middot; <a href="https://github.com/Enkrata">GitHub</a></p>
</footer>
"""

# -------------------------------------------------------------- undercrew
undercrew_body = f"""
<header class="masthead">
  <a href="/" aria-label="Enkrata home">{lock_sm}</a>
  <h1 class="title">Undercrew</h1>
  <p class="tagline">The depth of a world-sim. The interaction model of a coach.</p>
</header>

<figure class="shot hero">
  <img src="shots/world.png" alt="A crew camp on a ridge above its own workings, ladders
       cut down into the stone, clouds drifting over the treeline."
       width="603" height="1211" loading="eager">
</figure>

<div class="prose">
  <p>A deep 2D sandbox world &mdash; mining, crafting, building, the full
  tunnel-by-tunnel progression &mdash; that you never directly play. Your crew
  of agents digs the tunnels, fells the timber, and hauls the ore. You write
  their standing orders, read their shift reports, and make the risk calls.
  When the crew mines a tunnel, the tunnel exists; zoom in and watch.</p>

  <p>No virtual joystick. No energy meters. The grind is real &mdash; it is
  just not yours any more.</p>
</div>

<section class="section">
  <h2>The charter is the game</h2>
  <p>Every crewhand carries a charter: a short list of standing rules, read
  from the top, first one that applies wins. Keep ten wood in stock. Head home
  to mend under 35 health. If idle, mine ore within a hundred tiles. Rules
  unlock as she earns the skill to hold them, and the one that is driving her
  right now is lit on the row, so you can always see <em>why</em> she is doing
  what she is doing.</p>
  <p>You do not pilot anyone. You decide what the crew is for, and then you
  find out whether you were right.</p>
</section>

<section class="section">
  <h2>Look at it</h2>
  <div class="shots">
    <figure class="shot">
      <img src="shots/charter.png" alt="A crewhand's charter: eleven standing
           rules with the winning one lit, and skill gates marked in amber."
           width="603" height="1211" loading="lazy">
      <figcaption>Her charter. Top rule that applies wins, and the one driving
      her is lit.</figcaption>
    </figure>
    <figure class="shot">
      <img src="shots/report.png" alt="A shift report listing what a crewhand
           did, what she gained, what hurt her, and a line in her own voice."
           width="603" height="1211" loading="lazy">
      <figcaption>The shift report. What she did, what it cost her, and a line
      in her own voice.</figcaption>
    </figure>
    <figure class="shot">
      <img src="shots/book.png" alt="The foreman's book: every tip the game has
           shown, kept and readable, newest first." width="603" height="1211"
           loading="lazy">
      <figcaption>The foreman&rsquo;s book. Everything the game has ever told
      you, kept.</figcaption>
    </figure>
    <figure class="shot">
      <img src="shots/title.png" alt="The Undercrew title screen over a cutaway
           of grass, dirt and stone." width="603" height="1211" loading="lazy">
      <figcaption>One world at a time. Abandon it and it goes on the
      memorial.</figcaption>
    </figure>
  </div>
</section>

<section class="section">
  <h2>Beta</h2>
  <p>Undercrew is in early testing on TestFlight for iPhone. It is a young
  game, changing week by week &mdash; the crew appreciates patient testers with
  opinions.</p>
  {beta_cta()}
</section>

<section class="section">
  <h2>What has been shipping</h2>
  <ol class="log">
    <li>
      <span class="ver">0.7.0 &middot; September 2026</span>
      <p><strong>Four dens hold a person.</strong> Every machine in the deep now
      has somebody on its books &mdash; a builder, a woodcutter, a deep-seam
      miner, a warder. Reaching her is not enough: the machine is what holds
      her, and breaking it is what frees her. The crew reaches eight.</p>
    </li>
    <li>
      <span class="ver">0.6.4 &middot; September 2026</span>
      <p><strong>The foreman keeps a book.</strong> Every tip the game has ever
      shown you is written down and readable, with a second sentence the
      one-line slot never had room for. The night watch became something a
      crewhand can actually stand.</p>
    </li>
    <li>
      <span class="ver">0.6.3 &middot; August 2026</span>
      <p><strong>The approach.</strong> Brass crawlers hold the workings above a
      den at any hour, and a Winder wound them. Killing them is not the answer;
      finding what is making them is.</p>
    </li>
    <li>
      <span class="ver">0.6.1 &middot; August 2026</span>
      <p><strong>Water, and the first machine.</strong> Ponds settle into dips
      and pools sit on cave floors; deep water breaks a fall. Something 157
      tiles down began breathing firedamp on a schedule.</p>
    </li>
    <li>
      <span class="ver">0.6.0 &middot; August 2026</span>
      <p><strong>Gear, and something in the dark.</strong> Finds get names and
      effects, and you decide who carries them. Nights stopped being empty.</p>
    </li>
  </ol>
</section>

<section class="section">
  <h2>Support</h2>
  <p>Questions, bugs, or thoughts: email
  <a href="mailto:{CONTACT}">{CONTACT}</a>, or use
  the feedback button inside TestFlight.</p>
</section>

<hr class="rule">
<footer>
  <p><a href="/undercrew/privacy.html">Privacy policy</a> &middot;
  An <a href="/">Enkrata</a> game &middot; &copy; 2026 Enkrata</p>
</footer>
"""

# ---------------------------------------------------------------- privacy
# Body copy below is byte-for-byte the previously published policy. It is
# referenced by App Store Connect and is legally operative — restyle only.
privacy_body = f"""
<header class="masthead">
  <a href="/" aria-label="Enkrata home">{lock_sm}</a>
  <h1 class="title">Undercrew — Privacy Policy</h1>
  <p class="date">Effective August 17, 2026</p>
</header>

<div class="prose">
  <p><strong>The short version: Undercrew does not collect your data.</strong></p>
</div>

<section class="section">
  <h2>What the app collects</h2>
  <p>Nothing. Undercrew has no accounts, no sign-in, no analytics, no
  advertising, no tracking, and no third-party SDKs. The game does not
  transmit any information off your device.</p>
</section>

<section class="section">
  <h2>What stays on your device</h2>
  <p>Your game saves — the world, your crew, and your progress — are stored
  only on your device. They are included in your normal device backups
  (iCloud or local), which are governed by
  <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>,
  not ours. Deleting the app deletes its data.</p>
</section>

<section class="section">
  <h2>TestFlight beta testing</h2>
  <p>If you're running Undercrew through TestFlight, Apple may share crash
  logs and usage statistics with us, and anything you choose to send through
  TestFlight's feedback tools (comments, screenshots) comes to us as you
  submitted it. This collection is performed by Apple under the
  <a href="https://www.apple.com/legal/internet-services/itunes/testflight/">TestFlight
  terms</a>; we see it only to fix bugs and improve the game, and we don't
  share it with anyone.</p>
</section>

<section class="section">
  <h2>Children</h2>
  <p>Undercrew collects no data from anyone, children included.</p>
</section>

<section class="section">
  <h2>Changes</h2>
  <p>If the game ever adds a feature that touches data (say, cloud sync or
  leaderboards), this policy will be updated first and the effective date
  above will change. No silent revisions.</p>
</section>

<section class="section">
  <h2>Contact</h2>
  <p>Questions about this policy:
  <a href="mailto:{CONTACT}">{CONTACT}</a></p>
</section>

<hr class="rule">
<footer>
  <p><a href="/undercrew/">Undercrew</a> &middot; An <a href="/">Enkrata</a>
  game &middot; &copy; 2026 Enkrata</p>
</footer>
"""

pages = [
    ("index.html", page("Enkrata",
        "Enkrata is Kevin Holloway's development studio — games, productivity apps, and fitness projects.",
        "/", index_body)),
    ("undercrew/index.html", page("Undercrew",
        "Undercrew: a deep 2D sandbox world you never directly play — you run the crew of agents that plays it, from your phone.",
        "/undercrew/", undercrew_body)),
    ("undercrew/privacy.html", page("Undercrew — Privacy Policy",
        "Undercrew collects no data. No accounts, no analytics, no tracking, no third-party SDKs.",
        "/undercrew/privacy.html", privacy_body)),
]

for path, html in pages:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(html)
    print(f"  wrote {path}  ({len(html)} bytes)")
