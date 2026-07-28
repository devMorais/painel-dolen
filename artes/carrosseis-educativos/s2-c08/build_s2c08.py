# -*- coding: utf-8 -*-
"""[S2-C08] Carrossel "Projeto real: sistema de votacao no ar" — 6 slides, feed 1080x1350.
Fundo BRANCO (regra de intercalacao — o S2-C07 foi escuro).

Caso REAL (Crown Up / Miss — votepelasuamiss.com.br), entao usa SCREENSHOT REAL do
projeto numa janela de navegador (mesma tecnica do story "Trabalhos", ja aprovada e
publicada), nao mockup generico nem foto de banco. Space Grotesk, mono, grao."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
TRABALHOS = os.path.join(GERADOR, "trabalhos")
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"
MISS_SHOT = "file:///" + os.path.join(TRABALHOS, "miss_desk.png").replace("\\", "/")

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
.mega{{font-weight:700;letter-spacing:-0.03em;line-height:1.02;}}
.support{{font-weight:400;line-height:1.42;opacity:0.72;text-wrap:pretty;}}
.rule{{height:3px;width:110px;background:currentColor;opacity:0.85;}}
.und{{text-decoration:underline;text-underline-offset:0.1em;}}
.swipe{{display:flex;align-items:center;gap:14px;font-size:27px;font-weight:600;opacity:0.9;}}
.arrow{{font-size:36px;}}
.pill{{display:inline-flex;align-items:center;gap:14px;font-size:29px;font-weight:600;padding:20px 42px;border-radius:100px;background:var(--ink);color:var(--paper);}}
.pill svg{{width:28px;height:28px;}}
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.4;font-weight:600;letter-spacing:0.04em;}}

.stat-big{{font-size:130px;font-weight:700;letter-spacing:-0.04em;line-height:0.82;}}

/* janela de navegador com o screenshot real do projeto */
.browser{{position:absolute;z-index:5;border-radius:20px;overflow:hidden;background:#fff;
  box-shadow:0 40px 90px -30px rgba(16,16,16,0.35), 0 0 0 1px rgba(16,16,16,0.06);}}
.browser .bar{{height:52px;display:flex;align-items:center;gap:16px;padding:0 22px;background:#ececea;border-bottom:1px solid rgba(0,0,0,0.06);}}
.browser .dots{{display:flex;gap:9px;flex:none;}}
.browser .dots i{{width:12px;height:12px;border-radius:50%;background:#c6c6c2;}}
.browser .url{{flex:1;height:32px;border-radius:100px;background:#fff;display:flex;align-items:center;gap:10px;padding:0 18px;font-size:18px;color:#5a5a5a;font-weight:500;}}
.browser .url svg{{width:16px;height:16px;flex:none;opacity:0.55;}}
.browser .shot{{display:block;width:100%;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

IC_SEND = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>'
IC_LOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'


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


def browser(style, crop=700, url="votepelasuamiss.com.br"):
    return f"""<div class="browser" style="{style}">
      <div class="bar"><span class="dots"><i></i><i></i><i></i></span><span class="url">{IC_LOCK}{url}</span></div>
      <div style="height:{crop}px;overflow:hidden;"><img class="shot" src="{MISS_SHOT}"/></div>
    </div>"""


# ===== SLIDE 1 — CAPA: mockup real no topo, titulo com respiro embaixo =====
render("s2c08_1_capa",
    browser("left:96px;right:-140px;top:180px;", crop=640) + f"""
  <div class="block" style="left:96px;right:96px;top:900px;">
    <span class="kicker">Dolen · caso real</span>
    <h1 class="mega" style="font-size:66px;margin-top:18px;">Por dentro de<br/>um projeto <span class="und">REAL</span><br/>feito pela Dolen.</h1>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — O DESAFIO (tipografico, sem browser — variacao) =====
render("s2c08_2_desafio", f"""
  <span class="ghost" style="font-size:280px;bottom:130px;right:-60px;">MISS</span>
  <div class="block" style="left:96px;right:96px;top:280px;">
    <span class="kicker">O desafio</span>
    <h2 class="mega" style="font-size:66px;margin-top:20px;">Um concurso<br/>de Miss precisava<br/>de votação online.</h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:740px;">Página pra cada candidata e voto direto pelo site.</p>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — A SOLUCAO (browser mockup real, texto com respiro embaixo) =====
render("s2c08_3_solucao",
    browser("left:96px;right:-140px;top:150px;", crop=700) + f"""
  <div class="block" style="left:96px;right:96px;top:940px;">
    <span class="kicker">A solução</span>
    <h2 class="mega" style="font-size:52px;margin-top:16px;">Sistema sob<br/>medida, do zero.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:30px;margin-top:20px;max-width:760px;">Perfil das candidatas, votação pelo site e apuração — tudo num lugar só.</p>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — O RESULTADO (numeral gigante, sem browser — variacao) =====
render("s2c08_4_resultado", f"""
  <span class="ghost" style="font-size:260px;top:150px;left:-50px;">LIVE</span>
  <div class="orbit" style="width:320px;height:320px;top:120px;right:-90px;"></div>
  <div class="block" style="left:96px;right:96px;top:340px;">
    <span class="kicker">O resultado</span>
    <div class="stat-big" style="margin-top:20px;">MILHARES</div>
    <h2 class="mega" style="font-size:44px;margin-top:14px;">de acessos no período<br/>de votação.</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;max-width:740px;">No ar e funcionando de verdade.</p>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — O QUE ISSO MOSTRA (tipografico) =====
render("s2c08_5_mostra", f"""
  <span class="ghost" style="font-size:270px;bottom:120px;right:-60px;">RÉGUA</span>
  <div class="block" style="left:96px;right:96px;top:300px;">
    <span class="kicker">O que isso mostra</span>
    <h2 class="mega" style="font-size:60px;margin-top:20px;">A gente não faz<br/>só página bonita.</h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:760px;">Faz sistema que resolve — do site simples à ferramenta completa, a régua é a mesma.</p>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — CTA =====
render("s2c08_6_cta", f"""
  <span class="ghost" style="font-size:280px;top:150px;left:-50px;">IDEIA</span>
  <div class="orbit" style="width:340px;height:340px;top:120px;right:-90px;"></div>
  <div class="block" style="left:96px;right:96px;top:400px;">
    <h2 class="mega" style="font-size:60px;">Tem uma ideia<br/>que parece<br/>complicada demais?</h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:720px;">Conta pra gente — a gente tira do papel.</p>
  </div>
  <div class="block" style="left:96px;bottom:180px;">
    <span class="pill">{IC_SEND}Chama no direct</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">ou link na bio</span>
  </div>
  {foot(6)}
""")

print("html ok — 6 slides gerados")
