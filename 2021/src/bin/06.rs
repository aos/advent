use aoc2021::Result;

fn main() -> Result<()> {
    let initial = include_str!("../../in/day06_in.txt");
    let fish = parse_input(initial)?;
    println!("part 1: {}", simulate(&fish, 80));
    println!("part 2: {}", simulate(&fish, 256));

    Ok(())
}

fn parse_input(input: &str) -> Result<Vec<usize>> {
    input.trim().split(",").map(|n| Ok(n.parse()?)).collect()
}

fn simulate(fish: &Vec<usize>, days: usize) -> usize {
    let mut schools = fish.iter().fold([0; 9], |mut school, &x| {
        school[x] += 1;
        school
    });
    (0..days).for_each(|i| schools[(i + 7) % 9] += schools[i % 9]);

    schools.iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "3,4,3,1,2";

    #[test]
    fn example_1() {
        let fish = parse_input(EX).unwrap();
        let count = simulate(&fish, 18);
        assert_eq!(count, 26);
    }

    #[test]
    fn example_2() {
        let fish = parse_input(EX).unwrap();
        let count = simulate(&fish, 80);
        assert_eq!(count, 5934);
    }

    #[test]
    fn example_3() {
        let fish = parse_input(EX).unwrap();
        let count = simulate(&fish, 256);
        assert_eq!(count, 26_984_457_539);
    }
}
