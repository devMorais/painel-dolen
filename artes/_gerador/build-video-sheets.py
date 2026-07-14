import glob, os
from PIL import Image, ImageDraw, ImageFont

FRAMES = r"C:\Users\UITEC\AppData\Local\Temp\claude\c--Users-UITEC-Herd-dolen-painel\84ffb5b7-22a7-47fc-bcb5-2cd0d8f793fe\scratchpad\design-course\frames"
SHEETS = r"C:\Users\UITEC\AppData\Local\Temp\claude\c--Users-UITEC-Herd-dolen-painel\84ffb5b7-22a7-47fc-bcb5-2cd0d8f793fe\scratchpad\design-course\sheets"

COLS, ROWS = 5, 4
THUMB_W, THUMB_H = 320, 180  # 16:9

for vid_num in range(1, 18):
    prefix = f"v{vid_num:02d}_"
    frames = sorted(glob.glob(os.path.join(FRAMES, prefix + "*.jpg")))
    if not frames:
        print(f"sem frames p/ v{vid_num:02d}")
        continue
    sheet = Image.new("RGB", (COLS * THUMB_W, ROWS * THUMB_H + 40), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((10, 8), f"Video {vid_num:02d}", fill="black")
    for i, fpath in enumerate(frames[:COLS * ROWS]):
        img = Image.open(fpath).convert("RGB")
        img = img.resize((THUMB_W, THUMB_H))
        r, c = divmod(i, COLS)
        sheet.paste(img, (c * THUMB_W, 40 + r * THUMB_H))
    out = os.path.join(SHEETS, f"video_{vid_num:02d}_sheet.jpg")
    sheet.save(out, quality=82)
    print(f"sheet ok: video_{vid_num:02d}_sheet.jpg ({len(frames)} frames)")

print("SHEETS COMPLETO")
