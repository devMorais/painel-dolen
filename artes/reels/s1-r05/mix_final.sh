#!/bin/bash
# Mixagem final S1-R05: video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/flipcard/pop)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r05"

SPEECH_MASK="between(t,0.78,2.51)+between(t,3.16,4.21)+between(t,4.60,5.81)+between(t,6.37,7.25)+between(t,7.91,9.26)+between(t,9.68,11.38)+between(t,12.00,12.65)+between(t,13.45,15.00)+between(t,15.59,17.37)+between(t,18.29,19.16)+between(t,19.55,20.26)+between(t,21.02,22.40)+between(t,23.11,24.38)+between(t,24.83,26.61)+between(t,27.41,32.61)+between(t,33.28,34.48)+between(t,35.18,35.92)+between(t,36.35,37.94)"

CUT=38.10

"$FFMPEG" -y \
  -i s1-r05-base.mp4 \
  -i "assets/audio-claudia.wav" \
  -i "assets/logo-sting-light.mp4" \
  -i "music/tutorial-themountain-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/flipcard.mp3" \
  -i "sfx/pop.mp3" \
  -filter_complex "
[1:a]atrim=0:${CUT},asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[voice];
[2:a]asetpts=PTS-STARTPTS+${CUT}/TB,volume=0.9,aformat=channel_layouts=stereo[stinga];

[3:a]atrim=0:41.1,asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.05,0.18)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=${CUT}:d=1.5[musfaded];

[4:a]volume=0.5,aformat=channel_layouts=stereo,asplit=14[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9][wb10][wb11][wb12][wb13];
[wb0]adelay=780|780[wh0];
[wb1]adelay=3240|3240[wh1];
[wb2]adelay=6480|6480[wh2];
[wb3]adelay=9860|9860[wh3];
[wb4]adelay=12380|12380[wh4];
[wb5]adelay=13580|13580[wh5];
[wb6]adelay=18380|18380[wh6];
[wb7]adelay=21040|21040[wh7];
[wb8]adelay=23200|23200[wh8];
[wb9]adelay=24900|24900[wh9];
[wb10]adelay=26980|26980[wh10];
[wb11]adelay=29200|29200[wh11];
[wb12]adelay=33340|33340[wh12];
[wb13]adelay=35240|35240[wh13];

[5:a]volume=0.6,aformat=channel_layouts=stereo,asplit=3[fb0][fb1][fb2];
[fb0]adelay=6480|6480[fc0];
[fb1]adelay=13580|13580[fc1];
[fb2]adelay=23200|23200[fc2];

[6:a]volume=0.32,aformat=channel_layouts=stereo,asplit=10[pb0][pb1][pb2][pb3][pb4][pb5][pb6][pb7][pb8][pb9];
[pb0]adelay=3990|3990[pop0];
[pb1]adelay=12380|12380[pop1];
[pb2]adelay=18380|18380[pop2];
[pb3]adelay=18880|18880[pop3];
[pb4]adelay=21040|21040[pop4];
[pb5]adelay=21490|21490[pop5];
[pb6]adelay=24900|24900[pop6];
[pb7]adelay=26980|26980[pop7];
[pb8]adelay=27430|27430[pop8];
[pb9]adelay=36740|36740[pop9];

[voice][stinga][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][wh10][wh11][wh12][wh13][fc0][fc1][fc2][pop0][pop1][pop2][pop3][pop4][pop5][pop6][pop7][pop8][pop9]amix=inputs=30:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -t 41.1 -c:v copy -c:a aac -b:a 192k \
  "s1-r05-landing-site-loja-COM-MUSICA.mp4"

echo "OK"
