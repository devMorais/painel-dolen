# -*- coding: utf-8 -*-
"""[S4-P02] Post unico "manifesto" — feed 1080x1350.
Fundo BRANCO (alternancia — S4-P01 foi escuro). Frase fixa:
"Presenca profissional nao e luxo. E necessidade."
Enfase em "necessidade" — serifa italica (Playfair) sublinhada, tratamento
grande/isolado pra virar o "money shot" do post. Composicao varia de propósito
em relacao ao P01 (que era coluna unica alinhada a esquerda): aqui usa uma
aspa gigante fantasma como pano de fundo e quebra assimetrica das linhas,
pra nao repetir o mesmo layout dentro do mesmo formato "manifesto"."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/logo-icon-black.png"
PLAYFAIR = "file:///" + os.path.join(BASE, "fonts", "PlayfairItalic.ttf").replace("\\", "/")

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.22;mix-blend-mode:multiply;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.4'/>
</svg>"""

PAPER = "#f5f4f1"
INK = "#0f0f0f"

CSS = FONTFACE + f"""
@font-face{{font-family:'Playfair';font-style:italic;font-weight:400 700;src:url('{PLAYFAIR}') format('truetype');}}
:root{{--ink:{INK};--paper:{PAPER};--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:100%;height:100%;overflow:hidden;}}
body{{font-family:var(--display);-webkit-font-smoothing:antialiased;}}
.canvas{{position:relative;overflow:hidden;isolation:isolate;background:var(--paper);color:var(--ink);width:1080px;height:1350px;}}

.quote{{position:absolute;top:-210px;right:20px;font-family:'Playfair',Georgia,serif;font-style:italic;font-weight:700;
  font-size:820px;line-height:1;color:transparent;-webkit-text-stroke:2px rgba(15,15,15,0.07);z-index:0;user-select:none;}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.30;color:var(--ink);}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:40px;height:40px;}}
.brand .wm{{font-size:28px;font-weight:700;color:var(--ink);}}

.kicker{{position:absolute;top:230px;left:96px;z-index:10;font-size:24px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;opacity:0.42;}}

.block{{position:absolute;z-index:10;left:96px;right:96px;top:300px;}}
.l1{{font-weight:700;letter-spacing:-0.03em;line-height:1.03;font-size:70px;}}
.l2{{font-weight:700;letter-spacing:-0.03em;line-height:1.0;font-size:70px;margin-top:8px;opacity:0.34;}}

.punch{{position:absolute;left:96px;right:70px;top:610px;z-index:11;}}
.necessidade{{display:block;font-family:'Playfair',Georgia,serif;font-style:italic;font-weight:700;
  font-size:168px;line-height:0.92;letter-spacing:-0.01em;color:var(--ink);
  text-decoration:underline;text-decoration-thickness:5px;text-underline-offset:0.08em;}}
.e{{font-family:var(--display);font-weight:700;font-size:60px;letter-spacing:-0.02em;display:block;margin-bottom:6px;opacity:0.75;}}

.rule{{position:absolute;left:96px;top:1040px;height:3px;width:110px;background:var(--ink);opacity:0.85;z-index:10;}}
.support{{position:absolute;left:96px;right:180px;top:1080px;z-index:10;font-size:29px;font-weight:500;opacity:0.62;line-height:1.4;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.4;font-weight:600;letter-spacing:0.06em;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
  <div class="quote">&rdquo;</div>
  {RM}
  <div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>
  <span class="kicker">Dolen &middot; direto ao ponto</span>

  <div class="block">
    <div class="l1">Presen&ccedil;a profissional<br/>n&atilde;o &eacute; luxo.</div>
  </div>

  <div class="punch">
    <span class="e">&Eacute;</span>
    <span class="necessidade">necessidade.</span>
  </div>

  <div class="rule"></div>
  <p class="support">Quem n&atilde;o &eacute; encontrado, em 2026,<br/>n&atilde;o &eacute; considerado.</p>

  <div class="foot">DOLEN &middot; SITES PROFISSIONAIS</div>
  {GRAIN}
</div>
</body></html>"""

open(os.path.join(BASE, "s4p02.html"), "w", encoding="utf-8").write(html)
print("html ok")
