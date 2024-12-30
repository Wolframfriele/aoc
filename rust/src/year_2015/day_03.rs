use anyhow::{bail, Result};
use std::collections::HashSet;

#[derive(Hash, Clone, Copy, PartialEq, Eq)]
struct Coordinate {
    x: i32,
    y: i32,
}

impl Coordinate {
    fn move_in_direction(self, direction: char) -> Result<Coordinate> {
        match direction {
            '>' => Ok(Coordinate {
                x: self.x + 1,
                y: self.y,
            }),
            '<' => Ok(Coordinate {
                x: self.x - 1,
                y: self.y,
            }),
            '^' => Ok(Coordinate {
                x: self.x,
                y: self.y + 1,
            }),
            'v' => Ok(Coordinate {
                x: self.x,
                y: self.y - 1,
            }),
            _ => bail!("input char is an unknown, should be >, <, ^ or v"),
        }
    }
}

struct DeliveryUnit {
    current: Coordinate,
    pub seen: HashSet<Coordinate>,
}

impl DeliveryUnit {
    fn new() -> DeliveryUnit {
        DeliveryUnit {
            current: Coordinate { x: 0, y: 0 },
            seen: HashSet::from_iter(vec![Coordinate { x: 0, y: 0 }].iter().cloned()),
        }
    }

    fn move_in_direction(&mut self, direction: char) {
        if let Ok(new_location) = self.current.move_in_direction(direction) {
            self.seen.insert(new_location);
            self.current = new_location;
        }
    }

    fn delivery_count(&self) -> usize {
        self.seen.len()
    }
}

fn part_a(input: &str) -> u32 {
    let mut santa = DeliveryUnit::new();
    for direction in input.chars() {
        santa.move_in_direction(direction);
    }
    santa.delivery_count() as u32
}

// fn part_b(input: &str) -> u32 {

// }

pub fn run_day() {
    let file = include_str!("../../../input/2015/day_03.txt");
    let answer_a = part_a(file);
    println!("Answer A: {answer_a}");
    // let answer_b = part_b(file);
    // println!("Answer B: {answer_b}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part_a_test_1() {
        let input = ">";
        let result = part_a(input);
        assert_eq!(result, 2);
    }

    #[test]
    fn part_a_test_2() {
        let input = "^>v<";
        let result = part_a(input);
        assert_eq!(result, 4);
    }

    #[test]
    fn part_a_test_3() {
        let input = "^v^v^v^v^v";
        let result = part_a(input);
        assert_eq!(result, 2);
    }
}
