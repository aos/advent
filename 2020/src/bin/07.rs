use std::{io, fs};

fn main() -> io::Result<()> {
    let file = fs::read_to_string("input.txt")?;

    // model as graph
    // topological sort
    Ok(())
}
