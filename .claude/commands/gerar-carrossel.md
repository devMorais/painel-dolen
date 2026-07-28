---
description: Gera um carrossel de feed (Instagram) no padrão editorial da Dolen
---

# /gerar-carrossel

Monta um carrossel de feed (slides 1080×1350, 4:5) no sistema visual já aprovado em
`artes/carrosseis-educativos/s2-c01` a `s2-c08`: crop marks, grain, logo, tipografia Space
Grotesk, foto que dissolve no fundo (mask-gradient, sem borda dura).

**Uso:** `/gerar-carrossel <slug> "tema/roteiro do carrossel"`

Exemplo: `/gerar-carrossel s2-c09 "5 sinais de que seu site está te fazendo perder clientes"`

## Antes de começar

1. Confirme com o usuário: slug (`s2-cNN`, ver próximo número livre em `artes/carrosseis-educativos/`),
   tema/roteiro (ou card do Avante Sprint 2 Carrosséis, id 402), quantidade de slides.
2. **Nunca invente dado/preço/afirmação não verificada** (regra do projeto — ver
   `[[no-unverified-claims]]`). Se o carrossel envolver números (preços, prazos), confirmar com o CLAUDE.md
   ("Modelo comercial") antes de escrever.
3. Checar `[[dolen-carrosseis-estilo]]`: foto dissolve no fundo, variação de composição POR SLIDE
   (não repetir o mesmo layout), texto em zona limpa.

## Passo 1 — Scaffold

Criar `artes/carrosseis-educativos/<slug>/build_<slug_sem_traco>.py` copiando a estrutura de
`s2-c01/build_s2c01.py` como modelo (é o mais completo: fade-b/fade-l/fade-r, ghost text, orbit,
num-erro). Reaproveitar:
- `CSS` base (`.canvas` 1080×1350, `.brand`, `.regmark` crop marks, `.foot` numerador `NN / total`)
- `GRAIN` (feTurbulence idêntico — textura de marca, não mexer)
- Fontface de `artes/_gerador/fontface.css` (Space Grotesk)
- Logo: `frontend/public/assets/images/dolen-icone-preto.png` (fundo claro) ou
  `logo-icon-white.png`/`dolen-icone-preto.png` com `filter:invert(1)` (fundo escuro)

Se o carrossel usa fotos (banco de imagens), criar `<slug>/fotos/` com as fotos brutas
baixadas (Pexels/Unsplash, mesma linha visual dos outros: candidato/laptop/código/relógio etc.)
e recortes finais (`final_*.jpg`) tratados no mesmo estilo (dissolve, P&B/duotone se aplicável).

## Passo 2 — Regra do feed: intercalar fundo

Verificar o ÚLTIMO carrossel/post publicado (ver nota no CLAUDE.md "Padrão do feed") e alternar:
se o anterior foi fundo escuro, este carrossel nasce fundo CLARO (`--paper`/`#ffffff`) e vice-versa.
Atualizar essa nota no CLAUDE.md depois de decidir.

## Passo 3 — Escrever os slides (`render(nome, inner)`)

Estrutura por slide (variar composição — não repetir o layout do slide anterior):
- **Capa** (slide 1): gancho forte, foto sangrando no topo ou tipografia pura com ghost text.
- **Conteúdo** (slides 2..N-1): 1 ideia por slide, `num-erro`/numeral grande OU ícone, título curto
  (`.mega`), 1 frase de apoio (`.support`). Composição alterna: foto topo / foto lateral esq / foto
  lateral dir / só tipografia — nunca duas seguidas iguais.
- **CTA** (último slide): sem foto, ghost text + orbit decorativo, texto convite + pill
  ("Chama no direct" ou equivalente), sempre com `.rule` acima do texto de apoio.
- Todo slide leva `foot(n, total)` no rodapé e os 4 `regmark` (crop marks) do `RM`.
- Zona de texto: manter dentro de `left/right:96px`, nada colado nas bordas do canvas.

## Passo 4 — Renderizar HTML → PNG

Rodar o script Python (gera os `.html`), depois screenshot de cada um via Chrome headless:

```
python artes/carrosseis-educativos/<slug>/build_<slug_sem_traco>.py

CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe"
cd artes/carrosseis-educativos/<slug>
for f in *.html; do
  "$CHROME" --headless=new --window-size=1080,1350 --force-device-scale-factor=1 \
    --screenshot="${f%.html}.png" --default-background-color=00000000 "file://$(pwd)/$f"
done
```

## Passo 5 — Legenda e entrega

Criar `<slug>/MIDIA-PRONTA/` com os PNGs finais renumerados (`01.png`, `02.png`, ...) e
`legenda.txt` (copy + hashtags, seguir o tom dos outros: pergunta de engajamento + CTA pro direct
+ hashtags locais/nicho). Mostrar ao usuário os PNGs gerados e pedir aprovação antes de considerar
pronto pra postar (regra do projeto: toda arte é aprovada pelo Fernando antes de publicar).

## Aprendizados a aplicar sempre (evoluir a cada carrossel)

- Fundo escuro/claro sempre intercalado com o post anterior do feed.
- Foto dissolve no fundo via `mask-image` gradient, nunca borda quadrada dura.
- Composição varia por slide E por carrossel — evitar template repetitivo entre S2-C01..C08.
- Se aparecer um padrão novo que funcionar bem, registrar em `[[dolen-carrosseis-estilo]]`
  (memória) e/ou no CLAUDE.md, do mesmo jeito que os erros rejeitados já estão documentados lá.
