# -*- coding: utf-8 -*-
"""[S4-P03] Post unico "manifesto" — feed 1080x1350.
Fundo ESCURO (alternancia — S4-P02 foi branco). Frase fixa:
"No ar em dias. Nao em meses."
CORRECAO DE BRIEF (confirmado com Fernando): a fonte serifada Playfair NAO
e a preferida — a identidade usa so Space Grotesk + Inter (ver CLAUDE.md,
secao Identidade visual). Enfase em "dias" feita SEM trocar de familia:
escala gigante + peso maximo na propria Space Grotesk, tratamento tipo
"numeral" (como o .stat-big do S2-C08), nao itálico serifado.
Composicao varia dos dois posts anteriores: P01 = coluna empilhada
esquerda; P02 = assimetrico com aspas fantasma; aqui = "dias" centralizado
gigante dominando o quadro, frase de contexto pequena acima e abaixo."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/logo-icon-white.png"

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.30;mix-blend-mode:overlay;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.45'/>
</svg>"""

INK = "#0b0b0b"

CSS = FONTFACE + f"""
:root{{--ink:{INK};--paper:#f5f4f1;--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:100%;height:100%;overflow:hidden;}}
body{{font-family:var(--display);-webkit-font-smoothing:antialiased;}}
.canvas{{position:relative;overflow:hidden;isolation:isolate;background:var(--ink);color:#fff;width:1080px;height:1350px;}}

.ghost{{position:absolute;font-weight:700;letter-spacing:-0.04em;line-height:0.8;z-index:0;color:transparent;
  -webkit-text-stroke:2px rgba(255,255,255,0.07);white-space:nowrap;user-select:none;}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.32;color:#fff;}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:40px;height:40px;}}
.brand .wm{{font-size:28px;font-weight:700;color:#fff;}}

.kicker{{position:absolute;top:230px;left:0;right:0;z-index:10;text-align:center;
  font-size:24px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;opacity:0.5;}}

.lead{{position:absolute;top:320px;left:96px;right:96px;z-index:10;text-align:center;
  font-size:48px;font-weight:600;letter-spacing:-0.01em;opacity:0.85;line-height:1.15;}}

.stage{{position:absolute;top:520px;left:0;right:0;z-index:11;text-align:center;}}
.no-ar{{font-size:52px;font-weight:600;letter-spacing:0.02em;opacity:0.7;display:block;}}
.dias{{display:block;font-weight:700;font-size:340px;line-height:0.82;letter-spacing:-0.045em;color:#fff;margin-top:6px;}}

.notmeses{{position:absolute;top:1000px;left:0;right:0;z-index:10;text-align:center;
  font-size:34px;font-weight:500;opacity:0.5;letter-spacing:0.01em;}}
.notmeses .strike{{text-decoration:line-through;text-decoration-thickness:2.5px;text-decoration-color:rgba(255,255,255,0.6);opacity:0.85;}}

.rule{{position:absolute;left:50%;transform:translateX(-50%);top:1080px;height:3px;width:110px;background:#fff;opacity:0.6;z-index:10;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.42;font-weight:600;letter-spacing:0.06em;color:#fff;}}
.foot-r{{position:absolute;right:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.42;font-weight:600;letter-spacing:0.06em;color:#fff;text-align:right;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
  <span class="ghost" style="font-size:520px;bottom:-110px;right:-60px;">D</span>
  {RM}
  <div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>
  <span class="kicker">Dolen &middot; velocidade real</span>
  <p class="lead">Site n&atilde;o precisa<br/>ser novela.</p>

  <div class="stage">
    <span class="no-ar">No ar em</span>
    <span class="dias">dias.</span>
  </div>

  <p class="notmeses">N&atilde;o em <span class="strike">meses</span>.</p>
  <div class="rule"></div>

  <div class="foot">DOLEN &middot; SITES PROFISSIONAIS</div>
  <div class="foot-r">Chama no direct &rarr;</div>
  {GRAIN}
</div>
</body></html>"""

open(os.path.join(BASE, "s4p03.html"), "w", encoding="utf-8").write(html)
print("html ok")
