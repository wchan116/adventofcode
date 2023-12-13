use std::cmp;

fn part1(input: Vec<String>) -> i32 {
    let red = 12;
    let green = 13;
    let blue = 14;

    let ids: i32 = input
        .iter()
        .filter(|l| !l.is_empty())
        .map(|l| {
            let sets: Vec<String> = l.split(':').map(str::to_string).collect();
            let game = sets[1].trim();
            let id: Vec<String> = sets[0].split(' ').map(str::to_string).collect();
            let id: i32 = id[1].parse::<i32>().unwrap();

            let results: Vec<bool> = game
                .split(';')
                .map(|set| {
                    let results: Vec<bool> = set
                        .split(',')
                        .map(|cube| {
                            let vals: Vec<String> = cube
                                .split(' ')
                                .filter(|c| !c.is_empty())
                                .map(str::to_string)
                                .collect();
                            let num = vals[0].parse::<i32>().unwrap();
                            let color = vals[1].trim();
                            match color {
                                "red" => num <= red,
                                "green" => num <= green,
                                "blue" => num <= blue,
                                _ => false,
                            }
                        })
                        .collect();

                    results.iter().all(|r| *r)
                })
                .collect();
            if results.iter().all(|r| *r) {
                id
            } else {
                0
            }
        })
        .sum::<i32>();

    ids
}

fn part2(input: Vec<String>) -> i32 {
    let ids: i32 = input
        .iter()
        .filter(|l| !l.is_empty())
        .map(|l| {
            let sets: Vec<String> = l.split(':').map(str::to_string).collect();
            let game = sets[1].trim();
            let id: Vec<String> = sets[0].split(' ').map(str::to_string).collect();
            let id: i32 = id[1].parse::<i32>().unwrap();

            let mut red = 0;
            let mut green = 0;
            let mut blue = 0;

            game.split(';').for_each(|set| {
                set.split(',').for_each(|cube| {
                    let vals: Vec<String> = cube
                        .split(' ')
                        .filter(|c| !c.is_empty())
                        .map(str::to_string)
                        .collect();
                    let num = vals[0].parse::<i32>().unwrap();
                    let color = vals[1].trim();
                    match color {
                        "red" => red = cmp::max(red, num),
                        "green" => green = cmp::max(green, num),
                        "blue" => blue = cmp::max(blue, num),
                        _ => {}
                    }
                });
            });
            red * green * blue
        })
        .sum::<i32>();

    ids
}

fn parse_file() -> Vec<String> {
    parse_input(include_str!("input.txt"))
}

fn parse_input(input: &'static str) -> Vec<String> {
    input.split('\n').map(str::to_string).collect()
}

fn main() {
    let solution = advent::new(parse_file).part(part1).part(part2).build();

    solution.cli()
}

#[cfg(test)]
mod tests {
    use crate::part1;
    use crate::part2;

    use crate::parse_input;

    #[test]
    fn test_part_one() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

        let parsed_input = parse_input(input);

        let result = part1(parsed_input);

        assert_eq!(result, 8);
    }

    #[test]
    fn test_part_two() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

        let parsed_input = parse_input(input);

        let result = part2(parsed_input);

        assert_eq!(result, 2286);
    }
}
