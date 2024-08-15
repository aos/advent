use std::collections::HashSet;
use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("in/day04_in.txt")?;
    let part1 = f.lines().filter(|l| fully_contained(l)).count();
    let part2 = f.lines().filter(|l| overlapping(l)).count();

    println!("part 1: {}", part1);
    println!("part 2: {}", part2);

    Ok(())
}

fn fully_contained(inp: &str) -> bool {
    let (first_range, second_range) = inp.split_once(",").expect("should always work");
    let (f1, f2) = get_range(first_range);
    let (s1, s2) = get_range(second_range);
    let set1: HashSet<isize> = HashSet::from_iter(f1..=f2);
    let set2: HashSet<isize> = HashSet::from_iter(s1..=s2);

    set1.is_subset(&set2) || set1.is_superset(&set2)
}

fn overlapping(inp: &str) -> bool {
    let (first_range, second_range) = inp.split_once(",").expect("should always work");
    let (f1, f2) = get_range(first_range);
    let (s1, s2) = get_range(second_range);

    let bounds_1 = (f2 - s1) >= 0;
    let bounds_2 = (s2 - f1) >= 0;

    bounds_1 && bounds_2
}

fn get_range(inp: &str) -> (isize, isize) {
    let (first, second) = inp.split_once("-").expect("should work");
    (
        first.parse::<isize>().expect("first"),
        second.parse::<isize>().expect("second"),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
";

    #[test]
    fn example_1() {
        let res = EX.lines().filter(|line| fully_contained(line)).count();
        assert_eq!(res, 2);
    }

    #[test]
    fn example_2() {
        let res = EX.lines().filter(|l| overlapping(l)).count();
        assert_eq!(res, 4);
    }
}
