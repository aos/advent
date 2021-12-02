type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

fn main() -> Result<()> {
    let input = include_str!("../../in/day02_in.txt");

    let (h, d) = run(input);
    println!("{:?}", h * d);
    
    Ok(())
}

fn run(input: &str) -> (usize, usize) {
    input.lines().fold((0, 0), |acc, comm| {
        let split = comm.split(" ").collect::<Vec<&str>>();
        match split[0] {
            "forward" => {
                (acc.0 + split[1].parse::<usize>().unwrap(), acc.1)
            },
            "up" => {
                (acc.0, acc.1 - split[1].parse::<usize>().unwrap())
            },
            "down" => {
                (acc.0, acc.1 + split[1].parse::<usize>().unwrap())
            }
            _ => unreachable!(),
        }
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "forward 5
down 5
forward 8
up 3
down 8
forward 2";

    #[test]
    fn example_1() {
        assert_eq!(run(EX), (15, 10));
    }
}
