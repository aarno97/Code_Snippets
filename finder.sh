#!/bin/bash
cd ~/Documents/GitHub/sherlock
echo "running sherlock"
python3 sherlock $1
filename=$1'.txt'
n=1
while read -r line; do
# reading each line
echo $line
open $line
n=$((n+1))
done < $filename