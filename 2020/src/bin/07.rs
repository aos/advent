use std::{io, fs};
use std::collections::{HashMap, HashSet};

use lazy_static:: lazy_static;
use regex::Regex;

#[derive(Debug, Eq, PartialEq, Clone)]
struct InnerBags(u32, String);

fn main() -> io::Result<()> {
    let mut rules: HashMap<String, Option<Vec<InnerBags>>> = HashMap::new();
    let file = fs::read_to_string("in/day07_input.txt")?;

    rules = file.trim()
        .split("\n")
        .map(|rule| parse_rule(rule))
        .fold(rules, |mut acc, r| {
            acc.insert(r.0, r.1);
            acc
        });

    println!("Part one: {}", part_1(&rules));

    Ok(())
}

fn parse_rule(inp: &str) -> (String, Option<Vec<InnerBags>>) {
    lazy_static! {
        static ref BAG_REGEX: Regex = Regex::new(r"([0-9]+) (\w+ \w+) bags?\.?").unwrap();
    }

    let rule: Vec<&str> = inp.split(" bags contain ").collect();

    if rule[1].contains("no other") {
        (rule[0].to_string(), None)
    } else {
        let lfh: Vec<InnerBags> = rule[1]
            .split(",")
            .map(|others| {
                match BAG_REGEX.captures(others) {
                    Some(caps) => {
                        let num: u32 = caps.get(1).unwrap().as_str().parse().unwrap();
                        let bags: String = caps.get(2).unwrap().as_str().into();
                        InnerBags(num, bags)
                    },
                    _ => unreachable!(),
                }
            })
            .collect();
        (rule[0].to_string(), Some(lfh))
    }
}

fn part_1(rules: &HashMap<String, Option<Vec<InnerBags>>>) -> u32 {
    // Part 1: Basically we're just trying to find all nodes that
    // eventually lead to "shiny gold" bag
    // Can do a DFS and short-circuit?
    let mut is_gold_container: HashSet<String> = HashSet::new();

    rules.iter()
        .for_each(|(bag_kind, maybe_bags)| {
            if let Some(bags) = maybe_bags {
                let mut to_visit: Vec<String> = bags.iter().cloned().map(|bags| bags.1).collect();
                
                while let Some(next) = to_visit.pop() {
                    if next == "shiny gold" {
                        is_gold_container.insert(bag_kind.to_string());
                        continue;
                    }

                    if let Some(inside_bags) = rules.get(&next).unwrap() {
                        to_visit.extend(inside_bags.iter().cloned().map(|bags| bags.1));
                    }

                }
            }
        });
    
    is_gold_container.len() as u32
}

mod test {
    #[allow(unused_imports)]
    use super::*;

    #[allow(dead_code)]
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
                InnerBags(3, "bright white".to_string()),
                InnerBags(4, "muted yellow".to_string())
            ]))),

        parse_rule, ex_rule_2: (
            "bright white bags contain 1 shiny gold bag.",
            ("bright white".to_string(),
            Some(vec![InnerBags(1, "shiny gold".to_string())]))),

        parse_rule, ex_rule_3: (
            "faded blue bags contain no other bags.",
            ("faded blue".to_string(), None)
        ),
    }

    #[test]
    fn test_example() {
        let mut rules: HashMap<String, Option<Vec<InnerBags>>> = HashMap::new();
        let mut required: HashMap<String, Option<Vec<InnerBags>>> = HashMap::new();

        required.insert(
            "light red".into(),
            Some(vec![InnerBags(1, "bright white".into()), InnerBags(2, "muted yellow".into())])
        );
        required.insert(
            "dark orange".into(),
            Some(vec![InnerBags(3, "bright white".into()), InnerBags(4, "muted yellow".into())])
        );
        required.insert(
            "bright white".into(), Some(vec![InnerBags(1, "shiny gold".into())])
        );
        required.insert(
            "muted yellow".into(),
            Some(vec![InnerBags(2, "shiny gold".into()), InnerBags(9, "faded blue".into())])
        );
        required.insert(
            "shiny gold".into(),
            Some(vec![InnerBags(1, "dark olive".into()), InnerBags(2, "vibrant plum".into())])
        );
        required.insert(
            "dark olive".into(),
            Some(vec![InnerBags(3, "faded blue".into()), InnerBags(4, "dotted black".into())])
        );
        required.insert(
            "vibrant plum".into(),
            Some(vec![InnerBags(5, "faded blue".into()), InnerBags(6, "dotted black".into())])
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

        assert_eq!(part_1(&rules), 4);
    }
}
