// 2020 - Day 2
//  Part 1 example
//  ---
//  1-3 a: abcde
//  1-3 b: cdefg
//  2-9 c: ccccccccc

use std::io::{Error, ErrorKind, BufRead, BufReader};
use regex::Regex;
use lazy_static::lazy_static;

#[derive(Debug)]
struct Line {
    min: u32,
    max: u32,
    chr: char,
    line: String,
}

fn main() -> std::io::Result<()> {
    let f = std::fs::File::open("in/day02_input.txt")?;
    let mut ls: Vec<Line> = vec![];
    let mut valid: u32 = 0;

    for line in BufReader::new(f).lines() {
        let parsed: Result<Line, Error> = parse_line(line?);
        ls.push(parsed?);
    }

    for line in &ls {
        let c = line.line.matches(line.chr).count() as u32;
        if (line.min..=line.max).contains(&c) {
            valid += 1;
        }
    }
    println!("Part one: {}", valid);

    valid = 0;
    for line in &ls {
        let first = line.line.as_bytes()[line.min as usize - 1] as char;
        let second = line.line.as_bytes()[line.max as usize - 1] as char;

        if (first == line.chr || second == line.chr) &&
            !(first == line.chr && second == line.chr) {
            valid += 1;
        }
    }
    println!("Part two: {}", valid);
    Ok(())
}

fn parse_line(line: String) -> Result<Line, Error> {
    lazy_static! {
        static ref RE: Regex = Regex::new(r"(\d+)-(\d+) ([[:alpha:]]): (.+)").unwrap();
    }
    let caps = RE.captures(&line).unwrap();
    let min: u32 = caps.get(1).unwrap().as_str().parse().map_err(|e| Error::new(ErrorKind::InvalidData, e))?;
    let max: u32 = caps.get(2).unwrap().as_str().parse().map_err(|e| Error::new(ErrorKind::InvalidData, e))?;
    let c: char = caps.get(3).unwrap().as_str().chars().next().unwrap();
    let line = caps.get(4).unwrap().as_str().to_string();

    Ok(Line {
        min,
        max,
        chr: c,
        line,
    })
}
