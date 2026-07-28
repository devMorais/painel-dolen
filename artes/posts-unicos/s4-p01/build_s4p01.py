# -*- coding: utf-8 -*-
"""[S4-P01] Post unico "manifesto" — feed 1080x1350.
Fundo ESCURO ja montado no Photoshop (grid diagonal de fotos duotone + grao),
arquivo bg.png nesta pasta. Frase fixa: "Seu trabalho e serio. Seu site, tambem."
Space Grotesk Bold (branco) + "tambem" em Playfair Display Italic com sublinhado.
Mesmo sistema editorial dos carrosseis: crop marks, logo, grao SVG por cima."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/logo-icon-white.png"
BG = "file:///" + os.path.join(BASE, "bg.png").replace("\\", "/")
PLAYFAIR = "file:///" + os.path.join(BASE, "fonts", "PlayfairItalic.ttf").replace("\\", "/")

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.30;mix-blend-mode:overlay;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.45'/>
</svg>"""

CSS = FONTFACE + f"""
@font-face{{font-family:'Playfair';font-style:italic;font-weight:400 700;src:url('{PLAYFAIR}') format('truetype');}}
:root{{--ink:#0b0b0b;--paper:#f5f4f1;--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:100%;height:100%;overflow:hidden;}}
body{{font-family:var(--display);-webkit-font-smoothing:antialiased;}}
.canvas{{position:relative;overflow:hidden;isolation:isolate;background:var(--ink);color:#fff;width:1080px;height:1350px;}}

.bg{{position:absolute;inset:0;z-index:0;}}
.bg img{{width:100%;height:100%;object-fit:cover;display:block;}}
.scrim{{position:absolute;inset:0;z-index:1;background:radial-gradient(120% 90% at 8% 78%, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.66) 46%, rgba(0,0,0,0.86) 100%);}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.32;color:#fff;}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:40px;height:40px;}}
.brand .wm{{font-size:28px;font-weight:700;color:#fff;}}

.block{{position:absolute;z-index:10;left:96px;right:120px;top:560px;}}
.line{{font-weight:700;letter-spacing:-0.03em;line-height:0.98;font-size:96px;color:#fff;}}
.serio{{position:relative;display:inline-block;padding:2px 18px 8px;margin-left:8px;background:#fff;}}
.serio-txt{{color:#0b0b0b;}}
.tambem{{font-family:'Playfair',Georgia,serif;font-style:italic;font-weight:600;letter-spacing:0;text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:0.14em;}}

.rule{{height:3px;width:110px;background:#fff;opacity:0.85;margin-top:44px;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.45;font-weight:600;letter-spacing:0.06em;color:#fff;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
  <div class="bg"><img src="{BG}"/></div>
  <div class="scrim"></div>
  {RM}
  <div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>

  <div class="block">
    <div class="line">Seu trabalho &eacute;<br/><span class="serio"><span class="serio-txt">s&eacute;rio</span></span>.</div>
    <div class="line" style="margin-top:22px;">Seu site,<br/><span class="tambem">tamb&eacute;m</span>.</div>
    <div class="rule"></div>
  </div>

  <div class="foot">DOLEN &middot; SITES PROFISSIONAIS</div>
  {GRAIN}
</div>
</body></html>"""

open(os.path.join(BASE, "s4p01.html"), "w", encoding="utf-8").write(html)
print("html ok")
