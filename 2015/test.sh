#!/usr/bin/bash

if [ $# -ne 1 ]; then
    for i in $(seq -f "%02g" 1 25); do
        if [ ! -f days/$i.ts ]; then
            continue
        fi
        echo ====== DAY $i =====
        npx ts-node days/$i.ts input/$i.in
    done
else
    day=$1
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    npx ts-node days/$day.ts input/$day.in
fi