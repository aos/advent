use std::collections::HashSet;
use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("./in/day06_in.txt")?;
    println!("part 1: {}", detect(&f, 4));
    println!("part 2: {}", detect(&f, 14));
    Ok(())
}

fn detect(inp: &str, n: usize) -> usize {
    inp.chars()
        .collect::<Vec<char>>()
        .windows(n)
        .position(|chunk| chunk.iter().cloned().collect::<HashSet<char>>().len() == n)
        .unwrap()
        + n
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let exs = vec![
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ];
        for ex in exs {
            assert_eq!(detect(ex.0, 4), ex.1)
        }
    }

    #[test]
    fn example_2() {
        let exs = vec![
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
            ("nppdvjthqldpwncqszvftbrmjlhg", 23),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
        ];
        for ex in exs {
            assert_eq!(detect(ex.0, 14), ex.1)
        }
    }
}
