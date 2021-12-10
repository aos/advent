fn main() {
    let input = include_str!("../../in/day03_in.txt");
    let len = input.lines().next().unwrap().len(); // Get line length
    let gamma = gamma(input);

    println!("part 1: {}", gamma * (!gamma & ((1 << len) - 1)));
    println!("part 2: {}", life_support(input));
}

fn gamma(input: &str) -> u64 {
    let len = input.lines().next().unwrap().len(); // Get line length
    (0..len)
        .map(|n| {
            input
                .lines()
                .map(|l| l.as_bytes()[n])
                .fold(0i64, |a, b| match b {
                    b'0' => a - 1,
                    b'1' => a + 1,
                    _ => unreachable!(),
                })
        })
        .fold(0, |a, b| if b > 0 { a * 2 + 1 } else { a * 2 })
}

fn life_support(input: &str) -> u64 {
    let rating = |most_common: bool| -> u64 {
        let mut seq: Vec<_> = input.lines().collect();
        let mut col = 0;
        while seq.len() > 1 {
            let ones = seq.iter().filter(|l| l.as_bytes()[col] == b'1').count();
            let bit = match (most_common, ones * 2 >= seq.len()) {
                (true, true) | (false, false) => b'1',
                _ => b'0',
            };
            seq = seq
                .into_iter()
                .filter(|l| l.as_bytes()[col] == bit)
                .collect();
            col += 1;
        }
        u64::from_str_radix(seq.first().unwrap(), 2).unwrap()
    };
    let (oxy, co2) = (rating(true), rating(false));
    oxy * co2
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010";

    #[test]
    fn example_1() {
        let len = EX.lines().next().unwrap().len(); // Get line length
        let x = gamma(EX);
        let z = !x & (1 << len) - 1;
        assert_eq!(x * z, 198);
    }

    #[test]
    fn example_2() {
        assert_eq!(230, life_support(EX));
    }
}
