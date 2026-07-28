#!/bin/bash
# Mixagem final S1-R09: video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/pop)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r09"

SPEECH_MASK="between(t,0.85,5.27)+between(t,5.54,6.76)+between(t,7.19,8.18)+between(t,8.58,9.53)+between(t,10.12,11.90)+between(t,12.32,16.16)+between(t,16.68,17.20)+between(t,17.53,20.88)+between(t,21.27,23.48)+between(t,23.81,25.13)+between(t,25.66,26.90)+between(t,27.30,28.16)+between(t,28.57,29.79)"

CUT=29.90

"$FFMPEG" -y \
  -i s1-r09-base.mp4 \
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

[4:a]volume=0.5,aformat=channel_layouts=stereo,asplit=14[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9][wb10][wb11][wb12][wb13];
[wb0]adelay=850|850[wh0];
[wb1]adelay=2630|2630[wh1];
[wb2]adelay=4150|4150[wh2];
[wb3]adelay=5570|5570[wh3];
[wb4]adelay=7040|7040[wh4];
[wb5]adelay=9850|9850[wh5];
[wb6]adelay=12180|12180[wh6];
[wb7]adelay=16690|16690[wh7];
[wb8]adelay=18420|18420[wh8];
[wb9]adelay=19820|19820[wh9];
[wb10]adelay=21230|21230[wh10];
[wb11]adelay=23680|23680[wh11];
[wb12]adelay=25420|25420[wh12];
[wb13]adelay=28160|28160[wh13];

[5:a]volume=0.32,aformat=channel_layouts=stereo,asplit=13[pb0][pb1][pb2][pb3][pb4][pb5][pb6][pb7][pb8][pb9][pb10][pb11][pb12];
[pb0]adelay=1400|1400[pop0];
[pb1]adelay=2630|2630[pop1];
[pb2]adelay=4150|4150[pop2];
[pb3]adelay=5850|5850[pop3];
[pb4]adelay=7040|7040[pop4];
[pb5]adelay=9850|9850[pop5];
[pb6]adelay=14080|14080[pop6];
[pb7]adelay=17240|17240[pop7];
[pb8]adelay=18420|18420[pop8];
[pb9]adelay=22380|22380[pop9];
[pb10]adelay=23830|23830[pop10];
[pb11]adelay=25420|25420[pop11];
[pb12]adelay=28160|28160[pop12];

[voice][stinga][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][wh10][wh11][wh12][wh13][pop0][pop1][pop2][pop3][pop4][pop5][pop6][pop7][pop8][pop9][pop10][pop11][pop12]amix=inputs=30:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -t 32.9 -c:v copy -c:a aac -b:a 192k \
  "s1-r09-voce-edita-sozinho-COM-MUSICA.mp4"

echo "OK"
