use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("in/day01_in.txt")?;

    println!("part 1: {}", count_top_cals(&f, 1));
    println!("part 1: {}", count_top_cals(&f, 3));
    Ok(())
}

fn count_top_cals(inp: &str, num: usize) -> usize {
    let mut totals = Vec::new();
    let mut curr: usize = 0;
    for line in inp.lines() {
        match line.parse::<usize>() {
            Ok(amount) => curr += amount,
            Err(_) => {
                totals.push(curr);
                curr = 0;
            },
        }
    }

    totals.sort();
    totals.iter().rev().take(num).sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

";

    #[test]
    fn example_1() {
        let res = count_top_cals(EX, 1);
        assert_eq!(res, 24000);
    }

    #[test]
    fn example_2() {
        let res = count_top_cals(EX, 3);
        assert_eq!(res, 45000);
    }
}
