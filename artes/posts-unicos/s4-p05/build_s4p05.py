# -*- coding: utf-8 -*-
"""[S4-P05] Post unico "manifesto" — feed 1080x1350.
Fundo ESCURO (alternancia — S4-P04 foi branco). Frase fixa:
"O Instagram e aluguel. O site e o imovel proprio do seu negocio."
CORRECAO DE BRIEF (mesma de S4-P03): identidade usa so Space Grotesk + Inter,
sem serifa (Playfair NAO e a fonte da marca — confirmado por Fernando).
Enfase em "imovel proprio" feita com escala/peso na propria Space Grotesk,
nao italico serifado.
Dispositivo: metafora aluguel x imovel proprio — "aluguel" tratado pequeno/
riscado/apagado (like a fine-print/expiring lease), "imovel proprio" gigante
e solido embaixo, como um contrato/placa "vendido". Varia da familia:
P01 coluna, P02 assimetrico+aspas, P03 centralizado gigante, P04 cards 2col;
aqui = bloco de "contrato" com timbre/placa, textura de carimbo."""
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

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.32;color:#fff;}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:40px;height:40px;}}
.brand .wm{{font-size:28px;font-weight:700;color:#fff;}}

.kicker{{position:absolute;top:170px;left:96px;z-index:10;font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.5;}}

/* bloco 1: o aluguel — pequeno, riscado, "vencendo" */
.lease{{position:absolute;top:220px;left:96px;right:96px;z-index:10;}}
.lease-row{{display:flex;align-items:baseline;gap:18px;}}
.lease-label{{font-size:22px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;opacity:0.4;border:1.5px solid rgba(255,255,255,0.3);border-radius:100px;padding:7px 16px;}}
.lease-txt{{font-size:44px;font-weight:600;letter-spacing:-0.01em;opacity:0.55;
  text-decoration:line-through;text-decoration-thickness:3px;text-decoration-color:rgba(255,255,255,0.45);}}
.lease-sub{{font-size:26px;font-weight:500;opacity:0.42;margin-top:14px;max-width:640px;line-height:1.4;}}

/* divisor */
.vs{{position:absolute;top:490px;left:96px;right:96px;z-index:10;display:flex;align-items:center;gap:20px;}}
.vs .ln{{flex:1;height:1.5px;background:rgba(255,255,255,0.18);}}
.vs .tx{{font-size:22px;font-weight:600;letter-spacing:0.15em;opacity:0.4;text-transform:uppercase;}}

/* bloco 2: o imovel proprio — gigante, solido, "placa vendido" */
.deed{{position:absolute;top:560px;left:96px;right:96px;z-index:11;}}
.deed-label{{display:inline-flex;align-items:center;gap:10px;font-size:22px;font-weight:700;letter-spacing:0.1em;
  text-transform:uppercase;background:#fff;color:var(--ink);border-radius:100px;padding:9px 20px 9px 16px;margin-bottom:26px;}}
.deed-label .dot{{width:9px;height:9px;border-radius:50%;background:#22c55e;}}
.deed-title{{font-weight:700;letter-spacing:-0.04em;line-height:0.94;font-size:104px;color:#fff;}}
.deed-sub{{font-size:32px;font-weight:500;opacity:0.72;margin-top:26px;line-height:1.4;max-width:760px;}}

.rule{{position:absolute;left:96px;top:1128px;height:3px;width:110px;background:#fff;opacity:0.5;z-index:10;}}
.exact{{position:absolute;left:96px;right:96px;top:1168px;z-index:10;font-size:22px;font-weight:500;opacity:0.4;line-height:1.45;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.42;font-weight:600;letter-spacing:0.06em;color:#fff;}}
.foot-r{{position:absolute;right:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.42;font-weight:600;letter-spacing:0.06em;color:#fff;text-align:right;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
  {RM}
  <div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>
  <span class="kicker">Dolen &middot; patrim&ocirc;nio digital</span>

  <div class="lease">
    <div class="lease-row">
      <span class="lease-label">Instagram</span>
      <span class="lease-txt">&eacute; aluguel.</span>
    </div>
    <p class="lease-sub">Voc&ecirc; paga com posts, algoritmo e alcance &mdash; e o im&oacute;vel nunca &eacute; seu.</p>
  </div>

  <div class="vs"><span class="ln"></span><span class="tx">enquanto isso</span><span class="ln"></span></div>

  <div class="deed">
    <span class="deed-label"><span class="dot"></span>O site &eacute;</span>
    <div class="deed-title">im&oacute;vel<br/>pr&oacute;prio.</div>
    <p class="deed-sub">Do seu neg&oacute;cio, no seu nome, sem pedir licen&ccedil;a pra ningu&eacute;m.</p>
  </div>

  <div class="rule"></div>
  <p class="exact">O Instagram &eacute; aluguel. O site &eacute; o im&oacute;vel pr&oacute;prio do seu neg&oacute;cio.</p>

  <div class="foot">DOLEN &middot; SITES PROFISSIONAIS</div>
  <div class="foot-r">Voc&ecirc; j&aacute; tem o seu? &rarr;</div>
  {GRAIN}
</div>
</body></html>"""

open(os.path.join(BASE, "s4p05.html"), "w", encoding="utf-8").write(html)
print("html ok")
