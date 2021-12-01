use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let input: Vec<usize> = fs::read_to_string("in/day01_in.txt")?
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    println!("part 1: {}", run(input.as_slice(), 1));
    println!("part 2: {}", run(input.as_slice(), 3));
    Ok(())
}

fn run(inp: &[usize], size: usize) -> usize {
    let mut count = 0;
    inp.windows(size).reduce(|a, b| {
        if b.iter().sum::<usize>() > a.iter().sum() {
            count += 1;
            b
        } else {
            b
        }
    });

    count
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "199
200
208
210
200
207
240
269
260
263";

    #[test]
    fn example_1() {
        let input: Vec<usize> = EX.trim().lines().map(|l| l.parse().unwrap()).collect();
        assert_eq!(run(input.as_slice(), 1), 7);
    }

    #[test]
    fn example_2() {
        let input: Vec<usize> = EX.trim().lines().map(|l| l.parse().unwrap()).collect();
        assert_eq!(run(input.as_slice(), 3), 5);
    }
}
