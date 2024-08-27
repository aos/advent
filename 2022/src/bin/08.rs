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

    fn max_each_row(&self) -> Vec<u32> {
        self.pos
            .chunks(self.dim.1)
            .map(|chunk| *chunk.iter().max().unwrap_or(&0))
            .collect()
    }

    fn max_each_col(&self) -> Vec<u32> {
        (0..self.dim.1)
            .map(|col| {
                self.pos
                    .iter()
                    .skip(col)
                    .step_by(self.dim.1)
                    .max()
                    .unwrap_or(&0)
                    .clone()
            })
            .collect::<Vec<_>>()
    }

    fn visible_trees(&self) -> usize {
        let mut total = (self.dim.0 * 2) + (self.dim.1 * 2) - 4;
        let max_row = self.max_each_row();
        let max_col = self.max_each_col();

        self.pos.iter().skip(self.dim.1).enumerate().fold(total, |acc, (idx, x)| {
            let (row, col) = self.pos_2d(idx);
            // Skip first and last columns
            if col == 0 || col == self.dim.1 {
                acc
            } else {
            }
        })
    }
}

static EX: &str = "30373
25512
65332
33549
35390";
