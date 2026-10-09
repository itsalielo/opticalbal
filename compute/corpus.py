"""Synthetic balance-test corpus for the optical-balancing computational track.

Generates geometric compositions (one factor varied at a time — the classic
paradigms) plus logo-like two-element marks. Each image ships with metadata
describing the intended manipulation. These are NOT human-judgment ground
truth — they are structured stimuli for model-vs-model comparison.

All images 400x400, white background. Run: python3 corpus.py
"""
import json
import os
from PIL import Image, ImageDraw

SIZE = 400
CX, CY = SIZE // 2, SIZE // 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")
META = []


def canvas():
    return Image.new("RGB", (SIZE, SIZE), "white")


def save(name, img, manipulation, note=""):
    img.save(os.path.join(OUT, name + ".png"))
    META.append({"name": name, "manipulation": manipulation, "note": note})


def disk(d, xy, r, fill):
    d.ellipse([xy[0] - r, xy[1] - r, xy[0] + r, xy[1] + r], fill=fill)


def build():
    os.makedirs(OUT, exist_ok=True)

    # ---- geometric: position ----
    im = canvas(); disk(ImageDraw.Draw(im), (CX, CY), 60, "black")
    save("disk_centered", im, "baseline", "single black disk, geometrically centered")

    im = canvas(); disk(ImageDraw.Draw(im), (CX - 100, CY), 60, "black")
    save("disk_left", im, "position", "disk shifted left: mass left of center")

    im = canvas(); disk(ImageDraw.Draw(im), (CX + 100, CY), 60, "black")
    save("disk_right", im, "position", "disk shifted right: mass right of center")

    im = canvas(); disk(ImageDraw.Draw(im), (CX, CY - 100), 60, "black")
    save("disk_top", im, "position", "disk shifted up (tests vertical anisotropy)")

    im = canvas(); disk(ImageDraw.Draw(im), (CX, CY + 100), 60, "black")
    save("disk_bottom", im, "position", "disk shifted down")

    # ---- geometric: area vs lightness (inverse-ratio paradigm) ----
    im = canvas(); d = ImageDraw.Draw(im)
    disk(d, (CX - 90, CY), 80, (200, 200, 200))   # big, light
    disk(d, (CX + 90, CY), 40, (0, 0, 0))          # small, black
    save("two_inverse_ratio", im, "area x lightness",
         "big light disk left vs small black disk right (Munsell-style)")

    im = canvas(); d = ImageDraw.Draw(im)
    disk(d, (CX - 90, CY), 60, (0, 0, 0))
    disk(d, (CX + 90, CY), 60, (210, 210, 210))
    save("dark_vs_light", im, "lightness", "equal areas, black vs light gray")

    im = canvas(); d = ImageDraw.Draw(im)
    disk(d, (CX - 90, CY), 80, (0, 0, 0))
    disk(d, (CX + 90, CY), 40, (0, 0, 0))
    save("big_vs_small", im, "area", "same black, 4:1 area ratio")

    # ---- geometric: hue / saturation ----
    im = canvas(); d = ImageDraw.Draw(im)
    disk(d, (CX - 90, CY), 60, (220, 20, 20))     # saturated red
    disk(d, (CX + 90, CY), 60, (20, 60, 220))     # saturated blue
    save("red_vs_blue", im, "hue", "equal area/saturation, red vs blue")

    im = canvas(); d = ImageDraw.Draw(im)
    disk(d, (CX - 90, CY), 60, (220, 20, 20))     # saturated red
    disk(d, (CX + 90, CY), 60, (170, 120, 120))   # desaturated red, ~same lightness
    save("sat_high_vs_low", im, "saturation", "same hue family, high vs low saturation")

    # ---- geometric: multi-element ----
    im = canvas(); d = ImageDraw.Draw(im)
    disk(d, (110, 110), 55, (0, 0, 0))
    disk(d, (300, 130), 30, (150, 150, 150))
    disk(d, (290, 300), 30, (150, 150, 150))
    save("quadrants_heavy_UL", im, "position x lightness",
         "heavy element upper-left, light elements elsewhere")

    im = canvas(); d = ImageDraw.Draw(im)
    disk(d, (CX, 120), 45, (0, 0, 0))
    disk(d, (120, 300), 45, (0, 0, 0))
    disk(d, (280, 300), 45, (0, 0, 0))
    save("three_triangle", im, "position", "three equal disks, triangular arrangement")

    im = canvas(); d = ImageDraw.Draw(im)
    d.rectangle([60, 170, 200, 230], fill=(0, 0, 0))
    d.rectangle([200, 170, 340, 230], fill=(160, 160, 160))
    save("bar_left_heavy", im, "lightness", "horizontal bar: black left half, gray right half")

    # ---- logo-like: two-element marks ----
    def bars(draw, left_style, right_style, right_width=None):
        # two vertical rounded bars, Switch-logo-like proportions
        w = 70
        h = 220
        x0 = CX - w - 18
        rw = right_width or w
        x1 = CX + 18
        if left_style == "outline":
            draw.rounded_rectangle([x0, CY - h // 2, x0 + w, CY + h // 2],
                                  radius=35, outline=(0, 0, 0), width=14)
        else:
            draw.rounded_rectangle([x0, CY - h // 2, x0 + w, CY + h // 2],
                                  radius=35, fill=(0, 0, 0))
        if right_style == "outline":
            draw.rounded_rectangle([x1, CY - h // 2, x1 + rw, CY + h // 2],
                                  radius=35, outline=(0, 0, 0), width=14)
        else:
            draw.rounded_rectangle([x1, CY - h // 2, x1 + rw, CY + h // 2],
                                  radius=35, fill=(0, 0, 0))

    im = canvas(); bars(ImageDraw.Draw(im), "solid", "solid")
    save("mark_symmetric", im, "baseline", "two identical solid bars, centered")

    im = canvas(); bars(ImageDraw.Draw(im), "outline", "solid")
    save("mark_switch_structure", im, "structure",
         "left bar outlined, right bar solid, same outer size (Switch-logo structure)")

    im = canvas(); bars(ImageDraw.Draw(im), "outline", "solid", right_width=56)
    save("mark_switch_narrow_right", im, "structure + area",
         "right solid bar drawn narrower (~outline width compensation, per Switch analyses)")

    im = canvas(); d = ImageDraw.Draw(im)
    d.ellipse([110, 110, 290, 290], fill=(66, 133, 244))
    d.rectangle([200, 175, 290, 225], fill=(255, 255, 255))  # crossbar gap, G-like
    save("mark_g_style", im, "structure", "circle with crossbar interruption (G-like)")

    with open(os.path.join(OUT, "metadata.json"), "w") as f:
        json.dump(META, f, indent=2)
    print(f"wrote {len(META)} images to {OUT}")


if __name__ == "__main__":
    build()
