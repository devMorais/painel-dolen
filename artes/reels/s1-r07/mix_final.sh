#!/bin/bash
# Mixagem final S1-R07: video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/pop)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r07"

SPEECH_MASK="between(t,1.01,2.60)+between(t,2.88,5.39)+between(t,5.79,9.01)+between(t,9.36,11.68)+between(t,12.09,13.62)+between(t,14.02,16.58)+between(t,17.42,21.79)+between(t,22.43,23.92)+between(t,24.71,27.64)+between(t,28.20,28.96)"

CUT=29.00

"$FFMPEG" -y \
  -i s1-r07-base.mp4 \
  -i "assets/audio-claudia.wav" \
  -i "assets/logo-sting-dark.mp4" \
  -i "music/tutorial-themountain-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -filter_complex "
[1:a]atrim=0:${CUT},asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[voice];
[2:a]asetpts=PTS-STARTPTS+${CUT}/TB,volume=0.9,aformat=channel_layouts=stereo[stinga];

[3:a]atrim=0:31.5,asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.05,0.18)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=${CUT}:d=1.5[musfaded];

[4:a]volume=0.5,aformat=channel_layouts=stereo,asplit=10[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9];
[wb0]adelay=1010|1010[wh0];
[wb1]adelay=4080|4080[wh1];
[wb2]adelay=5710|5710[wh2];
[wb3]adelay=7300|7300[wh3];
[wb4]adelay=12070|12070[wh4];
[wb5]adelay=13960|13960[wh5];
[wb6]adelay=17130|17130[wh6];
[wb7]adelay=22280|22280[wh7];
[wb8]adelay=24450|24450[wh8];
[wb9]adelay=27640|27640[wh9];

[5:a]volume=0.32,aformat=channel_layouts=stereo,asplit=8[pb0][pb1][pb2][pb3][pb4][pb5][pb6][pb7];
[pb0]adelay=5710|5710[pop0];
[pb1]adelay=9100|9100[pop1];
[pb2]adelay=12070|12070[pop2];
[pb3]adelay=13960|13960[pop3];
[pb4]adelay=22380|22380[pop4];
[pb5]adelay=24450|24450[pop5];
[pb6]adelay=27640|27640[pop6];
[pb7]adelay=28190|28190[pop7];

[voice][stinga][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][pop0][pop1][pop2][pop3][pop4][pop5][pop6][pop7]amix=inputs=21:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -t 32.0 -c:v copy -c:a aac -b:a 192k \
  "s1-r07-primeira-impressao-COM-MUSICA.mp4"

echo "OK"
