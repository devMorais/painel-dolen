# -*- coding: utf-8 -*-
"""[S2-C05] Carrossel "Por dentro do painel proprio" — 6 slides, feed 1080x1350.
Fundo ESCURO (regra de intercalacao — o S2-C04 foi claro).

Cada slide mostra um MOCKUP fiel de uma tela real do painel Dolen (dashboard, editor de
texto, grade de midia, CRM de leads, form de publicacao) — o painel EXISTE de verdade,
entao mockup UI e' mais forte que foto de banco. Estilo: numeral gigante + icone linear no
canto + titulo + apoio + mockup. Space Grotesk, mono, grao. Variacao: capa e CTA diferentes."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GERADOR = r"C:\Users\UITEC\Herd\dolen-painel\artes\_gerador"
FONTFACE = open(os.path.join(GERADOR, "fontface.css"), encoding="utf-8").read()
LOGO = "file:///C:/Users/UITEC/Herd/dolen-painel/frontend/public/assets/images/dolen-icone-preto.png"

GRAIN = """<svg style="position:absolute;inset:0;width:100%;height:100%;z-index:50;pointer-events:none;opacity:0.45;mix-blend-mode:overlay;" xmlns='http://www.w3.org/2000/svg'>
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

.icon-top{{position:absolute;top:120px;right:96px;z-index:15;color:#fff;opacity:0.9;}}
.icon-top svg{{width:88px;height:88px;}}

.block{{position:absolute;z-index:10;}}
.kicker{{font-size:24px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;opacity:0.55;}}
.mega{{font-weight:700;letter-spacing:-0.03em;line-height:1.02;}}
.support{{font-weight:400;line-height:1.42;opacity:0.72;text-wrap:pretty;}}
.rule{{height:3px;width:110px;background:currentColor;opacity:0.85;}}
.und{{text-decoration:underline;text-underline-offset:0.1em;}}
.num-big{{font-size:150px;font-weight:700;letter-spacing:-0.04em;line-height:0.78;}}
.swipe{{display:flex;align-items:center;gap:14px;font-size:27px;font-weight:600;opacity:0.9;}}
.arrow{{font-size:36px;}}
.pill{{display:inline-flex;align-items:center;gap:14px;font-size:29px;font-weight:600;padding:20px 42px;border-radius:100px;border:2px solid #fff;color:#fff;}}
.pill svg{{width:28px;height:28px;}}
.foot{{position:absolute;left:96px;bottom:70px;z-index:10;font-size:24px;opacity:0.48;font-weight:600;letter-spacing:0.04em;}}

/* ---- mockups de UI (telas reais do painel) ---- */
.ui{{position:absolute;z-index:5;background:#151515;border:1px solid rgba(255,255,255,0.1);border-radius:22px;overflow:hidden;box-shadow:0 30px 80px -30px rgba(0,0,0,0.9);}}
.ui-bar{{display:flex;align-items:center;gap:12px;padding:20px 24px;border-bottom:1px solid rgba(255,255,255,0.07);}}
.ui-dot{{width:12px;height:12px;border-radius:50%;background:rgba(255,255,255,0.16);}}
.ui-brand{{margin-left:8px;font-size:22px;font-weight:700;opacity:0.85;}}
.ui-body{{padding:26px;}}
.lbl{{font-size:22px;opacity:0.5;margin-bottom:10px;}}
.field{{background:#1e1e1e;border:1px solid rgba(255,255,255,0.09);border-radius:12px;padding:20px;font-size:24px;opacity:0.85;margin-bottom:20px;line-height:1.4;}}
.btn-mock{{background:#fff;color:#111;border-radius:12px;padding:18px;text-align:center;font-size:24px;font-weight:600;}}
.btn-out{{border:1px solid rgba(255,255,255,0.2);border-radius:12px;padding:18px;text-align:center;font-size:24px;font-weight:600;opacity:0.85;}}
/* grade de midia */
.media-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px;}}
.media-cell{{aspect-ratio:1;background:#242424;border-radius:10px;background-size:cover;background-position:center;}}
/* tabela de leads */
.row{{display:flex;align-items:center;justify-content:space-between;padding:18px 0;border-bottom:1px solid rgba(255,255,255,0.06);font-size:23px;}}
.row .nm{{opacity:0.9;}}
.badge{{font-size:19px;padding:6px 16px;border-radius:100px;border:1px solid rgba(255,255,255,0.2);opacity:0.8;}}
.badge.f{{background:rgba(255,255,255,0.12);border-color:transparent;}}
/* dashboard stats */
.stats{{display:flex;gap:16px;margin-bottom:22px;}}
.stat{{flex:1;background:#1e1e1e;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:22px;}}
.stat .n{{font-size:52px;font-weight:700;}}
.stat .k{{font-size:20px;opacity:0.5;margin-top:4px;}}
.stat .up{{font-size:20px;opacity:0.6;margin-top:8px;}}
.chart{{height:120px;background:linear-gradient(180deg,rgba(255,255,255,0.08),transparent);border-radius:12px;position:relative;overflow:hidden;}}
.chart svg{{position:absolute;inset:0;width:100%;height:100%;}}
.nav-mini{{display:flex;flex-direction:column;gap:14px;font-size:20px;opacity:0.4;}}
.side{{display:flex;gap:26px;}}
"""

RM = '<span class="regmark" style="top:76px;left:70px;"></span><span class="regmark" style="top:76px;right:70px;"></span><span class="regmark" style="bottom:76px;left:70px;"></span><span class="regmark" style="bottom:76px;right:70px;"></span>'

IC_EDIT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>'
IC_CEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>'
IC_USERS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
IC_CAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><circle cx="12" cy="15" r="2.5"/></svg>'
IC_SEND = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>'


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


def icon_top(svg):
    return f'<div class="icon-top">{svg}</div>'


CHART_SVG = '<svg viewBox="0 0 400 120" preserveAspectRatio="none"><polyline points="0,90 50,80 100,85 150,60 200,65 250,40 300,45 350,25 400,20" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="3"/></svg>'


def ui_dashboard(style, compact=False):
    nav = '' if compact else '<div class="nav-mini"><span>Painel</span><span>Conteúdo</span><span>Mídia</span><span>Leads</span><span>Publicações</span></div>'
    return f"""<div class="ui" style="{style}">
      <div class="ui-bar"><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-brand">dolen · painel</span></div>
      <div class="ui-body"><div class="side">{nav}<div style="flex:1;">
        <div class="stats">
          <div class="stat"><div class="n">1.250</div><div class="k">Visitas do site</div><div class="up">+18%</div></div>
          <div class="stat"><div class="n">24</div><div class="k">Pedidos</div><div class="up">+20%</div></div>
        </div>
        <div class="chart">{CHART_SVG}</div>
      </div></div></div>
    </div>"""


# ===== SLIDE 1 — CAPA: titulo forte + mockup do dashboard =====
render("s2c05_1_capa",
    ui_dashboard("left:120px;right:-140px;bottom:-60px;height:560px;") + f"""
  <div class="block" style="left:96px;right:96px;top:170px;">
    <span class="kicker">Dolen · painel próprio</span>
    <h1 class="mega" style="font-size:74px;margin-top:22px;">O painel que<br/>devolve o<br/><span class="und">CONTROLE</span> do<br/>site pra você.</h1>
  </div>
  <div class="block" style="left:96px;bottom:110px;"><div class="swipe">Arraste <span class="arrow">&rarr;</span></div></div>
  {foot(1)}
""")

# ===== SLIDE 2 — 01 EDITE NA HORA (mockup editor de texto) =====
render("s2c05_2_item1", icon_top(IC_EDIT) + f"""
  <div class="block" style="left:96px;top:210px;">
    <span class="num-big">01</span>
    <h2 class="mega" style="font-size:52px;margin-top:16px;">EDITE NA HORA</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;">Textos, preços e avisos:<br/>você muda e já está no ar.<br/>Sem chamar programador.</p>
  </div>
  <div class="ui" style="left:120px;right:96px;bottom:120px;">
    <div class="ui-bar"><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-brand">Editar texto</span></div>
    <div class="ui-body">
      <div class="lbl">Título</div>
      <div class="field">Soluções que geram resultados para o seu negócio</div>
      <div class="btn-mock" style="width:260px;">Salvar alterações</div>
    </div>
  </div>
  {foot(2)}
""")

# ===== SLIDE 3 — 02 TROQUE FOTOS DO CELULAR (mockup grade de midia) =====
render("s2c05_3_item2", icon_top(IC_CEL) + f"""
  <div class="block" style="left:96px;top:210px;">
    <span class="num-big">02</span>
    <h2 class="mega" style="font-size:50px;margin-top:16px;">TROQUE FOTOS<br/>DO CELULAR</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;">Subiu produto novo?<br/>Foto nova no site em 2 minutos,<br/>de onde você estiver.</p>
  </div>
  <div class="ui" style="left:300px;right:96px;bottom:120px;">
    <div class="ui-bar"><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-brand">Mídia</span></div>
    <div class="ui-body">
      <div class="media-grid">
        <div class="media-cell"></div><div class="media-cell"></div><div class="media-cell"></div>
        <div class="media-cell"></div><div class="media-cell"></div><div class="media-cell"></div>
      </div>
      <div class="btn-mock">Enviar imagem</div>
    </div>
  </div>
  {foot(3)}
""")

# ===== SLIDE 4 — 03 CONTATOS ORGANIZADOS (mockup tabela de leads) =====
render("s2c05_4_item3", icon_top(IC_USERS) + f"""
  <div class="block" style="left:96px;top:210px;">
    <span class="num-big">03</span>
    <h2 class="mega" style="font-size:46px;margin-top:16px;">SEUS CONTATOS<br/>ORGANIZADOS</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:30px;margin-top:20px;max-width:820px;">Todo pedido de orçamento cai num quadro organizado — você vê quem chegou, responde e acompanha até fechar.</p>
  </div>
  <div class="ui" style="left:200px;right:96px;bottom:120px;">
    <div class="ui-bar"><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-brand">Pedidos de orçamento</span></div>
    <div class="ui-body" style="padding:12px 26px;">
      <div class="row"><span class="nm">Maria Silva</span><span class="badge f">Novo</span><span style="opacity:0.4;">12/05</span></div>
      <div class="row"><span class="nm">João Souza</span><span class="badge">Em atendimento</span><span style="opacity:0.4;">12/05</span></div>
      <div class="row"><span class="nm">Empresa ABC</span><span class="badge">Proposta enviada</span><span style="opacity:0.4;">11/05</span></div>
      <div class="row" style="border-bottom:none;"><span class="nm">Ana Martins</span><span class="badge">Fechado</span><span style="opacity:0.4;">10/05</span></div>
    </div>
  </div>
  {foot(4)}
""")

# ===== SLIDE 5 — 04 E TEM MAIS (mockup form de publicacao Instagram) =====
render("s2c05_5_item4", icon_top(IC_CAL) + f"""
  <div class="block" style="left:96px;top:210px;">
    <span class="num-big">04</span>
    <h2 class="mega" style="font-size:52px;margin-top:16px;">E TEM MAIS</h2>
    <div class="rule" style="margin-top:20px;"></div>
    <p class="support" style="font-size:31px;margin-top:20px;">Dá até pra programar<br/>publicações do Instagram por lá.<br/>Seu negócio digital num lugar só.</p>
  </div>
  <div class="ui" style="left:200px;right:96px;bottom:120px;">
    <div class="ui-bar"><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-dot"></span><span class="ui-brand">Nova publicação</span></div>
    <div class="ui-body">
      <div class="lbl">Texto da publicação</div>
      <div class="field">Novo projeto entregue! Mais um site no ar e pronto para gerar resultados.</div>
      <div style="display:flex;gap:16px;margin-bottom:20px;">
        <div style="flex:1;"><div class="lbl">Data</div><div class="field" style="margin:0;">20/07/2026</div></div>
        <div style="width:180px;"><div class="lbl">Hora</div><div class="field" style="margin:0;">10:00</div></div>
      </div>
      <div class="btn-mock">Agendar publicação</div>
    </div>
  </div>
  {foot(5)}
""")

# ===== SLIDE 6 — CTA (numeral 05 + texto, dashboard embaixo dissolvendo, botao) =====
render("s2c05_6_cta", f"""
  <span class="ghost" style="font-size:260px;top:130px;right:-60px;">PAINEL</span>
  <div class="block" style="left:96px;right:96px;top:200px;">
    <span class="num-big">05</span>
    <h2 class="mega" style="font-size:52px;margin-top:16px;">Todo site da Dolen<br/>já vem com esse painel.</h2>
    <div class="rule" style="margin-top:22px;"></div>
    <p class="support" style="font-size:31px;margin-top:22px;">Quer ver funcionando ao vivo?<br/>Chama no direct que a gente mostra.</p>
  </div>
  {ui_dashboard("left:96px;right:-200px;top:640px;height:340px;", compact=True)}
  <div class="block" style="left:96px;bottom:150px;">
    <span class="pill">{IC_SEND}CHAMA NO DIRECT</span>
  </div>
  {foot(6)}
""")

print("html ok — 6 slides gerados")
