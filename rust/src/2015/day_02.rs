fn parse_line(line: &str, sort_input: bool) -> (u32, u32, u32) {
    let parts = line.split("x");
    let mut v: Vec<u32> = parts.map(|x| x.parse::<u32>().unwrap()).collect();
    if sort_input {
        v.sort();
    }
    (v[0], v[1], v[2])
}

fn calculate_area(l: u32, w: u32, h: u32) -> u32 {
    let side_a: u32 = l * w;
    let side_b: u32 = w * h;
    let side_c: u32 = h * l;

    let smallest: u32 = *vec![side_a, side_b, side_c].iter().min().unwrap();

    2 * side_a + 2 * side_b + 2 * side_c + smallest
}

fn ribbon_per_present(l: u32, w: u32, h: u32) -> u32 {
    (2 * l) + (2 * w) + (l * w * h)
}

fn part_a(input: &str) -> u32 {
    let mut total_area: u32 = 0;
    for line in input.trim().lines() {
        let (l, w, h) = parse_line(line, false);
        total_area += calculate_area(l, w, h)
    }
    total_area
}

fn part_b(input: &str) -> u32 {
    let mut feet_of_ribbon: u32 = 0;
    for line in input.trim().lines() {
        let (l, w, h) = parse_line(line, true);
        feet_of_ribbon += ribbon_per_present(l, w, h);
    }
    feet_of_ribbon
}

pub fn run_day() {
    let file = include_str!("../input/day_02_real.txt");
    let answer_a = part_a(file);
    println!("Answer A: {answer_a}");
    let answer_b = part_b(file);
    println!("Answer B: {answer_b}");
}
