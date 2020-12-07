use std::fs;

const SUM: usize = 2020;

fn main() {
    let input: Vec<usize> = fs::read_to_string("input.txt").unwrap()
        .lines()
        .map(|l| l.parse().unwrap())
        .collect();

    let max = *input.iter().max().unwrap();
    let min = *input.iter().min().unwrap();
    let mut big = vec![false; max + 1];

    for &i in &input {
        big[i] = true;
    }

    for &i in &input {
        let diff = SUM - i;

        if big[diff] {
            println!("Part one: {} * {} = {}", i, diff, i * diff);
            break;
        }
    }

    for &i in &input {
        let diff = SUM - i;

        // skip if difference cannot be made up by more than 1 number
        if diff <= min {
            continue;
        }

        for &j in &input {
            if j >= diff {
                continue;
            }

            let second_diff = diff - j;

            if big[second_diff] {
                println!("Part two: {} * {} * {} = {}", i, j, second_diff, i * j * second_diff);
                return;
            }
        }
    }
}
