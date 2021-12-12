use aoc2021::Result;

fn main() -> Result<()> {
    println!("Hello world");

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
                    covered: 0,
                },
                Point {
                    x: lx.parse().unwrap(),
                    y: ly.parse().unwrap(),
                    covered: 0,
                },
            )
        })
        .collect()
}

fn draw(points: &mut Vec<(Point, Point)>) {
    for (first, last) in points {
    }
}

#[derive(Debug)]
struct Point {
    x: u32,
    y: u32,
    covered: u32,
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
        let x = parse(EX);
        println!("{:?}", x);
        assert_eq!(0, 0);
    }
}
