# -*- coding: utf-8 -*-
"""[S4-P04] Post unico "manifesto" — feed 1080x1350.
Fundo BRANCO (alternancia — S4-P03 foi escuro). Frase fixa:
"Site COM painel: voce edita tudo sozinho. Site SEM painel: refem de programador."
Sem serifa aqui (brief pede layout comparativo, nao tipografia de enfase).
Duas colunas: ESQUERDA = "COM painel" bloco solido preto + check (o lado certo);
DIREITA = "SEM painel" cinza riscado + X (o lado errado). Varia da familia:
P01 coluna unica esquerda, P02 assimetrico c/ aspas, P03 centralizado gigante;
aqui = grid de comparacao 2 colunas, dispositivo novo (cards, nao bloco de texto)."""
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
GREY = "#d9d7d2"

CSS = FONTFACE + f"""
:root{{--ink:{INK};--paper:{PAPER};--grey:{GREY};--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}}
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

.kicker{{position:absolute;top:150px;left:96px;z-index:10;font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.45;}}
.headline{{position:absolute;top:192px;left:96px;right:96px;z-index:10;font-weight:700;letter-spacing:-0.03em;line-height:1.05;font-size:52px;}}

.grid{{position:absolute;top:360px;left:96px;right:96px;height:600px;z-index:10;display:flex;gap:22px;}}
.card{{flex:1;border-radius:26px;padding:40px 34px;display:flex;flex-direction:column;}}
.card.win{{background:var(--ink);color:var(--paper);}}
.card.lose{{background:var(--grey);color:var(--ink);}}

.mark{{width:64px;height:64px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;margin-bottom:28px;}}
.card.win .mark{{background:var(--paper);}}
.card.lose .mark{{background:rgba(15,15,15,0.12);}}
.mark svg{{width:30px;height:30px;}}

.tag{{font-size:21px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;opacity:0.6;margin-bottom:10px;}}
.card.lose .tag{{opacity:0.5;}}
.title{{font-size:38px;font-weight:700;letter-spacing:-0.02em;line-height:1.08;margin-bottom:24px;}}
.card.lose .title{{text-decoration:line-through;text-decoration-thickness:3px;text-decoration-color:rgba(15,15,15,0.4);opacity:0.75;}}
.desc{{font-size:26px;font-weight:500;line-height:1.38;opacity:0.82;margin-top:auto;}}
.card.lose .desc{{opacity:0.62;}}

.verdict{{position:absolute;left:96px;right:96px;top:1010px;z-index:10;}}
.rule{{height:3px;width:110px;background:var(--ink);opacity:0.7;margin-bottom:24px;}}
.exact{{font-size:29px;font-weight:600;line-height:1.42;letter-spacing:-0.005em;opacity:0.88;}}
.exact b{{font-weight:700;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.4;font-weight:600;letter-spacing:0.06em;}}
.foot-r{{position:absolute;right:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.4;font-weight:600;letter-spacing:0.06em;text-align:right;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="#0f0f0f" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
XMARK = '<svg viewBox="0 0 24 24" fill="none" stroke="#0f0f0f" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="M6 6l12 12"/></svg>'

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
  {RM}
  <div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>
  <span class="kicker">Dolen &middot; de que lado voc&ecirc; est&aacute;?</span>
  <h1 class="headline">Todo site da Dolen<br/>j&aacute; nasce do lado certo.</h1>

  <div class="grid">
    <div class="card win">
      <span class="mark">{CHECK}</span>
      <span class="tag">Com painel</span>
      <div class="title">Voc&ecirc; edita<br/>tudo sozinho.</div>
      <p class="desc">Texto, pre&ccedil;o, imagem &mdash; sem depender de ningu&eacute;m.</p>
    </div>
    <div class="card lose">
      <span class="mark">{XMARK}</span>
      <span class="tag">Sem painel</span>
      <div class="title">Ref&eacute;m de<br/>programador.</div>
      <p class="desc">Qualquer troca vira e-mail, prazo e fatura.</p>
    </div>
  </div>

  <div class="verdict">
    <div class="rule"></div>
    <p class="exact">Site <b>COM</b> painel: voc&ecirc; edita tudo sozinho.<br/>Site <b>SEM</b> painel: ref&eacute;m de programador.</p>
  </div>

  <div class="foot">DOLEN &middot; SITES PROFISSIONAIS</div>
  <div class="foot-r">Chama no direct &rarr;</div>
  {GRAIN}
</div>
</body></html>"""

open(os.path.join(BASE, "s4p04.html"), "w", encoding="utf-8").write(html)
print("html ok")
