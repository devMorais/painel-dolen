import os

BASE = os.path.dirname(os.path.abspath(__file__))
FONTFACE = open(os.path.join(BASE, "fontface.css"), encoding="utf-8").read()
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
.canvas{position:relative;overflow:hidden;display:flex;flex-direction:column;isolation:isolate;}
.story{width:1080px;height:1920px;}
.feed{width:1080px;height:1350px;}
.bg-black{background:#0d0d0d;color:var(--paper);}
.bg-white{background:var(--paper);color:var(--ink);}
.bg-soft{background:var(--soft);color:var(--ink);}

.vignette::before{content:"";position:absolute;inset:0;z-index:2;pointer-events:none;
  background:radial-gradient(ellipse 120% 90% at 50% 42%, transparent 55%, rgba(0,0,0,0.36) 100%);}

.ghost{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:1;color:transparent;white-space:nowrap;}
.on-black .ghost{-webkit-text-stroke:2px rgba(255,255,255,0.12);}
.on-light .ghost{-webkit-text-stroke:2px rgba(10,10,10,0.08);}

.halftone{position:absolute;z-index:1;pointer-events:none;}
.on-black .halftone{background-image:radial-gradient(rgba(255,255,255,0.22) 1.7px, transparent 1.7px);background-size:15px 15px;}
.on-light .halftone{background-image:radial-gradient(rgba(10,10,10,0.16) 1.7px, transparent 1.7px);background-size:15px 15px;}
.fade-r{-webkit-mask-image:linear-gradient(to right, black, transparent);}
.fade-t{-webkit-mask-image:linear-gradient(to top, black, transparent);}

.orbit{position:absolute;border-radius:50%;z-index:1;}
.on-black .orbit{border:2px solid rgba(255,255,255,0.12);}
.on-light .orbit{border:2px solid rgba(10,10,10,0.08);}
.orbit::after{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);}
.on-black .orbit::after{background:rgba(255,255,255,0.3);}
.on-light .orbit::after{background:rgba(10,10,10,0.22);}

.regmark{position:absolute;width:30px;height:30px;z-index:6;opacity:0.32;}
.regmark::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}
.regmark::after{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}

/* conteúdo com ZONA SEGURA: nada encostado nas bordas */
.content{position:relative;z-index:10;flex:1;display:flex;flex-direction:column;justify-content:space-between;}
.story .content{padding:240px 120px 320px;}
.feed .content{padding:130px 116px 140px;}

.brand{display:flex;align-items:center;gap:18px;}
.brand img{width:46px;height:46px;}
.invert{filter:invert(1) brightness(2);}
.brand .wm{font-size:31px;font-weight:700;}

.kicker{font-size:26px;font-weight:600;letter-spacing:0.22em;text-transform:uppercase;opacity:0.55;}
.mega{font-weight:700;letter-spacing:-0.03em;line-height:0.98;}
.support{font-weight:400;line-height:1.42;opacity:0.75;text-wrap:pretty;}
.rule{height:3px;width:120px;background:currentColor;opacity:0.85;}

.badge{align-self:flex-start;font-size:25px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;padding:12px 30px;border-radius:100px;background:var(--ink);color:var(--paper);}

.pde{font-size:38px;opacity:0.5;text-decoration:line-through;font-weight:500;}
.ptotal{font-weight:700;font-size:112px;letter-spacing:-0.02em;line-height:1;}
.ptotal .permes{font-size:44px;font-weight:600;opacity:0.5;}
.psub{font-size:32px;opacity:0.62;}
.maint{font-size:26px;opacity:0.55;border-top:2px solid rgba(128,128,128,0.28);padding-top:22px;line-height:1.45;}

.swipe{display:flex;align-items:center;gap:14px;font-size:28px;font-weight:600;opacity:0.9;}
.arrow{font-size:38px;}
.pill{align-self:flex-start;font-size:31px;font-weight:600;padding:20px 44px;border-radius:100px;background:var(--paper);color:var(--ink);}

.itemlist{display:flex;flex-direction:column;}
.item{display:flex;align-items:baseline;gap:28px;padding:30px 0;border-bottom:2px solid rgba(128,128,128,0.22);}
.item:last-child{border-bottom:none;}
.item .n{font-size:30px;font-weight:700;opacity:0.35;}
.item .t{font-size:48px;font-weight:700;letter-spacing:-0.02em;}
.item .d{font-size:27px;opacity:0.65;margin-left:auto;text-align:right;max-width:320px;line-height:1.3;}
"""

# regmarks afastados das bordas (zona segura)
RM_STORY = '<span class="regmark" style="top:190px;left:70px;"></span><span class="regmark" style="top:190px;right:70px;"></span><span class="regmark" style="bottom:270px;left:70px;"></span><span class="regmark" style="bottom:270px;right:70px;"></span>'
RM_FEED = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'


def page(name, fmt, body, bgcls, lightcls):
    rm = RM_STORY if fmt == "story" else RM_FEED
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas {fmt} {bgcls} {lightcls}">
{rm}
{body}
{GRAIN}
</div>
</body></html>"""
    open(os.path.join(BASE, name + ".html"), "w", encoding="utf-8").write(html)


def brand(inv=""):
    return f'<div class="brand"><img class="{inv}" src="{LOGO}"/><span class="wm">dolen</span></div>'


def preco(de, valor, ano):
    return f'''
      <div style="display:flex;flex-direction:column;gap:14px;">
        <span class="pde">de R$ {de}/mês</span>
        <span class="ptotal">R$ {valor}<span class="permes">/mês</span></span>
        <span class="psub">12x no cartão · 1º ano R$ {ano}</span>
      </div>
      <div class="maint">A partir do 2º ano: manutenção de R$ 1.500/ano.<br/>Desconto de fundador já aplicado · valores sujeitos a alteração.</div>'''


# ================= STORIES SERVIÇOS (6) =================
page("sv3_1_capa", "story", f"""
  <div class="vignette" style="position:absolute;inset:0;"></div>
  <span class="ghost" style="font-size:400px;bottom:180px;left:-40px;">PLANOS</span>
  <div class="halftone fade-r" style="top:400px;right:60px;width:340px;height:400px;"></div>
  <div class="orbit" style="width:300px;height:300px;top:900px;right:-60px;"></div>
  <div class="content">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:34px;">
      <span class="kicker">Serviços</span>
      <h1 class="mega" style="font-size:124px;">Qual desses<br/>é o seu?</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:37px;max-width:780px;">4 jeitos de colocar seu negócio no ar — todos com painel próprio pra você editar sozinho.</p>
    </div>
    <div class="swipe">Veja os planos <span class="arrow">&rarr;</span></div>
  </div>
""", "bg-black", "on-black")

page("sv3_2_landing", "story", f"""
  <span class="ghost" style="font-size:290px;bottom:400px;right:-60px;">LAND</span>
  <div class="halftone fade-t" style="bottom:270px;left:110px;width:400px;height:220px;"></div>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:30px;">
      <span class="kicker">Plano 01</span>
      <h2 class="mega" style="font-size:94px;">Landing<br/>Page</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:740px;">Uma página de alta conversão — feita pra transformar visita em contato.</p>
    </div>
    {preco("105", "84", "1.008")}
  </div>
""", "bg-white", "on-light")

page("sv3_3_premium", "story", f"""
  <span class="ghost" style="font-size:260px;bottom:420px;right:-70px;">SITE</span>
  <div class="orbit" style="width:340px;height:340px;top:60px;left:-100px;"></div>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:30px;">
      <span class="badge">Mais escolhido</span>
      <h2 class="mega" style="font-size:84px;">Site institucional<br/>Premium</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:760px;">Site completo com painel próprio: páginas, blog, SEO local e caixa de mensagens.</p>
    </div>
    {preco("210", "168", "2.016")}
  </div>
""", "bg-soft", "on-light")

page("sv3_4_pro", "story", f"""
  <span class="ghost" style="font-size:280px;bottom:410px;right:-50px;">LOJA</span>
  <div class="halftone fade-t" style="bottom:270px;left:110px;width:400px;height:220px;"></div>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:30px;">
      <span class="kicker">Plano 03</span>
      <h2 class="mega" style="font-size:94px;">Loja virtual<br/>Pro</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:760px;">Tudo do Premium + carrinho, pagamento por PIX e cartão no próprio site e frete configurado.</p>
    </div>
    {preco("340", "272", "3.264")}
  </div>
""", "bg-white", "on-light")

page("sv3_5_personalizado", "story", f"""
  <span class="ghost" style="font-size:240px;bottom:440px;right:-70px;">CODE</span>
  <div class="orbit" style="width:320px;height:320px;bottom:340px;left:-100px;"></div>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:30px;">
      <span class="kicker">Plano 04</span>
      <h2 class="mega" style="font-size:84px;">Sistema<br/>personalizado</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:760px;">Algo maior ou sob medida — votação, doações, área de membros e outros sistemas específicos.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="ptotal" style="font-size:80px;">Sob consulta</span>
      <div class="maint">Orçamento conforme o escopo · valores sujeitos a alteração.</div>
    </div>
  </div>
""", "bg-soft", "on-light")

page("sv3_6_fecho", "story", f"""
  <div class="vignette" style="position:absolute;inset:0;"></div>
  <span class="ghost" style="font-size:320px;top:170px;left:-40px;">BORA</span>
  <div class="orbit" style="width:380px;height:380px;bottom:240px;right:-110px;"></div>
  <div class="halftone fade-r" style="top:760px;right:70px;width:280px;height:340px;"></div>
  <div class="content">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:34px;">
      <h2 class="mega" style="font-size:96px;">Vamos colocar<br/>seu negócio<br/>no ar?</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:760px;">Os 3 primeiros clientes ganham 20% de desconto — já aplicado nos valores que você viu.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="pill">Link na bio</span>
      <span class="support" style="font-size:29px;opacity:0.6;">ou chama no direct — @dolen.ia</span>
    </div>
  </div>
""", "bg-black", "on-black")

# ================= CARROSSEL APRESENTAÇÃO (4) =================
page("apr3_1", "feed", f"""
  <div class="vignette" style="position:absolute;inset:0;"></div>
  <span class="ghost" style="font-size:470px;bottom:60px;left:-30px;">DOLEN</span>
  <div class="halftone fade-r" style="top:200px;right:80px;width:360px;height:380px;"></div>
  <div class="orbit" style="width:280px;height:280px;top:600px;right:-70px;"></div>
  <div class="content">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:34px;">
      <span class="kicker">Apresentação</span>
      <h1 class="mega" style="font-size:138px;">Prazer,<br/>Dolen.</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:37px;max-width:760px;">A empresa por trás dos sites e sistemas que você viu por aqui.</p>
    </div>
    <div class="swipe">Arraste <span class="arrow">&rarr;</span></div>
  </div>
""", "bg-black", "on-black")

page("apr3_2", "feed", f"""
  <span class="ghost" style="font-size:310px;bottom:150px;right:-70px;">SITES</span>
  <div class="halftone fade-t" style="bottom:90px;left:116px;width:420px;height:200px;"></div>
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
""", "bg-white", "on-light")

page("apr3_3", "feed", f"""
  <span class="ghost" style="font-size:230px;bottom:100px;right:-60px;">EDITE</span>
  <div class="orbit" style="width:340px;height:340px;top:-60px;left:-90px;"></div>
  <div class="halftone fade-r" style="bottom:280px;right:80px;width:320px;height:280px;"></div>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:36px;">
      <span class="kicker">Nosso diferencial</span>
      <h2 class="mega" style="font-size:96px;">Você edita<br/>tudo sozinho.</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:35px;max-width:790px;">Todo site da Dolen vem com painel próprio: troque textos, fotos e preços quando quiser — sem depender de programador, sem taxa por alteração.</p>
    </div>
    <p class="support" style="font-size:28px;opacity:0.5;">Não é template genérico. É código de verdade, sob medida.</p>
  </div>
""", "bg-soft", "on-light")

page("apr3_4", "feed", f"""
  <div class="vignette" style="position:absolute;inset:0;"></div>
  <span class="ghost" style="font-size:300px;top:90px;left:-40px;">BORA</span>
  <div class="orbit" style="width:380px;height:380px;bottom:-100px;right:-110px;"></div>
  <div class="halftone fade-r" style="top:460px;right:80px;width:280px;height:320px;"></div>
  <div class="content">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:32px;">
      <h2 class="mega" style="font-size:102px;">Vamos colocar<br/>seu negócio<br/>no ar?</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:760px;">Hospedagem grátis no 1º ano · até 12x no cartão · painel pra você editar sozinho.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:22px;">
      <span class="pill">Link na bio</span>
      <span class="support" style="font-size:28px;opacity:0.6;">ou chama no direct — @dolen.ia</span>
    </div>
  </div>
""", "bg-black", "on-black")

print("ok")
