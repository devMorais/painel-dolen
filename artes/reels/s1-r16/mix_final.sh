#!/bin/bash
# Mixagem final: voz+video (s1-r16-projeto-real.mp4) + musica de fundo (bem mais baixa) + SFX (whoosh/pop/chime)
set -e
FFMPEG="C:\Users\Claudia\AppData\Local\Programs\Python\Python314\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/Claudia/Herd/dolen-painel/artes/reels/s1-r16"

SPEECH_MASK="between(t,0.00,4.24)+between(t,5.02,8.66)+between(t,9.00,15.58)+between(t,15.96,17.82)+between(t,18.48,22.90)+between(t,23.74,26.90)+between(t,27.60,32.76)+between(t,33.34,34.64)+between(t,35.08,36.98)"

"$FFMPEG" -y \
  -i s1-r16-projeto-real.mp4 \
  -i "music/upbeat-success-cinematicsoul-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -i "sfx/chime.mp3" \
  -filter_complex "
[1:a]atrim=0:39.8,asetpts=PTS-STARTPTS[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.055,0.20)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=37.0:d=2.8[musfaded];

[2:a]volume=0.55,asplit=9[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8];
[wb0]adelay=5020|5020[wh0];
[wb1]adelay=9000|9000[wh1];
[wb2]adelay=15960|15960[wh2];
[wb3]adelay=18480|18480[wh3];
[wb4]adelay=23740|23740[wh4];
[wb5]adelay=27600|27600[wh5];
[wb6]adelay=33340|33340[wh6];
[wb7]adelay=35080|35080[wh7];
[wb8]adelay=36980|36980[wh8];

[3:a]volume=0.40,asplit=4[pb0][pb1][pb2][pb3];
[pb0]adelay=5520|5520[pop0];
[pb1]adelay=9900|9900[pop1];
[pb2]adelay=19380|19380[pop2];
[pb3]adelay=28500|28500[pop3];

[4:a]volume=0.32,adelay=37080|37080[chime0];

[0:a][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][pop0][pop1][pop2][pop3][chime0]amix=inputs=16:duration=longest:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -c:v copy -c:a aac -b:a 192k \
  "s1-r16-projeto-real-COM-MUSICA.mp4"

echo "OK"
