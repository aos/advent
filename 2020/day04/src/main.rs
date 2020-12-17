use std::{env, fs};
use regex;

#[derive(Debug, Default)]
struct Passport {
    byr: Option<String>,
    iyr: Option<String>,
    eyr: Option<String>,
    hgt: Option<String>,
    hcl: Option<String>,
    ecl: Option<String>,
    pid: Option<String>,
    cid: Option<String>
}

fn main() -> std::io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let filename = args.get(1).map_or("example.txt", |v| v);

    let file = fs::read_to_string(filename)?;
    let pps: Vec<Passport> = file
        .trim()
        .split("\n\n")
        .map(|p| parse_passport(p))
        .collect();

    println!("part one: {}", part1(&pps));
    println!("part two: {}", part2(&pps));

    Ok(())
}

fn parse_passport(pass: &str) -> Passport {
    pass.split(|c| c == '\n' || c == ' ')
        .into_iter()
        .map(|kv| kv.split(':').collect::<Vec<_>>())
        .fold(Passport{ ..Default::default() }, |mut a, v| {
            match v[0] {
                "byr" => a.byr = Some(v[1].to_string()),
                "iyr" => a.iyr = Some(v[1].to_string()),
                "eyr" => a.eyr = Some(v[1].to_string()),
                "hgt" => a.hgt = Some(v[1].to_string()),
                "hcl" => a.hcl = Some(v[1].to_string()),
                "ecl" => a.ecl = Some(v[1].to_string()),
                "pid" => a.pid = Some(v[1].to_string()),
                "cid" => a.cid = Some(v[1].to_string()),
                _ => ()
            }
            a
        })
}

fn part1(passports: &Vec<Passport>) -> usize {
    passports
        .iter()
        .filter(|p| {
            match p {
                Passport {
                    byr: Some(_),
                    iyr: Some(_),
                    eyr: Some(_),
                    hgt: Some(_),
                    hcl: Some(_),
                    ecl: Some(_),
                    pid: Some(_), .. } => true,
                _ => false
            }
        })
        .count()
}

fn part2(passports: &Vec<Passport>) -> usize {
    let hcl_check = regex::Regex::new(r"#[0-9a-f]{6}").unwrap();
    let ecl_check = regex::Regex::new(r"(amb|blu|brn|gry|grn|hzl|oth)").unwrap();
    let pid_check = regex::Regex::new(r"^[0-9]{9}$").unwrap();

    passports
        .iter()
        .filter(|p| {
            match p {
                Passport {
                    byr: Some(_),
                    iyr: Some(_),
                    eyr: Some(_),
                    hgt: Some(_),
                    hcl: Some(_),
                    ecl: Some(_),
                    pid: Some(_), .. } => true,
                _ => false
            }
        })
        .filter(|p| {
            match p {
                Passport {
                    byr, iyr, eyr, hgt, hcl, ecl, pid, ..
                } => {
                    let mut valid = 0;
                    valid += byr.as_ref()
                        .unwrap()
                        .parse::<usize>()
                        .map_or(0, |n| if (1920..=2002).contains(&n) { 1 } else { 0 });
                    valid += iyr.as_ref()
                        .unwrap()
                        .parse::<usize>()
                        .map_or(0, |n| if (2010..=2020).contains(&n) { 1 } else { 0 });
                    valid += eyr.as_ref()
                        .unwrap()
                        .parse::<usize>()
                        .map_or(0, |n| if (2020..=2030).contains(&n) { 1 } else { 0 });
                    valid += hgt.as_ref()
                        .map_or(0, |h| {
                            if h.ends_with("cm") {
                                h.strip_suffix("cm")
                                    .unwrap()
                                    .parse::<usize>()
                                    .map_or(0, |n| if (150..=193).contains(&n) { 1 } else { 0 })
                            } else if h.ends_with("in") {
                                h.strip_suffix("in")
                                    .unwrap()
                                    .parse::<usize>()
                                    .map_or(0, |n| if (59..=76).contains(&n) { 1 } else { 0 })
                            } else {
                                0
                            }
                        });
                    valid += hcl.as_ref()
                        .map_or(0, |h| {
                            if hcl_check.find_iter(&h).count() > 0 { 1 } else { 0 }
                        });
                    valid += ecl.as_ref()
                        .map_or(0, |e| {
                            if ecl_check.find_iter(&e).count() == 1 { 1 } else { 0 }
                        });
                    valid += pid.as_ref()
                        .map_or(0, |p| {
                            if pid_check.find_iter(&p).count() > 0 { 1 } else { 0 }
                        });

                    valid == 7
                },
            }
        })
        .count()
}
