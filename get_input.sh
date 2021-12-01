#!/usr/bin/bash

# load env variables
set -o allexport
source .env
set +o allexport

# get the wanted year and day
if [ $# -ne 2 ]; then
    year=$(date | cut -d' ' -f7)
    day=$(date | cut -d' ' -f3)
    if [ -z "$day" ]; then
        day=$(date | cut -d' ' -f4)
    fi
else
    year=$1
    day=$2
fi

# prepend leading zeroes if needed
str_day=$day
if [ $str_day -lt 10 ]; then
    str_day="0$str_day"
fi

# dl
URL="https://adventofcode.com/$year/day/$day/input"
echo "Downloading $URL" 1>&2
curl $URL \
-H 'authority: adventofcode.com' \
-H 'cache-control: max-age=0' \
-H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
-H 'sec-ch-ua-mobile: ?0' \
-H 'sec-ch-ua-platform: "Windows"' \
-H 'dnt: 1' \
-H 'upgrade-insecure-requests: 1' \
-H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36' \
-H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
-H 'sec-fetch-site: same-origin' \
-H 'sec-fetch-mode: navigate' \
-H 'sec-fetch-user: ?1' \
-H 'sec-fetch-dest: document' \
-H 'referer: https://adventofcode.com/2021/day/1' \
-H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
-H "cookie: session=$COOKIE" \
--compressed > "$year/input/$str_day.in"