use std::{env, fs};

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
                    match Some(byr).parse() {

                    }
                },
                _ => false
            }
        })
        .count()
}
