#!/bin/bash
# Mixagem final S1-R04 (v3, timing corrigido via Whisper): video(voz+sting) + musica de fundo (baixa) + SFX (whoosh/pop/typing)
set -e
FFMPEG="C:\Users\UITEC\AppData\Local\Programs\Python\Python311\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
cd "/c/Users/UITEC/Herd/dolen-painel/artes/reels/s1-r04"

SPEECH_MASK="between(t,0.00,5.00)+between(t,5.30,7.04)+between(t,7.38,11.90)+between(t,12.16,14.62)+between(t,14.88,20.38)+between(t,21.06,26.90)+between(t,27.10,29.68)"

"$FFMPEG" -y \
  -i s1-r04-nao-aparece-no-google.mp4 \
  -i "music/technology-apalonbeats-pixabay.mp3" \
  -i "sfx/whoosh.mp3" \
  -i "sfx/pop.mp3" \
  -i "sfx/typing.mp3" \
  -filter_complex "
[1:a]atrim=0:31,asetpts=PTS-STARTPTS[musraw];
[musraw]volume=eval=frame:volume='if(${SPEECH_MASK},0.05,0.18)'[musduck];
[musduck]afade=t=in:st=0:d=1.0,afade=t=out:st=29.3:d=2.0[musfaded];

[2:a]volume=0.55,asplit=11[wb0][wb1][wb2][wb3][wb4][wb5][wb6][wb7][wb8][wb9][wb10];
[wb0]adelay=900|900[wh0];
[wb1]adelay=3860|3860[wh1];
[wb2]adelay=5360|5360[wh2];
[wb3]adelay=6360|6360[wh3];
[wb4]adelay=7440|7440[wh4];
[wb5]adelay=10320|10320[wh5];
[wb6]adelay=12220|12220[wh6];
[wb7]adelay=14940|14940[wh7];
[wb8]adelay=18340|18340[wh8];
[wb9]adelay=21120|21120[wh9];
[wb10]adelay=27160|27160[wh10];

[3:a]volume=0.34,asplit=10[pb0][pb1][pb2][pb3][pb4][pb5][pb6][pb7][pb8][pb9];
[pb0]adelay=4410|4410[pop0];
[pb1]adelay=6810|6810[pop1];
[pb2]adelay=8440|8440[pop2];
[pb3]adelay=13880|13880[pop3];
[pb4]adelay=15790|15790[pop4];
[pb5]adelay=19800|19800[pop5];
[pb6]adelay=23400|23400[pop6];
[pb7]adelay=24600|24600[pop7];
[pb8]adelay=25660|25660[pop8];
[pb9]adelay=28440|28440[pop9];

[4:a]atrim=0:1.0,volume=0.30[typing0];
[typing0]adelay=2400|2400[ty0];

[0:a][musfaded][wh0][wh1][wh2][wh3][wh4][wh5][wh6][wh7][wh8][wh9][wh10][pop0][pop1][pop2][pop3][pop4][pop5][pop6][pop7][pop8][pop9][ty0]amix=inputs=24:duration=first:dropout_transition=0:normalize=0[outa]
" \
  -map 0:v -map "[outa]" -c:v copy -c:a aac -b:a 192k \
  "s1-r04-nao-aparece-no-google-FINAL.mp4"

echo "OK"
