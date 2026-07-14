import os

BASE = os.path.dirname(os.path.abspath(__file__))
FOTOS = os.path.join(BASE, "fotos").replace("\\", "/")
FONTFACE = open(r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador\fontface.css", encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"

def foto(n):
    return f"file:///{FOTOS}/pb{n}.jpg"

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
.bg-black{background:#0b0b0b;color:var(--paper);}
.bg-white{background:var(--paper);color:var(--ink);}
.bg-soft{background:var(--soft);color:var(--ink);}

/* foto de fundo fullbleed */
.photo{position:absolute;inset:0;z-index:0;background-size:cover;background-position:center;}
/* overlay de leitura (esquerda escura -> direita mais aberta) */
.ov-left{position:absolute;inset:0;z-index:1;background:linear-gradient(100deg, rgba(5,5,5,0.94) 30%, rgba(5,5,5,0.55) 62%, rgba(5,5,5,0.30) 100%);}
.ov-heavy{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg, rgba(5,5,5,0.82) 0%, rgba(5,5,5,0.88) 60%, rgba(5,5,5,0.96) 100%);}
.ov-white{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg, rgba(255,255,255,0.90) 0%, rgba(255,255,255,0.96) 55%, rgba(242,242,240,1) 100%);}

/* foto como banda superior com fade */
.photo-band{position:absolute;top:0;left:0;right:0;height:560px;z-index:0;background-size:cover;background-position:center 30%;
  -webkit-mask-image:linear-gradient(to bottom, black 55%, transparent 100%);}
.photo-band::after{content:"";position:absolute;inset:0;background:rgba(255,255,255,0.42);}

.vignette::before{content:"";position:absolute;inset:0;z-index:2;pointer-events:none;
  background:radial-gradient(ellipse 120% 90% at 50% 42%, transparent 52%, rgba(0,0,0,0.42) 100%);}

.ghost{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:2;color:transparent;white-space:nowrap;}
.on-black .ghost{-webkit-text-stroke:2px rgba(255,255,255,0.13);}
.on-light .ghost{-webkit-text-stroke:2px rgba(10,10,10,0.09);}

.regmark{position:absolute;width:30px;height:30px;z-index:6;opacity:0.35;}
.regmark::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}
.regmark::after{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}

.content{position:relative;z-index:10;flex:1;display:flex;flex-direction:column;justify-content:space-between;padding:130px 116px 140px;}
.row{display:flex;align-items:center;justify-content:space-between;}
.brand{display:flex;align-items:center;gap:18px;}
.brand img{width:46px;height:46px;}
.invert{filter:invert(1) brightness(2);}
.brand .wm{font-size:31px;font-weight:700;}

.kicker{font-size:26px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;opacity:0.6;}
.mega{font-weight:700;letter-spacing:-0.03em;line-height:0.98;}
.support{font-weight:400;line-height:1.42;opacity:0.8;text-wrap:pretty;}
.rule{height:3px;width:120px;background:currentColor;opacity:0.85;}

.itemlist{display:flex;flex-direction:column;}
.item{display:flex;align-items:baseline;gap:28px;padding:29px 0;border-bottom:2px solid rgba(128,128,128,0.24);}
.item:last-child{border-bottom:none;}
.item .n{font-size:30px;font-weight:700;opacity:0.35;}
.item .t{font-size:48px;font-weight:700;letter-spacing:-0.02em;}
.item .d{font-size:27px;opacity:0.65;margin-left:auto;text-align:right;max-width:320px;line-height:1.3;}

.wpp-badge{display:inline-flex;align-items:center;gap:14px;padding:16px 30px 16px 20px;border-radius:100px;border:2px solid currentColor;}
.wpp-badge svg{width:30px;height:30px;flex:none;}
.wpp-badge span{font-size:28px;font-weight:600;}

/* sombra de texto sutil quando sobre foto */
.on-photo .mega, .on-photo .support, .on-photo .kicker{text-shadow:0 2px 24px rgba(0,0,0,0.55);}
"""

REGMARKS = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

WPP = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'''


def page(name, body, bgcls, lightcls):
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas {bgcls} {lightcls}">
{body}
{REGMARKS}
{GRAIN}
</div>
</body></html>"""
    open(os.path.join(BASE, name + ".html"), "w", encoding="utf-8").write(html)


def brand(inv=""):
    return f'<div class="brand"><img class="{inv}" src="{LOGO}"/><span class="wm">dolen</span></div>'


# ---- 1 CAPA: laptop brilhando no escuro, texto sobre a área escura ----
page("apr5_1", f"""
  <div class="photo" style="background-image:url('{foto(1)}');background-position:70% center;"></div>
  <div class="ov-left"></div>
  <div class="vignette" style="position:absolute;inset:0;"></div>
  <span class="ghost" style="font-size:440px;bottom:50px;left:-30px;">DOLEN</span>
  <div class="content on-photo">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:34px;">
      <span class="kicker">Apresentação</span>
      <h1 class="mega" style="font-size:130px;">Prazer,<br/>Dolen.</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:37px;max-width:700px;">A empresa por trás dos sites e sistemas que você viu por aqui.</p>
    </div>
    <div class="support" style="font-size:28px;opacity:0.65;">Arraste →</div>
  </div>
""", "bg-black", "on-black")

# ---- 2 O QUE FAZEMOS: banda de foto (workspace/código) com fade pro branco ----
page("apr5_2", f"""
  <div class="photo-band" style="background-image:url('{foto(2)}');"></div>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:34px;margin-top:230px;">
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
""", "bg-white", "on-light")

# ---- 3 DIFERENCIAL: mãos digitando, overlay branco (foto sutil) ----
page("apr5_3", f"""
  <div class="photo" style="background-image:url('{foto(3)}');"></div>
  <div class="ov-white"></div>
  <span class="ghost" style="font-size:230px;bottom:90px;right:-60px;">EDITE</span>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:36px;">
      <span class="kicker">Nosso diferencial</span>
      <h2 class="mega" style="font-size:96px;">Você edita<br/>tudo sozinho.</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:35px;max-width:760px;">Todo site da Dolen vem com painel próprio: troque textos, fotos e preços quando quiser — sem depender de programador, sem taxa por alteração.</p>
    </div>
    <p class="support" style="font-size:28px;opacity:0.55;">Não é template genérico. É código de verdade, sob medida.</p>
  </div>
""", "bg-soft", "on-light")

# ---- 4 CTA: mesa/equipe de cima, overlay preto pesado ----
page("apr5_4", f"""
  <div class="photo" style="background-image:url('{foto(4)}');"></div>
  <div class="ov-heavy"></div>
  <div class="vignette" style="position:absolute;inset:0;"></div>
  <span class="ghost" style="font-size:300px;top:80px;left:-40px;">BORA</span>
  <div class="content on-photo">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:32px;">
      <h2 class="mega" style="font-size:100px;">Vamos colocar<br/>seu negócio<br/>no ar?</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:740px;">Hospedagem grátis no 1º ano · até 12x no cartão · painel pra você editar sozinho.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:22px;">
      <span class="wpp-badge">{WPP}<span>Chama no direct — @dolen.ia</span></span>
      <span class="support" style="font-size:27px;opacity:0.6;">ou link na bio</span>
    </div>
  </div>
""", "bg-black", "on-black")

print("ok")
