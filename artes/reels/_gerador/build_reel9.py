import os
from PIL import Image, ImageDraw, ImageFilter

BASE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(BASE, "tpl_pt")
FRAMES = os.path.join(BASE, "frames9")
os.makedirs(FRAMES, exist_ok=True)

W, H = 1080, 1920
FPS = 30
COVER_T = 1.8
SEG_B = 1.2
END_T = 2.2
XF = 0.4
XT = 0.30
FADE = 0.3

TEMPLATES = ["clarity", "medilab", "restaurantly", "flexstart", "mentor", "arsha", "logis", "day"]
N = len(TEMPLATES)
BODY_T = N * SEG_B
C, B, E = COVER_T, BODY_T, END_T
D = C + B + E

WIN_W, WIN_X, WIN_TOP = 780, 150, 190
BAR_H, VIEW_H, RADIUS = 52, 1076, 24
WIN_H = BAR_H + VIEW_H

def rounded_mask(size, r):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0]-1, size[1]-1], radius=r, fill=255)
    return m

WIN_MASK = rounded_mask((WIN_W, WIN_H), RADIUS)

def make_bar():
    bar = Image.new("RGBA", (WIN_W, BAR_H), (26, 25, 23, 255))
    d = ImageDraw.Draw(bar)
    cy = BAR_H//2
    for i in range(3):
        x = 30 + i*28
        d.ellipse([x-8, cy-8, x+8, cy+8], fill=(74, 72, 68, 255))
    d.rounded_rectangle([130, cy-16, WIN_W-130, cy+16], radius=16, fill=(44, 43, 40, 255))
    return bar

BAR = make_bar()

SCALED, TRAVEL = {}, {}
for p in TEMPLATES:
    im = Image.open(os.path.join(TPL, f"{p}.png")).convert("RGB")
    sh = int(im.height * WIN_W / im.width)
    SCALED[p] = im.resize((WIN_W, sh), Image.LANCZOS)
    TRAVEL[p] = max(0, sh - VIEW_H)

def make_base():
    base = Image.new("RGBA", (W, H), (10, 10, 10, 255))
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([WIN_X-4, WIN_TOP+30, WIN_X+WIN_W+4, WIN_TOP+WIN_H+42], radius=RADIUS+8, fill=(0,0,0,205))
    sh = sh.filter(ImageFilter.GaussianBlur(38))
    return Image.alpha_composite(base, sh)

BASE_IMG = make_base()
OVERLAY = Image.open(os.path.join(BASE, "overlay_body9.png")).convert("RGBA")
COVER = Image.open(os.path.join(BASE, "cover_c9.png")).convert("RGB")
ENDC = Image.open(os.path.join(BASE, "endcard9.png")).convert("RGB")

def zoom(img, s):
    if s <= 1.001: return img.copy()
    nw, nh = int(W*s), int(H*s)
    big = img.resize((nw, nh), Image.LANCZOS)
    x, y = (nw-W)//2, (nh-H)//2
    return big.crop((x, y, x+W, y+H))

def window_img(p, scroll):
    win = Image.new("RGBA", (WIN_W, WIN_H), (255, 255, 255, 255))
    view = SCALED[p].crop((0, scroll, WIN_W, scroll+VIEW_H)).convert("RGBA")
    win.paste(view, (0, BAR_H))
    win.paste(BAR, (0, 0))
    win.putalpha(WIN_MASK)
    return win

def scroll_of(p, tb, i):
    prog = min(1.0, max(0.0, (tb - i*SEG_B)/SEG_B))
    return int((0.0 + 0.97*prog) * TRAVEL[p])

def body_window_frame(win):
    fr = BASE_IMG.copy()
    fr.alpha_composite(win, (WIN_X, WIN_TOP))
    return fr

def render_body(t):
    tb = t - C
    i = min(int(tb / SEG_B), N-1)
    trans = None
    for k in range(1, N):
        b = k*SEG_B
        if b-XT/2 <= tb <= b+XT/2:
            trans = (k-1, k, (tb-(b-XT/2))/XT); break
    if trans:
        a, bb, al = trans
        pa, pb = TEMPLATES[a], TEMPLATES[bb]
        fa = body_window_frame(window_img(pa, scroll_of(pa, tb, a)))
        fb = body_window_frame(window_img(pb, scroll_of(pb, tb, bb)))
        fr = Image.blend(fa, fb, al)
    else:
        p = TEMPLATES[i]
        fr = body_window_frame(window_img(p, scroll_of(p, tb, i)))
    fr.alpha_composite(OVERLAY)
    return fr.convert("RGB")

def render_cover(t):
    return zoom(COVER, 1.0 + 0.045*(t/max(C,0.001)))

def render_end(t):
    te = t-(C+B)
    return zoom(ENDC, 1.0 + 0.035*(te/max(E,0.001)))

total = int(D * FPS)
for f in range(total):
    t = f / FPS
    b_cb, b_be = C, C+B
    if t <= b_cb - XF/2:
        frame = render_cover(t)
    elif t < b_cb + XF/2:
        frame = Image.blend(render_cover(t), render_body(t), (t-(b_cb-XF/2))/XF)
    elif t <= b_be - XF/2:
        frame = render_body(t)
    elif t < b_be + XF/2:
        frame = Image.blend(render_body(t), render_end(t), (t-(b_be-XF/2))/XF)
    else:
        frame = render_end(t)
    k = 1.0
    if t < FADE: k = t/FADE
    elif t > D-FADE: k = max(0.0, (D-t)/FADE)
    if k < 1.0:
        frame = Image.blend(Image.new("RGB", (W, H), (0,0,0)), frame, k)
    frame.save(os.path.join(FRAMES, f"fr_{f:04d}.png"))

print("frames:", total, "dur:", round(D,2))
