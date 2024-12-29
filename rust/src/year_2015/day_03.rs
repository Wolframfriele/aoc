fn part_a(input: &str) -> u32 {
    for direction in input.chars() {
        match direction {
            '>' => println!("Right"),
            '<' => println!("Left"),
            '^' => println!("Up"),
            'v' => println!("Down"),
            _ => (),
        }
    }
    32
}

// fn part_b(input: &str) -> u32 {

// }

/// Does this add documentation to the method
pub fn run_day() {
    let file = include_str!("../../../input/2015/day_03.txt");
    let answer_a = part_a(file);
    println!("Answer A: {answer_a}");
    // let answer_b = part_b(file);
    // println!("Answer B: {answer_b}");
}
