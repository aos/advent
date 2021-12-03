type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

fn main() -> Result<()> {
    let input = include_str!("../../in/day02_in.txt");
    println!("part 1: {}", run(input, false));
    println!("part 2: {:?}", run(input, true));

    Ok(())
}

// (forward, depth, aim)
fn run(input: &str, aim: bool) -> usize {
    let (h, d, _) = input.lines()
        .map(|l| l.split_once(" ").unwrap())
        .fold((0, 0, 0), |(f, d, a), (k, v)| {
            match (k, v.parse::<usize>().unwrap()) {
                ("forward", v) => {
                    if aim {
                        (f + v, d + a * v, a)
                    } else {
                        (f + v, d, a)
                    }
                }
                ("up", v) => {
                    if aim {
                        (f, d, a - v)
                    } else {
                        (f, d - v, a)
                    }
                }
                ("down", v) => {
                    if aim {
                        (f, d, a + v)
                    } else {
                        (f, d + v, a)
                    }
                }
                _ => unreachable!(),
            }
        });

    h * d
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
        assert_eq!(run(EX, false), 150);
    }

    #[test]
    fn example_2() {
        assert_eq!(run(EX, true), 900);
    }
}
