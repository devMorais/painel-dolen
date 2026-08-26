# -*- coding: utf-8 -*-
"""[LP-C04] Carrossel "Sua loja não precisa fechar nunca" — 6 slides, feed 1080x1350.
Fundo ESCURO (regra de intercalacao do feed — o LP-C03 foi claro).

O slide 2 mostra um MOCKUP da vitrine (grid de produtos) do site "Loja Bonita"
(lojabonita_mock.html) — Loja Bonita e um exemplo ilustrativo criado no LP-C01, NAO um
cliente real, entao a barra de URL do mockup diz "Exemplo · Loja Bonita" (nunca um
dominio real) e a copy evita "site real"/"loja bonita mostra como" (a legenda original
pedia isso, ajustada pra "veja como ficaria"). Precos nos cards de produto sao dado
ficticio de demonstracao (mesma logica do StudioDemoSeeder), nao preco real da Dolen."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", "..", ".."))
GERADOR = os.path.join(REPO, "artes", "_gerador")
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///" + os.path.join(REPO, "frontend", "public", "assets", "images", "dolen-icone-preto.png").replace("\\", "/")
FOTO_RELOGIO = "file:///" + os.path.join(REPO, "artes", "carrosseis-educativos", "s2-c01", "fotos", "final_relogio.jpg").replace("\\", "/")
MOCK_SHOT = "file:///" + os.path.join(BASE, "lojabonita_mock.png").replace("\\", "/")

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
.fade-l img{{-webkit-mask-image:linear-gradient(270deg, #000 28%, transparent 62%);}}
.fade-r img{{-webkit-mask-image:linear-gradient(90deg, #000 28%, transparent 62%);}}

.ghost{{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:0;color:transparent;-webkit-text-stroke:2px rgba(255,255,255,0.13);white-space:nowrap;}}
.orbit{{position:absolute;border-radius:50%;border:2px solid rgba(255,255,255,0.13);z-index:0;}}
.orbit::after{{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);background:rgba(255,255,255,0.3);}}

.icon-badge{{width:88px;height:88px;border-radius:50%;border:2px solid rgba(255,255,255,0.35);display:flex;align-items:center;justify-content:center;z-index:10;}}
.icon-badge svg{{width:40px;height:40px;stroke:#fff;}}

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
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.5;font-weight:600;letter-spacing:0.04em;}}

.browser{{position:absolute;z-index:8;border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 50px 120px rgba(0,0,0,0.85), 0 0 0 1px rgba(255,255,255,0.10);}}
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


def foot(n, total=6):
    return f'<div class="foot">{n:02d} / {total:02d}</div>'


ICON_PHONE = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/></svg>'''
ICON_PAGAMENTO = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/></svg>'''
ICON_CHAT = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-9 8.35A8.5 8.5 0 1 1 21 11.5z"/><path d="M8 10h8M8 14h5"/></svg>'''

# ===== SLIDE 1 — CAPA: foto sangrando no topo + dissolve pra baixo =====
render("lpc04_1_capa", f"""
  <div class="foto fade-b" style="top:0;left:0;right:0;height:760px;"><img src="{FOTO_RELOGIO}"/></div>
  <div class="block" style="left:96px;right:96px;bottom:180px;">
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="kicker">Dolen · e-commerce</span>
      <h1 class="mega" style="font-size:66px;">Sua loja física<br/>fecha às 18h.<br/><span class="und">Seu site, não.</span></h1>
      <div class="rule"></div>
      <p class="support" style="font-size:31px;">(vender enquanto você dorme)</p>
    </div>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — mockup da vitrine da Loja Bonita, em janela de navegador =====
render("lpc04_2_mockup", f"""
  <span class="ghost" style="font-size:220px;top:110px;left:-40px;">EXEMPLO</span>
  <div class="browser" style="left:50px;width:980px;top:220px;">
    <div class="bar"><span class="dots"><i></i><i></i><i></i></span><span class="url">Exemplo · Loja Bonita</span></div>
    <div style="height:620px;overflow:hidden;"><img class="shot" src="{MOCK_SHOT}"/></div>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="kicker">Assim ficaria sua vitrine</span>
    <h2 class="mega" style="font-size:52px;margin-top:14px;">Um exemplo de como<br/>a Dolen pensaria.</h2>
    <div class="rule" style="margin-top:18px;"></div>
    <p class="support" style="font-size:29px;margin-top:18px;max-width:760px;">Mockup ilustrativo — não é um cliente real, é o padrão que aplicaríamos na sua loja.</p>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — celular: tipografico puro (variacao, sem foto) =====
render("lpc04_3_celular", f"""
  <span class="ghost" style="font-size:260px;top:130px;left:-40px;">MOBILE</span>
  <div class="orbit" style="width:300px;height:300px;top:160px;right:-90px;"></div>
  <div class="block" style="left:96px;right:96px;bottom:200px;">
    <div class="icon-badge">{ICON_PHONE}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Onde ela compra</span>
    <h2 class="mega" style="font-size:58px;margin-top:16px;">O celular é onde<br/>sua cliente compra.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:740px;">Se o site não funciona bem no celular, ela desiste antes de finalizar.</p>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — pagamento: tipografico puro =====
render("lpc04_4_pagamento", f"""
  <span class="ghost" style="font-size:280px;bottom:200px;right:-50px;">PIX</span>
  <div class="block" style="left:96px;right:96px;top:420px;">
    <div class="icon-badge">{ICON_PAGAMENTO}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Sem fricção na hora de pagar</span>
    <h2 class="mega" style="font-size:58px;margin-top:16px;">PIX, cartão e frete<br/>bem claros.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:740px;">Nada de descobrir o frete só no fim — isso é o que mais derruba uma venda.</p>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — FAQ: tipografico puro com icone de chat =====
render("lpc04_5_faq", f"""
  <span class="ghost" style="font-size:280px;top:130px;left:-40px;">FAQ</span>
  <div class="block" style="left:96px;right:96px;bottom:200px;">
    <div class="icon-badge">{ICON_CHAT}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Última dúvida antes da compra</span>
    <h2 class="mega" style="font-size:58px;margin-top:16px;">FAQ tira a dúvida<br/>que quase te<br/>custou a venda.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:740px;">Troca, tamanho, prazo — respondido no site, sem esperar resposta no direct.</p>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — CTA: tipografico puro, ghost text + orbita =====
render("lpc04_6_cta", f"""
  <span class="ghost" style="font-size:300px;top:150px;left:-50px;">VITRINE</span>
  <div class="orbit" style="width:360px;height:360px;top:120px;right:-110px;"></div>
  <div class="block" style="left:96px;right:96px;top:460px;">
    <h2 class="mega" style="font-size:64px;">Vamos montar<br/><strong>sua vitrine</strong><br/>digital?</h2>
    <div class="rule" style="margin-top:24px;"></div>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="pill">Chama no direct</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">@dolen.ia</span>
  </div>
  {foot(6)}
""")

print("html ok — 6 slides gerados (lp-c04)")
