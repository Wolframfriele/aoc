fn part_a(input: &str) -> i32 {
    let mut floor_counter: i32 = 0;

    for char in input.chars() {
        match char {
            '(' => floor_counter += 1,
            ')' => floor_counter -= 1,
            _ => continue,
        }
    }
    return floor_counter;
}

fn part_b(input: &str) -> u32 {
    let mut floor_counter: i32 = 0;
    let mut index: u32 = 1;

    for char in input.chars() {
        match char {
            '(' => floor_counter += 1,
            ')' => floor_counter -= 1,
            _ => continue,
        }
        if floor_counter < 0 {
            break;
        }
        index += 1;
    }
    return index;
}

pub fn run_day() {
    println!("AoC Day 1.");
    let file = include_str!("../../../input/2015/day_01.txt");
    let answer_a = part_a(file);
    println!("Answer A: {answer_a}");
    let answer_b = part_b(file);
    println!("Answer B: {answer_b}");
}
