#!/bin/bash
# render + mix each chapter listed in args
cd "$(dirname "$0")"
for k in "$@"; do
  cp out_en/$k.html en$k.html
  python3 render_en.py $k > render$k.log 2>&1 && python3 mix_en.py $k ../en/audio/$k.wav en${k}_mix.m4a >> render$k.log 2>&1 && \
  ffmpeg -v error -y -i en${k}_noaudio.mp4 -i en${k}_mix.m4a -c copy -shortest -movflags +faststart en$k.mp4 && echo "$k done" >> queue.log
done
echo "ALL $* done" >> queue.log
