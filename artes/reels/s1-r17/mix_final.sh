#!/bin/bash
# Mixagem final: voz+video (s1-r17-antes-depois.mp4) + musica de fundo (bem mais baixa) + SFX (whoosh/pop/chime)
set -e
FFMPEG="C:\Users\Claudia\AppData\Local\Programs\Python\Python314\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/Claudia/Herd/dolen-painel/artes/reels/s1-r17"

SPEECH_MASK="between(t,0.00,4.00)+between(t,5.06,5.58)+between(t,6.20,9.84)+between(t,10.60,14.84)+between(t,15.26,17.76)+between(t,18.70,21.00)+between(t,21.70,25.24)+between(t,25.88,31.42)+between(t,32.06,34.02)+between(t,34.70,35.92)+between(t,36.46,37.14)"

"$FFMPEG" -y \
  -i s1-r17-antes-depois.mp4 \
  -i "music/tutorial-themountain-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -i "sfx/chime.mp3" \
  -filter_complex "
[1:a]atrim=0:39.96,asetpts=PTS-STARTPTS[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.055,0.20)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=37.2:d=2.7[musfaded];

[2:a]volume=0.55,asplit=11[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9][wb10];
[wb0]adelay=5060|5060[wh0];
[wb1]adelay=6200|6200[wh1];
[wb2]adelay=10600|10600[wh2];
[wb3]adelay=15260|15260[wh3];
[wb4]adelay=18700|18700[wh4];
[wb5]adelay=21700|21700[wh5];
[wb6]adelay=25880|25880[wh6];
[wb7]adelay=32060|32060[wh7];
[wb8]adelay=34700|34700[wh8];
[wb9]adelay=36460|36460[wh9];
[wb10]adelay=37140|37140[wh10];

[3:a]volume=0.40,asplit=4[pb0][pb1][pb2][pb3];
[pb0]adelay=5060|5060[pop0];
[pb1]adelay=6800|6800[pop1];
[pb2]adelay=19050|19050[pop2];
[pb3]adelay=27180|27180[pop3];

[4:a]volume=0.32,adelay=37240|37240[chime0];

[0:a][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][wh10][pop0][pop1][pop2][pop3][chime0]amix=inputs=18:duration=longest:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -c:v copy -c:a aac -b:a 192k \
  "s1-r17-antes-depois-COM-MUSICA.mp4"

echo "OK"
