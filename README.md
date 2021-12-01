# Advent of Code
Contains my answers for each year of advent of code.

## File Structure
```
|-- year
|  |-- days
|  |  |-- $day.$ext
|  |-- input
|  |  |-- $day.in
|  |-- utils
|  |  |-- $utils
|  |-- test.sh
|-- get_all_input.sh
|-- get_input.sh
|-- .env
```

## Usage
Setup an .env file with these contents:
```bash
export COOKIE=<your cookie>
```
You can get the cookie from logging into AOC manually, going to https://adventofcode.com/2021/day/1/input (any day will do as long as it is the input),
then going to the Chrome Developer Tools (F12 or Right Click > Inspect Element) then going to the Application tab select Cookies > "input_site" and copy the value of the session found there.
### Get all daily input for every year (2016-)
```bash
chmod +x get_all_input.sh
./get_all_input.sh 
```
### Get all daily input for a specific year
```bash
chmod +x get_all_input.sh
./get_all_input.sh <year>
```
### Get input for current day
```bash
chmod +x get_input.sh
./get_input.sh
```
### Get input for specific day
```bash
chmod +x get_input.sh
./get_input.sh <day>
```
### Test the current day
```bash
cd <year>
chmod +x test.sh
./test.sh 
```
By default the test data is input/$day.in
### Test a specific day
```bash
cd <year>
chmod +x test.sh
./test.sh <day>
```
By default the test data is input/$day.in
### Test a specific day with a different file
```bash
cd <year>
chmod +x test.sh
./test.sh <day> <file>
```