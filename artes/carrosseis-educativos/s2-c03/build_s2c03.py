# -*- coding: utf-8 -*-
"""[S2-C03] Carrossel "Checklist: seu site esta pronto pra vender?" — 8 slides, feed 1080x1350.
Fundo ESCURO (regra de intercalacao — o S2-C02 foi claro).

Estilo aprovado (foto dissolvendo no fundo via mask, variacao por slide) + estrutura da
referencia: numeral gigante (1-5), icone linear tematico no canto, mockup/foto onde faz
sentido, slides especiais (RESULTADO com check/x, CTA com botao). Space Grotesk, mono, grao."""
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
  <rect width='100%' height='100%' filter='url(#g)' opacity='0.5'/>
</svg>"""

BG = "#0b0b0b"

CSS = FONTFACE + f"""
:root{{--ink:#0a0a0a;--paper:#ffffff;--display:'Space Grotesk','Segoe UI',system-ui,sans-serif;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:100%;height:100%;overflow:hidden;}}
body{{font-family:var(--display);-webkit-font-smoothing:antialiased;}}
.canvas{{position:relative;overflow:hidden;isolation:isolate;background:{BG};color:var(--paper);width:1080px;height:1350px;}}

.foto{{position:absolute;z-index:1;overflow:hidden;}}
.foto img{{width:100%;height:100%;object-fit:cover;display:block;}}
.fade-b img{{-webkit-mask-image:linear-gradient(180deg, #000 42%, transparent 100%);}}
.fade-l img{{-webkit-mask-image:linear-gradient(270deg, #000 52%, transparent 100%);}}
.fade-t img{{-webkit-mask-image:linear-gradient(0deg, #000 45%, transparent 100%);}}

.ghost{{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:0;color:transparent;-webkit-text-stroke:2px rgba(255,255,255,0.12);white-space:nowrap;}}
.orbit{{position:absolute;border-radius:50%;border:2px solid rgba(255,255,255,0.13);z-index:0;}}
.orbit::after{{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);background:rgba(255,255,255,0.3);}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.26;color:#fff;}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:38px;height:38px;filter:invert(1) brightness(2);}}
.brand .wm{{font-size:27px;font-weight:700;}}

.icon-top{{position:absolute;top:120px;right:96px;z-index:15;color:#fff;opacity:0.92;}}
.icon-top svg{{width:96px;height:96px;}}

.block{{position:absolute;z-index:10;}}
.kicker{{font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.55;}}
.mega{{font-weight:700;letter-spacing:-0.03em;line-height:1.02;}}
.support{{font-weight:400;line-height:1.42;opacity:0.72;text-wrap:pretty;}}
.rule{{height:3px;width:110px;background:currentColor;opacity:0.85;}}
.und{{text-decoration:underline;text-underline-offset:0.1em;}}

.swipe{{display:flex;align-items:center;gap:14px;font-size:27px;font-weight:600;opacity:0.9;}}
.arrow{{font-size:36px;}}
.pill{{display:inline-flex;align-items:center;gap:14px;font-size:30px;font-weight:600;padding:22px 40px;border-radius:100px;border:2px solid #fff;color:#fff;}}
.pill.solid{{background:#fff;color:var(--ink);border-color:#fff;}}
.pill svg{{width:30px;height:30px;}}

.num-big{{font-size:180px;font-weight:700;letter-spacing:-0.04em;line-height:0.78;}}
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.48;font-weight:600;letter-spacing:0.04em;}}

/* mockups de UI (Google, painel) — desenhados, mais fieis que foto de banco */
.mock{{position:absolute;z-index:1;}}
.g-bar{{display:flex;align-items:center;gap:20px;background:#161616;border:1px solid rgba(255,255,255,0.14);border-radius:100px;padding:24px 34px;width:760px;}}
.g-bar .g-logo{{font-size:34px;font-weight:700;letter-spacing:-0.02em;opacity:0.9;}}
.g-bar .g-txt{{flex:1;font-size:28px;opacity:0.5;}}
.panel{{background:#141414;border:1px solid rgba(255,255,255,0.12);border-radius:20px;overflow:hidden;width:820px;}}
.panel-bar{{display:flex;gap:12px;padding:20px 24px;border-bottom:1px solid rgba(255,255,255,0.08);}}
.panel-dot{{width:14px;height:14px;border-radius:50%;background:rgba(255,255,255,0.18);}}
.panel-row{{display:flex;gap:16px;padding:22px 26px;font-size:26px;align-items:center;border-bottom:1px solid rgba(255,255,255,0.05);}}
.panel-row .k{{opacity:0.5;width:200px;}}
.panel-row .v{{flex:1;height:38px;background:rgba(255,255,255,0.07);border-radius:8px;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

# ---- icones lineares (stroke branco) ----
IC_VELOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 14l4-4"/><path d="M3.05 11a9 9 0 1 1 .5 4"/><circle cx="12" cy="14" r="1.4" fill="currentColor" stroke="none"/></svg>'
IC_CELULAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>'
IC_WPP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'
IC_LUPA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>'
IC_EDIT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>'
IC_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
IC_X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>'
IC_CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>'


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


def foot(n, total=8):
    return f'<div class="foot">{n:02d} / {total:02d}</div>'


def icon_top(svg):
    return f'<div class="icon-top">{svg}</div>'


# ===== SLIDE 1 — CAPA: titulo + mockup do site (laptop) dissolvendo embaixo =====
render("s2c03_1_capa",
    foto("final_laptop.jpg", "fade-t", "left:0;right:0;bottom:0;height:520px;") + f"""
  <div class="block" style="left:96px;right:96px;top:150px;">
    <h1 class="mega" style="font-size:76px;">CHECKLIST —<br/>seu site está<br/>pronto pra<br/><span class="und">VENDER?</span></h1>
    <div class="rule" style="margin-top:26px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;">Faça o teste.</p>
    <div class="swipe" style="margin-top:40px;">Arraste <span class="arrow">&rarr;</span></div>
  </div>
  {foot(1)}
""")

# ===== SLIDE 2 — 1 · velocidade (foto velocimetro dissolve pra cima) =====
render("s2c03_2_item1",
    foto("final_veloc.jpg", "fade-t", "left:0;right:0;bottom:0;height:640px;") + icon_top(IC_VELOC) + f"""
  <div class="block" style="left:96px;right:96px;top:230px;">
    <span class="num-big">1.</span>
    <h2 class="mega" style="font-size:56px;margin-top:20px;">Carrega rápido?</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:32px;margin-top:22px;">Mais de 3 segundos<br/>e o cliente já desistiu.</p>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — 2 · celular (foto lateral direita) =====
render("s2c03_3_item2",
    foto("final_celular.jpg", "fade-l", "top:0;right:0;bottom:0;width:600px;") + icon_top(IC_CELULAR) + f"""
  <div class="block" style="left:96px;top:270px;width:540px;">
    <span class="num-big">2.</span>
    <h2 class="mega" style="font-size:52px;margin-top:20px;">Funciona perfeito<br/>no celular?</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;">Abra agora e confira:<br/>nada cortado, nada minúsculo.</p>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — 3 · WhatsApp (icone + botao mockup, sem foto) =====
render("s2c03_4_item3", icon_top(IC_WPP) + f"""
  <div class="block" style="left:96px;right:96px;top:230px;">
    <span class="num-big">3.</span>
    <h2 class="mega" style="font-size:52px;margin-top:20px;">Tem botão de<br/>WhatsApp visível<br/>em TODAS as<br/>páginas?</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;">Falar com você tem<br/>que ser óbvio.</p>
  </div>
  <div class="block" style="right:96px;bottom:210px;">
    <span class="pill">{IC_WPP}Fale conosco</span>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — 4 · Google (mockup barra de busca) =====
render("s2c03_5_item4", icon_top(IC_LUPA) + f"""
  <div class="block" style="left:96px;right:96px;top:270px;">
    <span class="num-big">4.</span>
    <h2 class="mega" style="font-size:52px;margin-top:20px;">Aparece no Google<br/>quando buscam<br/>o seu serviço?</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;">Se não aparece,<br/>o concorrente aparece.</p>
    <div class="mock g-bar" style="margin-top:56px;position:relative;">
      <span class="g-logo">Google</span>
      <span class="g-txt">seu serviço aqui</span>
      {IC_LUPA.replace('width="1.6"','width="1.6" style="width:28px;height:28px;opacity:0.6;"')}
    </div>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — 5 · painel (mockup do painel) =====
render("s2c03_6_item5", icon_top(IC_EDIT) + f"""
  <div class="block" style="left:96px;right:96px;top:210px;">
    <span class="num-big">5.</span>
    <h2 class="mega" style="font-size:50px;margin-top:18px;">Você consegue<br/>atualizar preço, foto<br/>e texto SOZINHO?</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;">Sem depender de ninguém?</p>
  </div>
  <div class="mock panel" style="left:96px;bottom:150px;">
    <div class="panel-bar"><span class="panel-dot"></span><span class="panel-dot"></span><span class="panel-dot"></span></div>
    <div class="panel-row"><span class="k">Título</span><span class="v"></span></div>
    <div class="panel-row"><span class="k">Preço</span><span class="v"></span></div>
    <div class="panel-row"><span class="k">Foto</span><span class="v"></span></div>
  </div>
  {foot(6)}
""")

# ===== SLIDE 7 — RESULTADO (check / x) =====
render("s2c03_7_resultado", f"""
  <span class="ghost" style="font-size:260px;bottom:120px;right:-60px;">5/5</span>
  <div class="block" style="left:96px;top:180px;">
    <h2 class="mega" style="font-size:70px;">RESULTADO</h2>
  </div>
  <div class="block" style="left:96px;right:96px;top:420px;">
    <div style="display:flex;align-items:flex-start;gap:32px;margin-bottom:60px;">
      <div style="width:110px;height:110px;border-radius:50%;border:2.5px solid #fff;display:flex;align-items:center;justify-content:center;flex:none;color:#fff;"><span style="width:52px;height:52px;">{IC_CHECK}</span></div>
      <div>
        <h3 class="mega" style="font-size:46px;">Marcou tudo?</h3>
        <p class="support" style="font-size:31px;margin-top:12px;">Parabéns,<br/>seu site vende.</p>
      </div>
    </div>
    <div style="display:flex;align-items:flex-start;gap:32px;">
      <div style="width:110px;height:110px;border-radius:50%;border:2.5px solid #fff;display:flex;align-items:center;justify-content:center;flex:none;color:#fff;"><span style="width:48px;height:48px;">{IC_X}</span></div>
      <div>
        <h3 class="mega" style="font-size:46px;">Faltou algum?</h3>
        <p class="support" style="font-size:31px;margin-top:12px;">Cada item desses<br/>é venda escapando.</p>
      </div>
    </div>
  </div>
  {foot(7)}
""")

# ===== SLIDE 8 — CTA =====
render("s2c03_8_cta", f"""
  <span class="ghost" style="font-size:300px;bottom:200px;right:-60px;">PAINEL</span>
  <div class="orbit" style="width:340px;height:340px;top:140px;left:-90px;"></div>
  <div class="block" style="left:96px;right:96px;top:360px;">
    <h2 class="mega" style="font-size:66px;">A gente<br/>resolve os 5 —</h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:33px;margin-top:24px;max-width:720px;">com painel próprio pra você nunca mais depender de programador.</p>
  </div>
  <div class="block" style="left:96px;bottom:200px;">
    <span class="pill solid">{IC_CHAT}CHAMA NO DIRECT</span>
  </div>
  {foot(8)}
""")

print("html ok — 8 slides gerados")
