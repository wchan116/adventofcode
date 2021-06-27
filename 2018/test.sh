#!/usr/bin/bash

if [ $# -ne 1 ]; then
    for i in $(seq -f "%02g" 1 25); do
        if [ ! -f days/$i.java ]; then
            continue
        fi
        echo ====== DAY $i =====
        cd days
        javac Utils.java Day$i.java 
        java Day$i ../input/$i.in
    done
else
    day=$1
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    cd days
    javac Utils.java Day$day.java 
    java Day$day ../input/$day.in
fi