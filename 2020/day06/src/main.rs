use std::{io, fs};
use std::collections::HashSet;

fn main() -> io::Result<()> {

    let file = fs::read_to_string("input.txt")?;
    let part1: usize = file
        .trim()
        .split("\n\n")
        .map(|g| count_group(g))
        .sum();
    
    println!("Part one: {}", part1);

    Ok(())
}

fn count_group(group: &str) -> usize {
    let mut h: HashSet<char> = group.chars().collect();
    h.remove(&'\n');

    h.len()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX_1: &str = "abcx
abcy
abcz";

    #[test]
    fn test_count_group() {
        let c = count_group(EX_1);
        assert_eq!(c, 6);
    }

    const EX_2: &str = "abc

a
b
c

ab
ac

a
a
a
a

b";

    #[test]
    fn test_sum_example() {
        let d: usize = EX_2
            .trim()
            .split("\n\n")
            .map(|g| count_group(g))
            .sum();
        assert_eq!(d, 11);
    }
}
