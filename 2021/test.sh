#!/usr/bin/bash

get_current_day () {
    day=$(date | cut -d' ' -f3)
    if [ -z "$day" ]; then
        day=$(date | cut -d' ' -f4)
    fi
}

get_current_day
if [ $# -eq 0 ]; then
    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    python3 days/$day.py input/$day.in
else
    num_regex='\D+'
    if [ $# -eq 1 ] && [[ $1 =~ [$num_regex] ]]; then
        input=$1
        echo $input
    else
        day=$1
        input=$2
    fi

    if [ "$day" -lt 10 ]; then
        day="0$day"
    fi
    if [ -z $input ]; then
        input="input/$day.in"
    fi
    python3 days/$day.py $input
fi