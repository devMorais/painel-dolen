#!/bin/bash
# Mixagem final S1-R08: video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/pop)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r08"

SPEECH_MASK="between(t,1.12,5.03)+between(t,5.46,6.43)+between(t,6.96,10.35)+between(t,10.84,12.39)+between(t,12.65,14.95)+between(t,15.44,20.27)+between(t,20.58,21.23)+between(t,21.54,22.43)+between(t,22.90,25.32)+between(t,25.81,27.88)+between(t,28.20,29.05)"

CUT=29.30

"$FFMPEG" -y \
  -i s1-r08-base.mp4 \
  -i "assets/audio-claudia.wav" \
  -i "assets/logo-sting-dark.mp4" \
  -i "music/tutorial-themountain-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -filter_complex "
[1:a]atrim=0:${CUT},asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[voice];
[2:a]asetpts=PTS-STARTPTS+${CUT}/TB,volume=0.9,aformat=channel_layouts=stereo[stinga];

[3:a]atrim=0:32.5,asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.05,0.18)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=${CUT}:d=1.5[musfaded];

[4:a]volume=0.5,aformat=channel_layouts=stereo,asplit=11[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9][wb10];
[wb0]adelay=1120|1120[wh0];
[wb1]adelay=5280|5280[wh1];
[wb2]adelay=6730|6730[wh2];
[wb3]adelay=8310|8310[wh3];
[wb4]adelay=10680|10680[wh4];
[wb5]adelay=12630|12630[wh5];
[wb6]adelay=15250|15250[wh6];
[wb7]adelay=18080|18080[wh7];
[wb8]adelay=22580|22580[wh8];
[wb9]adelay=25640|25640[wh9];
[wb10]adelay=28280|28280[wh10];

[5:a]volume=0.32,aformat=channel_layouts=stereo,asplit=13[pb0][pb1][pb2][pb3][pb4][pb5][pb6][pb7][pb8][pb9][pb10][pb11][pb12];
[pb0]adelay=3120|3120[pop0];
[pb1]adelay=5280|5280[pop1];
[pb2]adelay=9310|9310[pop2];
[pb3]adelay=10680|10680[pop3];
[pb4]adelay=12680|12680[pop4];
[pb5]adelay=13480|13480[pop5];
[pb6]adelay=14180|14180[pop6];
[pb7]adelay=15400|15400[pop7];
[pb8]adelay=16150|16150[pop8];
[pb9]adelay=20480|20480[pop9];
[pb10]adelay=22580|22580[pop10];
[pb11]adelay=25640|25640[pop11];
[pb12]adelay=28280|28280[pop12];

[voice][stinga][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][wh10][pop0][pop1][pop2][pop3][pop4][pop5][pop6][pop7][pop8][pop9][pop10][pop11][pop12]amix=inputs=27:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -t 32.3 -c:v copy -c:a aac -b:a 192k \
  "s1-r08-no-ar-em-dias-COM-MUSICA.mp4"

echo "OK"
