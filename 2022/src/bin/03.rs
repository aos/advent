use std::collections::HashSet;
use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("in/day03_in.txt")?;
    let s = get_priority(&f);
    println!("Part 1: {}", s);

    Ok(())
}

fn get_priority(inp: &str) -> usize {
    inp.lines()
       .fold(0, |acc, l| {
            let mut z = HashSet::new();
            let (f, s) = l.split_at(l.len() / 2);
            f.chars().fold(&mut z, |acc, n| {
                acc.insert(n);
                acc
            });

            for c in s.chars() {
                if z.contains(&c) {
                    let n = if c.is_ascii_lowercase() {
                        (c as usize) - 96
                    } else {
                        (c as usize) - 38
                    };
                    return acc + n
                }
            }
            return acc
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
";

    #[test]
    fn example_1() {
        let res = get_priority(EX);
        assert_eq!(res, 157);
    }

    #[test]
    fn example_2() {
    }
}
