#!/bin/bash
# Mixagem final: voz+video (s1-r19-bora-colocar-no-ar.mp4) + musica de fundo (bem mais baixa) + SFX (whoosh/pop/chime)
set -e
FFMPEG="C:\Users\Claudia\AppData\Local\Programs\Python\Python314\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/Claudia/Herd/dolen-painel/artes/reels/s1-r19"

SPEECH_MASK="between(t,0.00,2.68)+between(t,2.68,4.88)+between(t,5.30,10.00)+between(t,10.54,11.74)+between(t,12.30,13.32)+between(t,13.70,14.70)+between(t,15.38,18.00)+between(t,18.66,21.54)+between(t,22.16,24.34)"

"$FFMPEG" -y \
  -i s1-r19-bora-colocar-no-ar.mp4 \
  -i "music/upbeat-success-cinematicsoul-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -i "sfx/chime.mp3" \
  -filter_complex "
[1:a]atrim=0:27.16,asetpts=PTS-STARTPTS[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.055,0.20)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=24.5:d=2.6[musfaded];

[2:a]volume=0.55,asplit=9[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8];
[wb0]adelay=2680|2680[wh0];
[wb1]adelay=5300|5300[wh1];
[wb2]adelay=10540|10540[wh2];
[wb3]adelay=12300|12300[wh3];
[wb4]adelay=13700|13700[wh4];
[wb5]adelay=15380|15380[wh5];
[wb6]adelay=18660|18660[wh6];
[wb7]adelay=22160|22160[wh7];
[wb8]adelay=24340|24340[wh8];

[3:a]volume=0.40,asplit=4[pb0][pb1][pb2][pb3];
[pb0]adelay=2680|2680[pop0];
[pb1]adelay=10540|10540[pop1];
[pb2]adelay=15380|15380[pop2];
[pb3]adelay=22860|22860[pop3];

[4:a]volume=0.32,adelay=24440|24440[chime0];

[0:a][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][pop0][pop1][pop2][pop3][chime0]amix=inputs=16:duration=longest:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -c:v copy -c:a aac -b:a 192k \
  "s1-r19-bora-colocar-no-ar-COM-MUSICA.mp4"

echo "OK"
