#!/usr/bin/env python3
"""Assemble the Enkrata site pages from a shared head template and the brand
lockup, so head tags and the mark cannot drift between pages."""
import os, subprocess, datetime

HEAD = open("_head.tmpl").read().strip()


def stamp():
    """The footer's machine line. It names the commit the page was generated
    from, so building and committing together leaves the stamp one commit
    behind — that is the honest reading of it, not a bug. No git, no sha."""
    today = datetime.date.today().isoformat()
    try:
        sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return f"Built {today}"
    return f'Built {today} &middot; <span class="sha">{sha}</span>'


STAMP = f'<p class="machine">{stamp()}</p>'

# The mark's own construction, stated next to it — the same numbers the
# wallpaper plate draws and brand-build.py works from.
GEOMETRY = '<p class="machine">R 32 &middot; Stroke 10 &middot; Opening 110&deg;</p>'

# The studio's construction language stays on the studio's own page. Undercrew
# wears its own world (brand/README.md section 4), so its pages take the
# machine layer — studio typography — and not the plate.
PLATE_MARKS = ('<span class="cm cm-tl" aria-hidden="true"></span>'
               '<span class="cm cm-tr" aria-hidden="true"></span>'
               '<span class="cm cm-br" aria-hidden="true"></span>'
               '<span class="cm cm-bl" aria-hidden="true"></span>')
LOCKUP = open("_lockup.frag").read().strip()

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
  {GEOMETRY}
</header>

<div class="prose">
  <p>Enkrata is Kevin Holloway's development studio — games, productivity apps,
  and fitness projects, built one at a time and shipped.</p>

  <p>The name comes from the Greek <em>enkrateia</em>: self-mastery, and the
  conviction that what you can control is enough to build something worth
  keeping.</p>
</div>

<section class="section">
  <h2>In beta</h2>
  <div class="plate">
    {PLATE_MARKS}
    <div class="now">
      <span class="status">In beta on TestFlight</span>
      <h3><a href="/undercrew/">Undercrew</a></h3>
      <p>A Terraria-deep 2D sandbox you never directly play. You run the crew
      of agents that plays it, from your phone.</p>
    </div>
  </div>
  <div class="plate" style="margin-top:16px">
    {PLATE_MARKS}
    <div class="now">
      <span class="status">In beta on TestFlight</span>
      <h3><a href="/wildhold/">Wildhold</a></h3>
      <p>A pixel-art zoo game for Mac, iPad and iPhone that you run like a
      ledger and a studbook: the business, the genetics, the numbers.</p>
    </div>
  </div>
</section>

<hr class="rule">
<footer>
  <p>&copy; 2026 Enkrata &middot; <a href="https://github.com/Enkrata">GitHub</a></p>
  {STAMP}
</footer>
"""

# -------------------------------------------------------------- undercrew
undercrew_body = f"""
<header class="masthead">
  <a href="/" aria-label="Enkrata home">{lock_sm}</a>
  <h1 class="title">Undercrew</h1>
  <p class="tagline">The depth of a world-sim. The interaction model of a coach.</p>
</header>

<div class="prose">
  <p>A deep 2D sandbox world — mining, crafting, building, the full
  tunnel-by-tunnel progression — that you never directly play. Your crew of
  agents digs the tunnels, fells the timber, and hauls the ore. You read
  their reports, draw intent on the map, write their standing orders, and
  make the risk calls. When the crew mines a tunnel, the tunnel exists; zoom
  in and watch.</p>

  <p>No virtual joystick. No energy meters. The grind is real — it's just not
  yours anymore.</p>
</div>

<section class="section">
  <h2>Beta</h2>
  <p>Undercrew is in early testing on TestFlight for iPhone. It is a young
  game, changing week by week — the crew appreciates patient testers with
  opinions.</p>
</section>

<section class="section">
  <h2>Support</h2>
  <p>Questions, bugs, or thoughts: email
  <a href="mailto:kevin@poshsocialfl.com">kevin@poshsocialfl.com</a>, or use
  the feedback button inside TestFlight.</p>
</section>

<hr class="rule">
<footer>
  <p><a href="/undercrew/privacy.html">Privacy policy</a> &middot;
  An <a href="/">Enkrata</a> game &middot; &copy; 2026 Enkrata</p>
  {STAMP}
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
  <a href="mailto:kevin@poshsocialfl.com">kevin@poshsocialfl.com</a></p>
</section>

<hr class="rule">
<footer>
  <p><a href="/undercrew/">Undercrew</a> &middot; An <a href="/">Enkrata</a>
  game &middot; &copy; 2026 Enkrata</p>
  {STAMP}
</footer>
"""

# --------------------------------------------------------------- wildhold
# Wildhold wears its own world too: the art is the game's own voxel render
# (wildhold repo, scripts/marketing/keyart.py, decision 0081), copied here.
# This page is the App Store marketing and support URL.
PIXEL_IMG = 'style="display:block;width:100%;height:auto;image-rendering:pixelated"'

wildhold_body = f"""
<header class="masthead">
  <a href="/" aria-label="Enkrata home">{lock_sm}</a>
  <h1 class="title">Wildhold</h1>
  <p class="tagline">Your zoo, your ledger, your legacy.</p>
</header>

<img src="/wildhold/art/key-art-1920x1080.png" width="1920" height="1080" {PIXEL_IMG}
  alt="Wildhold key art: a block-built savanna zoo in pixel art, with giraffes, zebras and elephants under a gold wordmark.">

<div class="prose">
  <p>Wildhold is a zoo you run like a ledger and a studbook. Start with an
  empty plot and a bank loan, lay out exhibits block by block, and close
  every month with a report: what each exhibit earned and cost, who was
  born, who died, and why the guests came or didn't.</p>

  <p>Every animal carries real genes. Keep the studbook, pair animals to keep
  inbreeding down, watch for the rare coats real populations throw, and breed
  at-risk species well enough to release them to the wild. Six biomes, forty
  species, one honest balance sheet. For Mac, iPad and iPhone.</p>
</div>

<section class="section">
  <h2>Beta</h2>
  <p>Wildhold is in testing on TestFlight. It will be free to try, with one
  purchase that unlocks the whole zoo. No ads, no accounts, no data
  collected.</p>
</section>

<section class="section">
  <h2>Support</h2>
  <p>Questions, bugs, or a zoo that went wrong: email
  <a href="mailto:wildhold@enkrata.dev">wildhold@enkrata.dev</a>, or use the
  feedback button inside TestFlight. Say which device you play on and, if
  you can, attach the saved zoo.</p>
  <p>Purchases are handled by the store you bought from. To restore the
  unlock on a new device, choose Restore on the unlock page in the game.</p>
</section>

<section class="section">
  <h2>Press</h2>
  <p>Wildhold is made by Enkrata, a small independent studio. For press
  enquiries and review copies, email
  <a href="mailto:press@enkrata.dev">press@enkrata.dev</a>.</p>
  <ul>
    <li><a href="/wildhold/art/key-art-3840x2160.png">Key art, 3840 &times; 2160</a></li>
    <li><a href="/wildhold/art/key-art-1920x1080.png">Key art, 1920 &times; 1080</a></li>
    <li><a href="/wildhold/art/logo-wordmark.png">Wordmark</a></li>
    <li><a href="/wildhold/art/icon-1024.png">App icon, 1024</a></li>
    <li><a href="/wildhold/art/animal-lineup.png">Animal lineup</a></li>
  </ul>
</section>

<hr class="rule">
<footer>
  <p><a href="/wildhold/privacy.html">Privacy policy</a> &middot;
  An <a href="/">Enkrata</a> game &middot; &copy; 2026 Enkrata</p>
  {STAMP}
</footer>
"""

# The Wildhold policy is referenced by App Store Connect once submitted, and
# is legally operative from publication — change it only with a new date.
wildhold_privacy_body = f"""
<header class="masthead">
  <a href="/" aria-label="Enkrata home">{lock_sm}</a>
  <h1 class="title">Wildhold — Privacy Policy</h1>
  <p class="date">Effective November 1, 2026</p>
</header>

<div class="prose">
  <p>Wildhold is a game made by Enkrata. This policy covers the game on Mac,
  iPad, iPhone and Steam.</p>
  <p><strong>The short version: Wildhold collects nothing.</strong></p>
</div>

<section class="section">
  <h2>What the game collects</h2>
  <p>Nothing. Wildhold has no accounts, no sign-in, no advertising, no
  analytics, no tracking, and no third-party SDKs. It does not send anything
  over the internet.</p>
</section>

<section class="section">
  <h2>What stays on your device</h2>
  <p>The game keeps your current zoo and a few settings on your device. A zoo
  you save to a file goes where you choose. Both are included in your normal
  device backups, which are governed by your platform's privacy policy, not
  ours. Deleting the game deletes what it kept.</p>
</section>

<section class="section">
  <h2>Purchases</h2>
  <p>If you buy the game or its unlock, the store you bought it from (the App
  Store or Steam) handles the payment under its own privacy policy. We do not
  receive your payment details or your identity.</p>
</section>

<section class="section">
  <h2>TestFlight beta testing</h2>
  <p>If you play Wildhold through TestFlight, Apple may share crash logs and
  usage statistics with us, and anything you choose to send through
  TestFlight's feedback tools (comments, screenshots) comes to us as you
  submitted it. This collection is performed by Apple under the
  <a href="https://www.apple.com/legal/internet-services/itunes/testflight/">TestFlight
  terms</a>; we see it only to fix bugs and improve the game, and we don't
  share it with anyone.</p>
</section>

<section class="section">
  <h2>Children</h2>
  <p>Wildhold collects no information from anyone, children included.</p>
</section>

<section class="section">
  <h2>Changes</h2>
  <p>If a future version ever needs to collect anything, this page will say
  what and why before that version ships, the effective date above will
  change, and the store's privacy label will change with it. No silent
  revisions.</p>
</section>

<section class="section">
  <h2>Contact</h2>
  <p>Questions about this policy:
  <a href="mailto:wildhold@enkrata.dev">wildhold@enkrata.dev</a></p>
</section>

<hr class="rule">
<footer>
  <p><a href="/wildhold/">Wildhold</a> &middot; An <a href="/">Enkrata</a>
  game &middot; &copy; 2026 Enkrata</p>
  {STAMP}
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
    ("wildhold/index.html", page("Wildhold",
        "Wildhold: a pixel-art zoo game for Mac, iPad and iPhone that you run like a ledger and a studbook.",
        "/wildhold/", wildhold_body)),
    ("wildhold/privacy.html", page("Wildhold — Privacy Policy",
        "Wildhold collects no data. No accounts, no analytics, no tracking, no third-party SDKs.",
        "/wildhold/privacy.html", wildhold_privacy_body)),
]

for path, html in pages:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(html)
    print(f"  wrote {path}  ({len(html)} bytes)")
