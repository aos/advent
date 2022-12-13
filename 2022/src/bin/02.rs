use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("in/day02_in.txt")?;

    println!("part 1: {}", count_total_score(&f, 1));
    println!("part 1: {}", count_total_score(&f, 2));
    Ok(())
}

fn count_total_score(inp: &str, part: usize) -> usize {
    let mut score: usize = 0;
    for line in inp.lines() {
        match line.split_once(" ") {
            Some((opp, me)) => {
                match me {
                    "X" => score += 1,
                    "Y" => score += 2,
                    "Z" => score += 3,
                    _ => unreachable!(),
                }
                match (opp, me) {
                    ("A", "X") => {
                        if part == 1 {
                            score += 3
                        } else {
                        }
                    },
                    ("A", "Y") => {
                        if part == 1 {
                            score += 6;
                        } else {
                        }
                    },
                    ("B", "Y") => {
                        if part == 1 {
                            score += 3;
                        } else {
                        }
                    },
                    ("B", "Z") => {
                        if part == 1 {
                            score += 6;
                        } else {
                        }
                    },
                    ("C", "X") => {
                        if part == 1 {
                            score += 6;
                        } else {
                        }
                    },
                    ("C", "Z") => {
                        if part == 1 {
                            score += 3;
                        } else {
                        }
                    },
                    (_, _) => (),
                }
            }
            _ => (),
        }
    }

    score
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "
A Y
B X
C Z
";

    #[test]
    fn example_1() {
        let res = count_total_score(EX, 1);
        assert_eq!(res, 15);
    }

    #[test]
    fn example_2() {
        let res = count_total_score(EX, 2);
        assert_eq!(res, 15);
    }
}
