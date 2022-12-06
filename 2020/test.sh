#!/usr/bin/bash
# get the wanted year and day

if [ $# -eq 1 ]; then
    day=$1
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    python3 days/$day.py input/$day.in
elif [ $# -eq 2 ]; then
    day=$1
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    python3 days/$day.py $2
else
    day=$(date | cut -d' ' -f3)
    if [ -z "$day" ]; then
        day=$(date | cut -d' ' -f4)
    fi
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    python3 days/$day.py input/$day.in
fi