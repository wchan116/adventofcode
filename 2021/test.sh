#!/usr/bin/bash

if [ $# -eq 0 ]; then
    for i in $(seq -f "%02g" 1 25); do
        if [ ! -f days/$i.py ]; then
            continue
        fi
        echo ====== DAY $i =====
        python3 days/$i.py input/$i.in
    done
else
    day=$1
    input=$2
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    if [ -z $input ]; then
        input="input/$day.in"
    fi
    python3 days/$day.py $input
fi