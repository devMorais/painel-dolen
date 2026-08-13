# -*- coding: utf-8 -*-
"""[LP-C07] Carrossel "O que é o Dolen Studio" — 6 slides, feed 1080x1350.
Fundo CLARO (regra de intercalacao — o LP-C06 foi escuro).

Pedido explicito do Fernando/Claudia: mais criatividade, fugir do template repetido
dos ultimos 5 carrosseis (hero em janela de navegador). Aqui o assunto e o proprio
servico da Dolen (nao um mockup de site de nicho), entao a linguagem visual muda pra
tres componentes novos, feitos em CSS/SVG puro (sem screenshot externo):
  - .phone  → mockup de celular com grade do Instagram (capa)
  - .cal    → mini calendario de conteudo com posts/reels marcados (slide 2)
  - .tl     → timeline de edicao de video (slide 3)

CORRIGIDO em 2026-08-13 apos achar o commit f43acc9 na main (Fernando, 01/08): o Studio
real tem DOIS niveis — Essencial (8 posts/mes) e Completo (Essencial + 4 Reels/mes), nao
uma oferta unica combinada como a v1 deste script sugeria. Envio de material e por um
link/portal dedicado (/enviar/{slug}), NAO WhatsApp. Studio e exclusivo pra quem ja e
cliente de site Dolen. Ainda sem preco em R$ no carrossel (evitar duplicar/errar valor
que ja existe no backend — quem decide o que citar publicamente e o Fernando na revisao)."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", "..", ".."))
GERADOR = os.path.join(REPO, "artes", "_gerador")
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///" + os.path.join(REPO, "frontend", "public", "assets", "images", "dolen-icone-preto.png").replace("\\", "/")

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

.icon-badge{{width:88px;height:88px;border-radius:50%;border:2px solid rgba(16,16,16,0.35);display:flex;align-items:center;justify-content:center;z-index:10;flex:none;}}
.icon-badge svg{{width:40px;height:40px;stroke:var(--ink);}}

.regmark{{position:absolute;width:30px;height:30px;z-index:6;opacity:0.28;color:#101010;}}
.regmark::before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:currentColor;transform:translateX(-50%);}}
.regmark::after{{content:"";position:absolute;top:50%;left:0;right:0;height:2px;background:currentColor;transform:translateY(-50%);}}

.brand{{display:flex;align-items:center;gap:14px;position:absolute;top:64px;left:96px;z-index:20;}}
.brand img{{width:40px;height:40px;}}
.brand .wm{{font-size:28px;font-weight:700;}}

.block{{position:absolute;z-index:10;}}
.kicker{{font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.5;}}
.mega{{font-weight:700;letter-spacing:-0.03em;line-height:1.0;}}
.support{{font-weight:400;line-height:1.42;opacity:0.72;text-wrap:pretty;}}
.rule{{height:3px;width:110px;background:currentColor;opacity:0.85;}}
.und{{text-decoration:underline;text-underline-offset:0.1em;}}

.swipe{{display:flex;align-items:center;gap:14px;font-size:27px;font-weight:600;opacity:0.9;}}
.arrow{{font-size:36px;}}
.pill{{display:inline-flex;font-size:29px;font-weight:600;padding:19px 40px;border-radius:100px;background:var(--ink);color:var(--paper);}}
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.4;font-weight:600;letter-spacing:0.04em;}}

/* ---- componente novo: celular com grade do Instagram ---- */
.phone{{position:absolute;width:320px;height:660px;background:var(--ink);border-radius:42px;padding:12px;box-shadow:0 40px 90px rgba(16,16,16,0.22);z-index:8;}}
.phone .screen{{width:100%;height:100%;background:#fff;border-radius:30px;overflow:hidden;position:relative;}}
.phone .notch{{position:absolute;top:0;left:50%;transform:translateX(-50%);width:110px;height:24px;background:var(--ink);border-radius:0 0 14px 14px;z-index:5;}}
.phone .igtop{{display:flex;align-items:center;gap:10px;padding:32px 16px 12px;}}
.phone .igtop .av{{width:32px;height:32px;border-radius:50%;background:#1a1a1a;}}
.phone .igtop .nm{{font-size:13px;font-weight:700;color:#1a1a1a;}}
.ig-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:2px;}}
.ig-grid .tile{{aspect-ratio:1/1;position:relative;}}
.ig-grid .tile svg{{position:absolute;top:7px;right:7px;width:14px;height:14px;stroke:#fff;fill:none;stroke-width:2;}}

/* ---- componente novo: mini calendario de conteudo ---- */
.cal{{width:660px;}}
.cal .row{{display:grid;grid-template-columns:repeat(7,1fr);gap:9px;}}
.cal .row + .row{{margin-top:9px;}}
.cal .day{{aspect-ratio:1/1;border-radius:9px;background:rgba(16,16,16,0.055);display:flex;align-items:center;justify-content:center;}}
.cal .day.post{{background:var(--ink);}}
.cal .day.post .dot{{width:8px;height:8px;border-radius:50%;background:#fff;}}
.cal .day.reel{{background:transparent;border:2px solid var(--ink);}}
.cal .day.reel svg{{width:14px;height:14px;stroke:var(--ink);fill:none;stroke-width:2;}}
.cal .legend{{display:flex;gap:32px;margin-top:22px;}}
.cal .legend span{{display:flex;align-items:center;gap:10px;font-size:22px;font-weight:600;opacity:0.7;}}
.cal .legend i{{width:16px;height:16px;border-radius:50%;display:inline-block;}}

/* ---- componente novo: timeline de edicao de video ---- */
.tl{{width:720px;}}
.tl .track{{height:74px;border-radius:14px;background:rgba(16,16,16,0.055);display:flex;gap:5px;padding:9px;}}
.tl .clip{{flex:1;border-radius:8px;background:rgba(16,16,16,0.14);}}
.tl .clip.active{{background:var(--ink);}}
.tl .head{{width:3px;height:96px;background:var(--ink);position:relative;margin-top:-11px;}}
.tl .head::before{{content:"";position:absolute;top:-8px;left:50%;transform:translateX(-50%);width:18px;height:18px;border-radius:50%;background:var(--ink);}}
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


PLAY = '<svg viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24"><path d="M9 12l2 2 4-4"/></svg>'
ICON_ROTEIRO = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.85 2.85 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5z"/></svg>'''
ICON_ARTE = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="13.5" cy="6.5" r=".5"/><circle cx="17.5" cy="10.5" r=".5"/><circle cx="8.5" cy="7.5" r=".5"/><circle cx="6.5" cy="12.5" r=".5"/><path d="M12 2a10 10 0 1 0 0 20 2 2 0 0 0 0-4h-1.5a2 2 0 0 1-2-2 2 2 0 0 1 2-2H15a5 5 0 0 0 5-5c0-4.4-3.6-7-8-7z"/></svg>'''
ICON_UPLOAD = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/></svg>'''
ICON_PUBLICAR = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4z"/></svg>'''


def ig_grid_tiles():
    # 9 tiles, 2 marcados como reel (play icon), tons variando pra parecer feed real
    tones = [0.92, 0.06, 0.4, 0.06, 0.7, 0.15, 0.5, 0.06, 0.25]
    reels = {1, 4, 7}
    out = ""
    for i, t in enumerate(tones):
        gray = int(255 * (1 - t)) if t < 0.5 else int(255 * (1 - t))
        bg = f"rgba(16,16,16,{t})"
        icon = PLAY if i in reels else ""
        out += f'<div class="tile" style="background:{bg};">{icon}</div>'
    return out


# ===== SLIDE 1 — CAPA: mockup de celular com grade do Instagram (composição nova) =====
render("lpc07_1_capa", f"""
  <div class="phone" style="right:-40px;top:210px;transform:rotate(4deg);">
    <div class="screen">
      <div class="notch"></div>
      <div class="igtop"><span class="av"></span><span class="nm">@dolen.ia</span></div>
      <div class="ig-grid">{ig_grid_tiles()}</div>
    </div>
  </div>
  <div class="block" style="left:96px;right:520px;top:230px;">
    <span class="kicker">Dolen Studio</span>
    <h1 class="mega" style="font-size:78px;margin-top:20px;">Site pronto<br/>é só o<br/><span class="und">começo</span>.</h1>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:29px;margin-top:22px;">O que mantém seu Instagram vivo depois?</p>
  </div>
  <div class="block" style="left:96px;bottom:70px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
""")

# ===== SLIDE 2 — publicacoes mensais: mini calendario de conteudo =====
# 4 semanas x 7 dias = 28 celulas; 8 posts + 4 reels marcados espalhados pelo mes
cells_list = []
posts = {1, 4, 8, 11, 15, 18, 22, 25}
reels = {3, 10, 17, 24}
for i in range(28):
    if i in posts:
        cells_list.append('<div class="day post"><span class="dot"></span></div>')
    elif i in reels:
        cells_list.append(f'<div class="day reel">{PLAY.replace(chr(34)+"#fff"+chr(34), chr(34)+"none"+chr(34))}</div>')
    else:
        cells_list.append('<div class="day"></div>')
CAL_ROWS = "".join(f'<div class="row">{"".join(cells_list[w*7:(w+1)*7])}</div>' for w in range(4))

render("lpc07_2_calendario", f"""
  <span class="ghost" style="font-size:280px;top:120px;left:-40px;">MENSAL</span>
  <div class="block" style="left:96px;right:96px;top:300px;">
    <span class="kicker">Publicações mensais</span>
    <h2 class="mega" style="font-size:56px;margin-top:16px;">Seu feed nunca<br/>fica parado.</h2>
  </div>
  <div class="block cal" style="left:96px;top:520px;">
    {CAL_ROWS}
    <div class="legend">
      <span><i style="background:var(--ink);"></i>Essencial: 8 posts/mês</span>
      <span><i style="background:transparent;border:2px solid var(--ink);"></i>Completo: +4 reels</span>
    </div>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — edicoes de video: timeline de edicao =====
render("lpc07_3_video", f"""
  <span class="ghost" style="font-size:260px;bottom:240px;right:-50px;">EDIÇÃO</span>
  <div class="block" style="left:96px;right:96px;top:340px;">
    <span class="kicker">Edições de vídeo</span>
    <h2 class="mega" style="font-size:58px;margin-top:16px;">Vídeo com corte,<br/>ritmo e trilha —<br/>profissional de verdade.</h2>
  </div>
  <div class="block tl" style="left:96px;top:700px;">
    <div class="track">
      <div class="clip active" style="flex:1.4;"></div>
      <div class="clip" style="flex:0.6;"></div>
      <div class="clip active" style="flex:1.8;"></div>
      <div class="clip" style="flex:0.9;"></div>
      <div class="clip active" style="flex:1.2;"></div>
    </div>
    <div class="head" style="margin-left:38%;"></div>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — artes e roteiro: dois icon-badges lado a lado (variacao) =====
render("lpc07_4_artes", f"""
  <div class="orbit" style="width:300px;height:300px;top:140px;right:-90px;"></div>
  <div class="block" style="left:96px;right:96px;top:300px;">
    <span class="kicker">Sem trabalho extra pra você</span>
    <h2 class="mega" style="font-size:58px;margin-top:16px;">Artes e roteiro<br/>já vêm inclusos.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:720px;">Você não escreve legenda, não pensa em arte — a gente cuida da ideia à publicação.</p>
  </div>
  <div class="block" style="left:96px;top:760px;display:flex;gap:28px;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:16px;">
      <div class="icon-badge">{ICON_ROTEIRO}</div>
      <span class="support" style="font-size:24px;font-weight:600;opacity:0.8;">Roteiro</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:16px;margin-left:40px;">
      <div class="icon-badge">{ICON_ARTE}</div>
      <span class="support" style="font-size:24px;font-weight:600;opacity:0.8;">Arte</span>
    </div>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — fluxo simples: voce envia -> a gente publica =====
render("lpc07_5_fluxo", f"""
  <span class="ghost" style="font-size:230px;top:130px;left:-40px;">SIMPLES</span>
  <div class="block" style="left:96px;right:96px;top:420px;">
    <span class="kicker">Como funciona</span>
    <h2 class="mega" style="font-size:56px;margin-top:16px;">Você envia o material.<br/>A gente publica.</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;max-width:720px;">Manda o material bruto por um link simples que a gente te passa — o resto (edição, arte, legenda, agenda) é com a gente.</p>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:180px;display:flex;align-items:center;gap:28px;">
    <div class="icon-badge">{ICON_UPLOAD}</div>
    <span class="support" style="font-size:40px;opacity:0.3;">→</span>
    <div class="icon-badge">{ICON_PUBLICAR}</div>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — CTA: tipografico puro, ghost text + orbita =====
render("lpc07_6_cta", f"""
  <span class="ghost" style="font-size:300px;top:150px;left:-50px;">STUDIO</span>
  <div class="orbit" style="width:360px;height:360px;top:120px;right:-110px;"></div>
  <div class="block" style="left:96px;right:96px;top:460px;">
    <h2 class="mega" style="font-size:60px;">Conheça os<br/><strong>planos do</strong><br/>Dolen Studio.</h2>
    <div class="rule" style="margin-top:24px;"></div>
  </div>
  <div class="block" style="left:96px;right:96px;bottom:150px;">
    <span class="pill">Link na bio</span>
    <span class="support" style="font-size:26px;opacity:0.6;margin-left:20px;">exclusivo pra clientes Dolen</span>
  </div>
  {foot(6)}
""")

print("html ok — 6 slides gerados (lp-c07)")
