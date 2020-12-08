#!/usr/bin/bash

for year in $(seq 2016 2019); do
    for day in $(seq -f "%02g" 1 25); do
        echo $year $day
        ./get_input.sh $year $(echo $day | sed 's/^0*//') > "$year/input/$day.in"
        sleep 120
    done
done