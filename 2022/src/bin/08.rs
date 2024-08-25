use std::io;

fn main() -> io::Result<()> {
    let z = parse_input(EX);

    println!("should be 0 -> {}", z.pos_at(4, 4));

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

    fn max_each_row(&self) -> Vec<u32> {
    }

    fn max_each_col(&self) -> Vec<u32> {
    }
}

static EX: &str = "30373
25512
65332
33549
35390";
