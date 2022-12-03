#!/usr/bin/bash

if [ $# -eq 2 ]; then
    day=$1
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    cd days
    echo "kscript Day$day.kts ../input/$2"
    kscript Day"$day".kts ../input/$2
elif [ $# -eq 1 ]; then
    day=$1
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    cd days
    echo "kscript Day$day.kts ../input/$day.in"
    kscript Day"$day".kts ../input/"$day".in
else
    for i in $(seq -f "%02g" 1 25); do
        if [ ! -f days/$i.java ]; then
            continue
        fi
        echo ====== DAY $i =====
        cd days
        echo "kscript Day$i.kts ../input/$i.in"
        kscript Day"$i".kts ../input/"$i".in
    done
fi