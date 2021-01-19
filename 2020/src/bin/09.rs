use std::{io, fs};

fn main() -> io::Result<()> {
    let file = fs::read_to_string("in/day09_input.txt")?;
    let input: Vec<usize> = file.trim().lines().map(|l| l.parse().unwrap()).collect();

    println!("Part one: {}", solve(&input, 25));
    Ok(())
}

fn solve(nums: &Vec<usize>, pre_len: usize) -> usize {
    let (mut head, mut tail) = (0, pre_len - 1);
    let mut next = tail + 1;

    while tail < nums.len() {
        let mut valid = false;
        // window
        let x = &nums[head..=tail];
        for i in x {
            let diff = nums[next].checked_sub(*i);
            match diff {
                Some(val) => {
                    if x.contains(&val) {
                        valid = true;
                        break;
                    }
                },
                None => ()
            }
        }

        if !valid {
            return nums[next];
        }

        head += 1;
        tail += 1;
        next += 1;
    }

    0
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576";

    #[test]
    fn text_example_1() {
        let input: Vec<usize> = EX.trim().lines().map(|l| l.parse().unwrap()).collect();
        assert_eq!(solve(&input, 5), 127);
    }

    fn text_example_2() {
        let input: Vec<usize> = EX.trim().lines().map(|l| l.parse().unwrap()).collect();
    }
}
