use std::fs;

#[derive(Debug)]
struct Point {
    x: usize,
    y: usize,
    is_tree: bool,
}

// (x, y)
struct Slope(usize, usize);

fn main() {
    let grid: Vec<Vec<Point>> = fs::read_to_string("example.txt").unwrap()
        .lines()
        .enumerate()
        .map(|(y, line)| parse_line(y, line))
        .collect();

    let width = grid[0].len();
}

fn parse_line(y: usize, line: &str) -> Vec<Point> {
    line
        .char_indices()
        .map(|(i, c)| Point { x: i, y, is_tree: c == '#' })
        .collect()
}
