use itertools::Itertools;
use std::collections::HashMap;

fn get_combined_digit(s: String) -> i32 {
    let first_digit: String = s
        .chars()
        .find_or_first(|c| c.is_numeric())
        .unwrap_or('0')
        .to_string();
    let last_digit: String = s
        .chars()
        .rev()
        .find_or_first(|c| c.is_numeric())
        .unwrap_or('0')
        .to_string();
    let digit: String = first_digit + &last_digit;
    digit.parse::<i32>().unwrap_or(0)
}

fn part1(input: Vec<String>) -> i32 {
    input
        .iter()
        .map(|c| get_combined_digit(c.clone()))
        .sum::<i32>()
}

fn convert_to_num(input: String) -> String {
    let valid_numbers = HashMap::from([
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]);

    let mut result: String = String::new();

    for i in 0..input.len() {
        let curr = input.as_bytes()[i] as char;
        if curr.is_numeric() {
            result.push(curr);
        } else {
            for j in i..input.len() {
                let slice = &input[i..=j];
                if valid_numbers.contains_key(slice) {
                    result.push(valid_numbers[slice].chars().next().unwrap());
                    break;
                }
            }
        }
    }
    result
}

fn part2(input: Vec<String>) -> i32 {
    input
        .iter()
        .map(|l| {
            let number = convert_to_num(l.clone());
            get_combined_digit(number)
        })
        .sum::<i32>()
}

fn parse_file() -> Vec<String> {
    parse_input(include_str!("input.txt"))
}

fn parse_input(input: &'static str) -> Vec<String> {
    input.split('\n').map(str::to_string).collect()
}

fn main() {
    let solution = advent::new(parse_file).part(part1).part(part2).build();

    solution.cli();
}

#[cfg(test)]
mod tests {
    use crate::part1;
    use crate::part2;

    use crate::parse_input;

    #[test]
    fn test_part_one() {
        let input = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";

        let parsed_input = parse_input(input);

        let result = part1(parsed_input);

        assert_eq!(result, 142);
    }

    #[test]
    fn test_part_two() {
        let input = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen";

        let parsed_input = parse_input(input);

        let result = part2(parsed_input);

        assert_eq!(result, 281);
    }
}
