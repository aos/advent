use std::{io, fs};

fn main() -> io::Result<()> {
    let file = fs::read_to_string("in/day09_input.txt")?;
    let input: Vec<u32> = file.trim().lines().map(|l| l.parse().unwrap()).collect();

    solve(&input, 25);
    Ok(())
}

fn solve(nums: &Vec<u32>, pre_len: usize) -> u32 {
    let (head, tail) = (0, pre_len - 1);
    // 1. preamble - 25 numbers
    // 2. every next number -> sum of any two of the 25 immediately previous #s
    0
}

#[cfg(test)]
mod tests {

}
