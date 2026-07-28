# -*- coding: utf-8 -*-
"""[S4-P08] Post unico "manifesto" — feed 1080x1350. FECHA A SPRINT 4.
Fundo BRANCO (alternancia — S4-P07 foi escuro).
ATUALIZADO: Fernando pediu pra trocar pra "resta 1 vaga somente" (contagem
mudou desde a primeira versao — 2 das 3 vagas de fundador ja foram
preenchidas). Frase da arte agora: "1 vaga com condicao de fundador.
Depois, o preco volta ao normal." Slots 1 e 2 aparecem riscados/ocupados
(preto solido + X), slot 3 aberto (destacado) — reforca visualmente que
so resta uma.
CORRECAO DE BRIEF (mesma de P03/P05/P07): sem serifa, so Space Grotesk.
Enfase em "fundador" via escala/peso; brief tambem pede banda PRETA com
"3 vagas" como elemento separado — isso vira um badge/etiqueta no topo,
tratamento novo pra familia (nenhum post anterior usou selo/badge).
Este e o post de OFERTA que fecha a sprint (mais comercial/direto que os
7 anteriores, que eram manifestos de marca) — precisa comunicar urgencia
e escassez sem parecer desesperado. 3 caixas de vaga (estilo "senha de
estacionamento"/ticket) reforcam visualmente o numero literal 3.
IMPORTANTE: o numero de vagas restantes muda (legenda tem placeholder [X]
pra Fernando atualizar antes de postar) — a ARTE fixa o numero por
extenso (nao ha contador dinamico); se a contagem mudar de novo, regerar
este script com o novo valor.
Varia da familia: primeiro a usar badge/etiqueta + blocos de "vaga",
mais proximo de um layout comercial (oferta) que os manifestos anteriores."""
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

/* selo / banda preta */
.badge{{position:absolute;top:168px;left:96px;z-index:10;display:inline-flex;align-items:center;gap:14px;
  background:var(--ink);color:var(--paper);border-radius:100px;padding:16px 28px 16px 20px;}}
.badge .dot{{width:10px;height:10px;border-radius:50%;background:#ef4444;flex:none;}}
.badge .tx{{font-size:24px;font-weight:700;letter-spacing:0.02em;}}
.badge .tx b{{font-weight:700;}}

/* 3 blocos de vaga estilo ticket — 2 preenchidas/riscadas (ocupadas), 1 aberta (a que resta) */
.slots{{position:absolute;top:250px;left:96px;right:96px;height:200px;z-index:10;display:flex;gap:16px;}}
.slot{{flex:1;border:2.5px solid var(--ink);border-radius:20px;display:flex;align-items:center;justify-content:center;
  font-size:56px;font-weight:700;letter-spacing:-0.02em;position:relative;}}
.slot::after{{content:"";position:absolute;inset:8px;border:1.5px dashed rgba(15,15,15,0.25);border-radius:12px;}}
.slot.taken{{background:var(--ink);color:rgba(245,244,241,0.35);}}
.slot.taken::after{{border-color:rgba(245,244,241,0.18);}}
.slot.taken .x{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;}}
.slot.taken .x svg{{width:38%;height:38%;}}
.slot.open{{background:var(--paper);box-shadow:0 0 0 4px var(--ink);}}

.headline{{position:absolute;top:498px;left:96px;right:96px;z-index:10;}}
.h1{{font-weight:700;letter-spacing:-0.03em;line-height:1.04;font-size:58px;}}

.punch{{position:absolute;left:96px;right:70px;top:700px;z-index:11;}}
.condicao{{font-size:34px;font-weight:600;opacity:0.7;display:block;}}
.fundador{{display:block;font-weight:700;font-size:150px;line-height:0.86;letter-spacing:-0.04em;color:var(--ink);margin-top:4px;}}

.depois{{position:absolute;left:96px;right:96px;top:970px;z-index:10;font-size:30px;font-weight:500;opacity:0.62;line-height:1.4;}}

.terms{{position:absolute;left:96px;right:96px;top:1082px;z-index:10;display:flex;align-items:center;gap:16px;
  font-size:21px;font-weight:600;opacity:0.4;letter-spacing:0.02em;}}
.terms .sep{{opacity:0.5;}}

.exact{{position:absolute;left:96px;right:96px;top:1128px;z-index:10;font-size:19px;font-weight:500;opacity:0.32;line-height:1.4;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.4;font-weight:600;letter-spacing:0.06em;}}
.foot-r{{position:absolute;right:96px;bottom:70px;z-index:10;font-size:22px;opacity:0.4;font-weight:600;letter-spacing:0.06em;text-align:right;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

XMARK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="M6 6l12 12"/></svg>'

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
  {RM}
  <div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>

  <div class="badge"><span class="dot"></span><span class="tx">RESTA <b>1 VAGA</b></span></div>

  <div class="slots">
    <div class="slot taken"><span class="x">{XMARK}</span></div>
    <div class="slot taken"><span class="x">{XMARK}</span></div>
    <div class="slot open">3</div>
  </div>

  <div class="headline">
    <h1 class="h1">Restou 1 cliente<br/>com condi&ccedil;&atilde;o de</h1>
  </div>

  <div class="punch">
    <span class="fundador">fundador.</span>
  </div>

  <p class="depois">Depois, o pre&ccedil;o volta ao normal &mdash;<br/>sem exce&ccedil;&atilde;o.</p>

  <div class="terms">
    <span>20% OFF</span><span class="sep">&middot;</span><span>1&ordm; ANO</span><span class="sep">&middot;</span><span>EM TROCA DE DEPOIMENTO</span>
  </div>
  <p class="exact">1 vaga com condi&ccedil;&atilde;o de fundador. Depois, o pre&ccedil;o volta ao normal.</p>

  <div class="foot">DOLEN &middot; SITES PROFISSIONAIS</div>
  <div class="foot-r">Direct ou link na bio &rarr;</div>
  {GRAIN}
</div>
</body></html>"""

open(os.path.join(BASE, "s4p08.html"), "w", encoding="utf-8").write(html)
print("html ok")
