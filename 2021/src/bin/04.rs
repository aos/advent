use aoc2021::Result;

fn main() -> Result<()> {
    let input = include_str!("../../in/day04_in.txt");
    let (draw, mut boards) = parse(input).unwrap();
    let mut wins = vec![];

    for num in draw {
        mark(num, &mut boards);

        let c = count_won_board(&mut boards);
        if c != 0 {
            wins.push(num * c);
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

fn parse(input: &str) -> Result<(Vec<u32>, Vec<Board>)> {
    let (draw, boards) = input.split_once("\n\n").ok_or("no lines")?;
    let draw = draw
        .split(",")
        .map(|n| n.parse())
        .collect::<std::result::Result<Vec<u32>, _>>()?;

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

fn mark(num: u32, boards: &mut Vec<Board>) {
    for board in boards {
        for line in &mut board.nums {
            for n in line {
                if num == n.n {
                    n.marked = true;
                }
            }
        }
    }
}

fn count_won_board(boards: &mut Vec<Board>) -> u32 {
    for board in boards {
        if board.won {
            continue;
        };

        let nums_len = board.nums.len();
        // horizontal
        for x in 0..nums_len {
            let mut count = 0;
            for y in 0..nums_len {
                if board.nums[x][y].marked {
                    count += 1;
                }
            }

            if count == nums_len {
                board.won = true;
                return count_unmarked(&board);
            }
        }

        // vertical
        for y in 0..nums_len {
            let mut count = 0;
            for x in 0..nums_len {
                if board.nums[x][y].marked {
                    count += 1;
                }
            }

            if count == nums_len {
                board.won = true;
                return count_unmarked(&board);
            }
        }
    }

    0
}

fn count_unmarked(board: &Board) -> u32 {
    board.nums.iter().fold(0u32, |count, nums| {
        count + nums.iter().filter(|n| !n.marked).map(|n| n.n).sum::<u32>()
    })
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

        for num in draw {
            mark(num, &mut boards);

            let c = count_won_board(&mut boards);
            if c != 0 {
                assert_eq!(c * num, 4512);
                break;
            }
        }
    }

    #[test]
    fn example_2() {
        let (draw, mut boards) = parse(EX).unwrap();
        let mut wins = vec![];

        for num in draw {
            mark(num, &mut boards);

            let c = count_won_board(&mut boards);
            if c != 0 {
                wins.push(num * c);
            }
        }

        assert_eq!(*wins.iter().last().unwrap(), 1924);
    }
}
