import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR_RAIZ = os.path.join(BASE, "..", "..", "_gerador")
FONTFACE = open(os.path.join(GERADOR_RAIZ, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/Claudia/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.5;mix-blend-mode:overlay;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.55'/>
</svg>"""

CSS = FONTFACE + """
:root{--ink:#0a0a0a;--paper:#ffffff;--soft:#f2f2f0;--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{width:100%;height:100%;overflow:hidden;}
body{font-family:var(--display);-webkit-font-smoothing:antialiased;}
.canvas{position:relative;overflow:hidden;display:flex;flex-direction:column;isolation:isolate;}
.story{width:1080px;height:1920px;}
.bg-white{background:var(--paper);color:var(--ink);}

.ghost{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:1;color:transparent;white-space:nowrap;}
.on-light .ghost{-webkit-text-stroke:2px rgba(10,10,10,0.075);}

.halftone{position:absolute;z-index:1;pointer-events:none;}
.on-light .halftone{background-image:radial-gradient(rgba(10,10,10,0.14) 1.7px, transparent 1.7px);background-size:15px 15px;}
.fade-r{-webkit-mask-image:linear-gradient(to right, black, transparent);}

.orbit{position:absolute;border-radius:50%;z-index:1;}
.on-light .orbit{border:2px solid rgba(10,10,10,0.12);}
.orbit::after{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);}
.on-light .orbit::after{background:rgba(10,10,10,0.22);}

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

.pill{align-self:flex-start;font-size:31px;font-weight:600;padding:20px 44px;border-radius:100px;background:var(--ink);color:var(--paper);}
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


# Fallback do S3-S02 "Eco do feed" (terça) — usar SÓ nos dias sem post no feed pra ecoar,
# conforme card: "dica rápida de 1 frase no padrão da marca". Nos dias com post, a ação é
# 100% no app (compartilhar + sticker), sem arte gerada.
page("s3s02_dica_rapida", f"""
  <span class="ghost" style="font-size:300px;top:150px;left:-30px;">DICA</span>
  <div class="orbit" style="width:340px;height:340px;bottom:260px;right:-100px;"></div>
  <div class="halftone fade-r" style="top:780px;right:70px;width:260px;height:320px;"></div>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:34px;">
      <span class="kicker">Dica rápida</span>
      <h2 class="mega" style="font-size:80px;max-width:840px;">Site que só o<br/>programador mexe<br/>não é seu.</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:760px;">No nosso, você troca texto e preço sozinho, quando quiser.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="pill">Link na bio</span>
      <span class="support" style="font-size:29px;opacity:0.6;">ou chama no direct — @dolen.ia</span>
    </div>
  </div>
""", "bg-white", "on-light")

print("ok")
