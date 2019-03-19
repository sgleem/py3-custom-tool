#!/bin/bash

# wav directory -> utt) spk wav_path
# text directory -> utt) text

# Output
# 1. utt2wav -> wav.scp
# 2. utt2spk -> spk2utt -> spk2gender
# 3. text -> glm, stm

corpus=$1
# 1. utt2wav -> wav.scp
# 1-1. utt2wav
find $corpus -iname "*.wav" > wav.tmp
# 1-2. wav.scp