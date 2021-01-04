use std::{io, fs};

fn main() -> io::Result<()> {
    let file = fs::read_to_string("in/day05_input.txt")?;
    let input = file
        .trim()
        .split_whitespace();

    println!("Part 1: {}", input.clone().map(|code| decode_seat_alt(code)).max().unwrap());

    let mut d: Vec<_> = input.map(|code| decode_seat_alt(code)).collect();
    d.sort();
    let (down, _) = d.iter().zip(d.clone().into_iter().skip(1))
        .filter(|&(a, b)| b != a + 1)
        .next().unwrap();
    println!("Part 2: {}", down + 1);

    Ok(())
}

fn decode_seat_alt(code: &str) -> u32 {
    code.chars()
        .fold(0u32, |acc, half| {
            (acc << 1) | if matches!(half, 'B' | 'R') { 1 } else { 0 }
        })
}

#[allow(dead_code)]
fn decode_seat(code: &str) -> u32 {
    let (row_code, col_code) = code.split_at(7);
    let (mut low, mut high) = (0u32, 127u32);
    let mut last_row = 0u32;

    row_code.chars()
        .for_each(|c| {
            match c {
                'F' => {
                    high = ((high - low) / 2) + low;
                    last_row = low;
                }
                'B' => {
                    low = ((high - low) / 2) + low + 1;
                    last_row = high;
                }
                _ => ()
            }            
        });

    low = 0u32;
    high = 7u32;
    let mut id = 0u32;

    col_code.chars()
        .for_each(|c| {
            match c {
                'L' => {
                    high = ((high - low) / 2) + low;
                    id = last_row * 8 + low;
                }
                'R' => {
                    low = ((high - low) / 2) + low + 1;
                    id = last_row * 8 + high;
                }
                _ => ()
            }
        });
    id
}

#[cfg(test)]
mod tests {
    use super::*;

    aoc2020::decode_tests! {
        decode_seat, ex_1: ("FBFBBFFRLR", 357),
        decode_seat, ex_2: ("BFFFBBFRRR", 567),
        decode_seat, ex_3: ("FFFBBBFRRR", 119),
        decode_seat, ex_4: ("BBFFBBFRLL", 820),
        decode_seat_alt, ex_1_alt: ("FBFBBFFRLR", 357),
        decode_seat_alt, ex_2_alt: ("BFFFBBFRRR", 567),
        decode_seat_alt, ex_3_alt: ("FFFBBBFRRR", 119),
        decode_seat_alt, ex_4_alt: ("BBFFBBFRLL", 820),
    }
}
