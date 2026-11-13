"""Make the 4:3 horizontal cover (1440x1080) from the same still as the vertical cover.

Same design language as the vertical 1080x1920 cover:
- full-bleed photo (a 1080x810 band of the 1080x1920 still, scaled to 1440x1080)
- dark gradient scrim at the bottom
- blue pill badge "AI 科普" bottom-left, white bold text
- two-line white bold title bottom-left, no episode number

Usage: python3 make_cover_h.py ep1
Rule: whenever a cover is made, make the 4:3 horizontal version at the same time.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"

# (source still 1080x1920, title line 1, title line 2, output file)
# Add one entry per episode; paths are relative to where you run the script.
EPISODES = {
    "ep1": ("stills/ep1-still-1080x1920.png", "标题第一行", "标题第二行",
            "output/ep1-cover-h-1440x1080.jpg"),
}

# Crop band of the 1080x1920 still: hair top ~230, face 230-620, torso below.
# y 150-960 keeps head + shoulders + upper torso, no desk cut mid-frame.
CROP_TOP = 150
CROP_H = 810

W, H = 1440, 1080
BLUE = (34, 100, 238)
LEFT = 72


def font(size):
    try:
        return ImageFont.truetype(BOLD, size, index=0)
    except Exception:
        return ImageFont.truetype(BOLD, size)


def make(src, line1, line2, out):
    base = Image.open(src).convert("RGB")
    assert base.size == (1080, 1920), base.size
    band = base.crop((0, CROP_TOP, 1080, CROP_TOP + CROP_H))
    img = band.resize((W, H), Image.LANCZOS)

    # dark gradient scrim over the bottom ~45%
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    top, bottom = 600, H
    max_alpha = 165
    for y in range(top, bottom):
        a = int(max_alpha * (y - top) / (bottom - top))
        sd.line([(0, y), (W, y)], fill=(0, 0, 0, a))
    img = Image.alpha_composite(img.convert("RGBA"), scrim).convert("RGB")
    d = ImageDraw.Draw(img)

    # blue pill badge "AI 科普"
    badge_font = font(46)
    badge_text = "AI 科普"
    bw = int(d.textlength(badge_text, font=badge_font)) + 56
    bh = 88
    bx, by = LEFT, 712
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=18, fill=BLUE)
    d.text((bx + 28, by + 18), badge_text, font=badge_font, fill=(255, 255, 255))

    # two-line title, bottom-left
    title_font = font(88)
    d.text((LEFT, 836), line1, font=title_font, fill=(255, 255, 255))
    d.text((LEFT, 940), line2, font=title_font, fill=(255, 255, 255))

    img.save(out, quality=95)
    print(out, img.size)


if __name__ == "__main__":
    key = sys.argv[1]
    src, l1, l2, out = EPISODES[key]
    make(src, l1, l2, out)
