# -*- coding: utf-8 -*-
"""[LP-C05] Carrossel "Arquitetos e engenheiros também vendem pela primeira impressão"
— 5 slides, feed 1080x1350. Fundo CLARO (regra de intercalacao — o LP-C04 foi escuro).

O slide 2 mostra um MOCKUP do hero do site "Traço Arquitetura" (traco_mock.html) — Traço
Arquitetura e um exemplo ilustrativo criado no LP-C01, NAO um cliente real, entao a barra
de URL do mockup diz "Exemplo · Traço Arquitetura" e a copy evita "exemplo real"
(a legenda original pedia isso, ajustada pra "veja como ficaria")."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", "..", ".."))
GERADOR = os.path.join(REPO, "artes", "_gerador")
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///" + os.path.join(REPO, "frontend", "public", "assets", "images", "dolen-icone-preto.png").replace("\\", "/")
FOTO_PREDIO = "file:///" + os.path.join(BASE, "fotos", "final_predio.jpg").replace("\\", "/")
MOCK_SHOT = "file:///" + os.path.join(BASE, "traco_mock.png").replace("\\", "/")

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
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.4;font-weight:600;letter-spacing:0.04em;}}

.browser{{position:absolute;z-index:8;border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 50px 110px rgba(0,0,0,0.28), 0 0 0 1px rgba(0,0,0,0.05);}}
.browser .bar{{height:56px;display:flex;align-items:center;gap:16px;padding:0 24px;background:#ececea;border-bottom:1px solid rgba(0,0,0,0.06);}}
.browser .dots{{display:flex;gap:9px;flex:none;}}
.browser .dots i{{width:12px;height:12px;border-radius:50%;background:#c6c6c2;}}
.browser .url{{flex:1;height:32px;border-radius:100px;background:#fff;display:flex;align-items:center;gap:10px;padding:0 18px;font-size:18px;color:#5a5a5a;font-weight:500;}}
.browser .shot{{display:block;width:100%;}}
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


def foot(n, total=5):
    return f'<div class="foot">{n:02d} / {total:02d}</div>'


ICON_PASSOS = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h4M4 12h4M4 18h4"/><path d="M12 6h8M12 12h8M12 18h8"/></svg>'''
ICON_FORM = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>'''

# ===== SLIDE 1 — CAPA: foto sangrando no topo + dissolve pra baixo =====
render("lpc05_1_capa", f"""
  <div class="foto fade-b" style="top:0;left:0;right:0;height:800px;"><img src="{FOTO_PREDIO}"/></div>
  <div class="block" style="left:96px;right:96px;bottom:180px;">
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="kicker">Dolen · primeira impressão</span>
      <h1 class="mega" style="font-size:66px;">Projeto incrível,<br/>site sem cara de<br/><span class="und">profissional</span>?</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:31px;">(o cliente sente essa diferença)</p>
    </div>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — mockup do hero do Traco Arquitetura, em janela de navegador =====
render("lpc05_2_mockup", f"""
  <span class="ghost" style="font-size:220px;top:110px;left:-40px;">EXEMPLO</span>
  <div class="browser" style="left:60px;width:960px;top:250px;">
    <div class="bar"><span class="dots"><i></i><i></i><i></i></span><span class="url">Exemplo · Traço Arquitetura</span></div>
    <div style="height:560px;overflow:hidden;"><img class="shot" src="{MOCK_SHOT}"/></div>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="kicker">Assim ficaria o seu portfólio</span>
    <h2 class="mega" style="font-size:52px;margin-top:14px;">Um exemplo de como<br/>a Dolen pensaria.</h2>
    <div class="rule" style="margin-top:18px;"></div>
    <p class="support" style="font-size:29px;margin-top:18px;max-width:760px;">Mockup ilustrativo — não é um cliente real, é o padrão que aplicaríamos no seu.</p>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — processo: tipografico puro =====
render("lpc05_3_processo", f"""
  <span class="ghost" style="font-size:260px;bottom:220px;right:-50px;">CONFIANÇA</span>
  <div class="block" style="left:96px;right:96px;top:420px;">
    <div class="icon-badge">{ICON_PASSOS}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Como trabalhamos</span>
    <h2 class="mega" style="font-size:58px;margin-top:16px;">Um processo claro<br/>gera confiança antes<br/>da primeira reunião.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:740px;">O cliente já entende as etapas do projeto antes mesmo de chamar no WhatsApp.</p>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — formulario: tipografico puro =====
render("lpc05_4_formulario", f"""
  <span class="ghost" style="font-size:280px;top:130px;left:-40px;">FILTRO</span>
  <div class="orbit" style="width:300px;height:300px;top:160px;right:-90px;"></div>
  <div class="block" style="left:96px;right:96px;bottom:200px;">
    <div class="icon-badge">{ICON_FORM}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Menos reunião perdida</span>
    <h2 class="mega" style="font-size:58px;margin-top:16px;">Um formulário que<br/>já filtra o tipo<br/>de projeto certo.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:740px;">Metragem, orçamento e prazo — você já chega na conversa sabendo se faz sentido.</p>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — CTA: tipografico puro, ghost text + orbita =====
render("lpc05_5_cta", f"""
  <span class="ghost" style="font-size:300px;top:150px;left:-50px;">DOLEN</span>
  <div class="orbit" style="width:360px;height:360px;top:120px;right:-110px;"></div>
  <div class="block" style="left:96px;right:96px;top:460px;">
    <h2 class="mega" style="font-size:60px;">Seu portfólio<br/>merece a <strong>mesma<br/>qualidade</strong> do<br/>seu projeto.</h2>
    <div class="rule" style="margin-top:24px;"></div>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="pill">Chama no direct</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">@dolen.ia</span>
  </div>
  {foot(5)}
""")

print("html ok — 5 slides gerados (lp-c05)")
