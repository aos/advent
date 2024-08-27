use std::io;

fn main() -> io::Result<()> {
    let z = parse_input(EX);

    let max_row = z.max_each_row();
    let max_col = z.max_each_col();

    println!("row: {:?}, col: {:?}", max_row, max_col);

    Ok(())
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

impl Grid {
    fn pos_at(&self, row: usize, col: usize) -> u32 {
        assert!(row < self.dim.0);
        assert!(col < self.dim.1);

        self.pos[self.dim.1 * row + col]
    }

    fn pos_2d(&self, idx: usize) -> (usize, usize) {
        assert!(idx < self.pos.len());
        (idx / self.dim.1, idx % self.dim.1)
    }

    // position of max item on each row
    fn max_each_row(&self) -> Vec<usize> {
        self.pos
            .chunks(self.dim.1)
            .enumerate()
            .map(|(idx, chunk)| {
                chunk
                    .iter()
                    .enumerate()
                    .max_by_key(|(_idx, x)| **x).unwrap()
                    .0 + (idx * self.dim.1)
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
                    .max_by_key(|(_idx, x)| **x).unwrap()
                    .clone()
                    .0 * self.dim.1 + col
            })
            .collect()
    }

    fn _visible_trees(&self) -> usize {
        let mut total = (self.dim.0 * 2) + (self.dim.1 * 2) - 4;
        let max_row = self.max_each_row();
        let max_col = self.max_each_col();

        self.pos.iter().skip(self.dim.1).enumerate().fold(total, |acc, (idx, x)| {
            let (row, col) = self.pos_2d(idx);
            // Skip first and last columns
            if col == 0 || col == self.dim.1 {
                acc
            } else {
                acc
            }
        })
    }
}

static EX: &str = "30373
25512
65332
33549
35390";
