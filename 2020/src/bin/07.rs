use std::{io, fs};
use std::collections::HashMap;

use lazy_static:: lazy_static;
use regex::Regex;

struct InsideBags(u32, String);

fn main() -> io::Result<()> {
    let mut rules: HashMap<String, Option<Vec<InsideBags>>> = HashMap::new();
    let file = fs::read_to_string("input.txt")?;

    file.trim()
        .split("\n")
        .map(|rule| parse_rule(rule))
        .fold(rules, |acc, r| {
            acc.insert(r.0, r.1);
            acc
        });

    Ok(())
}

fn parse_rule(inp: &str) -> (String, Option<Vec<InsideBags>>) {
    lazy_static! {
        static ref BAG_REGEX: Regex = Regex::new(r"([0-9]+) (\w+) bags?\.?").unwrap();
    }

    let rule: Vec<&str> = inp.split(" bags contain ").collect();
    rule[1]
        .split(",")
        .map(|others| {
            match BAG_REGEX.captures(others) {
                Some(caps) => {
                    let num: u32 = caps.get(1).unwrap().as_str().parse().unwrap();
                },
                None => None,
            }
        });
}

mod test {
    use super::*;

    const EX_RULES: &str = "light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
";

    #[test]
    fn example() {

    }
}
