# -*- coding: utf-8 -*-
"""[S2-C06] Carrossel "Como funciona trabalhar com a gente" — 6 slides, feed 1080x1350.
Fundo BRANCO (regra de intercalacao — o S2-C05 foi escuro).

Conceito proprio (nao repete mockup-UI do C05 nem foto-dissolvendo dos anteriores):
TRILHA DE PROGRESSO vertical com 4 pontos (Conversa -> Proposta -> Construcao -> No ar),
o passo atual preenchido e os demais em contorno — reforca visualmente "onde voce esta".
Cada passo tem icone linear proprio. Space Grotesk, mono, grao."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"

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

/* ---- trilha de progresso vertical ---- */
.trilha{{position:absolute;left:96px;top:290px;display:flex;flex-direction:column;gap:0;z-index:10;}}
.t-item{{display:flex;align-items:flex-start;gap:26px;position:relative;padding-bottom:56px;}}
.t-item:last-child{{padding-bottom:0;}}
.t-line{{position:absolute;left:29px;top:60px;bottom:0;width:2px;background:rgba(16,16,16,0.15);}}
.t-item.done .t-line{{background:var(--ink);}}
.t-dot{{width:60px;height:60px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;border:2.5px solid rgba(16,16,16,0.25);position:relative;z-index:2;background:var(--paper);}}
.t-dot svg{{width:26px;height:26px;opacity:0.4;}}
.t-item.active .t-dot{{border-color:var(--ink);background:var(--ink);}}
.t-item.active .t-dot svg{{opacity:1;stroke:#fff;}}
.t-item.done .t-dot{{border-color:var(--ink);}}
.t-item.done .t-dot svg{{opacity:0.85;}}
.t-txt{{padding-top:8px;}}
.t-num{{font-size:22px;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;opacity:0.4;}}
.t-item.active .t-num{{opacity:0.8;}}
.t-name{{font-size:30px;font-weight:700;margin-top:4px;}}
.t-item.active .t-name{{font-size:36px;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

IC_CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>'
IC_DOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/></svg>'
IC_TOOL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
IC_ROCKET = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>'
IC_SEND = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>'

PASSOS = [
    ("Passo 01", "Conversa", IC_CHAT),
    ("Passo 02", "Proposta clara", IC_DOC),
    ("Passo 03", "Construção", IC_TOOL),
    ("Passo 04", "No ar em dias", IC_ROCKET),
]


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


def trilha(ativo_idx, top="290px"):
    """desenha a trilha completa dos 4 passos; done = antes do ativo, active = o atual."""
    items = []
    for i, (tag, nome, icon) in enumerate(PASSOS):
        cls = "t-item"
        if i < ativo_idx:
            cls += " done"
        elif i == ativo_idx:
            cls += " active"
        line = '<div class="t-line"></div>' if i < len(PASSOS) - 1 else ''
        items.append(f"""<div class="{cls}">{line}
          <div class="t-dot">{icon}</div>
          <div class="t-txt"><div class="t-num">{tag}</div><div class="t-name">{nome}</div></div>
        </div>""")
    return f'<div class="trilha" style="top:{top};">{"".join(items)}</div>'


# ===== SLIDE 1 — CAPA: titulo + trilha completa (visao geral do processo) =====
render("s2c06_1_capa", f"""
  <div class="block" style="left:96px;right:96px;top:170px;">
    <span class="kicker">Dolen · como trabalhamos</span>
    <h1 class="mega" style="font-size:74px;margin-top:22px;">Do primeiro oi<br/>ao site <span class="und">no ar</span>.</h1>
    <p class="support" style="font-size:31px;margin-top:20px;">Veja como funciona.</p>
  </div>
  {trilha(-1, top="620px")}
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDES 2-5 — cada PASSO com a trilha destacando o atual =====
TEXTOS = [
    ("Você conta o que precisa e a gente entende o seu momento.", "Sem compromisso, sem tecniquês."),
    ("Escopo, prazo e valor num documento simples.", "Sem letra miúda, sem surpresa depois."),
    ("A gente monta e você acompanha.", "Ajustes fazem parte — o site tem que ter a SUA cara."),
    ("Site publicado, painel configurado e você treinado pra editar sozinho.", "Aí é só vender."),
]

for i, ((tag, nome, icon), (linha1, linha2)) in enumerate(zip(PASSOS, TEXTOS)):
    slide_n = i + 2
    render(f"s2c06_{slide_n}_passo{i+1}", f"""
      {trilha(i)}
      <div class="block" style="left:96px;right:96px;bottom:150px;">
        <div class="rule" style="margin-bottom:22px;"></div>
        <p class="support" style="font-size:31px;max-width:820px;">{linha1}<br/><span style="opacity:0.55;">{linha2}</span></p>
      </div>
      {foot(slide_n)}
    """)

# ===== SLIDE 6 — CTA =====
render("s2c06_6_cta", f"""
  <span class="ghost" style="font-size:280px;top:150px;left:-50px;">BORA</span>
  <div class="orbit" style="width:340px;height:340px;top:120px;right:-90px;"></div>
  <div class="block" style="left:96px;right:96px;top:400px;">
    <h2 class="mega" style="font-size:64px;">Simples assim,<br/>do jeito que<br/>deveria ser.</h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:720px;">Bora dar o passo 1?</p>
  </div>
  <div class="block" style="left:96px;bottom:200px;">
    <span class="pill">{IC_SEND}Chama no direct</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">a conversa é grátis</span>
  </div>
  {foot(6)}
""")

print("html ok — 6 slides gerados")
