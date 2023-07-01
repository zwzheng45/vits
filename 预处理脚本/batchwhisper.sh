#!/bin/bash
total=161
for((i=0;i<total;i++));
do
echo "开始处理第$((i+1))个音频，共$((total))个"
./main -m models/ggml-large.bin -f 1.5-1.7/"$i.wav" -l zh -otxt -t 16
done
echo "完成"
