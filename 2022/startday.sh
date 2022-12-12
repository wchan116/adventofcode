#!/usr/bin/env bash

year=$(date | cut -d' ' -f7)
if [ -z "$year" ]; then
  year=$(date | cut -d' ' -f6)
fi
day=$(date | cut -d' ' -f3)
if [ -z "$day" ]; then
  day=$(date | cut -d' ' -f4)
fi
if [ "$day" -lt 10 ]; then
  day="0$day"
fi
echo "Copying day $year $day"
cp days/template.kts days/Day"$day".kts