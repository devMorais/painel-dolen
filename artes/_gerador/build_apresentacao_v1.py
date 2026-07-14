import os

BASE = os.path.dirname(os.path.abspath(__file__))
FONTFACE = open(r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador\fontface.css", encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.5;mix-blend-mode:overlay;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.55'/>
</svg>"""

CSS = FONTFACE + """
:root{--ink:#0a0a0a;--paper:#ffffff;--soft:#f2f2f0;--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{width:100%;height:100%;overflow:hidden;}
body{font-family:var(--display);-webkit-font-smoothing:antialiased;}
.canvas{position:relative;width:1080px;height:1350px;overflow:hidden;display:flex;flex-direction:column;isolation:isolate;}
.bg-black{background:#0c0c0c;color:var(--paper);}
.bg-white{background:var(--paper);color:var(--ink);}
.bg-soft{background:var(--soft);color:var(--ink);}

/* --- corte diagonal de fundo (profundidade tonal, sem cor) --- */
.diag::before{content:"";position:absolute;inset:0;z-index:0;
  clip-path:polygon(0 62%, 100% 38%, 100% 100%, 0 100%);}
.on-black .diag::before{background:#050505;}
.on-light .diag::before{background:rgba(10,10,10,0.05);}

/* --- luz diagonal (feixe suave cruzando a peça) --- */
.lightsweep{position:absolute;inset:-10% -20%;z-index:1;pointer-events:none;transform:rotate(-12deg);}
.on-black .lightsweep{background:linear-gradient(90deg, transparent 40%, rgba(255,255,255,0.10) 50%, transparent 60%);}
.on-light .lightsweep{background:linear-gradient(90deg, transparent 40%, rgba(10,10,10,0.06) 50%, transparent 60%);}

.vignette::before{content:"";position:absolute;inset:0;z-index:2;pointer-events:none;
  background:radial-gradient(ellipse 120% 90% at 50% 42%, transparent 55%, rgba(0,0,0,0.4) 100%);}

.ghost{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:1;color:transparent;white-space:nowrap;}
.on-black .ghost{-webkit-text-stroke:2px rgba(255,255,255,0.11);}
.on-light .ghost{-webkit-text-stroke:2px rgba(10,10,10,0.08);}

.regmark{position:absolute;width:30px;height:30px;z-index:6;opacity:0.32;}
.regmark::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}
.regmark::after{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}

.content{position:relative;z-index:10;flex:1;display:flex;flex-direction:column;justify-content:space-between;padding:130px 116px 140px;}
.row{display:flex;align-items:center;justify-content:space-between;}
.brand{display:flex;align-items:center;gap:18px;}
.brand img{width:46px;height:46px;}
.invert{filter:invert(1) brightness(2);}
.brand .wm{font-size:31px;font-weight:700;}

.kicker{font-size:26px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;opacity:0.55;}
.mega{font-weight:700;letter-spacing:-0.03em;line-height:0.98;}
.support{font-weight:400;line-height:1.42;opacity:0.75;text-wrap:pretty;}
.rule{height:3px;width:120px;background:currentColor;opacity:0.85;}

.itemlist{display:flex;flex-direction:column;}
.item{display:flex;align-items:baseline;gap:28px;padding:30px 0;border-bottom:2px solid rgba(128,128,128,0.22);}
.item:last-child{border-bottom:none;}
.item .n{font-size:30px;font-weight:700;opacity:0.35;}
.item .t{font-size:48px;font-weight:700;letter-spacing:-0.02em;}
.item .d{font-size:27px;opacity:0.65;margin-left:auto;text-align:right;max-width:320px;line-height:1.3;}

.pill{align-self:flex-start;font-size:31px;font-weight:600;padding:20px 44px;border-radius:100px;background:var(--paper);color:var(--ink);}

/* --- selo WhatsApp (linha, monocromatico) --- */
.wpp-badge{display:inline-flex;align-items:center;gap:14px;padding:16px 30px 16px 20px;border-radius:100px;
  border:2px solid currentColor;}
.wpp-badge svg{width:30px;height:30px;flex:none;}
.wpp-badge span{font-size:28px;font-weight:600;}
"""

REGMARKS = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

WHATSAPP_ICON = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'''


def facet_shape(tone, seed_offset=0):
    """
    Cristal facetado (low-poly): cluster de triangulos convergindo, cada um
    com opacidade levemente diferente para simular luz batendo em ângulos
    distintos — a técnica mais sofisticada observada no curso, em P&B puro.
    """
    import random
    random.seed(42 + seed_offset)
    cx, cy = 780, 480
    spread = 420
    tris = []
    n_points = 9
    pts = []
    for i in range(n_points):
        ang = (2 * 3.14159 * i / n_points) + random.uniform(-0.25, 0.25)
        r = spread * random.uniform(0.55, 1.0)
        pts.append((cx + r * __import__("math").cos(ang), cy + r * __import__("math").sin(ang)))
    for i in range(n_points):
        p1 = pts[i]
        p2 = pts[(i + 1) % n_points]
        op = random.uniform(0.05, 0.22)
        tris.append(f'<polygon points="{cx},{cy} {p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}" fill="{tone}" opacity="{op:.2f}"/>')
        # linha fina de aresta (acabamento "corte de vidro")
        tris.append(f'<line x1="{cx}" y1="{cy}" x2="{p1[0]:.0f}" y2="{p1[1]:.0f}" stroke="{tone}" stroke-width="1.5" opacity="0.18"/>')
    return f'<svg style="position:absolute;top:-120px;right:-180px;z-index:1;" width="1000" height="1000" viewBox="0 0 1560 960">{"".join(tris)}</svg>'


def page(name, body, bgcls, lightcls, diag=True):
    diagclass = "diag" if diag else ""
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas {bgcls} {lightcls} {diagclass}">
{REGMARKS}
<div class="lightsweep"></div>
{body}
{GRAIN}
</div>
</body></html>"""
    open(os.path.join(BASE, name + ".html"), "w", encoding="utf-8").write(html)


def brand(inv=""):
    return f'<div class="brand"><img class="{inv}" src="{LOGO}"/><span class="wm">dolen</span></div>'


# ---- SLIDE 1 (preto): capa com cristal facetado branco ----
page("apr4_1", f"""
  <div class="vignette" style="position:absolute;inset:0;"></div>
  {facet_shape("#ffffff", 1)}
  <span class="ghost" style="font-size:460px;bottom:60px;left:-30px;">DOLEN</span>
  <div class="content">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:34px;">
      <span class="kicker">Apresentação</span>
      <h1 class="mega" style="font-size:132px;">Prazer,<br/>Dolen.</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:37px;max-width:740px;">A empresa por trás dos sites e sistemas que você viu por aqui.</p>
    </div>
    <div class="row"><div class="support" style="font-size:28px;opacity:0.6;">Arraste →</div></div>
  </div>
""", "bg-black", "on-black")

# ---- SLIDE 2 (branco): o que fazemos, cristal em preto sutil ----
page("apr4_2", f"""
  {facet_shape("#0a0a0a", 2)}
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:36px;">
      <span class="kicker">O que fazemos</span>
      <div class="itemlist">
        <div class="item"><span class="n">01</span><span class="t">Sites</span><span class="d">institucionais, com painel próprio</span></div>
        <div class="item"><span class="n">02</span><span class="t">Lojas</span><span class="d">venda online integrada</span></div>
        <div class="item"><span class="n">03</span><span class="t">Sistemas</span><span class="d">sob medida pro seu negócio</span></div>
        <div class="item"><span class="n">04</span><span class="t">Landing pages</span><span class="d">páginas de alta conversão</span></div>
      </div>
    </div>
    <p class="support" style="font-size:30px;">Tudo no ar em dias — não em meses.</p>
  </div>
""", "bg-white", "on-light", diag=False)

# ---- SLIDE 3 (cinza): diferencial, cristal grande atras do headline ----
page("apr4_3", f"""
  {facet_shape("#0a0a0a", 3)}
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:36px;">
      <span class="kicker">Nosso diferencial</span>
      <h2 class="mega" style="font-size:96px;">Você edita<br/>tudo sozinho.</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:35px;max-width:760px;">Todo site da Dolen vem com painel próprio: troque textos, fotos e preços quando quiser — sem depender de programador, sem taxa por alteração.</p>
    </div>
    <p class="support" style="font-size:28px;opacity:0.5;">Não é template genérico. É código de verdade, sob medida.</p>
  </div>
""", "bg-soft", "on-light")

# ---- SLIDE 4 (preto): CTA com selo WhatsApp ----
page("apr4_4", f"""
  <div class="vignette" style="position:absolute;inset:0;"></div>
  {facet_shape("#ffffff", 4)}
  <span class="ghost" style="font-size:300px;top:90px;left:-40px;">BORA</span>
  <div class="content">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:32px;">
      <h2 class="mega" style="font-size:100px;">Vamos colocar<br/>seu negócio<br/>no ar?</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:740px;">Hospedagem grátis no 1º ano · até 12x no cartão · painel pra você editar sozinho.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="wpp-badge">{WHATSAPP_ICON}<span>Chama no direct — @dolen.ia</span></span>
      <span class="support" style="font-size:27px;opacity:0.55;">ou link na bio</span>
    </div>
  </div>
""", "bg-black", "on-black")

print("ok")
