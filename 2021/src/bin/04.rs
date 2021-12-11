use aoc2021::Result;

fn main() -> Result<()> {
    let input = include_str!("../../in/day04_in.txt");
    let (draw, mut boards) = parse(input).unwrap();
    let mut wins = vec![];

    for num in draw {
        for board in boards.iter_mut().filter(|b| !b.won) {
            if board.mark_check_win(num) {
                wins.push(num * board.sum_unmarked());
            }
        }
    }

    println!("part 1: {}", wins.iter().next().ok_or("no first")?);
    println!("part 2: {}", *wins.iter().last().ok_or("no last")?);

    Ok(())
}

struct Num {
    n: u32,
    marked: bool,
}

struct Board {
    nums: Vec<Vec<Num>>,
    won: bool,
}

impl Board {
    fn mark_check_win(&mut self, num: u32) -> bool {
        for line in &mut self.nums {
            for n in line {
                if num == n.n {
                    n.marked = true;
                }
            }
        }

        let nums_len = self.nums.len();
        for x in 0..nums_len {
            let mut count_x = 0;
            let mut count_y = 0;
            for y in 0..nums_len {
                if self.nums[x][y].marked {
                    count_x += 1;
                }

                if self.nums[y][x].marked {
                    count_y += 1;
                }
            }

            if count_x == nums_len || count_y == nums_len {
                self.won = true;
            }
        }

        self.won
    }

    fn sum_unmarked(&self) -> u32 {
        self.nums.iter().fold(0u32, |count, nums| {
            count + nums.iter().filter(|n| !n.marked).map(|n| n.n).sum::<u32>()
        })
    }
}

fn parse(input: &str) -> Result<(Vec<u32>, Vec<Board>)> {
    let (draw, boards) = input.split_once("\n\n").ok_or("no lines")?;
    let draw = draw
        .split(",")
        .map(|n| Ok(n.parse()?))
        .collect::<Result<_>>()?;

    let boards: Vec<Board> = boards
        .split("\n\n")
        .map(|b| {
            b.lines()
                .map(|l| {
                    l.split_whitespace()
                        .map(|n| Num {
                            n: n.parse().unwrap(),
                            marked: false,
                        })
                        .collect()
                })
                .fold(
                    Board {
                        nums: vec![],
                        won: false,
                    },
                    |mut b, n| {
                        b.nums.push(n);
                        b
                    },
                )
        })
        .collect();
    Ok((draw, boards))
}

impl std::fmt::Debug for Board {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let mut s = String::new();
        for line in &self.nums {
            for num in line {
                s.push_str(&format!("{:?}", num));
            }
            s.push('\n');
        }

        write!(f, "{}", s)
    }
}

impl std::fmt::Debug for Num {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        if self.marked {
            f.write_fmt(format_args!("{:>3}", "X"))
        } else {
            f.write_fmt(format_args!("{:>3}", self.n))
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7";

    #[test]
    fn example_1() {
        let (draw, mut boards) = parse(EX).unwrap();
        let mut wins = vec![];

        for num in draw {
            for board in boards.iter_mut().filter(|b| !b.won) {
                if board.mark_check_win(num) {
                    wins.push(num * board.sum_unmarked());
                }
            }
        }
        assert_eq!(*wins.iter().next().unwrap(), 4512);
    }

    #[test]
    fn example_2() {
        let (draw, mut boards) = parse(EX).unwrap();
        let mut wins = vec![];

        for num in draw {
            for board in boards.iter_mut().filter(|b| !b.won) {
                if board.mark_check_win(num) {
                    wins.push(num * board.sum_unmarked());
                }
            }
        }
        assert_eq!(*wins.iter().last().unwrap(), 1924);
    }
}
