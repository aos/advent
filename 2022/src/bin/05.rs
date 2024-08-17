use std::error::Error;
use std::fs;
use std::cell::LazyCell;

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


fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("in/day05_in.txt")?;
    // println!("{:?}", parse(EX.trim_start_matches("\n")).0);
    println!("{:#?}", parse(&f));
    Ok(())
}

#[derive(Debug)]
struct Cr(String, usize);

fn parse(inp: &str) -> (Vec<Vec<Cr>>, (usize, usize, usize)) {
    let (starting_stacks, procedure) = inp.split_once("\n\n").expect("should work");
    let stacks = parse_stacks(starting_stacks);

    (stacks, (1, 1, 1))
}

fn parse_instructions(inp: &str) -> usize {
    3
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
    crs
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        println!("{:?}", EX.trim_start_matches("\n").split_once("\n\n"));
    }

    #[test]
    fn example_2() {}
}
