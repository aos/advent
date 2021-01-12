use std::{io, fs};
use std::collections::HashSet;

fn main() -> io::Result<()> {
    let file = fs::read_to_string("in/day08_input.txt")?;
    let ops: Vec<_> = file.trim()
        .lines()
        .map(|o| {
            let t: Vec<&str> = o.splitn(2, " ").collect();
            (t[0], t[1].parse::<i32>().unwrap())
        })
        .collect();

    println!("Part one: {}", part_1(&ops));
    Ok(())
}

fn part_1(ops: &Vec<(&str, i32)>) -> i32 {
    let mut ip = 0;
    let mut acc = 0i32;
    let mut visited = HashSet::new();

    loop {
        if visited.contains(&ip) {
            return acc;
        }

        visited.insert(ip);
        let (op, value) = ops[ip];
        match op {
            "nop" => (),
            "acc" => acc += value,
            "jmp" => {
                if value.is_negative() {
                    ip -= value.wrapping_abs() as usize;
                } else {
                    ip += value as usize;
                }
                continue
            },
            _ => (),
        }

        ip += 1;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6";

    #[test]
    fn text_example() {
        let ops: Vec<_> = EX.trim()
            .lines()
            .map(|o| {
                let t: Vec<&str> = o.splitn(2, " ").collect();
                (t[0], t[1].parse::<i32>().unwrap())
            })
            .collect();
        assert_eq!(part_1(&ops), 5);
    }
}
