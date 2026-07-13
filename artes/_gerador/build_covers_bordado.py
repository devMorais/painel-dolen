import os

BASE = os.path.dirname(os.path.abspath(__file__))

CSS = """
*{box-sizing:border-box;margin:0;padding:0;}
html,body{width:100%;height:100%;overflow:hidden;}
.canvas{position:relative;width:1080px;height:1080px;display:flex;align-items:center;justify-content:center;}
.bg-black{background:#0a0a0a;}
.bg-white{background:#ffffff;}
.badge-icon{width:620px;height:620px;}
"""

# ícone: navegador (Trabalhos) — traço mais grosso, cantos redondos, estilo "linha de costura"
ICON_TRABALHOS = '<rect x="10" y="20" width="80" height="60" rx="7"/><path d="M10 35h80"/><circle cx="21" cy="27.5" r="2.1" fill="currentColor" stroke="none"/><circle cx="29" cy="27.5" r="2.1" fill="currentColor" stroke="none"/>'
# ícone: camadas (Serviços)
ICON_SERVICOS = '<path d="M50 14 14 32l36 18 36-18z"/><path d="M14 50l36 18 36-18"/><path d="M14 68l36 18 36-18"/>'


def badge(bg, fg, icon_path, dash_border, dash_icon):
    """Badge estilo bordado: borda dupla (tracejada + fina) + ícone grosso centralizado."""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="canvas {bg}">
  <svg width="1080" height="1080" viewBox="0 0 1080 1080">
    <circle cx="540" cy="540" r="486" fill="none" stroke="{fg}" stroke-width="7" stroke-dasharray="{dash_border}" stroke-linecap="round" opacity="0.92"/>
    <circle cx="540" cy="540" r="452" fill="none" stroke="{fg}" stroke-width="2.5" opacity="0.55"/>
    <g transform="translate(230,230) scale(6.2)" fill="none" stroke="{fg}" stroke-width="{dash_icon}" stroke-linecap="round" stroke-linejoin="round">
      {icon_path}
    </g>
  </svg>
</div>
</body></html>"""


jobs = [
    ("cover_1_trabalhos_v2", "bg-black", "#ffffff", ICON_TRABALHOS, "3 14", "1.55"),
    ("cover_2_servicos_v2", "bg-white", "#0a0a0a", ICON_SERVICOS, "3 14", "1.55"),
]

for name, bg, fg, icon, dash_b, dash_i in jobs:
    html = badge(bg, fg, icon, dash_b, dash_i)
    open(os.path.join(BASE, name + ".html"), "w", encoding="utf-8").write(html)

print("ok")
