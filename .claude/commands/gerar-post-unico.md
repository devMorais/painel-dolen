---
description: Gera um post único de feed (frase-manifesto) no padrão editorial da Dolen
---

# /gerar-post-unico

Monta um post único de feed (1080×1350, 4:5) no padrão de `artes/posts-unicos/s4-p01` a `s4-p08`:
frase-manifesto curta, fundo com foto tratada (duotone/P&B + grão) ou cor sólida, tipografia
Space Grotesk Bold + destaque em Playfair Display Italic sublinhado.

**Uso:** `/gerar-post-unico <slug> "frase-manifesto"`

Exemplo: `/gerar-post-unico s4-p09 "Seu cliente não espera. Seu site também não deveria."`

## Antes de começar

Confirme com o usuário: slug (`s4-pNN`, ver próximo número livre em `artes/posts-unicos/`), a
frase exata (regra do projeto: nunca parafrasear/inventar a frase-manifesto — ela deve vir do
roteiro/card do Avante Sprint 4 Posts, id 419, ou ser fornecida literalmente pelo usuário), e se
já existe um `bg.png` pronto (fundo tratado no Photoshop) ou se o fundo é só cor sólida via CSS.

## Passo 1 — Regra do feed: intercalar fundo

Mesma regra dos carrosséis: verificar o último post publicado no CLAUDE.md ("Padrão do feed") e
alternar claro/escuro com o anterior.

## Passo 2 — Scaffold

Criar `artes/posts-unicos/<slug>/build_<slug_sem_traco>.py` a partir do modelo `s4-p01`
(mais completo — usa `bg.png` + Playfair) ou `s4-p03` (mais simples — só CSS, sem imagem de fundo,
ver esse arquivo se a frase pedir fundo liso). Reaproveitar:
- `.canvas` 1080×1350, `regmark` (crop marks), `.brand` (logo + wordmark "dolen")
- `GRAIN` (feTurbulence — textura de marca, idêntica em todo post)
- `.line` (Space Grotesk Bold, a frase principal) + destaque opcional em `.tambem`
  (Playfair Display Italic sublinhado — usar pra UMA palavra-chave da frase, não a frase toda)
- `.foot` = "DOLEN · SITES PROFISSIONAIS" (rodapé fixo)
- Se usar foto de fundo: `.scrim` (gradient escurecendo pra legibilidade do texto) por cima da `.bg`

Se precisar de fundo tratado (grid de fotos duotone etc.), esse preparo é feito fora do Claude
(Photoshop, pelo Fernando) — perguntar se já existe um `bg.png` pronto antes de assumir que precisa
gerar um.

## Passo 3 — Composição da frase

- 1 frase curta, 2 linhas no máximo, quebrada com bom senso editorial (`<br/>` nos pontos certos).
- Destaque de UMA palavra em Playfair itálico sublinhado — a palavra que carrega a virada de
  sentido da frase (ex.: "também", "sério" no s4-p01).
- Texto sempre dentro de `left:96px; right:120px`, nunca colado nas bordas.
- `.rule` (linha de 110px) abaixo do bloco de texto como assinatura visual.

## Passo 4 — Renderizar HTML → PNG

```
python artes/posts-unicos/<slug>/build_<slug_sem_traco>.py

CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe"
cd artes/posts-unicos/<slug>
"$CHROME" --headless=new --window-size=1080,1350 --force-device-scale-factor=1 \
  --screenshot="<slug>.png" --default-background-color=00000000 "file://$(pwd)/<slug>.html"
```

## Passo 5 — Entrega

Mostrar o PNG gerado e pedir aprovação antes de considerar pronto pra postar (regra do projeto:
toda arte é aprovada pelo Fernando antes de publicar). Perguntar se quer legenda também
(mesmo estilo dos carrosséis: pergunta de engajamento + CTA + hashtags).

## Aprendizados a aplicar sempre

- Fundo escuro/claro sempre intercalado com o post anterior do feed.
- Frase nunca inventada — vem do roteiro/card ou do que o usuário mandar literalmente.
- 1 palavra de destaque em Playfair itálico, não mais que isso (senão perde força).
