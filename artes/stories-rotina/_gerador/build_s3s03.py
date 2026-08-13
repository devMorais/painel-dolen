import os

BASE = os.path.dirname(os.path.abspath(__file__))
BASEURL = BASE.replace("\\", "/")
GERADOR_RAIZ = os.path.join(BASE, "..", "..", "_gerador")
FONTFACE = open(os.path.join(GERADOR_RAIZ, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/Claudia/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"
MISS_SHOT = os.path.join(GERADOR_RAIZ, "trabalhos", "miss_desk.png").replace("\\", "/")

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.5;mix-blend-mode:overlay;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.5'/>
</svg>"""

CSS = FONTFACE + """
:root{--ink:#0a0a0a;--paper:#ffffff;--soft:#f2f2f0;--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{width:100%;height:100%;overflow:hidden;}
body{font-family:var(--display);-webkit-font-smoothing:antialiased;}
.canvas{position:relative;overflow:hidden;display:flex;flex-direction:column;isolation:isolate;}
.story{width:1080px;height:1920px;}
.bg-white{background:var(--paper);color:var(--ink);}

.regmark{position:absolute;width:30px;height:30px;z-index:6;opacity:0.32;}
.regmark::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}
.regmark::after{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}

.content{position:relative;z-index:10;flex:1;display:flex;flex-direction:column;justify-content:space-between;}
.story .content{padding:240px 120px 320px;}

.brand{display:flex;align-items:center;gap:18px;}
.brand img{width:46px;height:46px;}
.brand .wm{font-size:31px;font-weight:700;}

.kicker{font-size:26px;font-weight:600;letter-spacing:0.24em;text-transform:uppercase;opacity:0.55;}
.mega{font-weight:700;letter-spacing:-0.03em;line-height:1.02;}
.support{font-weight:400;line-height:1.42;opacity:0.75;text-wrap:pretty;}
.rule{height:3px;width:120px;background:currentColor;opacity:0.85;}

.frames{display:flex;flex-direction:column;gap:34px;}
.frame-wrap{position:relative;}
.tag{position:absolute;top:-22px;left:-22px;z-index:11;width:64px;height:64px;border-radius:50%;background:var(--ink);color:var(--paper);display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;box-shadow:0 10px 24px rgba(0,0,0,0.25);}
.browser{border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 40px 90px rgba(0,0,0,0.22), 0 0 0 1px rgba(0,0,0,0.05);}
.browser .bar{height:56px;display:flex;align-items:center;gap:16px;padding:0 24px;background:#ececea;border-bottom:1px solid rgba(0,0,0,0.06);}
.browser .dots{display:flex;gap:10px;flex:none;}
.browser .dots i{width:13px;height:13px;border-radius:50%;background:#c6c6c2;}
.browser .url{flex:1;height:34px;border-radius:100px;background:#fff;display:flex;align-items:center;padding:0 20px;font-size:20px;color:#5a5a5a;font-weight:500;letter-spacing:0.01em;}
.browser .shot-wrap{overflow:hidden;}
.browser img{display:block;width:100%;}
"""

RM_STORY = '<span class="regmark" style="top:190px;left:70px;"></span><span class="regmark" style="top:190px;right:70px;"></span><span class="regmark" style="bottom:270px;left:70px;"></span><span class="regmark" style="bottom:270px;right:70px;"></span>'


def page(name, body, bgcls, lightcls):
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas story {bgcls} {lightcls}">
{RM_STORY}
{body}
{GRAIN}
</div>
</body></html>"""
    open(os.path.join(BASE, name + ".html"), "w", encoding="utf-8").write(html)


def brand():
    return f'<div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>'


def frame(tag, shot_src, url_label, crop_h, shift=0):
    return f"""<div class="frame-wrap">
      <span class="tag">{tag}</span>
      <div class="browser">
        <div class="bar"><span class="dots"><i></i><i></i><i></i></span><span class="url">{url_label}</span></div>
        <div class="shot-wrap" style="height:{crop_h}px;"><img style="margin-top:-{shift}px;" src="{shot_src}"/></div>
      </div>
    </div>"""


# site "amador" e generico, sem citar nenhuma marca real (mockup proprio, nao capturado de site de terceiros)
page("s3s03_enquete", f"""
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:20px;">
      <span class="kicker">Enquete rápida</span>
      <h2 class="mega" style="font-size:62px;max-width:840px;">Qual passa mais confiança?</h2>
      <div class="rule"></div>
      <div class="frames">
        {frame("A", f"file:///{BASEURL}/amador_mock.png", "lojadaana.paginagratis.net", 360)}
        {frame("B", f"file:///{MISS_SHOT}", "votepelasuamiss.com.br", 360, shift=380)}
      </div>
    </div>
    <p class="support" style="font-size:28px;">Escolhe aí no sticker ☝ — depois eu conto o resultado.</p>
  </div>
""", "bg-white", "on-light")

print("ok")
