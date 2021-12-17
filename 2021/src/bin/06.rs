use aoc2021::Result;

fn main() -> Result<()> {
    let initial = include_str!("../../in/day06_in.txt");
    let mut fish = parse_input(initial)?;
    for _ in 0..80 {
        simulate(&mut fish);
    }
    println!("part 1: {}", fish.len());

    Ok(())
}

fn parse_input(input: &str) -> Result<Vec<usize>> {
    input.trim().split(",").map(|n| Ok(n.parse()?)).collect()
}

fn simulate(fish: &mut Vec<usize>) {
    let mut x = vec![];

    for f in fish {
        if *f == 0 {
            *f = 6;
            x.push(8);
        } else {
            *f -= 1;
        }
    }

    fish.extend(x);
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "3,4,3,1,2";

    #[test]
    fn example_1() {
        let mut fish = parse_input(EX).unwrap();
        for _ in 0..18 {
            fish = simulate(fish);
        }
        assert_eq!(fish.len(), 26);
    }

    #[test]
    fn example_2() {
        let mut fish = parse_input(EX).unwrap();
        for _ in 0..256 {
            fish = simulate(fish);
        }
        assert_eq!(fish.len(), 26984457539);
    }
}
