use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("in/day02_in.txt")?;

    println!("part 1: {}", count_total_score(&f, 1));
    println!("part 2: {}", count_total_score(&f, 2));
    Ok(())
}

fn count_total_score(inp: &str, part: usize) -> usize {
    let mut score: usize = 0;
    for line in inp.lines() {
        match line.split_once(" ") {
            Some((opp, me)) => {
                match me {
                    "X" => {
                        if part == 1 {
                            score += 1;
                        }
                    }
                    "Y" => {
                        if part == 1 {
                            score += 2;
                        }
                        else {
                            score += 3;
                        }
                    }
                    "Z" => {
                        if part == 1 {
                            score += 3;
                        } else {
                            score += 6;
                        }
                    }
                    _ => unreachable!(),
                }
                match (opp, me) {
                    ("A", "X") => {
                        score += 3;
                    },
                    ("A", "Y") => {
                        if part == 1 {
                            score += 6;
                        } else {
                            score += 1;
                        }
                    },
                    ("A", "Z") => {
                        if part == 2 {
                            score += 2;
                        }
                    },
                    ("B", "X") => {
                        if part == 2 {
                            score += 1;
                        }
                    },
                    ("B", "Y") => {
                        if part == 1 {
                            score += 3;
                        } else {
                            score += 2;
                        }
                    },
                    ("B", "Z") => {
                        if part == 1 {
                            score += 6;
                        } else {
                            score += 3;
                        }
                    },
                    ("C", "X") => {
                        if part == 1 {
                            score += 6;
                        } else {
                            score += 2;
                        }
                    },
                    ("C", "Y") => {
                        if part == 2 {
                            score += 3;
                        }
                    },
                    ("C", "Z") => {
                        if part == 1 {
                            score += 3;
                        } else {
                            score += 1;
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
        assert_eq!(res, 12);
    }
}
