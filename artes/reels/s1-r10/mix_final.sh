#!/bin/bash
# Mixagem final S1-R10: video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/pop)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r10"

SPEECH_MASK="between(t,0.00,0.25)+between(t,0.72,4.50)+between(t,4.93,8.62)+between(t,9.02,10.43)+between(t,10.76,11.80)+between(t,12.14,13.77)+between(t,14.18,14.87)+between(t,15.27,16.27)+between(t,17.01,18.60)+between(t,19.13,21.39)+between(t,21.89,22.65)+between(t,23.35,24.25)"

CUT=24.60

"$FFMPEG" -y \
  -i s1-r10-base.mp4 \
  -i "assets/audio-claudia.wav" \
  -i "assets/logo-sting-dark.mp4" \
  -i "music/tutorial-themountain-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -filter_complex "
[1:a]atrim=0:${CUT},asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[voice];
[2:a]asetpts=PTS-STARTPTS+${CUT}/TB,volume=0.9,aformat=channel_layouts=stereo[stinga];

[3:a]atrim=0:27.7,asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.05,0.18)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=${CUT}:d=1.5[musfaded];

[4:a]volume=0.5,aformat=channel_layouts=stereo,asplit=14[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9][wb10][wb11][wb12][wb13];
[wb0]adelay=720|720[wh0];
[wb1]adelay=2420|2420[wh1];
[wb2]adelay=4770|4770[wh2];
[wb3]adelay=6420|6420[wh3];
[wb4]adelay=7660|7660[wh4];
[wb5]adelay=8860|8860[wh5];
[wb6]adelay=10680|10680[wh6];
[wb7]adelay=12030|12030[wh7];
[wb8]adelay=14280|14280[wh8];
[wb9]adelay=15230|15230[wh9];
[wb10]adelay=16680|16680[wh10];
[wb11]adelay=18970|18970[wh11];
[wb12]adelay=21650|21650[wh12];
[wb13]adelay=23150|23150[wh13];

[5:a]volume=0.32,aformat=channel_layouts=stereo,asplit=13[pb0][pb1][pb2][pb3][pb4][pb5][pb6][pb7][pb8][pb9][pb10][pb11][pb12];
[pb0]adelay=720|720[pop0];
[pb1]adelay=2420|2420[pop1];
[pb2]adelay=6420|6420[pop2];
[pb3]adelay=7660|7660[pop3];
[pb4]adelay=8860|8860[pop4];
[pb5]adelay=10680|10680[pop5];
[pb6]adelay=12580|12580[pop6];
[pb7]adelay=14280|14280[pop7];
[pb8]adelay=15230|15230[pop8];
[pb9]adelay=16880|16880[pop9];
[pb10]adelay=20070|20070[pop10];
[pb11]adelay=21650|21650[pop11];
[pb12]adelay=23150|23150[pop12];

[voice][stinga][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][wh10][wh11][wh12][wh13][pop0][pop1][pop2][pop3][pop4][pop5][pop6][pop7][pop8][pop9][pop10][pop11][pop12]amix=inputs=30:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -t 27.6 -c:v copy -c:a aac -b:a 192k \
  "s1-r10-bora-acelerar-COM-MUSICA.mp4"

echo "OK"
