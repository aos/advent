use std::collections::HashSet;
use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("in/day05_in.txt")?;

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
";

    #[test]
    fn example_1() {
    }

    #[test]
    fn example_2() {
    }
}
