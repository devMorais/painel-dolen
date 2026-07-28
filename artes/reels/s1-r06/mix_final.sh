#!/bin/bash
# Mixagem final S1-R06: video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/pop)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r06"

SPEECH_MASK="between(t,0.94,4.52)+between(t,4.95,6.20)+between(t,6.90,8.50)+between(t,8.98,10.19)+between(t,10.68,12.22)+between(t,12.82,15.61)+between(t,16.07,17.10)+between(t,17.50,18.13)+between(t,18.43,19.82)+between(t,20.25,20.69)+between(t,20.96,22.01)+between(t,22.34,22.83)+between(t,23.64,24.25)+between(t,24.96,26.49)+between(t,27.06,28.19)+between(t,28.83,29.96)"

CUT=30.00

"$FFMPEG" -y \
  -i s1-r06-base.mp4 \
  -i "assets/audio-claudia.wav" \
  -i "assets/logo-sting-dark.mp4" \
  -i "music/tutorial-themountain-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -filter_complex "
[1:a]atrim=0:${CUT},asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[voice];
[2:a]asetpts=PTS-STARTPTS+${CUT}/TB,volume=0.9,aformat=channel_layouts=stereo[stinga];

[3:a]atrim=0:32.65,asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.05,0.18)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=${CUT}:d=1.5[musfaded];

[4:a]volume=0.5,aformat=channel_layouts=stereo,asplit=9[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8];
[wb0]adelay=940|940[wh0];
[wb1]adelay=3160|3160[wh1];
[wb2]adelay=6980|6980[wh2];
[wb3]adelay=9040|9040[wh3];
[wb4]adelay=12940|12940[wh4];
[wb5]adelay=16080|16080[wh5];
[wb6]adelay=23660|23660[wh6];
[wb7]adelay=27080|27080[wh7];
[wb8]adelay=28700|28700[wh8];

[5:a]volume=0.32,aformat=channel_layouts=stereo,asplit=10[pb0][pb1][pb2][pb3][pb4][pb5][pb6][pb7][pb8][pb9];
[pb0]adelay=5060|5060[pop0];
[pb1]adelay=7080|7080[pop1];
[pb2]adelay=7730|7730[pop2];
[pb3]adelay=9040|9040[pop3];
[pb4]adelay=16180|16180[pop4];
[pb5]adelay=18230|18230[pop5];
[pb6]adelay=20230|20230[pop6];
[pb7]adelay=24760|24760[pop7];
[pb8]adelay=28700|28700[pop8];
[pb9]adelay=29550|29550[pop9];

[voice][stinga][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][pop0][pop1][pop2][pop3][pop4][pop5][pop6][pop7][pop8][pop9]amix=inputs=22:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -t 33.0 -c:v copy -c:a aac -b:a 192k \
  "s1-r06-painel-proprio-COM-MUSICA.mp4"

echo "OK"
