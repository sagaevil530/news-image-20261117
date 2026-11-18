#!/usr/bin/env python3
"""Compose entry.png: a one-page newspaper summary of 17 November 2026.

Build-time script only (not run by the entry program). Renders crisp
PIL text over a generated, text-free illustration banner.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (18, 40, 75)
NAVY_LIGHT = (30, 58, 102)
GOLD = (212, 144, 32)
CREAM = (247, 243, 232)
INK = (24, 24, 24)
GREY = (90, 88, 80)
RULE = (180, 172, 150)

SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=200))
    # wrap by pixel width
    out = []
    for line in lines:
        words = line.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    out.append(cur)
                cur = w
        if cur:
            out.append(cur)
    return out


img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 124], fill=NAVY)
d.text((512, 24), "THE WORLD IN ONE DAY", font=font(SANS_B, 24),
       fill=GOLD, anchor="ma")
d.text((512, 56), "TUESDAY  17  NOVEMBER  2026", font=font(SERIF_B, 50),
       fill=(255, 255, 255), anchor="ma")
d.line([36, 120, W - 36, 120], fill=GOLD, width=3)

# ---- banner illustration ----
banner = Image.open("assets/media-generation-banner-globe-0-f25c22f7-b456-4a81-aa07-1efcc43e0e30.webp").convert("RGB")
bw, bh = banner.size
# wide band across the globe, bridge and plane: top 6% to 48% of height
top = int(bh * 0.06)
bot = int(bh * 0.48)
band = banner.crop((0, top, bw, bot))
band = band.resize((964, int(964 * (bot - top) / bw)), Image.LANCZOS)
img.paste(band, (30, 138))
d.rectangle([30, 138, 994, 138 + band.height], outline=NAVY, width=3)
banner_h = band.height

y0 = 138 + banner_h + 10
d.text((512, y0), "Six stories that defined the day", font=font(SERIF, 25),
       fill=GREY, anchor="ma")
y0 += 38

# ---- story cards: 2 columns x 3 rows ----
stories = [
    ("UKRAINE  •  WAR",
     "Kerch Bridge span collapses",
     "Ukraine strikes the bridge linking Russia to occupied Crimea; a road span falls. Zelenskyy hails an \u201cunprecedented operation\u201d."),
    ("ASIA  •  DIPLOMACY",
     "Trump lands in Manila",
     "The president opens a three-day Asia trip at the ASEAN summit, heading for talks in China with Xi Jinping and Vladimir Putin."),
    ("MIDDLE EAST  •  CONFLICT",
     "Iran drones target US radar in Bahrain",
     "Drones fired at the US radar site at Sheikh Isa base are intercepted; no casualties reported."),
    ("ASIA-PACIFIC  •  SECURITY",
     "Japan scrambles jets",
     "Tokyo launches fighter jets and protests strongly after two suspected Russian aircraft enter its airspace early in the morning."),
    ("MIDDLE EAST  •  DIPLOMACY",
     "UK sanctions settlement builders",
     "Britain sanctions eight Israeli firms building West Bank settlements; the UK, Australia, Canada and Italy urge Israel to open Gaza aid crossings."),
    ("BUSINESS  •  TECHNOLOGY",
     "Nvidia reports after the bell",
     "First earnings since Jensen Huang stepped down as chief executive; markets watch the AI bellwether closely."),
]

card_w = 472
card_h = 160
gap_x = 12
gap_y = 8
x0, y_top = 30, y0
for i, (kicker, head, body) in enumerate(stories):
    col = i % 2
    row = i // 2
    x = x0 + col * (card_w + gap_x)
    y = y_top + row * (card_h + gap_y)
    d.rectangle([x, y, x + card_w, y + card_h], fill=(255, 255, 255),
                outline=NAVY, width=2)
    d.rectangle([x, y, x + card_w, y + 30], fill=NAVY)
    d.text((x + 12, y + 15), kicker, font=font(SANS_B, 17),
           fill=GOLD, anchor="lm")
    head_lines = wrap(d, head, font(SERIF_B, 25), card_w - 24)
    hy = y + 38
    for ln in head_lines[:2]:
        d.text((x + 12, hy), ln, font=font(SERIF_B, 25), fill=INK)
        hy += 30
    lines = wrap(d, body, font(SANS, 19), card_w - 24)
    max_body = 2 if len(head_lines) > 1 else 3
    ly = hy + 6
    for ln in lines[:max_body]:
        d.text((x + 12, ly), ln, font=font(SANS, 19), fill=(40, 40, 40))
        ly += 24

foot_y = y_top + 3 * card_h + 2 * gap_y + 8
d.line([36, foot_y, W - 36, foot_y], fill=RULE, width=2)
d.text((512, foot_y + 12),
       "Every event above happened, or was first reported, on 17 November 2026.",
       font=font(SERIF, 21), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
