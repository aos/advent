use std::{env, fs};

struct Slope(usize, usize);

fn main() -> std::io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let filename = args.get(1).map_or("input/day03_example.txt", |v| v);

    let grid: Vec<Vec<usize>> = fs::read_to_string(filename)?
        .lines()
        .map(|line| parse_line(line))
        .collect();

    println!("Part one: {}", descend(&grid, Slope(3, 1)));

    let part2 = vec![
        Slope(1, 1),
        Slope(3, 1),
        Slope(5, 1),
        Slope(7, 1),
        Slope(1, 2)]
            .into_iter()
            .map(|s| descend(&grid, s))
            .fold(1, |acc, x| acc * x);
    println!("Part two: {}", part2);

    Ok(())
}

fn parse_line(line: &str) -> Vec<usize> {
    line
        .chars()
        .map(|c| if c == '#' { 1 } else { 0 })
        .collect()
}

fn descend(grid: &Vec<Vec<usize>>, slope: Slope) -> usize {
    let width = grid[0].len();
    grid
        .iter()
        .step_by(slope.1)
        .enumerate()
        .fold(0, |acc, (y, line)| acc + line[(slope.0 * y) % width])
}
