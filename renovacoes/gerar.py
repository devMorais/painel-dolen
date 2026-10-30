#!/usr/bin/env python3
"""Monta o PDF de renovacao com o link de pagamento do cliente.

O HTML guarda o link como __LINK_PAGAMENTO__ em vez de cravado: o link da
InfinitePay so existe depois de criado la, e cada cobranca tem o seu. Assim
o mesmo HTML serve pra qualquer renovacao - troca o link e gera de novo.

  python gerar.py https://pay.infinitepay.io/...     -> PDF pronto pra enviar
  python gerar.py                                    -> PREVIA, sem link

A previa sai com outro nome pra nunca ser confundida com a versao final.
"""
import io
import pathlib
import subprocess
import sys

import segno

AQUI = pathlib.Path(__file__).parent
CHROME = pathlib.Path(
    "C:/Users/FernandoAguiardaCost/AppData/Local/Google/Chrome/Application/chrome.exe"
)

link = sys.argv[1] if len(sys.argv) > 1 else None
if link and not link.startswith("https://"):
    sys.exit(f"Link invalido (precisa comecar com https://): {link}")

html = (AQUI / "renovacao-miss.html").read_text(encoding="utf-8")

def qr_svg(url: str) -> str:
    """QR em SVG inline: vetorial, entao continua nitido impresso, e sem
    arquivo externo pra faltar quando o PDF sair daqui.

    error='l' de proposito: a URL da InfinitePay tem 254 caracteres e com
    correcao 'm' o simbolo ia a 65x65 modulos - a 32mm cada modulo ficaria
    com 0,49mm, no limite do que a camera de celular le. Com 'l' cai para
    57x57 (0,56mm por modulo)."""
    # segno escreve bytes mesmo em SVG, entao o buffer e BytesIO.
    buf = io.BytesIO()
    segno.make(url, error="l").save(
        buf, kind="svg", svgclass=None, lineclass=None,
        omitsize=True, xmldecl=False, svgns=True, border=0, dark="#0a0a0a",
    )
    return buf.getvalue().decode("utf-8")


if link:
    html = html.replace("__QR__", qr_svg(link))
    html = html.replace("__LINK_PAGAMENTO__", link)
    nome = "Dolen-Renovacao-Vote-pela-sua-Miss"
else:
    # Deixa evidente na propria pagina que ainda falta o link.
    html = html.replace("__QR__", '<div style="width:28mm;height:28mm;background:#e5e5e5"></div>')
    html = html.replace(
        'href="__LINK_PAGAMENTO__"', 'href="#" style="background:#8a8a8a"'
    ).replace(
        "__LINK_PAGAMENTO__", "[ LINK DE PAGAMENTO AINDA NAO INSERIDO ]"
    )
    nome = "PREVIA-renovacao-miss"

tmp = AQUI / f"_{nome}.html"
tmp.write_text(html, encoding="utf-8")
pdf = AQUI / f"{nome}.pdf"

subprocess.run([
    str(CHROME), "--headless=new", "--disable-gpu",
    "--no-pdf-header-footer",         # sem cabecalho "about:blank" do Chrome
    "--allow-file-access-from-files", # fonte e logo vem de file://
    "--virtual-time-budget=5000",     # espera a fonte carregar antes de imprimir
    f"--print-to-pdf={pdf}",
    tmp.as_uri(),
], check=True)

tmp.unlink()
print(f"OK: {pdf}  ({pdf.stat().st_size // 1024} KB)")
if not link:
    print("ATENCAO: previa sem link. Rode de novo passando o link pra versao final.")
