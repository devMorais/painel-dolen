# -*- coding: utf-8 -*-
"""[LP-C02] Carrossel "Por que sua clínica precisa de site" — 6 slides, feed 1080x1350.
Fundo ESCURO (regra de intercalacao do feed — o LP-C01 foi claro).

O slide 4 mostra um MOCKUP do hero do site "Vitalis Saude" (vitalis_mock.html, renderizado
e recortado em janela de navegador) — Vitalis Saude e um exemplo ilustrativo criado no
LP-C01, NAO um cliente real, entao a barra de URL do mockup diz "Exemplo · Vitalis Saude"
(nunca um dominio real) e a copy evita "site real"/"ja entregamos"."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", "..", ".."))
GERADOR = os.path.join(REPO, "artes", "_gerador")
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///" + os.path.join(REPO, "frontend", "public", "assets", "images", "dolen-icone-preto.png").replace("\\", "/")
FOTO_CLINICA = "file:///" + os.path.join(BASE, "fotos", "hero_clinica.jpg").replace("\\", "/")
FOTO_CELULAR = "file:///" + os.path.join(BASE, "fotos", "final_celular.jpg").replace("\\", "/")
MOCK_SHOT = "file:///" + os.path.join(BASE, "vitalis_mock.png").replace("\\", "/")

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

/* janela de navegador (mockup do site) */
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


ICON_LUPA = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>'''
ICON_MONITOR = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg>'''
ICON_CHAT = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-9 8.35A8.5 8.5 0 1 1 21 11.5z"/><path d="M8 10h8M8 14h5"/></svg>'''
WPP = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'''


# ===== SLIDE 1 — CAPA: foto sangrando no topo + dissolve pra baixo =====
render("lpc02_1_capa", f"""
  <div class="foto fade-b" style="top:0;left:0;right:0;height:760px;"><img src="{FOTO_CLINICA}"/></div>
  <div class="block" style="left:96px;right:96px;bottom:180px;">
    <div style="display:flex;flex-direction:column;gap:24px;">
      <span class="kicker">Dolen · pergunta direta</span>
      <h1 class="mega" style="font-size:80px;">Sua clínica<br/>ainda não tem<br/><span class="und">site</span>?</h1>
      <div class="rule"></div>
      <p class="support" style="font-size:31px;">(seu concorrente já tem)</p>
    </div>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — paciente pesquisa: foto lateral direita (celular), texto esquerda =====
render("lpc02_2_pesquisa", f"""
  <div class="foto fade-l" style="top:0;right:0;bottom:0;width:520px;"><img src="{FOTO_CELULAR}"/></div>
  <div class="block" style="left:96px;top:300px;width:540px;">
    <div class="icon-badge">{ICON_LUPA}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Comportamento do paciente</span>
    <h2 class="mega" style="font-size:56px;margin-top:16px;">O paciente pesquisa<br/>antes de ligar.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;">Antes do telefone tocar, ele já pesquisou seu nome — e o que encontra decide se liga ou não.</p>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — primeira impressao: tipografico puro (variacao, sem foto) =====
render("lpc02_3_impressao", f"""
  <span class="ghost" style="font-size:260px;top:130px;left:-40px;">CLIQUE</span>
  <div class="orbit" style="width:300px;height:300px;top:160px;right:-90px;"></div>
  <div class="block" style="left:96px;right:96px;bottom:200px;">
    <div class="icon-badge">{ICON_MONITOR}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Primeira impressão</span>
    <h2 class="mega" style="font-size:60px;margin-top:16px;">O site chega antes<br/>da recepção.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:760px;">É a primeira coisa que o paciente vê da sua clínica — antes de qualquer atendimento.</p>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — mockup do hero da Vitalis Saude, em janela de navegador =====
render("lpc02_4_mockup", f"""
  <span class="ghost" style="font-size:240px;top:120px;left:-40px;">EXEMPLO</span>
  <div class="browser" style="left:60px;width:960px;top:250px;">
    <div class="bar"><span class="dots"><i></i><i></i><i></i></span><span class="url">Exemplo · Vitalis Saúde</span></div>
    <div style="height:560px;overflow:hidden;"><img class="shot" src="{MOCK_SHOT}"/></div>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="kicker">Assim ficaria o site da sua clínica</span>
    <h2 class="mega" style="font-size:52px;margin-top:14px;">Um exemplo de como<br/>a Dolen pensaria.</h2>
    <div class="rule" style="margin-top:18px;"></div>
    <p class="support" style="font-size:29px;margin-top:18px;max-width:760px;">Mockup ilustrativo — não é um cliente real, é o padrão que aplicaríamos no seu.</p>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — FAQ: tipografico puro com icone de chat (variacao, sem foto) =====
render("lpc02_5_faq", f"""
  <span class="ghost" style="font-size:280px;bottom:200px;right:-50px;">FAQ</span>
  <div class="block" style="left:96px;right:96px;top:420px;">
    <div class="icon-badge">{ICON_CHAT}</div>
    <div style="height:26px;"></div>
    <span class="kicker">Menos WhatsApp repetido</span>
    <h2 class="mega" style="font-size:58px;margin-top:16px;">FAQ tira dúvida sem<br/>sobrecarregar sua equipe.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:740px;">Horário, convênio e endereço — já respondidos no site, antes mesmo de perguntarem.</p>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — CTA: tipografico puro, ghost text + orbita =====
render("lpc02_6_cta", f"""
  <span class="ghost" style="font-size:300px;top:150px;left:-50px;">CLÍNICA</span>
  <div class="orbit" style="width:360px;height:360px;top:120px;right:-110px;"></div>
  <div class="block" style="left:96px;right:96px;top:460px;">
    <h2 class="mega" style="font-size:64px;"><strong>Fala com a Dolen</strong><br/>sobre o site da<br/>sua clínica.</h2>
    <div class="rule" style="margin-top:24px;"></div>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="pill">Chama no direct</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">@dolen.ia</span>
  </div>
  {foot(6)}
""")

print("html ok — 6 slides gerados (lp-c02)")
