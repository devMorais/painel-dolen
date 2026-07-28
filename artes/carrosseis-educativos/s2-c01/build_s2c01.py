# -*- coding: utf-8 -*-
"""[S2-C01] Carrossel "5 erros no site que afastam clientes" — 7 slides, feed 1080x1350.
Fundo ESCURO (regra de intercalacao do feed).

V4 — a foto DISSOLVE no fundo (mask-image), sem borda dura. Composicao VARIA por slide
(foto no topo sangrando, foto lateral, slide so com numeral gigante) — ritmo editorial.
Identidade: Space Grotesk, mono, grao, ghost text, numeral gigante do erro como acento."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FOTOS = os.path.join(BASE, "fotos")
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"


def foto_uri(nome):
    return "file:///" + os.path.join(FOTOS, nome).replace("\\", "/")


GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.5;mix-blend-mode:overlay;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.55'/>
</svg>"""

BG = "#0d0d0d"

CSS = FONTFACE + f"""
:root{{--ink:#0a0a0a;--paper:#ffffff;--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:100%;height:100%;overflow:hidden;}}
body{{font-family:var(--display);-webkit-font-smoothing:antialiased;}}
.canvas{{position:relative;overflow:hidden;isolation:isolate;background:{BG};color:var(--paper);width:1080px;height:1350px;}}

.foto{{position:absolute;z-index:1;overflow:hidden;}}
.foto img{{width:100%;height:100%;object-fit:cover;display:block;}}
.fade-b img{{-webkit-mask-image:linear-gradient(180deg, #000 45%, transparent 100%);}}
.fade-l img{{-webkit-mask-image:linear-gradient(270deg, #000 55%, transparent 100%);}}
.fade-r img{{-webkit-mask-image:linear-gradient(90deg, #000 55%, transparent 100%);}}

.ghost{{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:0;color:transparent;-webkit-text-stroke:2px rgba(255,255,255,0.13);white-space:nowrap;}}
.orbit{{position:absolute;border-radius:50%;border:2px solid rgba(255,255,255,0.13);z-index:0;}}
.orbit::after{{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);background:rgba(255,255,255,0.3);}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.28;color:#fff;}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:40px;height:40px;filter:invert(1) brightness(2);}}
.brand .wm{{font-size:28px;font-weight:700;}}

.block{{position:absolute;z-index:10;}}
.kicker{{font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.55;}}
.mega{{font-weight:700;letter-spacing:-0.03em;line-height:1.0;}}
.support{{font-weight:400;line-height:1.42;opacity:0.78;text-wrap:pretty;}}
.rule{{height:3px;width:110px;background:currentColor;opacity:0.85;}}
.und{{text-decoration:underline;text-underline-offset:0.1em;}}

.swipe{{display:flex;align-items:center;gap:14px;font-size:27px;font-weight:600;opacity:0.9;}}
.arrow{{font-size:36px;}}
.pill{{display:inline-flex;font-size:29px;font-weight:600;padding:19px 40px;border-radius:100px;background:var(--paper);color:var(--ink);}}

.num-erro{{font-size:150px;font-weight:700;letter-spacing:-0.04em;line-height:0.8;opacity:0.95;}}
.num-tag{{font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.55;}}
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.5;font-weight:600;letter-spacing:0.04em;}}
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


def foot(n, total=7):
    return f'<div class="foot">{n:02d} / {total:02d}</div>'


WPP_ICON = '''<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="width:120px;height:120px;opacity:0.85;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'''


# ===== SLIDE 1 — CAPA: foto (setup) no topo sangrando + dissolve pra baixo =====
render("s2c01_1_capa",
    foto("final_laptop.jpg", "fade-b", "top:0;left:0;right:0;height:760px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:180px;">
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="kicker">Dolen · verdade dura</span>
      <h1 class="mega" style="font-size:80px;">5 erros no seu<br/>site que <span class="und">AFASTAM</span><br/>clientes</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:31px;">(e você nem percebe)</p>
    </div>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — ERRO 01 (velocidade): foto topo sangrando, numeral gigante + texto embaixo =====
render("s2c01_2_erro01",
    foto("final_laptop.jpg", "fade-b", "top:0;left:0;right:0;height:620px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <div style="display:flex;align-items:baseline;gap:22px;">
      <span class="num-erro">01</span><span class="num-tag">Erro 01</span>
    </div>
    <h2 class="mega" style="font-size:56px;margin-top:16px;">Demora pra carregar.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:760px;">Cada segundo a mais é gente desistindo antes de ver o que você faz.</p>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — ERRO 02 (celular): foto lateral DIREITA (split), texto ESQUERDA =====
render("s2c01_3_erro02",
    foto("final_celular.jpg", "fade-l", "top:0;right:0;bottom:0;width:640px;") + f"""
  <div class="block" style="left:96px;top:280px;width:540px;">
    <div style="display:flex;align-items:baseline;gap:22px;">
      <span class="num-erro">02</span><span class="num-tag">Erro 02</span>
    </div>
    <h2 class="mega" style="font-size:54px;margin-top:16px;">Não funciona<br/>direito no celular.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;">É onde a maioria dos seus clientes está te vendo agora.</p>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — ERRO 03 (contato): SEM foto — numeral gigante + icone de chat (variacao) =====
render("s2c01_4_erro03", f"""
  <span class="ghost" style="font-size:280px;top:120px;left:-40px;">CONTATO</span>
  <div class="orbit" style="width:240px;height:240px;top:280px;right:150px;display:flex;align-items:center;justify-content:center;">{WPP_ICON}</div>
  <div class="block" style="left:96px;right:96px;bottom:200px;">
    <div style="display:flex;align-items:baseline;gap:22px;">
      <span class="num-erro">03</span><span class="num-tag">Erro 03</span>
    </div>
    <h2 class="mega" style="font-size:56px;margin-top:16px;">Botão de contato<br/>escondido.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:760px;">Se a pessoa precisa PROCURAR como te chamar, ela não chama.</p>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — ERRO 04 (desatualizado): foto lateral ESQUERDA (split espelhado), texto DIREITA =====
render("s2c01_5_erro04",
    foto("final_relogio.jpg", "fade-r", "top:0;left:0;bottom:0;width:640px;") + f"""
  <div class="block" style="right:96px;top:280px;width:540px;text-align:right;">
    <div style="display:flex;align-items:baseline;gap:22px;justify-content:flex-end;">
      <span class="num-tag">Erro 04</span><span class="num-erro">04</span>
    </div>
    <h2 class="mega" style="font-size:56px;margin-top:16px;">Informação<br/>desatualizada.</h2>
    <div class="rule" style="margin-top:20px;margin-left:auto;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;">Preço velho e telefone errado destroem a confiança na hora.</p>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — ERRO 05 (preso ao programador): foto topo (codigo) sangrando =====
render("s2c01_6_erro05",
    foto("final_codigo.jpg", "fade-b", "top:0;left:0;right:0;height:640px;") + f"""
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <div style="display:flex;align-items:baseline;gap:22px;">
      <span class="num-erro">05</span><span class="num-tag">Erro 05</span>
    </div>
    <h2 class="mega" style="font-size:54px;margin-top:16px;">Você não consegue<br/>editar nada sozinho.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:760px;">Site que depende de programador pra tudo trabalha contra você.</p>
  </div>
  {foot(6)}
""")

# ===== SLIDE 7 — CTA: tipografico puro (sem foto), ghost text + orbita =====
render("s2c01_7_cta", f"""
  <span class="ghost" style="font-size:300px;top:150px;left:-50px;">PAINEL</span>
  <div class="orbit" style="width:360px;height:360px;top:120px;right:-110px;"></div>
  <div class="block" style="left:96px;right:96px;top:430px;">
    <h2 class="mega" style="font-size:70px;">Seu site deveria<br/>trabalhar por você.</h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:720px;">Na Dolen, todos os sites possuem um painel simples para você atualizar tudo quando quiser.</p>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <div style="display:flex;flex-direction:column;gap:14px;padding:30px 34px;border:2px solid rgba(255,255,255,0.4);border-radius:20px;">
      <span class="support" style="font-size:29px;opacity:0.95;font-weight:600;">Quer um site profissional e fácil de administrar?</span>
      <span class="pill" style="align-self:flex-start;">Chama no direct</span>
    </div>
  </div>
  {foot(7)}
""")

print("html ok — 7 slides gerados (fade + composicao variada)")
