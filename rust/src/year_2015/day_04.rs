use md5;

// in hexadecimal each char represents 4 bits
// so the first 5 chars being 0 is the same as the first 20 bits being 0
// and the first 6 chars being 0 is the same as the first 24 bits being 0:q
// 

fn calculate_digest(key: &str, number: u32) -> md5::Digest {
    let combined = format!("{}{}", key, number);
    md5::compute(combined)
}

fn first_five_chars_not_zero(digest: md5::Digest) -> bool {
    let hex_digest = format!("{:x}", digest);
    !(hex_digest[0..5] == *"00000")
}

fn first_six_chars_not_zero(digest: md5::Digest) -> bool {
    let hex_digest = format!("{:x}", digest);
    !(hex_digest[0..6] == *"000000")
}

fn part_a(input: &str) -> u32 {
    let mut number = 0;

    let mut digest = calculate_digest(input, number);
    while first_five_chars_not_zero(digest) {
        number += 1;
        digest = calculate_digest(input, number);
    }

    number
}

fn part_b(input: &str) -> u32 {
    let mut number = 0;

    let mut digest = calculate_digest(input, number);
    while first_six_chars_not_zero(digest) {
        number += 1;
        digest = calculate_digest(input, number);
    }

    number
}

pub fn run_day() {
    let file = include_str!("../../../input/2015/day_04.txt").trim();
    let answer_a = part_a(file);
    println!("Answer A: {answer_a}");
    let answer_b = part_b(file);
    println!("Answer B: {answer_b}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part_a_test_1() {
        let input = "abcdef";
        let result = part_a(input);
        assert_eq!(result, 609043);
    }

    #[test]
    fn part_a_test_2() {
        let input = "pqrstuv";
        let result = part_a(input);
        assert_eq!(result, 1048970);
    }
}
