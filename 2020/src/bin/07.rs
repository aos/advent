use std::{io, fs};
use std::collections::HashMap;

use lazy_static:: lazy_static;
use regex::Regex;

#[derive(Debug, Eq, PartialEq)]
struct InsideBags(u32, String);

fn main() -> io::Result<()> {
    let mut rules: HashMap<String, Option<Vec<InsideBags>>> = HashMap::new();
    let file = fs::read_to_string("in/input.txt")?;

    rules = file.trim()
        .split("\n")
        .map(|rule| parse_rule(rule))
        .fold(rules, |mut acc, r| {
            acc.insert(r.0, r.1);
            acc
        });

    Ok(())
}

fn parse_rule(inp: &str) -> (String, Option<Vec<InsideBags>>) {
    lazy_static! {
        static ref BAG_REGEX: Regex = Regex::new(r"([0-9]+) (\w+ \w+) bags?\.?").unwrap();
    }

    let rule: Vec<&str> = inp.split(" bags contain ").collect();

    if rule[1].contains("no other") {
        (rule[0].to_string(), None)
    } else {
        let lfh: Vec<InsideBags> = rule[1]
            .split(",")
            .map(|others| {
                match BAG_REGEX.captures(others) {
                    Some(caps) => {
                        let num: u32 = caps.get(1).unwrap().as_str().parse().unwrap();
                        let bags: String = caps.get(2).unwrap().as_str().into();
                        InsideBags(num, bags)
                    },
                    _ => unreachable!(),
                }
            })
            .collect();
        (rule[0].to_string(), Some(lfh))
    }
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

    aoc2020::decode_tests! {
        parse_rule, ex_rule_1: (
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            ("dark orange".to_string(),
            Some(vec![
                InsideBags(3, "bright white".to_string()),
                InsideBags(4, "muted yellow".to_string())
            ]))),

        parse_rule, ex_rule_2: (
            "bright white bags contain 1 shiny gold bag.",
            ("bright white".to_string(),
            Some(vec![InsideBags(1, "shiny gold".to_string())]))),

        parse_rule, ex_rule_3: (
            "faded blue bags contain no other bags.",
            ("faded blue".to_string(), None)
        ),
    }

    #[test]
    fn test_example() {
        let mut rules: HashMap<String, Option<Vec<InsideBags>>> = HashMap::new();
        let mut required: HashMap<String, Option<Vec<InsideBags>>> = HashMap::new();

        required.insert(
            "light red".into(),
            Some(vec![InsideBags(1, "bright white".into()), InsideBags(2, "muted yellow".into())])
        );
        required.insert(
            "dark orange".into(),
            Some(vec![InsideBags(3, "bright white".into()), InsideBags(4, "muted yellow".into())])
        );
        required.insert(
            "bright white".into(), Some(vec![InsideBags(1, "shiny gold".into())])
        );
        required.insert(
            "muted yellow".into(),
            Some(vec![InsideBags(2, "shiny gold".into()), InsideBags(9, "faded blue".into())])
        );
        required.insert(
            "shiny gold".into(),
            Some(vec![InsideBags(1, "dark olive".into()), InsideBags(2, "vibrant plum".into())])
        );
        required.insert(
            "dark olive".into(),
            Some(vec![InsideBags(3, "faded blue".into()), InsideBags(4, "dotted black".into())])
        );
        required.insert(
            "vibrant plum".into(),
            Some(vec![InsideBags(5, "faded blue".into()), InsideBags(6, "dotted black".into())])
        );
        required.insert("faded blue".into(), None);
        required.insert("dotted black".into(), None);

        rules = EX_RULES
            .trim()
            .split("\n")
            .map(|rule| parse_rule(rule))
            .fold(rules, |mut acc, r| {
                acc.insert(r.0, r.1);
                acc
            });

        assert_eq!(rules, required);
    }
}
