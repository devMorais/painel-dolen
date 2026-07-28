# -*- coding: utf-8 -*-
"""[S2-C07] Carrossel "7 sinais de que você precisa de um site" — 9 slides, feed 1080x1350.
Fundo ESCURO (regra de intercalacao — o S2-C06 foi claro).

Conceito proprio: MEDIDOR DE SINAIS — 7 pontinhos no topo de cada slide, preenchendo
conforme avanca (reforca a mecanica "em quantos voce se reconheceu"). Numeral gigante do
sinal + icone linear tematico por cenario. Space Grotesk, mono, grao, ghost text variando."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"

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

.ghost{{position:absolute;font-weight:700;letter-spacing:-0.03em;line-height:0.82;z-index:0;color:transparent;-webkit-text-stroke:2px rgba(255,255,255,0.11);white-space:nowrap;}}
.orbit{{position:absolute;border-radius:50%;border:2px solid rgba(255,255,255,0.12);z-index:0;}}
.orbit::after{{content:"";position:absolute;width:15px;height:15px;border-radius:50%;top:-8px;left:50%;transform:translateX(-50%);background:rgba(255,255,255,0.3);}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.26;color:#fff;}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:38px;height:38px;filter:invert(1) brightness(2);}}
.brand .wm{{font-size:27px;font-weight:700;}}

/* medidor de 7 pontos no topo direito */
.medidor{{position:absolute;top:70px;right:96px;display:flex;gap:10px;z-index:20;}}
.m-dot{{width:16px;height:16px;border-radius:50%;border:2px solid rgba(255,255,255,0.28);}}
.m-dot.on{{background:#fff;border-color:#fff;}}

.icon-top{{position:absolute;top:150px;right:96px;z-index:15;color:#fff;opacity:0.9;}}
.icon-top svg{{width:84px;height:84px;}}

.block{{position:absolute;z-index:10;}}
.kicker{{font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.55;}}
.mega{{font-weight:700;letter-spacing:-0.03em;line-height:1.04;}}
.support{{font-weight:400;line-height:1.42;opacity:0.75;text-wrap:pretty;}}
.rule{{height:3px;width:110px;background:currentColor;opacity:0.85;}}
.und{{text-decoration:underline;text-underline-offset:0.1em;}}
.num-big{{font-size:200px;font-weight:700;letter-spacing:-0.04em;line-height:0.76;opacity:0.95;}}
.swipe{{display:flex;align-items:center;gap:14px;font-size:27px;font-weight:600;opacity:0.9;}}
.arrow{{font-size:36px;}}
.pill{{display:inline-flex;align-items:center;gap:14px;font-size:29px;font-weight:600;padding:20px 42px;border-radius:100px;background:#fff;color:var(--ink);}}
.pill svg{{width:28px;height:28px;}}
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.48;font-weight:600;letter-spacing:0.04em;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

# icones lineares (um por sinal)
IC_PERGUNTA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>'
IC_IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.6" cy="6.4" r="1" fill="currentColor" stroke="none"/></svg>'
IC_CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
IC_SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>'
IC_SHARE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.9 4M15.4 6.5l-6.8 4"/></svg>'
IC_IMG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>'
IC_STAR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'
IC_SEND = '<svg viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>'

SINAIS = [
    ("1", "Perguntas repetidas.", "Os clientes te perguntam as MESMAS coisas todo dia — horário, preço, endereço, como funciona.", "REPETE", IC_PERGUNTA),
    ("2", "Só o Instagram.", "O Instagram é a sua única vitrine — e você sabe que conta bloqueada é negócio parado.", "VITRINE", IC_IG),
    ("3", "Contato perdido.", "Você perde contato de gente que te procura fora do horário comercial.", "PERDIDO", IC_CLOCK),
    ("4", "Sumido no Google.", "O seu concorrente aparece no Google. Você não.", "SUMIDO", IC_SEARCH),
    ("5", "Só indicação.", "Você depende só de indicação pra crescer.", "BOCA A BOCA", IC_SHARE),
    ("6", "Preço por foto.", "Você manda tabela de preço por FOTO no WhatsApp.", "PRINT", IC_IMG),
    ("7", "Parece amador.", "O seu negócio é mais profissional do que ele PARECE na internet.", "IMAGEM", IC_STAR),
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


def foot(n, total=9):
    return f'<div class="foot">{n:02d} / {total:02d}</div>'


def medidor(preenchidos):
    dots = "".join(f'<span class="m-dot{" on" if i < preenchidos else ""}"></span>' for i in range(7))
    return f'<div class="medidor">{dots}</div>'


# ===== SLIDE 1 — CAPA =====
render("s2c07_1_capa", f"""
  <span class="ghost" style="font-size:300px;bottom:150px;left:-50px;">SINAIS</span>
  <div class="orbit" style="width:340px;height:340px;top:100px;right:-90px;"></div>
  <div class="block" style="left:96px;right:96px;top:230px;">
    <span class="kicker">Dolen · autoavaliação</span>
    <h1 class="mega" style="font-size:82px;margin-top:22px;">7 sinais de que<br/>o seu negócio<br/>está <span class="und">PRECISANDO</span><br/>de um site.</h1>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDES 2-8 — cada sinal =====
for i, (num, titulo, texto, ghost_word, icon) in enumerate(SINAIS):
    slide_n = i + 2
    lado = "right:-50px;" if i % 2 == 0 else "left:-50px;"
    render(f"s2c07_{slide_n}_sinal{num}", medidor(i + 1) + f"""
      <span class="ghost" style="font-size:230px;bottom:100px;{lado}">{ghost_word}</span>
      <div class="icon-top">{icon}</div>
      <div class="block" style="left:96px;right:96px;top:230px;">
        <span class="kicker">Sinal {num} de 7</span>
        <span class="num-big" style="display:block;margin-top:14px;">{num}</span>
        <h2 class="mega" style="font-size:58px;margin-top:20px;">{titulo}</h2>
        <div class="rule" style="margin-top:22px;"></div>
        <p class="support" style="font-size:31px;margin-top:22px;max-width:780px;">{texto}</p>
      </div>
      {foot(slide_n)}
    """)

# ===== SLIDE 9 — CTA =====
render("s2c07_9_cta", medidor(7) + f"""
  <span class="ghost" style="font-size:280px;top:150px;left:-50px;">DOLEN</span>
  <div class="block" style="left:96px;right:96px;top:260px;">
    <h2 class="mega" style="font-size:64px;">Se você se viu<br/>em 2 ou mais...<br/><span class="und">é o sinal.</span></h2>
    <div class="rule" style="margin-top:24px;"></div>
    <p class="support" style="font-size:32px;margin-top:24px;max-width:740px;">A gente coloca seu negócio no ar em dias, com painel pra você editar sozinho.</p>
  </div>
  <div class="block" style="left:96px;bottom:180px;">
    <span class="pill">{IC_SEND}Chama no direct</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">ou link na bio</span>
  </div>
  {foot(9)}
""")

print("html ok — 9 slides gerados")
