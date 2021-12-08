fn main() {
    let input = include_str!("../../in/day03_in.txt");
    let len = input.lines().next().unwrap().len(); // Get line length
    let gamma = gamma(input);
    let epsilon = !gamma & (1 << len) - 1;

    println!("part 1: {}", gamma * epsilon);
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

fn bit_count(input: &Vec<Vec<u8>>) -> Vec<i64> {
    let len = input.iter().next().unwrap().len(); // Get line length
    (0..len)
        .map(|n| {
            input
                .iter()
                .map(|l| l[n])
                .fold(0i64, |a, b| match b {
                    b'0' => a - 1,
                    b'1' => a + 1,
                    _ => unreachable!(),
                })
        })
        .collect()
}

fn life_support(input: &str) -> u64 {
    let len = input.lines().next().unwrap().len(); // Get line length
    let ins: Vec<Vec<u8>> = input.lines().map(|l| l.as_bytes().to_vec()).collect();
    let mut oxygen = vec![true; ins.len()];
    let mut co2 = vec![true; ins.len()];

    for n in 0..len {
        let mut ins_cloned = ins.clone();
        let mut oxy_iter = oxygen.iter();
        ins_cloned.retain(|_| *oxy_iter.next().unwrap());

        let z = if bit_count(&ins_cloned)[n] >= 0 { 49 } else { 48 }; // more 1s than 0s

        for (i, v) in ins.iter().enumerate() {
            if v[n] != z {
                if oxygen.iter().filter(|&&x| x).count() > 1 {
                    oxygen[i] = false;
                }
            }
        }

        let mut ins_co2_cloned = ins.clone();
        let mut co2_iter = co2.iter();
        ins_co2_cloned.retain(|_| *co2_iter.next().unwrap());
        let w = if bit_count(&ins_co2_cloned)[n] >= 0 { 48 } else { 49 }; // reverse it

        for (i, v) in ins.iter().enumerate() {
            if v[n] != w {
                if co2.iter().filter(|&&x| x).count() > 1 {
                    co2[i] = false;
                }
            }
        }
    }

    let mut zyyy = 0u64;
    let mut zyy = 0u64;
    if let Some(idx) = oxygen.iter().position(|&x| x) {
        let mut yyy = ins[idx].clone();
        zyyy = yyy.iter_mut().fold(0, |a, b| if *b == b'1' { a * 2 + 1 } else { a * 2 });
    }
    if let Some(idx) = co2.iter().position(|&x| x) {
        let mut yyy = ins[idx].clone();
        zyy = yyy.iter_mut().fold(0, |a, b| if *b == b'1' { a * 2 + 1 } else { a * 2 });
    }

    zyyy * zyy
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
