import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR_RAIZ = os.path.join(BASE, "..", "..", "_gerador")
FONTFACE = open(os.path.join(GERADOR_RAIZ, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"

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
.bg-black{background:#0d0d0d;color:var(--paper);}

.vignette::before{content:"";position:absolute;inset:0;z-index:2;pointer-events:none;
  background:radial-gradient(ellipse 120% 90% at 50% 42%, transparent 55%, rgba(0,0,0,0.36) 100%);}

.ghost{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:1;color:transparent;white-space:nowrap;}
.on-black .ghost{-webkit-text-stroke:2px rgba(255,255,255,0.12);}

.halftone{position:absolute;z-index:1;pointer-events:none;}
.on-black .halftone{background-image:radial-gradient(rgba(255,255,255,0.22) 1.7px, transparent 1.7px);background-size:15px 15px;}
.fade-r{-webkit-mask-image:linear-gradient(to right, black, transparent);}

.orbit{position:absolute;border-radius:50%;z-index:1;}
.on-black .orbit{border:2px solid rgba(255,255,255,0.12);}
.orbit::after{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);}
.on-black .orbit::after{background:rgba(255,255,255,0.3);}

.regmark{position:absolute;width:30px;height:30px;z-index:6;opacity:0.32;}
.regmark::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}
.regmark::after{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}

.content{position:relative;z-index:10;flex:1;display:flex;flex-direction:column;justify-content:space-between;}
.story .content{padding:240px 120px 320px;}

.brand{display:flex;align-items:center;gap:18px;}
.brand img{width:46px;height:46px;}
.invert{filter:invert(1) brightness(2);}
.brand .wm{font-size:31px;font-weight:700;}

.mega{font-weight:700;letter-spacing:-0.03em;line-height:0.98;}
.support{font-weight:400;line-height:1.42;opacity:0.75;text-wrap:pretty;}
.rule{height:3px;width:120px;background:currentColor;opacity:0.85;}

.vagas-badge{display:inline-flex;align-items:center;gap:16px;align-self:flex-start;padding:16px 32px 16px 20px;border-radius:100px;background:rgba(255,255,255,0.08);border:2px solid rgba(255,255,255,0.22);}
.vagas-dots{display:flex;gap:8px;}
.vagas-dot{width:14px;height:14px;border-radius:50%;background:rgba(255,255,255,0.18);}
.vagas-dot.filled{background:#ffffff;}
.vagas-txt{font-size:26px;font-weight:700;letter-spacing:0.02em;}

.pill{align-self:flex-start;font-size:31px;font-weight:600;padding:20px 44px;border-radius:100px;background:var(--paper);color:var(--ink);}
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


def brand(inv=""):
    return f'<div class="brand"><img class="{inv}" src="{LOGO}"/><span class="wm">dolen</span></div>'


def vagas_dots(preenchidas, total):
    dots = "".join(
        f'<span class="vagas-dot{" filled" if i < preenchidas else ""}"></span>'
        for i in range(total)
    )
    return dots


# 2 de 3 vagas já fechadas — resta 1 (número real, confirmado com o Fernando em 21/07/2026)
page("s3s07_oferta_fundador", f"""
  <div class="vignette" style="position:absolute;inset:0;"></div>
  <span class="ghost" style="font-size:320px;top:170px;left:-40px;">BORA</span>
  <div class="orbit" style="width:380px;height:380px;bottom:240px;right:-110px;"></div>
  <div class="halftone fade-r" style="top:760px;right:70px;width:280px;height:340px;"></div>
  <div class="content">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:34px;">
      <div class="vagas-badge">
        <div class="vagas-dots">{vagas_dots(2, 3)}</div>
        <span class="vagas-txt">RESTA 1 VAGA DE FUNDADOR</span>
      </div>
      <h2 class="mega" style="font-size:96px;">Começa a semana<br/>tirando seu negócio<br/>do papel.</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:760px;">A última vaga de fundador garante 20% de desconto — já aplicado nos valores que você viu.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="pill">Link na bio</span>
      <span class="support" style="font-size:29px;opacity:0.6;">ou chama no direct — @dolen.ia</span>
    </div>
  </div>
""", "bg-black", "on-black")

print("ok")
