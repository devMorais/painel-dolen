#!/bin/bash
# Mixagem final S1-R11: video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/pop)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r11"

SPEECH_MASK="between(t,0.74,7.44)+between(t,8.66,13.35)+between(t,13.89,15.30)+between(t,15.69,16.28)+between(t,16.55,17.66)+between(t,17.98,19.15)+between(t,19.55,22.58)+between(t,23.07,25.08)+between(t,25.37,26.41)+between(t,26.87,28.34)+between(t,28.76,29.64)"

CUT=29.90

"$FFMPEG" -y \
  -i s1-r11-base.mp4 \
  -i "assets/audio-claudia.wav" \
  -i "assets/logo-sting-dark.mp4" \
  -i "music/tutorial-themountain-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -filter_complex "
[1:a]atrim=0:${CUT},asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[voice];
[2:a]asetpts=PTS-STARTPTS+${CUT}/TB,volume=0.9,aformat=channel_layouts=stereo[stinga];

[3:a]atrim=0:33.0,asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.05,0.18)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=${CUT}:d=1.5[musfaded];

[4:a]volume=0.5,aformat=channel_layouts=stereo,asplit=17[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9][wb10][wb11][wb12][wb13][wb14][wb15][wb16];
[wb0]adelay=740|740[wh0];
[wb1]adelay=2260|2260[wh1];
[wb2]adelay=3530|3530[wh2];
[wb3]adelay=4780|4780[wh3];
[wb4]adelay=6240|6240[wh4];
[wb5]adelay=8180|8180[wh5];
[wb6]adelay=10850|10850[wh6];
[wb7]adelay=12140|12140[wh7];
[wb8]adelay=13720|13720[wh8];
[wb9]adelay=15660|15660[wh9];
[wb10]adelay=16420|16420[wh10];
[wb11]adelay=19450|19450[wh11];
[wb12]adelay=20960|20960[wh12];
[wb13]adelay=22840|22840[wh13];
[wb14]adelay=25120|25120[wh14];
[wb15]adelay=26460|26460[wh15];
[wb16]adelay=28700|28700[wh16];

[5:a]volume=0.32,aformat=channel_layouts=stereo,asplit=12[pb0][pb1][pb2][pb3][pb4][pb5][pb6][pb7][pb8][pb9][pb10][pb11];
[pb0]adelay=2260|2260[pop0];
[pb1]adelay=3530|3530[pop1];
[pb2]adelay=6790|6790[pop2];
[pb3]adelay=8180|8180[pop3];
[pb4]adelay=8530|8530[pop4];
[pb5]adelay=8880|8880[pop5];
[pb6]adelay=10850|10850[pop6];
[pb7]adelay=12140|12140[pop7];
[pb8]adelay=13720|13720[pop8];
[pb9]adelay=19450|19450[pop9];
[pb10]adelay=22840|22840[pop10];
[pb11]adelay=26460|26460[pop11];

[voice][stinga][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][wh10][wh11][wh12][wh13][wh14][wh15][wh16][pop0][pop1][pop2][pop3][pop4][pop5][pop6][pop7][pop8][pop9][pop10][pop11]amix=inputs=32:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -t 32.9 -c:v copy -c:a aac -b:a 192k \
  "s1-r11-codigo-de-verdade-COM-MUSICA.mp4"

echo "OK"
