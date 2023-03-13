use std::vec;

fn parse_line(line: &str) -> (u32, u32, u32) {
    let mut lengths = line.split("x");
    let l = lengths.next().unwrap().parse::<u32>().unwrap();
    let w = lengths.next().unwrap().parse::<u32>().unwrap();
    let h = lengths.next().unwrap().parse::<u32>().unwrap();
    (l, w, h)
}

fn calculate_area(l: u32, w: u32, h: u32) -> u32 {
    let side_a: u32 = l * w;
    let side_b: u32 = w * h;
    let side_c: u32 = h * l;

    let smallest: u32 = *vec![side_a, side_b, side_c].iter().min().unwrap();

    2 * side_a + 2 * side_b + 2 * side_c + smallest
}

fn part_a(input: &str) -> u32 {
    let mut total_area: u32 = 0;
    for line in input.trim().lines() {
        let (l, w, h) = parse_line(line);
        total_area += calculate_area(l, w, h)
    }
    total_area
}

fn sort_tuple(tup: (u32, u32, u32)) -> (u32, u32, u32){
    let (a, b, c) = tup;
    let mut v = [a, b, c];
    v.sort();
    (v[0], v[1], v[2])
}

fn calculate_wrap(l: u32, w: u32) -> u32 {
   (2 * l) + (2 * w) 
}

fn calculate_bow(l: u32, w: u32, h: u32) -> u32 {
    l * w * h
}

fn ribbon_per_present(l: u32, w: u32, h: u32) -> u32 {
    calculate_wrap(l, w) + calculate_bow(l, w, h)
}

fn part_b(input: &str) -> u32 {
    let mut feet_of_ribbon: u32 = 0;
    for line in input.trim().lines() {
        let tupl = parse_line(line);
        let (l, w, h) = sort_tuple(tupl);
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
