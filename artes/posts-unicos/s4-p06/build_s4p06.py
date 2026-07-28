# -*- coding: utf-8 -*-
"""[S4-P06] Post unico "manifesto" — feed 1080x1350.
Fundo BRANCO (alternancia — S4-P05 foi escuro). Frase fixa (a mais curta da
serie, 5 palavras): "Quem nao e visto, nao vende."
Enfase pedida no brief: "visto" = marca-texto (highlighter); "vende" =
sublinhado. Sem substituicao de fonte — so Space Grotesk.
Dispositivo: como a frase e curta, vai poster-scale — tipografia gigante
preenchendo quase o quadro todo, muito respiro em cima/embaixo (diferente
da densidade dos posts anteriores). O marca-texto e um rabisco organico
(path SVG), nao um retangulo perfeito — pra parecer feito a mao, nao
"caixa de PowerPoint". Varia da familia: P01 coluna, P02 assimetrico+aspas,
P03 centralizado gigante c/ device, P04 cards 2col, P05 lease/deed;
aqui = poster tipografico puro, minimo de elementos."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/logo-icon-black.png"

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.20;mix-blend-mode:multiply;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.4'/>
</svg>"""

PAPER = "#f5f4f1"
INK = "#0f0f0f"

CSS = FONTFACE + f"""
:root{{--ink:{INK};--paper:{PAPER};--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:100%;height:100%;overflow:hidden;}}
body{{font-family:var(--display);-webkit-font-smoothing:antialiased;}}
.canvas{{position:relative;overflow:hidden;isolation:isolate;background:var(--paper);color:var(--ink);width:1080px;height:1350px;}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.30;color:var(--ink);}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:40px;height:40px;}}
.brand .wm{{font-size:28px;font-weight:700;color:var(--ink);}}

.kicker{{position:absolute;top:180px;left:0;right:0;z-index:10;text-align:center;
  font-size:24px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;opacity:0.42;}}

.stage{{position:absolute;top:400px;left:0;right:0;z-index:10;text-align:center;padding:0 60px;}}
.line{{font-weight:700;letter-spacing:-0.04em;line-height:1.0;font-size:118px;}}

.visto-wrap{{position:relative;display:inline-block;}}
.hl{{position:absolute;left:-4%;right:-4%;top:8%;bottom:2%;z-index:-1;}}
.hl path{{fill:#ffd447;}}

.vende{{text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:0.1em;text-decoration-color:var(--ink);}}

.sub{{position:absolute;top:960px;left:0;right:0;z-index:10;text-align:center;
  font-size:28px;font-weight:500;opacity:0.55;line-height:1.5;padding:0 140px;}}

.rule{{position:absolute;left:50%;transform:translateX(-50%);top:1090px;height:3px;width:110px;background:var(--ink);opacity:0.6;z-index:10;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.4;font-weight:600;letter-spacing:0.06em;}}
.foot-r{{position:absolute;right:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.4;font-weight:600;letter-spacing:0.06em;text-align:right;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

HL_SVG = """<svg class="hl" viewBox="0 0 100 40" preserveAspectRatio="none">
  <path d="M1,22 C1,10 8,5 22,6 C45,7 70,4 98,9 C99,14 99,20 98,26 C72,33 40,35 4,32 C1,29 0,26 1,22 Z"/>
</svg>"""

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
  {RM}
  <div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>
  <span class="kicker">Dolen &middot; regra de com&eacute;rcio</span>

  <div class="stage">
    <div class="line">Quem n&atilde;o &eacute;<br/><span class="visto-wrap">{HL_SVG}visto</span>,<br/>n&atilde;o <span class="vende">vende</span>.</div>
  </div>

  <p class="sub">Ser visto hoje &eacute; aparecer no Google<br/>e passar confian&ccedil;a no primeiro clique.</p>
  <div class="rule"></div>

  <div class="foot">DOLEN &middot; SITES PROFISSIONAIS</div>
  <div class="foot-r">Link na bio &rarr;</div>
  {GRAIN}
</div>
</body></html>"""

open(os.path.join(BASE, "s4p06.html"), "w", encoding="utf-8").write(html)
print("html ok")
