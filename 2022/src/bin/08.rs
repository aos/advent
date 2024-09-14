use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let f = fs::read_to_string("./in/day08_in.txt")?;
    let grid = parse_input(&f);

    println!("part 1: {}", part1(&grid));
    println!("part 2: {}", part2(&grid));

    Ok(())
}

fn part1(grid: &Grid) -> usize {
    grid.pos
        .iter()
        .enumerate()
        .filter(|(idx, _)| grid.check_edges(*idx))
        .count()
}

fn part2(grid: &Grid) -> usize {
    grid.pos
        .iter()
        .enumerate()
        .map(|(idx, _)| grid.scenic_score(idx))
        .max()
        .unwrap_or(0)
}

fn parse_input(inp: &str) -> Grid {
    let lines = inp.trim().lines();
    let height = lines.clone().count();
    let width = lines.clone().nth(0).unwrap().chars().count();
    let pos = lines
        .flat_map(|line| {
            line.chars()
                .map(|c| c.to_digit(10).unwrap())
                .collect::<Vec<_>>()
        })
        .collect();

    Grid {
        pos,
        dim: (width, height),
    }
}

#[derive(Debug)]
struct Grid {
    pos: Vec<u32>,
    dim: (usize, usize),
}

#[allow(dead_code)]
impl Grid {
    fn value_at(&self, row: usize, col: usize) -> u32 {
        assert!(row < self.dim.0);
        assert!(col < self.dim.1);

        self.pos[self.dim.1 * row + col]
    }

    fn pos_2d(&self, idx: usize) -> (usize, usize) {
        assert!(idx < self.pos.len());
        (idx / self.dim.1, idx % self.dim.1)
    }

    fn check_edges(&self, current_pos: usize) -> bool {
        let (row_two_d, col_two_d) = self.pos_2d(current_pos);
        if row_two_d == 0
            || col_two_d == 0
            || row_two_d == (self.dim.0 - 1)
            || col_two_d == (self.dim.1 - 1)
        {
            return true;
        }

        let range_row_start = row_two_d * self.dim.1;
        let range_row_end = (row_two_d * self.dim.1) + self.dim.1 - 1;
        let range_col_end = (self.dim.0 - 1) * self.dim.1 + col_two_d;

        let me = self.pos[current_pos];

        // Go from right to left
        let left = (range_row_start..current_pos)
            .rev()
            .map(|p| self.pos[p])
            .all(|v| me > v);
        let right = (current_pos + 1..=range_row_end)
            .map(|p| self.pos[p])
            .all(|v| me > v);
        // Go from down to up
        let up = (col_two_d..=current_pos - self.dim.1)
            .rev()
            .step_by(self.dim.1)
            .map(|p| self.pos[p])
            .all(|v| me > v);
        let down = (current_pos + self.dim.1..=range_col_end)
            .step_by(self.dim.1)
            .map(|p| self.pos[p])
            .all(|v| me > v);

        left || right || up || down
    }

    fn count_trees(&self, through: impl Iterator<Item = u32>, val: u32) -> usize {
        let mut total = 0;
        for p in through {
            if val > p {
                total += 1;
            } else {
                total += 1;
                break;
            }
        }

        total
    }

    fn scenic_score(&self, current_pos: usize) -> usize {
        let (row_two_d, col_two_d) = self.pos_2d(current_pos);
        if row_two_d == 0
            || col_two_d == 0
            || row_two_d == (self.dim.0 - 1)
            || col_two_d == (self.dim.1 - 1)
        {
            return 0;
        }

        let range_row_start = row_two_d * self.dim.1;
        let range_row_end = (row_two_d * self.dim.1) + self.dim.1 - 1;
        let range_col_end = (self.dim.0 - 1) * self.dim.1 + col_two_d;

        let me = self.pos[current_pos];

        // Go from right to left
        let left = self.count_trees(
            (range_row_start..current_pos).rev().map(|p| self.pos[p]),
            me,
        );
        let right = self.count_trees((current_pos + 1..=range_row_end).map(|p| self.pos[p]), me);
        // Go from down to up
        let up = self.count_trees(
            (col_two_d..=current_pos - self.dim.1)
                .rev()
                .step_by(self.dim.1)
                .map(|p| self.pos[p]),
            me,
        );
        let down = self.count_trees(
            (current_pos + self.dim.1..=range_col_end)
                .step_by(self.dim.1)
                .map(|p| self.pos[p]),
            me,
        );

        left * right * up * down
    }

    fn max_each_row(&self) -> Vec<usize> {
        self.pos
            .chunks(self.dim.1)
            .enumerate()
            .map(|(idx, chunk)| {
                chunk
                    .iter()
                    .enumerate()
                    .max_by_key(|(_idx, x)| **x)
                    .unwrap()
                    .0
                    + (idx * self.dim.1)
            })
            .collect()
    }

    fn max_each_col(&self) -> Vec<usize> {
        (0..self.dim.1)
            .map(|col| {
                self.pos
                    .iter()
                    .skip(col)
                    .step_by(self.dim.1)
                    .enumerate()
                    .max_by_key(|(_idx, x)| **x)
                    .unwrap()
                    .clone()
                    .0
                    * self.dim.1
                    + col
            })
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    static EX: &str = "30373
25512
65332
33549
35390";

    #[test]
    fn example_1() {
        let grid = parse_input(EX);
        let total = part1(&grid);
        assert_eq!(total, 21);
    }

    #[test]
    fn example_2() {
        let grid = parse_input(EX);
        let total = part2(&grid);
        assert_eq!(total, 8);
    }
}
