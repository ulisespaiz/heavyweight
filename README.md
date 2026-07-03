# Heavyweight Linemen

Source for [heavyweightlineman.com](https://heavyweightlineman.com) — an elite offensive line training academy in Salinas, California.

## Structure

The entire site is a single static file, `index.html`, with all CSS and JavaScript inlined. Sections, in order:

- **Hero** — animated headline with CTA buttons
- **Philosophy** (`#philosophy`) — four expandable pillars: Technique Mastery, Functional Strength, Mental Toughness, Film Study
- **Programs** (`#programs`) — Youth Development (10–13), High School Training (14–18), Position-Specific, Off-Season
- **Coaches** (`#coaching`) — Antonio Velasquez and Uli Paiz
- **Skills** (`#skills`) — eight-item curriculum list
- **Details + FAQ** (`#details`) — logistics and five FAQs
- **Contact** (`#contact`) — contact info and inquiry form

External dependencies (loaded from CDNs): Google Fonts (Bebas Neue, Oswald, Source Serif 4) and GSAP 3.12.5 with ScrollTrigger for animations.

## Local preview

No build step. Open the file directly, or serve it:

```sh
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploying

The site is plain static HTML, so any static host works (GitHub Pages, Netlify, Vercel, Cloudflare Pages). Deploy the repository root; `index.html` is the only page.

## Known issues / improvement ideas

- **Contact form is not wired up.** The form's `action` still points to the Formspree placeholder `https://formspree.io/f/YOUR_FORM_ID`, so submissions fall back to opening a `mailto:` link. Create a free form at [formspree.io](https://formspree.io) and replace the placeholder with the real form ID.
- No favicon.
- No Open Graph / Twitter card meta tags for link previews.
- No sitemap or robots.txt.
- Single-file architecture: fine at this size, but CSS/JS could be split out if the site grows.
