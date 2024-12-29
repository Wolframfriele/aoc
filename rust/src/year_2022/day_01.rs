

#[cfg(test)]
mod tests {
    #[test]
    fn tescase_a() {
        let input = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";
    let result = solve_a(input);
    assert_eq!(result, 2400);
    }
} 
