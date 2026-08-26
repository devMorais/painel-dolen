#!/bin/bash
# Mixagem final: voz+video (s1-r18-condicao-fundador.mp4) + musica de fundo (bem mais baixa) + SFX (whoosh/pop/chime)
set -e
FFMPEG="C:\Users\Claudia\AppData\Local\Programs\Python\Python314\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/Claudia/Herd/dolen-painel/artes/reels/s1-r18"

SPEECH_MASK="between(t,0.72,2.26)+between(t,2.54,3.90)+between(t,3.90,6.86)+between(t,6.86,11.04)+between(t,11.34,12.62)+between(t,12.62,16.60)+between(t,17.28,19.60)+between(t,20.16,22.92)+between(t,23.50,24.70)+between(t,25.16,27.22)"

"$FFMPEG" -y \
  -i s1-r18-condicao-fundador.mp4 \
  -i "music/friendly-corporate-mood-royaltyfreemusicstudio-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -i "sfx/chime.mp3" \
  -filter_complex "
[1:a]atrim=0:30.00,asetpts=PTS-STARTPTS[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.055,0.20)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=27.3:d=2.7[musfaded];

[2:a]volume=0.55,asplit=10[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9];
[wb0]adelay=2540|2540[wh0];
[wb1]adelay=3900|3900[wh1];
[wb2]adelay=6860|6860[wh2];
[wb3]adelay=11340|11340[wh3];
[wb4]adelay=12620|12620[wh4];
[wb5]adelay=17280|17280[wh5];
[wb6]adelay=20160|20160[wh6];
[wb7]adelay=23500|23500[wh7];
[wb8]adelay=25160|25160[wh8];
[wb9]adelay=27220|27220[wh9];

[3:a]volume=0.40,asplit=3[pb0][pb1][pb2];
[pb0]adelay=7960|7960[pop0];
[pb1]adelay=11340|11340[pop1];
[pb2]adelay=20860|20860[pop2];

[4:a]volume=0.32,adelay=27320|27320[chime0];

[0:a][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][pop0][pop1][pop2][chime0]amix=inputs=16:duration=longest:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -c:v copy -c:a aac -b:a 192k \
  "s1-r18-condicao-fundador-COM-MUSICA.mp4"

echo "OK"
