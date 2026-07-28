# -*- coding: utf-8 -*-
"""[S2-C04] Carrossel "Quanto custa um site profissional?" — 7 slides, feed 1080x1350.
Fundo BRANCO (regra de intercalacao — o S2-C03 foi escuro).

VALORES CHEIOS (sem desconto de fundador — este post e' pos-3-primeiros-clientes):
Landing R$105/mes, Premium R$210/mes, Loja Pro R$340/mes.

Variacao propria (nao repetir o layout do S2-C03): o PRECO e' o numeral gigante.
Foto lateral dissolvendo nos planos, slides tipograficos no incluso/fundador/CTA.
Space Grotesk, mono, grao, fade sem borda dura."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FOTOS = os.path.join(BASE, "fotos")
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"


def foto_uri(nome):
    return "file:///" + os.path.join(FOTOS, nome).replace("\\", "/")


GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.35;mix-blend-mode:multiply;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.4'/>
</svg>"""

PAPER = "#f5f4f1"

CSS = FONTFACE + f"""
:root{{--ink:#101010;--paper:{PAPER};--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:100%;height:100%;overflow:hidden;}}
body{{font-family:var(--display);-webkit-font-smoothing:antialiased;}}
.canvas{{position:relative;overflow:hidden;isolation:isolate;background:var(--paper);color:var(--ink);width:1080px;height:1350px;}}

.foto{{position:absolute;z-index:1;overflow:hidden;}}
.foto img{{width:100%;height:100%;object-fit:cover;display:block;}}
.fade-l img{{-webkit-mask-image:linear-gradient(270deg, #000 55%, transparent 100%);}}
.fade-r img{{-webkit-mask-image:linear-gradient(90deg, #000 55%, transparent 100%);}}
.fade-b img{{-webkit-mask-image:linear-gradient(180deg, #000 45%, transparent 100%);}}

.ghost{{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:0;color:transparent;-webkit-text-stroke:2px rgba(16,16,16,0.09);white-space:nowrap;}}
.orbit{{position:absolute;border-radius:50%;border:2px solid rgba(16,16,16,0.10);z-index:0;}}
.orbit::after{{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);background:rgba(16,16,16,0.2);}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.28;color:#101010;}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:40px;height:40px;}}
.brand .wm{{font-size:28px;font-weight:700;}}

.block{{position:absolute;z-index:10;}}
.kicker{{font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.5;}}
.mega{{font-weight:700;letter-spacing:-0.03em;line-height:1.0;}}
.support{{font-weight:400;line-height:1.42;opacity:0.72;text-wrap:pretty;}}
.rule{{height:3px;width:110px;background:currentColor;opacity:0.85;}}
.und{{text-decoration:underline;text-underline-offset:0.1em;}}

.swipe{{display:flex;align-items:center;gap:14px;font-size:27px;font-weight:600;opacity:0.9;}}
.arrow{{font-size:36px;}}
.pill{{display:inline-flex;align-items:center;gap:14px;font-size:29px;font-weight:600;padding:20px 42px;border-radius:100px;background:var(--ink);color:var(--paper);}}
.pill svg{{width:28px;height:28px;}}
.tag-top{{display:inline-flex;font-size:22px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;padding:9px 20px;border-radius:100px;background:var(--ink);color:var(--paper);}}

/* preco: numeral gigante */
.preco{{display:flex;align-items:baseline;gap:6px;}}
.preco .cifra{{font-size:56px;font-weight:700;opacity:0.7;}}
.preco .valor{{font-size:170px;font-weight:700;letter-spacing:-0.04em;line-height:0.8;}}
.preco .mes{{font-size:44px;font-weight:600;opacity:0.55;}}
.parcelas{{font-size:28px;opacity:0.6;font-weight:500;margin-top:8px;}}

.check-item{{display:flex;align-items:flex-start;gap:20px;padding:20px 0;border-bottom:1.5px solid rgba(16,16,16,0.12);}}
.check-item:last-child{{border-bottom:none;}}
.check-item svg{{width:32px;height:32px;flex:none;margin-top:2px;}}
.check-item span{{font-size:32px;font-weight:600;}}

.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.4;font-weight:600;letter-spacing:0.04em;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

IC_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
IC_CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>'


def render(name, inner):
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas">
{RM}
<div class="brand"><img src="{LOGO}"/><span class="wm">dolen</span></div>
{inner}
{GRAIN}
</div>
</body></html>"""
    open(os.path.join(BASE, name + ".html"), "w", encoding="utf-8").write(html)


def foto(nome, cls, style):
    return f'<div class="foto {cls}" style="{style}"><img src="{foto_uri(nome)}"/></div>'


def foot(n, total=6):
    return f'<div class="foot">{n:02d} / {total:02d}</div>'


def preco(valor):
    return f'<div class="preco"><span class="cifra">R$</span><span class="valor">{valor}</span><span class="mes">/mês</span></div>'


# ===== SLIDE 1 — CAPA: pergunta forte, tipografico + foto laptop lateral dissolvendo =====
render("s2c04_1_capa",
    foto("final_laptop.jpg", "fade-b", "top:0;left:0;right:0;height:660px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:170px;">
    <span class="kicker">Dolen · transparência total</span>
    <h1 class="mega" style="font-size:78px;margin-top:22px;">Quanto custa um<br/>site <span class="und">profissional?</span></h1>
    <div class="rule" style="margin-top:26px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;">Sem enrolação. Vem ver.</p>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — LANDING PAGE (foto topo, preco gigante embaixo) =====
render("s2c04_2_landing",
    foto("final_alvo.jpg", "fade-b", "top:0;left:0;right:0;height:600px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="kicker" style="opacity:0.65;">Landing page</span>
    <div style="margin-top:10px;">{preco("105")}</div>
    <div class="parcelas">12x no cartão · 1º ano</div>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;max-width:760px;">Uma página de alta conversão pro seu serviço ou campanha.</p>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — PREMIUM (VARIACAO: split lateral com badge, pra destacar o "mais escolhido") =====
render("s2c04_3_premium",
    foto("final_predio.jpg", "fade-l", "top:0;right:0;bottom:0;width:560px;") + f"""
  <div class="block" style="left:96px;top:300px;width:580px;">
    <span class="tag-top">Mais escolhido</span>
    <div style="height:20px;"></div>
    <span class="kicker" style="opacity:0.65;">Site institucional · Premium</span>
    <div style="margin-top:10px;">{preco("210")}</div>
    <div class="parcelas">12x no cartão · 1º ano</div>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:30px;margin-top:22px;">Site completo COM painel próprio pra você editar tudo sozinho.</p>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — LOJA VIRTUAL PRO (foto topo, preco gigante embaixo) =====
render("s2c04_4_loja",
    foto("final_caixa.jpg", "fade-b", "top:0;left:0;right:0;height:600px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="kicker" style="opacity:0.65;">Loja virtual · Pro</span>
    <div style="margin-top:10px;">{preco("340")}</div>
    <div class="parcelas">12x no cartão · 1º ano</div>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;max-width:760px;">Tudo do Premium + carrinho, pagamento e frete.</p>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — O QUE ESTA INCLUSO (lista com checks, tipografico) =====
render("s2c04_5_incluso", f"""
  <span class="ghost" style="font-size:250px;bottom:110px;right:-50px;">TUDO</span>
  <div class="block" style="left:96px;top:210px;">
    <span class="kicker">O que está incluso</span>
    <h2 class="mega" style="font-size:60px;margin-top:18px;">Sem surpresa,<br/>sem letra miúda.</h2>
  </div>
  <div class="block" style="left:96px;right:96px;top:450px;">
    <div class="check-item">{IC_CHECK}<span>Hospedagem e domínio grátis no 1º ano</span></div>
    <div class="check-item">{IC_CHECK}<span>Painel próprio pra editar sozinho</span></div>
    <div class="check-item">{IC_CHECK}<span>Suporte da gente, de verdade</span></div>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — CTA =====
render("s2c04_6_cta", f"""
  <span class="ghost" style="font-size:280px;bottom:190px;right:-60px;">ORÇA</span>
  <div class="orbit" style="width:340px;height:340px;top:140px;left:-90px;"></div>
  <div class="block" style="left:96px;right:96px;top:380px;">
    <h2 class="mega" style="font-size:64px;">Quer o valor<br/>exato pro<br/>SEU caso?</h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:720px;">Resposta rápida, sem compromisso.</p>
  </div>
  <div class="block" style="left:96px;bottom:200px;">
    <span class="pill">{IC_CHAT}Peça o orçamento</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">link na bio ou direct</span>
  </div>
  {foot(6)}
""")

print("html ok — 6 slides gerados")
