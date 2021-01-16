use std::collections::HashSet;
use std::{fs, io};

fn main() -> io::Result<()> {
    let file = fs::read_to_string("in/day08_input.txt")?;
    let ops: Vec<_> = file
        .trim()
        .lines()
        .map(|o| {
            let t: Vec<&str> = o.splitn(2, " ").collect();
            (t[0], t[1].parse::<i32>().unwrap())
        })
        .collect();

    println!("Part one: {}", part_1(&ops));
    println!("Part one: {}", part_2(&ops));

    Ok(())
}

fn run(ops: &Vec<(&str, i32)>) -> (bool, i32) {
    let mut ip = 0usize;
    let mut acc = 0i32;
    let mut visited = HashSet::new();

    while ip < ops.len() {
        if visited.contains(&ip) {
            return (false, acc);
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
                continue;
            }
            _ => unreachable!(),
        }

        ip += 1;
    }

    (true, acc)
}

fn part_1(ops: &Vec<(&str, i32)>) -> i32 {
    let (_, acc) = run(&ops);
    acc
}

fn part_2(ops: &Vec<(&str, i32)>) -> i32 {
    for i in 0..ops.len() {
        if matches!(ops[i].0, "nop" | "jmp") {
            let mut changed = ops.clone();
            changed[i].0 = if ops[i].0 == "nop" { "jmp" } else { "nop" };

            let (r_halt, r_acc) = run(&changed);
            if r_halt {
                return r_acc;
            }
        }
    }

    0
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
        let ops: Vec<_> = EX
            .trim()
            .lines()
            .map(|o| {
                let t: Vec<&str> = o.splitn(2, " ").collect();
                (t[0], t[1].parse::<i32>().unwrap())
            })
            .collect();
        assert_eq!(part_1(&ops), 5);
        assert_eq!(part_2(&ops), 8);
    }
}
