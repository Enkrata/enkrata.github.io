# enkrata.github.io

The public face of [Enkrata](https://github.com/Enkrata) — the studio landing page,
the Undercrew page, and the privacy policy that external TestFlight requires.

Live at <https://enkrata.github.io>.

## Layout

    index.html              studio landing
    undercrew/index.html    Undercrew — description, beta, support
    undercrew/privacy.html  Undercrew privacy policy (referenced by App Store Connect)
    brand.css               tokens + page styles
    plate/                  dither tile and crop mark, mirrored from the brand kit
    build.py                assembles the three pages
    _head.tmpl              shared <head>: meta, icons, Open Graph
    _lockup.frag            the lockup, inlined so it follows the viewer's theme

## Building

```bash
python3 build.py
```

The pages are generated, so **edit `build.py`, not the HTML** — the next run
overwrites it. This exists so the head tags and the lockup cannot drift apart
across three pages.

## Brand

Colour, type and the mark come from the brand kit in
[enkrata-workspace](https://github.com/Enkrata/enkrata-workspace) under `brand/`.
`brand.css` mirrors its `tokens.css`; that file is the source of truth, so change
it there first and mirror it here.

`plate/dither-12.svg` and `plate/corner.svg` are copies of the generated files in
that repo's `brand/plate/`. They are mirrored here rather than linked, the same as
the favicons; re-copy them if the kit's geometry changes.

Two things not to undo by accident:

- **The favicon uses the mark's small cut.** Below 20px the standard cut's bar
  closes against the arc and fills the counter in. `favicon.svg` is the right file.
- **The plate assets are masks, not images.** Both are drawn in `currentColor`,
  which an external SVG cannot see when it is used as a CSS `background-image` —
  it renders black and looks deliberate. They are applied as `mask-image` with
  the ink set as `background-color`, and they must stay that way.
- **The footer stamp names the commit the page was generated from.** Building
  and committing in the same breath leaves it one commit behind. That is the
  honest reading of a build stamp, not a bug to fix.
- **No third-party fonts.** The brand specifies Jost and IBM Plex, but loading them
  from a font CDN would send visitors' IP addresses to a third party, which the
  privacy policy on this very site says does not happen. Self-host or use the
  fallback stacks.

The privacy policy's text is legally operative and is linked from App Store
Connect. Restyle it freely; do not reword it without meaning to.
