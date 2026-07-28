#!/bin/bash
# Mixagem final: voz+sting (video) + musica de fundo (bem mais baixa) + SFX (whoosh/pop/marker)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r02"

SPEECH_MASK="between(t,1.19,5.13)+between(t,5.63,7.05)+between(t,7.44,8.50)+between(t,9.10,10.97)+between(t,11.37,14.11)+between(t,14.25,15.61)+between(t,16.26,17.65)+between(t,17.83,18.98)+between(t,19.63,21.52)+between(t,22.36,23.89)+between(t,24.48,27.39)+between(t,28.00,30.00)"

"$FFMPEG" -y \
  -i s1-r02-site-barato-sai-caro.mp4 \
  -i "music/upbeat-success-cinematicsoul-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -i "sfx/marker.mp3" \
  -filter_complex "
[1:a]atrim=0:33.5,asetpts=PTS-STARTPTS[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.055,0.20)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=30.3:d=2.5[musfaded];

[2:a]volume=0.55,asplit=9[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8];
[wb0]adelay=1250|1250[wh0];
[wb1]adelay=5690|5690[wh1];
[wb2]adelay=9160|9160[wh2];
[wb3]adelay=14310|14310[wh3];
[wb4]adelay=16320|16320[wh4];
[wb5]adelay=19690|19690[wh5];
[wb6]adelay=24540|24540[wh6];
[wb7]adelay=28060|28060[wh7];
[wb8]adelay=29940|29940[wh8];

[3:a]volume=0.38,asplit=3[pb0][pb1][pb2];
[pb0]adelay=9210|9210[pop0];
[pb1]adelay=11360|11360[pop1];
[pb2]adelay=13570|13570[pop2];

[4:a]volume=0.30,asplit=2[mb0][mb1];
[mb0]adelay=6650|6650[mk0];
[mb1]adelay=19690|19690[mk1];

[0:a][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][pop0][pop1][pop2][mk0][mk1]amix=inputs=16:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -c:v copy -c:a aac -b:a 192k \
  "s1-r02-site-barato-sai-caro-COM-MUSICA.mp4"

echo "OK"
