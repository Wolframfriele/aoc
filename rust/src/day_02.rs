use std::vec;

fn calculate_area(l: u32, w: u32, h: u32) -> u32 {
    let side_a: u32 = l * w;
    let side_b: u32 = w * h;
    let side_c: u32 = h * l;

    let smallest: u32 = *vec![side_a, side_b, side_c].iter().min().unwrap();

    return 2 * side_a + 2 * side_b + 2 * side_c + smallest
}

fn part_a(input: &str) -> u32 {
    let mut total_area: u32 = 0;
    for line in input.trim().lines() {
        let mut lengths = line.split("x");
        let l = lengths.next().unwrap().parse::<u32>().unwrap();
        let w = lengths.next().unwrap().parse::<u32>().unwrap();
        let h = lengths.next().unwrap().parse::<u32>().unwrap();

        total_area += calculate_area(l, w, h)
    }
    return total_area

}

// fn part_b(input: &str) -> u32 {

// }

pub fn run_day() {
    let file = include_str!("../input/day_02_real.txt");
    let answer_a = part_a(file);
    println!("Answer A: {answer_a}");
    // let answer_b = part_b(file);
    // println!("Answer B: {answer_b}");
}
