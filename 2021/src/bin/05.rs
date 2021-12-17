use aoc2021::Result;

fn main() -> Result<()> {
    let input = include_str!("../../in/day05_in.txt");
    let part1 = draw(
        &parse(input),
        |&(Point { x: x1, y: y1 }, Point { x: x2, y: y2 })| x1 == x2 || y1 == y2,
    );
    println!("part 1: {}", part1);
    println!("part 2: {}", draw(&parse(input), |_| true));

    Ok(())
}

fn parse(input: &str) -> Vec<(Point, Point)> {
    input
        .lines()
        .map(|line| line.split_once(" -> ").unwrap())
        .map(|(first, last)| {
            let (fx, fy) = first.split_once(",").unwrap();
            let (lx, ly) = last.split_once(",").unwrap();
            (
                Point {
                    x: fx.parse().unwrap(),
                    y: fy.parse().unwrap(),
                },
                Point {
                    x: lx.parse().unwrap(),
                    y: ly.parse().unwrap(),
                },
            )
        })
        .collect()
}

fn draw(points: &Vec<(Point, Point)>, filter: fn(&&(Point, Point)) -> bool) -> usize {
    use std::iter::{once, successors};
    let max_x = points
        .iter()
        .flat_map(|ps| once(ps.0.x).chain(once(ps.1.x)))
        .max()
        .unwrap();
    let max_y = points
        .iter()
        .flat_map(|ps| once(ps.0.y).chain(once(ps.1.y)))
        .max()
        .unwrap();

    let mut board = vec![0i32; (max_x as usize) * (max_y as usize)];
    let range = |a: i32, b: i32| successors(Some(a), move |n| Some(n + (b - a).signum()));
    for line in points.iter().filter(filter) {
        let ((x1, x2), (y1, y2)) = (
            (line.0.x as i32, line.1.x as i32),
            (line.0.y as i32, line.1.y as i32),
        );
        let dx = (x1 - x2).abs();
        let dy = (y1 - y2).abs();
        let count = dx.max(dy) + 1;

        let z = range(x1, x2).zip(range(y1, y2)).take(count as usize);

        for (x, y) in z {
            let i = (x as u32 + (max_x * (y as u32 % max_y))) as usize;
            board[i] += 1;
        }
    }

    board.iter().filter(|&&p| p >= 2).count()
}

#[derive(Debug)]
struct Point {
    x: u32,
    y: u32,
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2";

    #[test]
    fn part_1() {
        let parsed = parse(EX);
        let z = draw(
            &parsed,
            |&(Point { x: x1, y: y1 }, Point { x: x2, y: y2 })| x1 == x2 || y1 == y2,
        );
        assert_eq!(z, 5);
    }

    #[test]
    fn part_2() {
        let parsed = parse(EX);
        let z = draw(&parsed, |_| true);
        assert_eq!(z, 12);
    }
}
