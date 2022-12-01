#!/usr/bin/bash

if [ $# -ne 1 ]; then
    for i in $(seq -f "%02g" 1 25); do
        if [ ! -f days/$i.java ]; then
            continue
        fi
        echo ====== DAY $i =====
        cd days
        echo "kscript Day$i.kts ../input/$i.in"
        kscript Day"$i".kts ../input/"$i".in
    done
else
    day=$1
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    cd days
    echo "kscript Day$day.kts ../input/$day.in"
    kscript Day"$day".kts ../input/"$day".in
fi