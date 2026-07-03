# Heavyweight Linemen

Marketing site for **Heavyweight Linemen** — elite offensive line training in
Salinas, California.

Live: <https://heavyweightlineman.com>

## What this is

A single, self-contained static page (`index.html`) with all CSS and JavaScript
inline. The only external dependencies are loaded from CDNs:

- [Google Fonts](https://fonts.google.com) — Bebas Neue, Oswald, Source Serif 4
- [GSAP](https://gsap.com) + ScrollTrigger — scroll and entrance animations

There is no build step or framework — open `index.html` in a browser to view it.

Page sections, in order: Hero, Philosophy (`#philosophy`), Programs
(`#programs`), Coaches (`#coaching`), Skills (`#skills`), Details + FAQ
(`#details`), Contact (`#contact`).

## Project structure

```
index.html            The entire site (markup + inline CSS + inline JS)
favicon.svg           Vector favicon (barbell mark)
favicon-32x32.png     PNG favicon fallback
apple-touch-icon.png  iOS home-screen icon
og-image.png          1200x630 social-share / Open Graph card
robots.txt            Crawler directives + sitemap reference
sitemap.xml           XML sitemap
llms.txt              Plain-text site summary for AI assistants / LLM crawlers
_headers              Cloudflare Pages response headers (security + caching)
scripts/
  generate-assets.py  Regenerates og-image.png and the icons (optional; needs Pillow)
```

## Deploying (Cloudflare Pages)

The site is served from Cloudflare. To deploy from this repo:

1. Cloudflare dashboard → **Workers & Pages** → create a **Pages** project.
2. Connect it to this GitHub repo (`ulisespaiz/heavyweight`).
3. Framework preset: **None**. Build command: *(empty)*. Build output directory: `/`.
4. Deploy.

`robots.txt`, `sitemap.xml`, `llms.txt`, the favicons and `og-image.png` are
committed, so they are served as real static files, and `_headers` is applied
automatically by Pages.

## Follow-ups

- **Contact form** posts to `https://formspree.io/f/YOUR_FORM_ID`. Replace
  `YOUR_FORM_ID` (in `index.html`) with a real [Formspree](https://formspree.io)
  form ID, or the form falls back to opening a `mailto:` link.
- Add a street address and phone number to the structured data in `index.html`
  (the `SportsActivityLocation` block) for stronger local SEO, and create a
  Google Business Profile.
- After deploying, submit `sitemap.xml` in
  [Google Search Console](https://search.google.com/search-console).
- Add real training photos (hero background, coach headshots, program cards)
  with descriptive, keyword-rich `alt` text.
