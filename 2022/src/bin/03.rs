use std::collections::HashSet;
use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("in/day03_in.txt")?;
    println!("Part 1: {}", get_priority(&f));
    println!("Part 2: {}", three(&f));

    Ok(())
}

fn get_priority(inp: &str) -> usize {
    inp.lines().fold(0, |acc, l| {
        let (f, s) = l.split_at(l.len() / 2);
        let z: HashSet<char> = f.chars().collect();
        let t: HashSet<char> = s.chars().collect();
        let i = z.intersection(&t);
        i.take(1).fold(0, |_, c| {
            let n = if c.is_ascii_lowercase() {
                (*c as usize) - 96
            } else {
                (*c as usize) - 38
            };
            acc + n
        })
    })
}

fn three(inp: &str) -> usize {
    let mut total = 0;
    let mut count = 0;
    let mut temp_line: Vec<char> = Vec::new();
    for l in inp.lines() {
        count += 1;
        match count {
            1 => {
                temp_line = l.chars().collect();
            }
            2 => {
                temp_line.retain(|c| l.contains(*c));
            }
            3 => {
                temp_line.retain(|c| l.contains(*c));
                let x = match temp_line.first().unwrap() {
                    n if n.is_ascii_lowercase() => (*n as usize) - 96,
                    n => (*n as usize) - 38,
                };
                total += x;
                count = 0;
            }
            _ => (),
        }
    }
    total
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
        let res = three(EX);
        assert_eq!(res, 70);
    }
}
