use regex::Regex;
use lazy_static::lazy_static;

const RULE_1: &str = "light red bags contain 1 bright white bag, 2 muted yellow bags.";
const RULE_2: &str = "faded blue bags contain no other bags.";
const RULE_3: &str = "bright white bags contain 1 shiny gold bag.";

fn main() {
    lazy_static! {
        static ref BAG_REGEX: Regex = Regex::new(r"([0-9]+) (\w+ \w+) bags?\.?").unwrap();
    }

    let r: Vec<&str> = RULE_2.split(" bags contain ").collect();
    let q: Vec<&str> = RULE_3.split(" bags contain ").collect();

    let x: Vec<&str> = r[1].split(",").collect();
    println!("{:?}", x);

    let z: Vec<&str> = q[1].split(",")
        .inspect(|r| println!("found: {}", r))
        .map(|r| {
            match BAG_REGEX.captures(r) {
                Some(caps) => {
                    let num: u32 = caps.get(1).unwrap().as_str().parse().unwrap();
                    println!("num: {}", num);
                    r
                },
                None => r,
            }
        })
        .collect();

    let caps = BAG_REGEX.captures(z[0]);
    println!("{:?}", caps);
}
