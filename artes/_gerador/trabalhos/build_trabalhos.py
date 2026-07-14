import os

BASE = os.path.dirname(os.path.abspath(__file__))
BASEURL = BASE.replace("\\", "/")
FONTFACE = open(r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador\fontface.css", encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"
FOTOS = "C:/Users/UITEC/Herd/dolen-painel/artes/_gerador/fotos"

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.5;mix-blend-mode:overlay;" xmlns='http://www.w3.org/2000/svg'>
  <filter id='g'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter>
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.5'/>
</svg>"""

CSS = FONTFACE + """
:root{--ink:#0a0a0a;--paper:#ffffff;--soft:#f2f2f0;--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{width:100%;height:100%;overflow:hidden;}
body{font-family:var(--display);-webkit-font-smoothing:antialiased;}
.canvas{position:relative;width:1080px;height:1920px;overflow:hidden;isolation:isolate;}
.bg-black{background:#0b0b0b;color:var(--paper);}
.bg-white{background:var(--paper);color:var(--ink);}

.photo{position:absolute;inset:0;z-index:0;background-size:cover;background-position:center;}
.ov-left{position:absolute;inset:0;z-index:1;background:linear-gradient(120deg, rgba(6,6,6,0.96) 32%, rgba(6,6,6,0.66) 64%, rgba(6,6,6,0.34) 100%);}
.ov-white{position:absolute;inset:0;z-index:1;background:linear-gradient(160deg, rgba(255,255,255,0.93) 0%, rgba(255,255,255,0.965) 52%, rgba(255,255,255,1) 100%);}
.vignette::before{content:"";position:absolute;inset:0;z-index:2;pointer-events:none;
  background:radial-gradient(ellipse 120% 85% at 50% 38%, transparent 50%, rgba(0,0,0,0.5) 100%);}

.ghost{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:2;color:transparent;white-space:nowrap;}
.on-black .ghost{-webkit-text-stroke:2px rgba(255,255,255,0.12);}
.on-light .ghost{-webkit-text-stroke:2px rgba(10,10,10,0.075);}

.regmark{position:absolute;width:30px;height:30px;z-index:6;opacity:0.32;}
.regmark::before{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}
.regmark::after{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}

.content{position:relative;z-index:10;height:100%;display:flex;flex-direction:column;padding:270px 96px 360px;}
.brand{display:flex;align-items:center;gap:18px;}
.brand img{width:44px;height:44px;}
.invert{filter:invert(1) brightness(2);}
.brand .wm{font-size:30px;font-weight:700;}

.kicker{font-size:26px;font-weight:600;letter-spacing:0.24em;text-transform:uppercase;opacity:0.55;}
.mega{font-weight:700;letter-spacing:-0.032em;line-height:0.98;}
.support{font-weight:400;line-height:1.44;opacity:0.78;text-wrap:pretty;}
.rule{height:3px;width:110px;background:currentColor;opacity:0.85;}
.on-photo .mega,.on-photo .support,.on-photo .kicker{text-shadow:0 2px 26px rgba(0,0,0,0.6);}

/* janela de navegador */
.browser{position:absolute;z-index:8;border-radius:26px;overflow:hidden;background:#fff;}
.on-light .browser{box-shadow:0 50px 110px rgba(0,0,0,0.28), 0 0 0 1px rgba(0,0,0,0.05);}
.on-black .browser{box-shadow:0 50px 120px rgba(0,0,0,0.85), 0 0 0 1px rgba(255,255,255,0.10);}
.browser .bar{height:70px;display:flex;align-items:center;gap:22px;padding:0 30px;background:#ececea;border-bottom:1px solid rgba(0,0,0,0.06);}
.browser .dots{display:flex;gap:12px;flex:none;}
.browser .dots i{width:16px;height:16px;border-radius:50%;background:#c6c6c2;}
.browser .url{flex:1;height:42px;border-radius:100px;background:#fff;display:flex;align-items:center;gap:14px;padding:0 24px;font-size:24px;color:#5a5a5a;font-weight:500;letter-spacing:0.01em;}
.browser .url svg{width:22px;height:22px;flex:none;opacity:0.55;}
.browser .shot{display:block;width:100%;}

.wpp-badge{display:inline-flex;align-items:center;gap:14px;padding:18px 34px 18px 24px;border-radius:100px;border:2px solid currentColor;}
.wpp-badge svg{width:32px;height:32px;flex:none;}
.wpp-badge span{font-size:30px;font-weight:600;}
"""

REGMARKS = '<span class="regmark" style="top:270px;left:60px;"></span><span class="regmark" style="top:270px;right:60px;"></span><span class="regmark" style="bottom:340px;left:60px;"></span><span class="regmark" style="bottom:340px;right:60px;"></span>'

WPP = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'''
LOCK = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'''


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


def browser(shot, label, style, crop=920):
    return f'''<div class="browser" style="{style}">
      <div class="bar">
        <span class="dots"><i></i><i></i><i></i></span>
        <span class="url">{LOCK}{label}</span>
      </div>
      <div style="height:{crop}px;overflow:hidden;">
        <img class="shot" src="file:///{BASEURL}/{shot}"/>
      </div>
    </div>'''


def head(inv, kicker, title, title_size, support, support_w=680):
    return f"""
    {brand(inv)}
    <div style="display:flex;flex-direction:column;gap:30px;margin-top:110px;max-width:850px;">
      <span class="kicker">{kicker}</span>
      <h2 class="mega" style="font-size:{title_size}px;">{title}</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:34px;max-width:{support_w}px;">{support}</p>
    </div>
    """


# ---- 1 CAPA (preto, foto) ----
page("tr_1", f"""
  <div class="photo" style="background-image:url('file:///{FOTOS}/pb3.jpg');"></div>
  <div class="ov-left"></div>
  <div class="vignette" style="position:absolute;inset:0;"></div>
  <span class="ghost" style="font-size:280px;bottom:360px;left:-46px;">TRABALHOS</span>
  <div class="content on-photo">
    {brand('invert')}
    <div style="display:flex;flex-direction:column;gap:38px;margin-top:220px;">
      <span class="kicker">Portfólio Dolen</span>
      <h1 class="mega" style="font-size:120px;">Feito pela<br/>Dolen.</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:38px;max-width:720px;">Alguns projetos reais que a gente criou — no ar agora.</p>
    </div>
    <div class="support" style="font-size:30px;opacity:0.6;margin-top:auto;">Arraste →</div>
  </div>
""", "bg-black", "on-black")

# ---- 2 MISS (branco) — endereco visivel ----
page("tr_2", f"""
  <span class="ghost" style="font-size:400px;top:250px;right:-20px;">01</span>
  {browser("miss_desk.png", "votepelasuamiss.com.br", "left:70px;width:940px;top:1010px;")}
  <div class="content">
    {head("", "01 · Votação online", "Vote pela<br/>sua Miss.", 104, "Do perfil da candidata ao voto — tudo pelo site, em tempo real.", 640)}
  </div>
""", "bg-white", "on-light")

# ---- 3 SHOPX (preto) — endereco oculto ----
page("tr_3", f"""
  <span class="ghost" style="font-size:400px;top:250px;right:-20px;">02</span>
  {browser("shopx_desk.png", "ShopX · Loja virtual", "left:70px;width:940px;top:1010px;")}
  <div class="content">
    {head("invert", "02 · Loja virtual", "ShopX.", 118, "E-commerce completo: catálogo, carrinho, frete e pagamento.", 640)}
  </div>
""", "bg-black", "on-black")

# ---- 4 AVANTE (branco) — endereco oculto ----
page("tr_4", f"""
  <span class="ghost" style="font-size:400px;top:250px;right:-20px;">03</span>
  {browser("avante_desk.png", "Avante · Sistema de gestão", "left:70px;width:940px;top:1010px;")}
  <div class="content">
    {head("", "03 · Sistema sob medida", "Avante.", 118, "Sistema de gestão de tarefas e projetos, organizados por quadros.", 640)}
  </div>
""", "bg-white", "on-light")

# ---- 5 AGF (preto) — endereco oculto ----
page("tr_5", f"""
  <span class="ghost" style="font-size:400px;top:250px;right:-20px;">04</span>
  {browser("agf_desk.png", "Associação Grande Família", "left:70px;width:940px;top:1010px;")}
  <div class="content">
    {head("invert", "04 · Institucional", "Grande<br/>Família.", 96, "Site de ONG — apresentação do projeto e doação já na primeira tela.", 660)}
  </div>
""", "bg-black", "on-black")

# ---- 6 SUDOKU (branco) — endereco oculto ----
page("tr_6", f"""
  <span class="ghost" style="font-size:400px;top:250px;right:-20px;">05</span>
  {browser("sudoku_desk.png", "Sudoku · Dolen", "left:70px;width:940px;top:1010px;")}
  <div class="content">
    {head("", "05 · Só por diversão", "Nosso<br/>joguinho.", 104, "Um Sudoku temático que criamos por conta — pra relaxar entre um projeto e outro.", 640)}
  </div>
""", "bg-white", "on-light")

# ---- 7 PAINEL (preto) — janela completa ----
page("tr_7", f"""
  <span class="ghost" style="font-size:250px;top:250px;right:-20px;">PAINEL</span>
  {browser("painel_desk.png", "Painel Dolen", "left:40px;width:1000px;top:1120px;", crop=504)}
  <div class="content">
    {head("invert", "E não para no site", "Você no<br/>controle.", 100, "Todo projeto vem com painel próprio: edite textos, fotos e preços — e acompanhe seus contatos sem depender de ninguém.", 720)}
  </div>
""", "bg-black", "on-black")

# ---- 8 CTA (branco, foto) ----
page("tr_8", f"""
  <div class="photo" style="background-image:url('file:///{FOTOS}/pb2.jpg');"></div>
  <div class="ov-white"></div>
  <span class="ghost" style="font-size:330px;bottom:400px;right:-56px;">SEU</span>
  <div class="content">
    {brand()}
    <div style="display:flex;flex-direction:column;gap:38px;margin-top:230px;">
      <span class="kicker">E agora?</span>
      <h2 class="mega" style="font-size:100px;">O próximo pode<br/>ser o seu.</h2>
      <div class="rule"></div>
      <p class="support" style="font-size:36px;max-width:760px;">Site, loja ou sistema sob medida — no ar em dias, com painel pra você editar sozinho.</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:24px;margin-top:auto;">
      <span class="wpp-badge">{WPP}<span>Chama no direct — @dolen.ia</span></span>
      <span class="support" style="font-size:28px;opacity:0.6;">ou toca o link na bio</span>
    </div>
  </div>
""", "bg-white", "on-light")

print("ok")
