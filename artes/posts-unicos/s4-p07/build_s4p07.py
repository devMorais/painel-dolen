# -*- coding: utf-8 -*-
"""[S4-P07] Post unico "manifesto" — feed 1080x1350.
Fundo ESCURO (alternancia — S4-P06 foi branco). Frase fixa:
"Antes de anunciar, arruma a base."
CORRECAO DE BRIEF (mesma de S4-P03/P05): sem serifa, so Space Grotesk.
Enfase em "base" via escala/peso gigante na propria fonte.
Dispositivo: sequencia numerada INVERTIDA — mostra o erro comum (anunciar
primeiro, PASSO 1 errado, riscado/apagado) sendo corrigido pela ordem certa
(arruma a base primeiro, PASSO 1 de verdade, solido). Literaliza a legenda
"Nessa ordem." Varia da familia: P01 coluna, P02 assimetrico+aspas,
P03 centralizado gigante, P04 cards 2col lado a lado, P05 lease/deed,
P06 poster tipografico puro; aqui = sequencia vertical numerada (novo eixo:
vertical em vez de horizontal, e o primeiro a usar numeracao)."""
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

.seq{{position:absolute;top:224px;left:96px;right:96px;z-index:10;}}
.step{{display:flex;align-items:flex-start;gap:26px;padding:24px 0;border-bottom:1.5px solid rgba(255,255,255,0.12);}}
.step:last-child{{border-bottom:none;}}
.num{{font-size:19px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;flex:none;width:110px;padding-top:10px;}}

.step.wrong .num{{opacity:0.32;}}
.step.wrong .txt{{font-size:40px;font-weight:700;letter-spacing:-0.02em;opacity:0.32;
  text-decoration:line-through;text-decoration-thickness:3px;text-decoration-color:rgba(255,255,255,0.4);}}
.step.wrong .tag{{display:block;font-size:19px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;opacity:0.28;margin-top:8px;}}

.step.right .num{{opacity:0.95;}}
.step.right .txt{{font-size:40px;font-weight:700;letter-spacing:-0.02em;line-height:1.15;}}
.step.right .tag{{display:block;font-size:19px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;opacity:0.55;margin-top:8px;}}

.punch{{position:absolute;left:96px;right:70px;top:660px;z-index:11;}}
.base{{display:block;font-weight:700;font-size:210px;line-height:0.86;letter-spacing:-0.045em;color:#fff;margin-top:4px;}}

.sub{{position:absolute;left:96px;right:120px;top:1080px;z-index:10;font-size:27px;font-weight:500;opacity:0.55;line-height:1.45;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.42;font-weight:600;letter-spacing:0.06em;color:#fff;}}
.foot-r{{position:absolute;right:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.42;font-weight:600;letter-spacing:0.06em;color:#fff;text-align:right;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
  {RM}
  <div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>
  <span class="kicker">Dolen &middot; a ordem certa</span>

  <div class="seq">
    <div class="step wrong">
      <span class="num">errado</span>
      <div><span class="txt">Anunciar primeiro</span><span class="tag">o erro mais comum</span></div>
    </div>
    <div class="step right">
      <span class="num">certo</span>
      <div><span class="txt">Antes de anunciar,<br/>arruma a</span><span class="tag">o passo que falta</span></div>
    </div>
  </div>

  <div class="punch">
    <span class="base">base.</span>
  </div>

  <p class="sub">An&uacute;ncio traz gente. O site transforma<br/>gente em cliente. Nessa ordem.</p>

  <div class="foot">DOLEN &middot; SITES PROFISSIONAIS</div>
  <div class="foot-r">Chama no direct &rarr;</div>
  {GRAIN}
</div>
</body></html>"""

open(os.path.join(BASE, "s4p07.html"), "w", encoding="utf-8").write(html)
print("html ok")
