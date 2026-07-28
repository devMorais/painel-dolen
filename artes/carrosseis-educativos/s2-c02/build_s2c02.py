# -*- coding: utf-8 -*-
"""[S2-C02] Carrossel "Landing, site ou loja? Escolha sem errar" — 6 slides, feed 1080x1350.
Fundo BRANCO (regra de intercalacao do feed — o S2-C01 e' escuro).

V4 — a foto DISSOLVE no fundo (mask-image com gradiente), sem borda dura/arredondada.
Composicao VARIA de slide pra slide (foto no topo sangrando, foto lateral esquerda,
foto lateral direita, fundo com fade forte, slide tipografico puro) — ritmo editorial,
nao um template unico repetido. Identidade mantida: Space Grotesk, mono, grao, ghost text."""
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

/* foto que DISSOLVE no fundo — a mask-image controla o fade em cada direcao */
.foto{{position:absolute;z-index:1;overflow:hidden;}}
.foto img{{width:100%;height:100%;object-fit:cover;display:block;}}
/* variantes de fade via mask (a foto vira transparente na direcao do gradiente) */
.fade-b img{{-webkit-mask-image:linear-gradient(180deg, #000 45%, transparent 100%);}}
.fade-l img{{-webkit-mask-image:linear-gradient(270deg, #000 55%, transparent 100%);}}
.fade-r img{{-webkit-mask-image:linear-gradient(90deg, #000 55%, transparent 100%);}}
/* dissolve a foto no canto superior direito, deixando o terco inferior-esquerdo limpo */
.fade-corner img{{-webkit-mask-image:radial-gradient(130% 105% at 78% 18%, #000 42%, transparent 82%);}}

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
.pill{{display:inline-flex;font-size:29px;font-weight:600;padding:19px 40px;border-radius:100px;background:var(--ink);color:var(--paper);}}
.num-tag{{font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.5;}}
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.4;font-weight:600;letter-spacing:0.04em;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'


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


# ===== SLIDE 1 — CAPA: foto grande no topo sangrando + dissolve pra baixo =====
render("s2c02_1_capa",
    foto("final_laptop_capa.jpg", "fade-b", "top:0;left:0;right:0;height:760px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:180px;">
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="kicker">Dolen · guia rápido</span>
      <h1 class="mega" style="font-size:82px;">Landing page,<br/>site ou <span class="und">loja</span> virtual?</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:31px;">Descubra qual é o SEU caso</p>
    </div>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — OPCAO 01 (landing/alvo): foto lateral DIREITA dissolvendo, texto ESQUERDA =====
render("s2c02_2_opcao1",
    foto("final_alvo.jpg", "fade-l", "top:0;right:0;bottom:0;width:620px;") + f"""
  <div class="block" style="left:96px;top:300px;width:560px;">
    <span class="num-tag">Opção 01</span>
    <div style="height:20px;"></div>
    <span class="kicker" style="opacity:0.65;">Landing page</span>
    <h2 class="mega" style="font-size:62px;margin-top:18px;">Uma página,<br/>um objetivo:<br/>converter.</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;">Ideal pra divulgar um serviço específico, uma campanha ou um lançamento.</p>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — OPCAO 02 (site/predio): foto alta no topo dissolvendo pra baixo =====
# (variacao de altura: bloco de foto mais ALTO que a capa, texto compacto embaixo)
render("s2c02_3_opcao2",
    foto("final_predio.jpg", "fade-b", "top:0;left:0;right:0;height:840px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="num-tag">Opção 02 · Site institucional</span>
    <h2 class="mega" style="font-size:64px;margin-top:20px;">A casa completa<br/>do seu negócio.</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;max-width:760px;">Quem você é, o que faz, portfólio e contato. Ideal pra construir autoridade e confiança.</p>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — OPCAO 03 (loja/caixas): foto lateral ESQUERDA (espelha o slide 2) =====
render("s2c02_4_opcao3",
    foto("final_caixa.jpg", "fade-r", "top:0;left:0;bottom:0;width:620px;") + f"""
  <div class="block" style="right:96px;top:300px;width:560px;text-align:right;">
    <span class="num-tag">Opção 03</span>
    <div style="height:20px;"></div>
    <span class="kicker" style="opacity:0.65;">Loja virtual</span>
    <h2 class="mega" style="font-size:62px;margin-top:18px;">Pra vender<br/>online<br/>de verdade.</h2>
    <div class="rule" style="margin-top:22px;margin-left:auto;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;">Catálogo, carrinho e pagamento. Sua loja aberta 24 horas.</p>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — COMO ESCOLHER (sinalizacao): foto topo sangrando (variacao da capa) =====
render("s2c02_5_comoescolher",
    foto("final_decisao.jpg", "fade-b", "top:0;left:0;right:0;height:700px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="num-tag">Como escolher</span>
    <h2 class="mega" style="font-size:62px;margin-top:18px;">Comece pelo que<br/>o seu momento pede.</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;max-width:740px;">E o melhor: dá pra começar simples e crescer sem jogar nada fora.</p>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — CTA: tipografico puro (sem foto), ghost text + orbita =====
render("s2c02_6_cta", f"""
  <span class="ghost" style="font-size:300px;top:150px;left:-50px;">DOLEN</span>
  <div class="orbit" style="width:360px;height:360px;top:120px;right:-110px;"></div>
  <div class="block" style="left:96px;right:96px;top:440px;">
    <h2 class="mega" style="font-size:74px;">Na dúvida,<br/>chama a gente.</h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:720px;">Te ajudamos a escolher o formato certo, sem compromisso.</p>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="pill">Chama no direct</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">ou link na bio</span>
  </div>
  {foot(6)}
""")

print("html ok — 6 slides gerados (fade + composicao variada)")
