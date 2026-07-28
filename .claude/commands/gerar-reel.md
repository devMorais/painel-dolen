---
description: Gera um Reel 9:16 da Dolen (Sprint Marketing) a partir de um áudio gravado
---

# /gerar-reel

Monta um Reel completo (vídeo 1080×1920, identidade Dolen) a partir de um áudio já gravado
pela Claudia, seguindo o mesmo pipeline usado em `artes/reels/s1-r02` a `s1-r11`.

**Uso:** `/gerar-reel <slug> <caminho-do-audio.wav> ["roteiro ou tema opcional"]`

Exemplo: `/gerar-reel s1-r12 C:\Users\UITEC\Desktop\audio-claudia-r12.wav`

## Antes de começar

1. Confirme com o usuário: slug do reel (`sN-rNN`, ver próximo número livre em `artes/reels/`),
   caminho do áudio `.wav`/`.mp3`, e se há roteiro/tema já definido (ex.: card do Avante Sprint 1 Reels,
   id 380) ou se o texto deve ser transcrito do áudio puro.
2. **Nunca invente o texto falado** — ele vem do áudio real (via whisper) ou do roteiro que o usuário colar.
   Isso é regra do projeto (ver CLAUDE.md: nunca assumir conteúdo não explícito).

## Passo 1 — Scaffold da pasta

Criar `artes/reels/<slug>/` copiando a estrutura fixa de um reel existente (ex. `s1-r02`):
- `capture_frames.js` (idêntico entre todos os reels — copiar como está)
- `package.json` (`{"name":"reel-tpl","version":"1.0.0","private":true,"dependencies":{"puppeteer-core":"^23.11.1"}}`)
- Rodar `npm install` dentro da pasta nova (gera `node_modules/`, ignorado pelo git)

## Passo 2 — Transcrever o áudio com timestamps

```
python -c "
import whisper, json
m = whisper.load_model('small')
r = m.transcribe('<caminho-do-audio>', language='pt')
json.dump(r, open('artes/reels/<slug>/whisper_result.json','w'), ensure_ascii=False, indent=2)
print(r['text'])
for s in r['segments']: print(f\"{s['start']:.2f}-{s['end']:.2f}  {s['text']}\")
"
```

Copiar (ou linkar) o áudio para `artes/reels/<slug>/assets/audio-claudia.wav`.

Os `segments` (start/end de cada frase) são a base pra bater o timing das cenas do `timeline.html`
com a fala real — cada scene deve começar/terminar alinhada a uma pausa natural da fala, não no meio de uma frase.

## Passo 3 — Escrever `timeline.html`

Copiar a estrutura de `artes/reels/s1-r02/timeline.html` como modelo (é o mais representativo) e adaptar:

- **Formato fixo**: `1080×1920`, fundo alterna `bg-dark`/`bg-light` por cena (nunca duas cenas iguais seguidas).
- **Zona segura** (regra do projeto, `.safe`): `top:250px; bottom:480px; left/right:96px` — nada de texto/CTA
  fora disso (UI do Instagram cobre topo ~250px, rodapé ~480px, direita ~160px).
- **Fonte**: Space Grotesk, carregada de `file:///.../frontend/public/assets/fonts/space-grotesk-latin-ext.woff2`.
- **Logo**: `frontend/public/assets/images/logo-icon-black.png` no `.brandmini` (cena 2 em diante, opcional).
- **Efeitos disponíveis** (`FX` no script, reusar os nomes — não inventar novos sem necessidade):
  `fadeIn`, `slideUp`, `popIn`, `shakeHit` (hook de abertura), `stackUp` (listas), `cashStack` (ícones em fila),
  `lockShut`, `spin`. Cada elemento `.fx` tem `data-fx`, `data-delay` (segundos desde o início da cena),
  `data-dur`.
- **Cada `<div class="scene">`** tem `data-start`/`data-end` em segundos = os timestamps do whisper.
  Última cena (assinatura/CTA final) fica com tela preta pura (`id="s9"` no exemplo) — o sting de logo
  entra depois, direto no ffmpeg, não HTML.
- **Grain**: manter o bloco `.grain` (feTurbulence) igual em todos — é a textura de marca, não mexer.
- Roteirizar as cenas com o texto REAL do whisper/roteiro fornecido, nunca parafrasear o gancho principal.

Peça para o usuário revisar/aprovar o texto das cenas antes de renderizar (regra do projeto: toda arte
é aprovada pelo Fernando antes de publicar) — mas pode gerar o rascunho primeiro pra ele ver.

## Passo 4 — Capturar frames e montar vídeo com voz

```
cd artes/reels/<slug>
node capture_frames.js <duracao_total_em_segundos>   # gera frames/fr_0000.png ...

FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
"$FFMPEG" -y -framerate 30 -i frames/fr_%04d.png -i assets/audio-claudia.wav \
  -c:v libx264 -pix_fmt yuv420p -crf 20 -movflags +faststart -c:a aac -shortest \
  <slug>-<tema-curto>.mp4
```

## Passo 5 — Mixar música + SFX

Assets compartilhados já ficam em `artes/reels/_assets/music/` e `artes/reels/_assets/sfx/`
(whoosh, pop, marker, chime, typing, flipcard + 4 trilhas Pixabay já usadas). Preferir reusar um
desses antes de baixar algo novo — só baixar música nova do Pixabay se nenhuma das existentes couber
no clima do reel.

Copiar os 1-2 arquivos escolhidos pra `artes/reels/<slug>/music/` e `artes/reels/<slug>/sfx/`
(mantém cada reel autocontido pra reprodução futura, mesmo que o `.gitignore` não versione isso).

Escrever `mix_final.sh` adaptado de `artes/reels/s1-r02/mix_final.sh`:
- `SPEECH_MASK`: montar a partir dos `segments` do whisper (`between(t,start,end)+...`) — abaixa a música
  enquanto há fala (ducking), sobe nos silêncios.
- SFX pontuais (`whoosh`/`pop`/etc.) posicionados nos momentos de transição de cena (`adelay` em ms,
  usando os mesmos `data-start` das cenas do timeline.html).
- Música: `volume=eval=frame` com o mask, fade in/out nas pontas.
- Rodar o script e conferir que `<slug>-<tema>-COM-MUSICA.mp4` foi gerado.

## Passo 6 — Entregar

Mostrar ao usuário onde ficou o vídeo final (`artes/reels/<slug>/<slug>-...-COM-MUSICA.mp4`) e pedir
aprovação antes de considerar pronto pra postar (regra do projeto). Não fazer commit automaticamente —
perguntar se já deve versionar (o `.gitignore` já está configurado para aceitar só o script gerador +
o MP4 final "-COM-MUSICA", ignorando frames/node_modules/áudio bruto).

## Aprendizados a aplicar sempre (evoluir a cada reel)

- Zonas seguras: nunca colar texto/logo nos ~250px do topo, ~480px do rodapé, ~160px da direita.
- Alternar fundo claro/escuro cena a cena — nunca duas iguais seguidas.
- Timing de cena SEMPRE derivado do whisper real, nunca estimado a olho.
- Se o resultado ficar bom (boa sincronia SFX/fala, timing natural), registrar no CLAUDE.md o que
  funcionou, do mesmo jeito que a nota de zonas seguras de 2026-07-14 já está lá — assim o próximo
  reel sai melhor que o anterior.
