#!/usr/bin/env python3
"""World News — November 21, 2026. Editorial front-page illustration.

Deterministic Pillow renderer. Writes /output/entry.png (1024x1024, PNG).
No network, no randomness, no timestamps in the image. All assets are
bundled in assets/ next to this file. Python 3.13, standard library + Pillow.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
W, H = 1024, 1024

# Palette: deep midnight blue, warm gold, muted red, earth tones, white.
BG_TOP = (13, 32, 58)
BG_BOT = (6, 14, 28)
GOLD = (201, 162, 39)
GOLD_LT = (226, 190, 90)
WHITE = (245, 242, 235)
MUTED = (176, 186, 200)
CARD_BG = (16, 36, 64)
CARD_LINE = (44, 72, 110)
RED = (178, 74, 66)
GREEN = (96, 150, 110)
BLUE = (96, 140, 190)
ORANGE = (198, 120, 58)

HERO = {
    "region": "BAHRAIN  ·  THE GULF",
    "headline": "Iran Strikes Bahrain in Gulf Escalation",
    "caption": "Missiles and drones hit US bases and a civilian site; fire, no injuries. Two tankers also hit in Hormuz.",
}

STORIES = [
    {"color": RED, "region": "GULF OF FINLAND  ·  BALTIC",
     "headline": "Russian Ship Ablaze After Drone Strike",
     "caption": "Sparta II ablaze after the strike; 16 crew evacuated to lifeboats."},
    {"color": BLUE, "region": "KRYVYI RIH  ·  UKRAINE",
     "headline": "Missile Kills 2 in Zelensky\u2019s Hometown",
     "caption": "A boy, 7, and a paramedic, 20, dead; 60 wounded, 6 of them children."},
    {"color": GOLD, "region": "NEW YORK  ·  FRIDAY\u2019S ROUT",
     "headline": "Wall Street in Correction as AI Sell-Off Deepens",
     "caption": "S&P \u22123.7%, Dow \u2212950 pts, Nasdaq \u22125.3%; Nvidia \u221214%, CEO ousted."},
    {"color": ORANGE, "region": "SINALOA  ·  MEXICO",
     "headline": "FBI Most-Wanted Cartel Boss Caught",
     "caption": "\u201cEl Chapo Isidro\u201d arrested in Sinaloa; 11 killed in the violence."},
    {"color": BLUE, "region": "LONDON  ·  BRUSSELS",
     "headline": "UK\u2013EU Seal Post-Brexit Reset Deal",
     "caption": "Food, carbon and youth mobility deals agreed after years of talks."},
    {"color": GREEN, "region": "ANTALYA  ·  TURKEY",
     "headline": "COP31 Deadlocked as Talks Run Into Overtime",
     "caption": "Second day of overtime; fossil-fuel language dropped from the draft."},
]


def font(name, size):
    return ImageFont.truetype(os.path.join(ASSETS, name), size)


F_TITLE = None
F_DATE = None
F_HERO_H = None
F_HERO_C = None
F_REGION = None
F_HEAD = None
F_CAP = None
F_FOOT = None


def load_fonts():
    global F_TITLE, F_DATE, F_HERO_H, F_HERO_C, F_REGION, F_HEAD, F_CAP, F_FOOT
    F_TITLE = font("DejaVuSerif-Bold.ttf", 66)
    F_DATE = font("DejaVuSans-Bold.ttf", 20)
    F_HERO_H = font("DejaVuSerif-Bold.ttf", 30)
    F_HERO_C = font("DejaVuSans.ttf", 17)
    F_REGION = font("DejaVuSans-Bold.ttf", 13)
    F_HEAD = font("DejaVuSerif-Bold.ttf", 19)
    F_CAP = font("DejaVuSans.ttf", 14)
    F_FOOT = font("DejaVuSans.ttf", 13)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, lines, fnt, fill, leading):
    for ln in lines:
        w = draw.textlength(ln, font=fnt)
        draw.text((cx - w / 2, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def gradient_bg():
    img = Image.new("RGB", (W, H), BG_BOT)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t)
        g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t)
        b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    return img


def earth_layer(diameter):
    """Apollo 17 Blue Marble, circular-masked, with a soft gold rim."""
    earth = Image.open(os.path.join(ASSETS, "earth_800.jpg")).convert("RGB")
    earth = earth.resize((diameter, diameter), Image.LANCZOS)
    mask = Image.new("L", (diameter, diameter), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([0, 0, diameter - 1, diameter - 1], fill=255)
    # Soften the very edge so the disk blends into the night sky.
    mask = mask.filter(ImageFilter.GaussianBlur(1.2))
    out = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    out.paste(earth, (0, 0), mask)
    rim = ImageDraw.Draw(out)
    rim.ellipse([1, 1, diameter - 2, diameter - 2], outline=GOLD + (255,), width=3)
    return out


def glow(img, cx, cy, r, color, alpha):
    """Soft radial glow behind the Earth."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(60))
    img.alpha_composite(layer)


def render():
    load_fonts()
    img = gradient_bg().convert("RGBA")
    d = ImageDraw.Draw(img)

    # --- Masthead ---
    d.text((W / 2, 26), "SATURDAY, NOVEMBER 21, 2026", font=F_DATE,
           fill=GOLD_LT, anchor="ma")
    d.text((W / 2, 52), "WORLD NEWS", font=F_TITLE, fill=WHITE, anchor="ma")
    d.line([(64, 128), (W - 64, 128)], fill=GOLD, width=2)
    d.line([(64, 132), (W - 64, 132)], fill=GOLD, width=1)

    # --- Hero Earth ---
    cx, cy, dia = 512, 340, 400
    glow(img, cx, cy, 300, (58, 96, 150), 90)
    glow(img, cx, cy, 240, (201, 162, 39), 34)
    d = ImageDraw.Draw(img)
    earth = earth_layer(dia)
    img.alpha_composite(earth, (cx - dia // 2, cy - dia // 2))
    d = ImageDraw.Draw(img)

    # --- Hero story (Kyiv attack) ---
    y = 572
    d.text((W / 2, y), HERO["region"], font=F_REGION, fill=GOLD_LT, anchor="ma")
    y += 22
    lines = wrap(d, HERO["headline"], F_HERO_H, 880)
    y = draw_centered(d, W / 2, y, lines, F_HERO_H, WHITE, 36)
    y += 6
    lines = wrap(d, HERO["caption"], F_HERO_C, 860)
    draw_centered(d, W / 2, y, lines, F_HERO_C, MUTED, 22)

    # --- Story grid: 2 rows x 3 columns ---
    gx, gy = 20, 692
    cw, chh, gap = 320, 132, 12
    for i, s in enumerate(STORIES):
        col, row = i % 3, i // 3
        x0 = gx + col * (cw + gap)
        y0 = gy + row * (chh + gap)
        d.rounded_rectangle([x0, y0, x0 + cw, y0 + chh], radius=6,
                            fill=CARD_BG, outline=CARD_LINE, width=1)
        d.rectangle([x0, y0, x0 + cw, y0 + 4], fill=s["color"])
        tx = x0 + 14
        ty = y0 + 14
        d.text((tx, ty), s["region"], font=F_REGION, fill=s["color"])
        ty += 20
        for ln in wrap(d, s["headline"], F_HEAD, cw - 28)[:2]:
            d.text((tx, ty), ln, font=F_HEAD, fill=WHITE)
            ty += 23
        ty += 2
        for ln in wrap(d, s["caption"], F_CAP, cw - 28)[:2]:
            d.text((tx, ty), ln, font=F_CAP, fill=MUTED)
            ty += 18

    # --- Footer ---
    d.line([(64, 984), (W - 64, 984)], fill=CARD_LINE, width=1)
    d.text((W / 2, 992), "Sources: AFP  ·  Reuters  ·  AP  ·  CNN  ·  ISW   —   Editorial illustration, November 21, 2026",
           font=F_FOOT, fill=MUTED, anchor="ma")

    return img.convert("RGB")


def main():
    img = render()
    out = "/output/entry.png"
    try:
        os.makedirs("/output", exist_ok=True)
        img.save(out, format="PNG", optimize=True, compress_level=9)
    except OSError:
        out = os.path.join(HERE, "output", "entry.png")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        img.save(out, format="PNG", optimize=True, compress_level=9)
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
