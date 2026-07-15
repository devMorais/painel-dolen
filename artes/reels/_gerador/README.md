# Gerador de Reels — Dolen

Pipeline pra montar Reels de portfólio (sites rolando + capa/overlay/card final em identidade Dolen).
Formato final: **1080×1920 (9:16, Reel tela cheia)**, ~13,6s, sem áudio (a trilha entra no Instagram).

## Como funciona (3 etapas)
1. **Capturar + traduzir os sites** (`translate.js`, via puppeteer-core dirigindo o Chrome local):
   carrega cada template do BootstrapMade, troca o texto pro português (dicionário GENERIC + PHRASES + HEROES)
   e salva `tpl_pt/<nome>.png` (1440×2800). Editar o objeto `TEMPLATES` pra trocar quais sites entram.
   ```
   npm install          # instala puppeteer-core (usa o Chrome já instalado)
   node translate.js
   ```
2. **Peças de marca** (renderizadas via Chrome headless → PNG):
   - `cover_c9.html`  → capa (fundo branco, "Um site pra cada profissão", círculos) — vira o 1º frame (capa do Reel)
   - `overlay_body9.html` → overlay fixo do corpo (logo + chamada "Criamos sites, landing pages e lojas")
   - `endcard9.html`  → card final preto ("Sites para todos os profissionais")
   ```
   chrome --headless=new --window-size=1080,1920 --screenshot=cover_c9.png   file://.../cover_c9.html
   chrome --headless=new --window-size=1080,1920 --screenshot=endcard9.png   file://.../endcard9.html
   chrome --headless=new --window-size=1080,1920 --default-background-color=00000000 --screenshot=overlay_body9.png file://.../overlay_body9.html
   ```
3. **Montar o vídeo** (`build_reel9.py`, PIL frame-a-frame + ffmpeg):
   janela de navegador com sombra, scroll do site inteiro, crossfade entre projetos, fade in/out.
   ```
   python build_reel9.py          # gera frames9/
   ffmpeg -framerate 30 -i frames9/fr_%04d.png -f lavfi -i anullsrc=r=44100:cl=stereo \
     -c:v libx264 -pix_fmt yuv420p -crf 20 -movflags +faststart -c:a aac -shortest reel.mp4
   ```
   ffmpeg usado: o bundled do `imageio-ffmpeg` (Python).

## Pra fazer um Reel novo
Trocar textos em `cover_c9.html` / `overlay_body9.html` / `endcard9.html`, escolher os sites em
`translate.js` e `build_reel9.py` (lista `TEMPLATES`), e rodar as 3 etapas. Regra: **Fernando aprova antes de publicar.**

## Zonas seguras do Reel (IMPORTANTE — feedback Fernando 2026-07-14)
A UI do Instagram cobre as bordas do Reel: **~250px topo**, **~480px rodapé** (nome, legenda, áudio, botões),
**~160px direita** (curtir/comentar/enviar). Manter texto/CTA/logo **centralizados no miolo**, nunca colados
nas bordas. No `reel-sites-profissoes.mp4` (v1) o rodapé (`dolen.com.br` / "Comece o seu") ficou parcialmente
coberto. Ajustar nos próximos: nas peças (`cover_c9.html`, `overlay_body9.html`, `endcard9.html`) subir os blocos
de texto pro centro (ex.: rodapé a ≥480px do fundo; nada importante à direita além de ~920px).

Fora do versionamento: `node_modules/`, `frames9/`, `tpl_pt/` (regeneráveis).
