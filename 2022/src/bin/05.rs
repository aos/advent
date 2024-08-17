use regex::Regex;
use std::cell::LazyCell;
use std::error::Error;
use std::fs;

#[derive(Debug, Clone)]
struct Cr(String, usize);

type Instructions = Vec<(usize, usize, usize)>;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("./in/day05_in.txt")?;
    println!("part 1: {}", part1(&f));
    println!("part 2: {}", part2(&f));
    Ok(())
}

fn part1(inp: &str) -> String {
    let (mut stacks, instructions) = parse(inp);
    for inst in instructions {
        for _ in 0..inst.0 {
            let taken = stacks[inst.1].pop().unwrap();
            stacks[inst.2].push(taken);
        }
    }

    stacks
        .iter()
        .map(|s| s.last().unwrap().0.clone())
        .collect::<String>()
}

fn part2(inp: &str) -> String {
    let (mut stacks, instructions) = parse(inp);
    for inst in instructions {
        let len = stacks[inst.1].len();
        let mut taken = stacks[inst.1].split_off(len - inst.0);
        stacks[inst.2].append(&mut taken);
    }

    stacks
        .iter()
        .map(|s| s.last().unwrap().0.clone())
        .collect::<String>()
}

fn parse(inp: &str) -> (Vec<Vec<Cr>>, Instructions) {
    let (starting_stacks, instructions) = inp.split_once("\n\n").expect("should work");
    let stacks = parse_stacks(starting_stacks);
    let instructions = parse_instructions(instructions);

    (stacks, instructions)
}

fn parse_instructions(inp: &str) -> Instructions {
    let re: LazyCell<Regex> =
        LazyCell::new(|| Regex::new(r"move (\d+) from (\d+) to (\d+)").unwrap());

    inp.lines()
        .map(|line| {
            let caps = re.captures(line).unwrap();
            let num = caps
                .get(1)
                .map(|m| m.as_str().parse::<usize>().unwrap())
                .unwrap();
            let from = caps
                .get(2)
                .map(|m| m.as_str().parse::<usize>().unwrap())
                .unwrap();
            let to = caps
                .get(3)
                .map(|m| m.as_str().parse::<usize>().unwrap())
                .unwrap();

            // zero index, subtract 1
            (num, from - 1, to - 1)
        })
        .collect()
}

fn parse_stacks(inp: &str) -> Vec<Vec<Cr>> {
    let mut crs: Vec<Vec<Cr>> = inp
        .lines()
        .map(|line| {
            line.chars()
                .enumerate()
                // store state of found char as the first element in the acc
                .fold((false, vec![]), |mut acc, (idx, c)| {
                    if acc.0 {
                        let cr = Cr(c.to_string(), idx / 4);
                        acc.0 = false;
                        acc.1.push(cr);
                        acc
                    } else if c == '[' {
                        acc.0 = true;
                        acc
                    } else {
                        acc
                    }
                })
                .1
        })
        .collect();

    crs.pop(); // remove the stack labels
    crs.reverse(); // bottom to top
    arrange(crs)
}

fn arrange(stacks: Vec<Vec<Cr>>) -> Vec<Vec<Cr>> {
    let max_len = stacks
        .iter()
        .flat_map(|v| v.iter().map(|cr| cr.1))
        .max()
        .unwrap();
    let mut result: Vec<Vec<Cr>> = vec![vec![]; max_len + 1];

    for row in stacks.into_iter() {
        for cr in row.into_iter() {
            result[cr.1].push(cr);
        }
    }

    result
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = r#"
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"#;

    #[test]
    fn example_1() {
        let s = part1(EX.trim_start_matches("\n"));
        assert_eq!(&s, "CMZ");
    }

    #[test]
    fn example_2() {
        let s = part2(EX.trim_start_matches("\n"));
        assert_eq!(&s, "MCD");
    }
}
