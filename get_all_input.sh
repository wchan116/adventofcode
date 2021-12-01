#!/usr/bin/bash

dl_year () {
    year=$1
    for day in $(seq -f "%02g" 1 25); do
        echo $year $day
        ./get_input.sh $year $(echo $day | sed 's/^0*//') > "$year/input/$day.in"
        sleep 120
    done
}

if [ $# -eq 1 ]; then
    dl_year $1
else
    for year in $(seq 2016 2021); do
        dl_year $year
    done
fi