#!/usr/bin/env python3
"""Generate brand image assets for Heavyweight Linemen.

Produces (committed to the repo, so no build step is needed to deploy):
  - og-image.png        1200x630 social-share / Open Graph card
  - apple-touch-icon.png 180x180 iOS home-screen icon
  - favicon-32x32.png    32x32 PNG favicon fallback

The barbell mark mirrors the inline SVG logo used in the site nav.
Run with: python3 scripts/generate-assets.py  (requires Pillow)
"""
from PIL import Image, ImageDraw, ImageFont

# ---- Brand palette (matches the CSS :root variables in index.html) ----
BLACK       = (26, 15, 14)
BROWN_DEEP  = (46, 26, 25)
ORANGE      = (217, 125, 58)
ORANGE_DARK = (184, 97, 42)
CREAM       = (245, 230, 211)
CREAM_DARK  = (232, 213, 191)
GRID        = (40, 27, 23)

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(size):
    try:
        return ImageFont.truetype(FONT_BOLD, size)
    except OSError:
        return ImageFont.load_default()


def spaced_width(draw, text, fnt, spacing):
    return sum(draw.textlength(c, font=fnt) for c in text) + spacing * max(len(text) - 1, 0)


def draw_spaced(draw, text, fnt, y, fill, spacing, center_x):
    """Draw letter-spaced text centred horizontally on center_x."""
    total = spaced_width(draw, text, fnt, spacing)
    x = center_x - total / 2
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + spacing


def barbell(draw, cx, cy, size):
    """Draw the barbell mark centred at (cx, cy) within a `size`x`size` box.

    Rect coords come straight from the 32x32 nav-logo SVG viewBox.
    """
    s = size / 32.0
    rects = [
        (2, 10, 5, 12, ORANGE),       # outer-left plate
        (7, 8, 4, 16, ORANGE_DARK),   # inner-left plate
        (11, 14, 10, 4, CREAM),       # bar
        (21, 8, 4, 16, ORANGE_DARK),  # inner-right plate
        (25, 10, 5, 12, ORANGE),      # outer-right plate
    ]
    ox, oy = cx - 16 * s, cy - 16 * s
    for x, y, w, h, color in rects:
        x0, y0 = ox + x * s, oy + y * s
        draw.rounded_rectangle([x0, y0, x0 + w * s, y0 + h * s],
                               radius=max(1, int(1.2 * s)), fill=color)


def make_og():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)

    # subtle background grid (echoes the hero section)
    for x in range(0, W, 60):
        d.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 60):
        d.line([(0, y), (W, y)], fill=GRID, width=1)

    barbell(d, W // 2, 150, 150)

    draw_spaced(d, "HEAVYWEIGHT", font(112), 215, CREAM,  6, W // 2)
    draw_spaced(d, "LINEMEN",     font(112), 330, ORANGE, 6, W // 2)

    # orange divider
    d.rectangle([W // 2 - 70, 470, W // 2 + 70, 474], fill=ORANGE)

    draw_spaced(d, "ELITE OFFENSIVE LINE TRAINING", font(34), 500, CREAM_DARK, 4, W // 2)
    draw_spaced(d, "SALINAS, CALIFORNIA", font(26), 560, ORANGE, 6, W // 2)

    # bottom accent bar
    d.rectangle([0, H - 8, W, H], fill=ORANGE)
    img.save("og-image.png")
    print("wrote og-image.png", img.size)


def make_icon(path, size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = max(2, int(size * 0.18))
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=BROWN_DEEP)
    barbell(d, size // 2, size // 2, int(size * 0.74))
    img.save(path)
    print("wrote", path, img.size)


if __name__ == "__main__":
    make_og()
    make_icon("apple-touch-icon.png", 180)
    make_icon("favicon-32x32.png", 32)
