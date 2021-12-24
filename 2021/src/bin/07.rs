use aoc2021::Result;

fn main() -> Result<()> {
    let crabs = parse(include_str!("../../in/day07_in.txt"))?;
    println!("part 1: {}", fuel(&crabs, |n| n));
    println!("part 2: {}", fuel(&crabs, |n| n*(n+1) / 2));

    Ok(())
}

fn parse(input: &str) -> Result<Vec<usize>> {
    let crabs: Result<Vec<usize>> = input.trim().split(",").map(|n| Ok(n.parse()?)).collect();
    let max = crabs.as_ref().unwrap().iter().max().unwrap().clone();
    let schools = crabs?.iter().fold(vec![0; max + 1], |mut school, &x| {
        school[x] += 1;
        school
    });
    Ok(schools)
}

fn fuel(schools: &Vec<usize>, aug: fn(isize) -> isize) -> isize {
    let mut min = isize::MAX;
    for (pos, _) in schools.iter().enumerate() {
        let mut tot = 0;
        for (i, n) in schools.iter().enumerate() {
            let distance = (i as isize - pos as isize).abs();
            let fuel = aug(distance) * *n as isize;
            tot += fuel;
        }
        if tot < min {
            min = tot
        };
    }
    min
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "16,1,2,0,4,2,7,1,2,14";

    #[test]
    fn example_1() {
        let z = parse(EX).unwrap();
        assert_eq!(37, fuel(&z, |n| n));
    }

    #[test]
    fn example_2() {
        let z = parse(EX).unwrap();
        assert_eq!(168, fuel(&z, |n| n*(n+1) / 2));
    }
}
