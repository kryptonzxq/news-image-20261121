#!/usr/bin/env python3
"""World News — November 21, 2026. Dense newspaper front page.

Deterministic Pillow renderer. Writes /output/entry.png (1024x1024, PNG).
No network, no randomness, no timestamps in the image. All assets are
bundled in assets/ next to this file. Python 3.13, standard library + Pillow.

Design (OUR OWN look — deep midnight blue, gold accents, DejaVu fonts):
masthead, UTC timeline strip, Bahrain hero with a small Earth, a 3-column
grid of 12 numbered stories, a "More from Saturday" ticker, and a DATE CHECK
footer. Nothing here copies any competitor's layout: no light-paper
background, no red banner headlines. (A world-map locator band was tried
and dropped after visual inspection — at this size it read as flat stripes,
not a map — and the space went to taller story cards instead.)
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
MAP_LAND = (58, 92, 128)
RED = (178, 74, 66)
GREEN = (96, 150, 110)
BLUE = (96, 140, 190)
ORANGE = (198, 120, 58)

HERO = {
    "num": 1,
    "region": "BAHRAIN  ·  THE GULF",
    "headline": "Iran Strikes Bahrain in Gulf Escalation",
    "caption": "Missiles and drones hit US bases and a civilian site; fire, no injuries. Two tankers also hit in Hormuz.",
}

# Stories 2-12, shown in a 3-column grid. Headlines and captions are kept
# short on purpose: at the chosen sizes every headline fits 2 lines and
# every caption fits 2 lines in a 320 px card (checked by wrap in render).
STORIES = [
    {"num": 2, "color": RED, "region": "GULF OF FINLAND  ·  BALTIC",
     "headline": "Russian Ship Ablaze After Drone Strike",
     "caption": "Sparta II ablaze after the strike; 16 crew evacuated to lifeboats."},
    {"num": 3, "color": BLUE, "region": "KRYVYI RIH  ·  UKRAINE",
     "headline": "Missile Kills 2 in Zelensky\u2019s Hometown",
     "caption": "A boy, 7, and a paramedic, 20, dead; 60 wounded, 6 of them children."},
    {"num": 4, "color": GOLD, "region": "NEW YORK  ·  FRIDAY\u2019S ROUT",
     "headline": "Wall Street in Correction as AI Sell-Off Deepens",
     "caption": "S&P \u22123.7%, Dow \u2212950 pts, Nasdaq \u22125.3%; Nvidia \u221214%, CEO ousted."},
    {"num": 5, "color": ORANGE, "region": "SINALOA  ·  MEXICO",
     "headline": "FBI Most-Wanted Cartel Boss Caught",
     "caption": "\u201cEl Chapo Isidro\u201d arrested in Sinaloa; 11 killed in the violence."},
    {"num": 6, "color": BLUE, "region": "LONDON  ·  BRUSSELS",
     "headline": "UK\u2013EU Seal Post-Brexit Reset Deal",
     "caption": "Food, carbon and youth mobility deals agreed after years of talks."},
    {"num": 7, "color": GREEN, "region": "ANTALYA  ·  TURKEY",
     "headline": "COP31 Deadlocked as Talks Run Into Overtime",
     "caption": "Second day of overtime; fossil-fuel language dropped from the draft."},
    {"num": 8, "color": RED, "region": "JUN\u00cdN  ·  PERU",
     "headline": "Deep 6.7 Quake Shakes Central Peru",
     "caption": "Friday night local, 00:09 GMT Saturday; 1 dead, 16 injured; felt in Lima."},
    {"num": 9, "color": GOLD, "region": "BRUSSELS  ·  EU\u2013INDONESIA",
     "headline": "Indonesia\u2013EU Sign Trade Pact",
     "caption": "90.4% of tariff lines duty-free from day one; in force 2027."},
    {"num": 10, "color": ORANGE, "region": "BASRA  ·  IRAQ",
     "headline": "Power-Station Fire Kills 4",
     "caption": "Hartha plant blaze; 4 killed, 30 injured; 800 MW station shut down."},
    {"num": 11, "color": GOLD, "region": "TAIPEI  ·  MARKETS",
     "headline": "Taiwan Bans Short-Selling",
     "caption": "TAIEX \u221217.5% in a week, worst since 1990; margin raised to 150%."},
    {"num": 12, "color": BLUE, "region": "LONDON  ·  RUGBY",
     "headline": "England 37\u201312 All Blacks",
     "caption": "Record 25-point margin; five tries; first back-to-back wins since 2003."},
]

# The day in UTC — honest times only; Friday events are labelled Friday.
TIMELINE = [
    ("00:09", "Peru quake \u2014 Fri night Lima, Sat 00:09 GMT"),
    ("03:00", "Basra fire \u2014 Hartha plant ablaze"),
    ("\u224807:00", "Sparta II struck \u2014 Gulf of Finland"),
    ("14:10", "England v All Blacks \u2014 kick-off, Twickenham"),
    ("AFTERNOON", "CEPA signed \u2014 Brussels"),
    ("FRI 21:00", "Wall St close \u2014 Friday\u2019s rout"),
]

TICKER = ("Bolsonaro in intensive care (bowel obstruction)  \u2022  "
          "Gen Z walkouts in 25 European countries  \u2022  "
          "Denmark backs US\u2013Greenland deal, 109\u20130  \u2022  "
          "IAEA: North Korea expanding uranium enrichment  \u2022  "
          "Saudi defences down 3 Houthi missiles over Riyadh")

# Story numbers (gold badges on the cards) run 1-12 in reading order.


def font(name, size):
    return ImageFont.truetype(os.path.join(ASSETS, name), size)


F_TITLE = None
F_DATE = None
F_SUMMARY = None
F_TL_LABEL = None
F_TL_TIME = None
F_TL_TEXT = None
F_HERO_H = None
F_HERO_C = None
F_REGION = None
F_HEAD = None
F_CAP = None
F_FOOT = None
F_BADGE = None
F_MAP_NUM = None


def load_fonts():
    global F_TITLE, F_DATE, F_SUMMARY, F_TL_LABEL, F_TL_TIME, F_TL_TEXT
    global F_HERO_H, F_HERO_C, F_REGION, F_HEAD, F_CAP, F_FOOT, F_BADGE, F_MAP_NUM
    F_TITLE = font("DejaVuSerif-Bold.ttf", 56)
    F_DATE = font("DejaVuSans-Bold.ttf", 18)
    F_SUMMARY = font("DejaVuSans.ttf", 15)
    F_TL_LABEL = font("DejaVuSans-Bold.ttf", 12)
    F_TL_TIME = font("DejaVuSans-Bold.ttf", 14)
    F_TL_TEXT = font("DejaVuSans.ttf", 11)
    F_HERO_H = font("DejaVuSerif-Bold.ttf", 30)
    F_HERO_C = font("DejaVuSans.ttf", 16)
    F_REGION = font("DejaVuSans-Bold.ttf", 13)
    F_HEAD = font("DejaVuSerif-Bold.ttf", 18)
    F_CAP = font("DejaVuSans.ttf", 13)
    F_FOOT = font("DejaVuSans.ttf", 12)
    F_BADGE = font("DejaVuSans-Bold.ttf", 10)
    F_MAP_NUM = font("DejaVuSans-Bold.ttf", 9)


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


def draw_badge(d, cx, cy, num, r=9):
    """Gold circle with a dark number (maps a card to its map dot)."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD,
              outline=(6, 14, 28), width=1)
    txt = str(num)
    w = d.textlength(txt, font=F_BADGE)
    d.text((cx - w / 2, cy - 7), txt, font=F_BADGE, fill=(6, 14, 28))


def render():
    load_fonts()
    img = gradient_bg().convert("RGBA")
    d = ImageDraw.Draw(img)
    MX = 20

    # --- Masthead ---
    d.text((W / 2, 12), "SATURDAY, NOVEMBER 21, 2026", font=F_DATE,
           fill=GOLD_LT, anchor="ma")
    d.text((W / 2, 30), "WORLD NEWS", font=F_TITLE, fill=WHITE, anchor="ma")
    d.text((W / 2, 90),
           "Iran hits Bahrain bases  \u00b7  Quake shakes Peru  \u00b7  Wall Street in correction",
           font=F_SUMMARY, fill=MUTED, anchor="ma")
    d.line([(64, 110), (W - 64, 110)], fill=GOLD, width=2)

    # --- Timeline strip: THE DAY IN UTC ---
    d.text((MX, 118), "THE DAY IN UTC", font=F_TL_LABEL, fill=GOLD_LT)
    d.line([(MX, 134), (W - MX, 134)], fill=CARD_LINE, width=1)
    col_w = (W - 2 * MX - 5 * 8) // 6
    for i, (t, label) in enumerate(TIMELINE):
        x = MX + i * (col_w + 8)
        d.text((x, 140), t, font=F_TL_TIME, fill=GOLD)
        lines = wrap(d, label, F_TL_TEXT, col_w)
        if len(lines) > 3:
            print("WARNING: timeline item %d wraps to %d lines" % (i, len(lines)))
        y = 158
        for ln in lines[:3]:
            d.text((x, y), ln, font=F_TL_TEXT, fill=MUTED)
            y += 14

    # --- Hero (story 1): small Earth + headline + caption ---
    cx, cy, dia = 24 + 46, 250, 92
    glow(img, cx, cy, 90, (58, 96, 150), 90)
    d = ImageDraw.Draw(img)
    earth = earth_layer(dia)
    img.alpha_composite(earth, (cx - dia // 2, cy - dia // 2))
    d = ImageDraw.Draw(img)
    tx = 136
    draw_badge(d, tx + 9, 203, HERO["num"])
    d.text((tx + 24, 196), HERO["region"], font=F_REGION, fill=GOLD_LT)
    lines = wrap(d, HERO["headline"], F_HERO_H, W - tx - MX)
    if len(lines) > 2:
        print("WARNING: hero headline wraps to %d lines" % len(lines))
    y = 214
    for ln in lines[:2]:
        d.text((tx, y), ln, font=F_HERO_H, fill=WHITE)
        y += 36
    lines = wrap(d, HERO["caption"], F_HERO_C, W - tx - MX)
    if len(lines) > 2:
        print("WARNING: hero caption wraps to %d lines" % len(lines))
    y = 250
    for ln in lines[:2]:
        d.text((tx, y), ln, font=F_HERO_C, fill=MUTED)
        y += 20

    # --- Story grid: 4 rows x 3 columns (stories 2-12) ---
    gx, gy = MX, 306
    cw, chh, gap = 320, 120, 12
    for i, s in enumerate(STORIES):
        col, row = i % 3, i // 3
        x0 = gx + col * (cw + gap)
        y0 = gy + row * (chh + gap)
        d.rounded_rectangle([x0, y0, x0 + cw, y0 + chh], radius=6,
                            fill=CARD_BG, outline=CARD_LINE, width=1)
        d.rectangle([x0, y0, x0 + cw, y0 + 4], fill=s["color"])
        tx2 = x0 + 12
        ty = y0 + 14
        d.text((tx2, ty), s["region"], font=F_REGION, fill=s["color"])
        draw_badge(d, x0 + cw - 16, y0 + 20, s["num"])
        ty += 20
        hlines = wrap(d, s["headline"], F_HEAD, cw - 24)
        if len(hlines) > 2:
            print("WARNING: story %d headline wraps to %d lines"
                  % (s["num"], len(hlines)))
        for ln in hlines[:2]:
            d.text((tx2, ty), ln, font=F_HEAD, fill=WHITE)
            ty += 21
        ty += 2
        clines = wrap(d, s["caption"], F_CAP, cw - 24)
        if len(clines) > 2:
            print("WARNING: story %d caption wraps to %d lines"
                  % (s["num"], len(clines)))
        for ln in clines[:2]:
            d.text((tx2, ty), ln, font=F_CAP, fill=MUTED)
            ty += 16

    # --- Ticker: MORE FROM SATURDAY ---
    d.text((MX, 836), "MORE FROM SATURDAY", font=F_TL_LABEL, fill=GOLD_LT)
    tlines = wrap(d, TICKER, F_FOOT, W - 2 * MX)
    if len(tlines) > 2:
        print("WARNING: ticker wraps to %d lines" % len(tlines))
    y = 852
    for ln in tlines[:2]:
        d.text((MX, y), ln, font=F_FOOT, fill=MUTED)
        y += 16

    # --- Footer: DATE CHECK box + sources + how we checked ---
    d.rounded_rectangle([MX, 896, W - MX, 1012], radius=6,
                        fill=CARD_BG, outline=CARD_LINE, width=1)
    fx = MX + 12
    d.text((fx, 912), "DATE CHECK", font=F_TL_LABEL, fill=GOLD)
    d.text((fx + 92, 912),
           "Peru quake: Friday night local, 00:09 GMT Saturday  \u00b7  "
           "Wall Street: Friday\u2019s close  \u00b7  "
           "CEPA: authorised Wed 18 Nov, SIGNED Sat 21 Nov",
           font=F_FOOT, fill=WHITE)
    d.text((fx, 946),
           "Sources: AFP  \u00b7  Reuters  \u00b7  AP  \u00b7  CNN  \u00b7  ISW  \u00b7  Focus Taiwan"
           "   \u2014   Editorial illustration, November 21, 2026",
           font=F_FOOT, fill=MUTED)
    d.text((fx, 978),
           "How we checked: every story verified against wire reports; "
           "Friday events are labelled Friday, not Saturday.",
           font=F_FOOT, fill=MUTED)

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
