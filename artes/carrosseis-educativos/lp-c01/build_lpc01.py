# -*- coding: utf-8 -*-
"""[LP-C01] Carrossel "5 sites, 5 nichos, 1 padrão (showcase geral)" — 7 slides, feed 1080x1350.
Fundo BRANCO (regra de intercalacao do feed — ultimo post publicado foi escuro).

Os 5 negocios mostrados (Vitalis Saude, Ferreira & Associados, Loja Bonita, Traco
Arquitetura, Cortex Consultoria) sao exemplos ilustrativos do padrao de site que a Dolen
constroi por nicho — NAO sao clientes reais ja entregues (o portfolio real fica em
artes/_gerador/trabalhos: Miss, ShopX, Avante, Grande Familia, Sudoku). Por isso a copy
evita "sites reais"/"ja entregamos" e cada slide leva o rotulo "Exemplo de aplicacao".

Composicao tipografica pura nos slides de nicho (numero ghost + icone), alternando
alinhamento esquerda/direita a cada slide — reforca o conceito de "1 padrao repetido"
sem repetir literalmente o mesmo layout. Capa e CTA seguem o padrao dos demais
carrosseis da pasta (foto dissolvendo no topo / tipografico puro com ghost+orbit)."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", "..", ".."))
GERADOR = os.path.join(REPO, "artes", "_gerador")
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///" + os.path.join(REPO, "frontend", "public", "assets", "images", "dolen-icone-preto.png").replace("\\", "/")
FOTO_CAPA = "file:///" + os.path.join(BASE, "fotos", "final_hexagono.jpg").replace("\\", "/")
FOTO_ADVOCACIA = "file:///" + os.path.join(BASE, "fotos", "final_advocacia.jpg").replace("\\", "/")
FOTO_MODA = "file:///" + os.path.join(BASE, "fotos", "final_moda.jpg").replace("\\", "/")
FOTO_CONSULTORIA = "file:///" + os.path.join(BASE, "fotos", "final_consultoria.jpg").replace("\\", "/")

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
.fade-b img{{-webkit-mask-image:linear-gradient(180deg, #000 45%, transparent 100%);}}
.fade-l img{{-webkit-mask-image:linear-gradient(270deg, #000 28%, transparent 62%);}}
.fade-r img{{-webkit-mask-image:linear-gradient(90deg, #000 28%, transparent 62%);}}

.ghost{{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:0;color:transparent;-webkit-text-stroke:2px rgba(16,16,16,0.09);white-space:nowrap;}}
.orbit{{position:absolute;border-radius:50%;border:2px solid rgba(16,16,16,0.10);z-index:0;}}
.orbit::after{{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);background:rgba(16,16,16,0.2);}}

.icon-badge{{width:88px;height:88px;border-radius:50%;border:2px solid rgba(16,16,16,0.35);display:flex;align-items:center;justify-content:center;z-index:10;}}
.icon-badge svg{{width:40px;height:40px;stroke:var(--ink);}}

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


def foot(n, total=7):
    return f'<div class="foot">{n:02d} / {total:02d}</div>'


ICON_SAUDE = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/></svg>'''
ICON_ADVOCACIA = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M5 7l-3 6a3 3 0 0 0 6 0l-3-6zm14 0l-3 6a3 3 0 0 0 6 0l-3-6zM5 7h14M8 21h8"/></svg>'''
ICON_MODA = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a2 2 0 0 1 2 2 2 2 0 0 1-4 0 2 2 0 0 1 2-2z"/><path d="M12 5 3 11l2 2 2-1.4V20h10v-8.4L19 13l2-2-9-6z"/></svg>'''
ICON_ARQUITETURA = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="2"/><path d="M12 7 4 20h16L12 7z"/><path d="M8.5 14h7"/></svg>'''
ICON_CONSULTORIA = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="12" rx="2"/><path d="M8 8V6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/></svg>'''


def niche(n, ghost_num, side, num_tag, nome, support, icon, photo=None):
    right = side == "right"
    align = "right" if right else "left"
    ghost_style = f"right:-40px;" if right else "left:-40px;"
    text_side = f"right:96px;" if right else "left:96px;"
    text_width = 560 if photo else 640
    # foto ocupa o lado OPOSTO ao texto, dissolvendo em direcao ao texto
    foto_html = ""
    if photo:
        foto_side = "left" if right else "right"
        fade_cls = "fade-r" if right else "fade-l"
        foto_html = f'<div class="foto {fade_cls}" style="top:0;{foto_side}:0;bottom:0;width:520px;"><img src="{photo}"/></div>'
    return f"""
  {foto_html}
  <span class="ghost" style="font-size:440px;top:330px;{ghost_style}">{ghost_num}</span>
  <div class="block" style="{text_side}top:450px;width:{text_width}px;text-align:{align};">
    <div class="icon-badge" style="{'margin-left:auto;' if right else ''}">{icon}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Exemplo de aplicação</span>
    <div style="height:10px;"></div>
    <span class="num-tag">{num_tag}</span>
    <h2 class="mega" style="font-size:66px;margin-top:16px;">{nome}</h2>
    <div class="rule" style="margin-top:22px;{'margin-left:auto;' if right else ''}"></div>
    <p class="support" style="font-size:31px;margin-top:22px;">{support}</p>
  </div>
  {foot(n)}
"""


# ===== SLIDE 1 — CAPA: foto sangrando no topo + dissolve pra baixo =====
render("lpc01_1_capa", f"""
  <div class="foto fade-b" style="top:0;left:0;right:0;height:760px;"><img src="{FOTO_CAPA}"/></div>
  <div class="block" style="left:96px;right:96px;bottom:180px;">
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="kicker">Dolen · como pensamos um site</span>
      <h1 class="mega" style="font-size:82px;">5 negócios.<br/>O <span class="und">mesmo</span> padrão.</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:31px;">Veja como um único padrão se adapta a nichos bem diferentes</p>
    </div>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — NICHO 01 · Saude (texto esquerda) =====
render("lpc01_2_saude", niche(
    2, "01", "left", "Nicho 01 · Clínica de saúde", "Vitalis Saúde",
    "Especialidades, agenda de consultas e localização — tudo numa página só.",
    ICON_SAUDE
))

# ===== SLIDE 3 — NICHO 02 · Advocacia (foto lateral esquerda + texto direita) =====
render("lpc01_3_advocacia", niche(
    3, "02", "right", "Nicho 02 · Advocacia", "Ferreira &<br/>Associados",
    "Áreas de atuação, credibilidade e contato direto pelo WhatsApp.",
    ICON_ADVOCACIA, photo=FOTO_ADVOCACIA
))

# ===== SLIDE 4 — NICHO 03 · Moda (foto lateral direita + texto esquerda) =====
render("lpc01_4_moda", niche(
    4, "03", "left", "Nicho 03 · Moda", "Loja Bonita",
    "Vitrine de produtos com cara de loja de verdade, pronta pra vender.",
    ICON_MODA, photo=FOTO_MODA
))

# ===== SLIDE 5 — NICHO 04 · Arquitetura (texto direita) =====
render("lpc01_5_arquitetura", niche(
    5, "04", "right", "Nicho 04 · Arquitetura", "Traço<br/>Arquitetura",
    "Portfólio de projetos em destaque, do jeito que um escritório criativo merece.",
    ICON_ARQUITETURA
))

# ===== SLIDE 6 — NICHO 05 · Consultoria (foto sangrando no topo, variacao da capa) =====
render("lpc01_6_consultoria", f"""
  <div class="foto fade-b" style="top:0;left:0;right:0;height:660px;"><img src="{FOTO_CONSULTORIA}"/></div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <div class="icon-badge">{ICON_CONSULTORIA}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Exemplo de aplicação</span>
    <div style="height:10px;"></div>
    <span class="num-tag">Nicho 05 · Consultoria</span>
    <h2 class="mega" style="font-size:66px;margin-top:16px;">Cortex Consultoria</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;max-width:760px;">Autoridade, serviços claros e um formulário que gera lead de verdade.</p>
  </div>
  {foot(6)}
""")

# ===== SLIDE 7 — CTA: tipografico puro, ghost text + orbita =====
render("lpc01_7_cta", f"""
  <span class="ghost" style="font-size:300px;top:150px;left:-50px;">VOCÊ</span>
  <div class="orbit" style="width:360px;height:360px;top:120px;right:-110px;"></div>
  <div class="block" style="left:96px;right:96px;top:440px;">
    <h2 class="mega" style="font-size:70px;">Qual desses<br/><strong>é o seu negócio?</strong></h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:720px;">Link na bio.</p>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="pill">Chama no direct</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">@dolen.ia</span>
  </div>
  {foot(7)}
""")

print("html ok — 7 slides gerados (lp-c01)")
