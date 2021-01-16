fn main() {
    let f = "nop +0\nacc -3\njmp +4\n";
    let z: Vec<_> = f.lines().collect();
    println!("{:?}", z);

    let y: Vec<_> = z
        .iter()
        .map(|o| {
            let t: Vec<&str> = o.splitn(2, " ").collect();
            println!("{:?}", t);
            (t[0], t[1].parse::<i32>().unwrap())
        })
        .collect();
    println!("{:?}", y);
}
