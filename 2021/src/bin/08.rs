use aoc2021::Result;

fn main() -> Result<()> {

    Ok(())
}

fn parse(input: &str) -> Result<(Vec<&str>, Vec<&str>)> {
    let (signals, output) = input.split_once(" | ").ok_or("no line")?;
}
