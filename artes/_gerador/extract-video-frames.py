import subprocess, re, glob, os, sys

FFMPEG = r"C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
SRC = r"C:\Users\UITEC\Downloads\AULAS DESIGN EMPRESAS"
OUT = r"C:\Users\UITEC\AppData\Local\Temp\claude\c--Users-UITEC-Herd-dolen-painel\84ffb5b7-22a7-47fc-bcb5-2cd0d8f793fe\scratchpad\design-course\frames"
FRAMES_PER_VIDEO = 20

files = sorted(
    glob.glob(os.path.join(SRC, "*.mp4")),
    key=lambda p: int(re.match(r"(\d+)", os.path.basename(p)).group(1)),
)

def get_duration(path):
    r = subprocess.run([FFMPEG, "-i", path], capture_output=True, text=True, errors="ignore")
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+)", r.stderr)
    if not m:
        return None
    h, mi, s = map(int, m.groups())
    return h * 3600 + mi * 60 + s

for idx, f in enumerate(files, 1):
    dur = get_duration(f)
    if not dur:
        print(f"SKIP (sem duracao): {f}")
        continue
    # evita os primeiros/ultimos 3% (intro/outro/tela preta)
    margin = dur * 0.03
    usable = dur - 2 * margin
    for i in range(FRAMES_PER_VIDEO):
        t = margin + usable * i / (FRAMES_PER_VIDEO - 1)
        out_name = f"v{idx:02d}_f{i:02d}.jpg"
        out_path = os.path.join(OUT, out_name)
        subprocess.run(
            [FFMPEG, "-y", "-ss", str(t), "-i", f, "-frames:v", "1", "-q:v", "4", out_path],
            capture_output=True,
        )
    print(f"v{idx:02d} ok ({FRAMES_PER_VIDEO} frames) - {os.path.basename(f)}")

print("EXTRACAO COMPLETA")
