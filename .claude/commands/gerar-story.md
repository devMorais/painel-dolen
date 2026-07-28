---
description: Gera um Story (Instagram) no padrão editorial da Dolen
---

# /gerar-story

Monta um Story (1080×1920, 9:16) no sistema visual já aprovado em `artes/stories-rotina`,
`artes/stories-servicos` e `artes/stories-trabalhos`: crop marks, grain, ghost text em outline,
halftone, vignette, tipografia Space Grotesk, zonas seguras do Instagram.

**Uso:** `/gerar-story <slug> "tema/roteiro do story"`

Exemplo: `/gerar-story s3-s08 "convite pra sexta-feira: agenda 2 horários de diagnóstico grátis"`

## Antes de começar

1. Confirme com o usuário: slug (`s3-sNN`, ver próximo número livre — Sprint 3 Stories, card no
   Avante id 411, rodízio semanal seg-dom), tema/roteiro, e se é story avulso ou parte de uma
   sequência (ex.: `stories-servicos` = 6 stories com preços, `stories-trabalhos` = 8 stories de
   portfólio capa→projetos→CTA).
2. **Nunca invente número/vaga/preço** — se o story mencionar dado variável (ex.: "restam N vagas
   de fundador"), confirmar o valor real com o usuário antes de escrever (ver
   `artes/stories-rotina/_gerador/build_s3s07.py`, que registra em comentário a data em que o
   número foi confirmado com o Fernando — seguir esse padrão).
3. Ver `[[dolen-design-workflow-ia]]`: se o story precisar de FOTO de fundo (não só tipografia),
   o Fernando gera o fundo na IA (Ideogram/Gemini) e entrega pronto — perguntar se já existe esse
   arquivo antes de assumir que precisa gerar um.

## Passo 1 — Scaffold

Criar `artes/stories-rotina/_gerador/build_<slug_sem_traco>.py` (ou pasta própria se for uma nova
série, ex. `artes/stories-<nome>/`) a partir do modelo `build_s3s07.py`. Reaproveitar sem alterar:
- `.story` (1080×1920), `GRAIN` (feTurbulence — textura de marca)
- `RM_STORY` (crop marks) — posicionados em `top:190px`/`bottom:270px`, já dentro da zona segura
- `.content { padding:240px 120px 320px }` — **essa é a zona segura real do Instagram**
  (~250px topo, ~480px rodapé incluindo espaço extra pro texto não ficar colado, ~160px direita).
  Não reduzir esse padding.
- `.ghost` (texto contorno gigante decorativo), `.halftone` (textura de pontos), `.orbit`
  (círculo decorativo), `.vignette` (escurece bordas pra legibilidade)
- `brand()` (logo + wordmark "dolen", `invert` quando fundo escuro)
- `.vagas-badge`/`.vagas-dots` se o story for de oferta/urgência com contagem (só usar com número
  real confirmado)
- `.pill` para CTA final (ex. "Link na bio")

## Passo 2 — Compor o story

- Fundo claro (`--paper`) ou escuro (`bg-black`) — não precisa seguir a intercalação do feed
  (essa regra é só pra carrosséis/posts do feed principal), mas evitar repetir o mesmo fundo do
  story anterior da mesma leva/dia se possível.
- 1 ideia central por story (stories são consumidos em ~5s, texto tem que bater de cara).
- `.mega` pro título/gancho, `.support` pra 1 frase de apoio, `.rule` como separador visual.
- CTA sempre presente: "Link na bio" (pill) e/ou "chama no direct — @dolen.ia".
- Se for parte de sequência (ex. stories-trabalhos), manter o MESMO sistema visual entre todos
  os stories da série (crop marks, grain, brand) pra parecer um conjunto coeso.

## Passo 3 — Renderizar HTML → PNG

```
python artes/stories-rotina/_gerador/build_<slug_sem_traco>.py

CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe"
"$CHROME" --headless=new --window-size=1080,1920 --force-device-scale-factor=1 \
  --screenshot="artes/stories-rotina/<slug>.png" --default-background-color=00000000 \
  "file:///C:/Users/UITEC/Herd/dolen-painel/artes/stories-rotina/_gerador/<slug>.html"
```

## Passo 4 — Entrega

Mostrar o PNG gerado e pedir aprovação antes de considerar pronto pra postar (regra do projeto:
toda arte é aprovada pelo Fernando antes de publicar).

## Aprendizados a aplicar sempre

- Zona segura do Story: nada de texto/CTA fora de `top:250px / bottom:480px / right:160px` —
  mesma regra já documentada pros Reels (feedback Fernando 2026-07-14), vale igual pra Stories.
- Números variáveis (vagas, prazo, desconto) só entram no story com confirmação explícita do
  Fernando, registrada em comentário no `.py` como no `s3s07` — nunca estimar ou repetir de memória.
- CTA final sempre com "Link na bio" + direct como alternativa.
