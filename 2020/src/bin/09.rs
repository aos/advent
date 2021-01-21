use std::{io, fs};

fn main() -> io::Result<()> {
    let file = fs::read_to_string("in/day09_input.txt")?;
    let input: Vec<usize> = file.trim().lines().map(|l| l.parse().unwrap()).collect();

    let invalid_num = find_invalid(&input, 25);
    println!("Part one: {}", invalid_num);
    println!("Part two: {}", find_weakness(&input, invalid_num));
    Ok(())
}

fn find_invalid(nums: &Vec<usize>, pre_len: usize) -> usize {
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

fn find_weakness(nums: &Vec<usize>, invalid: usize) -> usize {
    for i in 0..nums.len()-1 {
        let mut current_sum = nums[i];

        for j in i+1..nums.len() {
            current_sum += nums[j];

            if current_sum == invalid {
                let mut range = vec![0; j-i+1];
                range.clone_from_slice(&nums[i..=j]);
                range.sort();
                return range.first().unwrap() + range.last().unwrap();
            }
        }
    };
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
        assert_eq!(find_invalid(&input, 5), 127);
    }

    #[test]
    fn text_example_2() {
        let input: Vec<usize> = EX.trim().lines().map(|l| l.parse().unwrap()).collect();
        let invalid = find_invalid(&input, 5);
        assert_eq!(find_weakness(&input, invalid), 62);
    }
}
