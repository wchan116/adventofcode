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
To get the cookie:
- Log into AOC manually
- Go to any problem and get your input (https://adventofcode.com/2021/day/1/input)
- Go to chrome Developer Tools (F12 or Right Click > Inspect Element)
- Go to the Application tab
- Select Cookies > "link where you got your input"
- Copy the value of the session you found here
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