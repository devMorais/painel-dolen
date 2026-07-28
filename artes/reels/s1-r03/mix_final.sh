#!/bin/bash
# Mixagem final S1-R03: video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/pop/chime)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r03"

SPEECH_MASK="between(t,0.87,2.81)+between(t,2.91,4.37)+between(t,4.72,6.08)+between(t,6.42,7.44)+between(t,8.25,11.92)+between(t,12.60,14.43)+between(t,14.76,17.38)+between(t,17.53,19.57)+between(t,20.24,22.09)+between(t,22.46,23.90)+between(t,24.73,25.63)+between(t,25.72,28.28)"

"$FFMPEG" -y \
  -i s1-r03-so-whatsapp.mp4 \
  -i "music/friendly-corporate-mood-royaltyfreemusicstudio-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -i "sfx/chime.mp3" \
  -filter_complex "
[1:a]atrim=0:32,asetpts=PTS-STARTPTS[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.05,0.19)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=29.3:d=2.0[musfaded];

[2:a]volume=0.55,asplit=9[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8];
[wb0]adelay=930|930[wh0];
[wb1]adelay=2970|2970[wh1];
[wb2]adelay=6480|6480[wh2];
[wb3]adelay=8310|8310[wh3];
[wb4]adelay=12660|12660[wh4];
[wb5]adelay=14820|14820[wh5];
[wb6]adelay=20300|20300[wh6];
[wb7]adelay=24790|24790[wh7];
[wb8]adelay=28220|28220[wh8];

[3:a]volume=0.36,asplit=7[pb0][pb1][pb2][pb3][pb4][pb5][pb6];
[pb0]adelay=4570|4570[pop0];
[pb1]adelay=8410|8410[pop1];
[pb2]adelay=8660|8660[pop2];
[pb3]adelay=14820|14820[pop3];
[pb4]adelay=16390|16390[pop4];
[pb5]adelay=17590|17590[pop5];
[pb6]adelay=26690|26690[pop6];

[4:a]volume=0.42[chime0];
[chime0]adelay=22520|22520[ch0];

[0:a][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][pop0][pop1][pop2][pop3][pop4][pop5][pop6][ch0]amix=inputs=19:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -c:v copy -c:a aac -b:a 192k \
  "s1-r03-so-whatsapp-FINAL.mp4"

echo "OK"
