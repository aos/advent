use std::collections::HashMap;
use std::error::Error;
use std::fs;

    const EX: &str = "$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k";

fn main() -> Result<(), Box<dyn Error>> {
    // let f = fs::read_to_string("./in/day07_in.txt")?;
    
    parse(EX);

    Ok(())
}

fn parse(inp: &str) -> usize {
    let cmds = parse_input(inp);

    3
}

fn parse_input(inp: &str) -> Vec<&str> {
    inp.split("\n").collect()
}

enum Input {
    Cd(String),
    Ls,
    DirList(Vec<String>),
}

enum Node {
    Dir {
        children: HashMap<String, Node>,
        total_size: usize,
    },
    File {
        size: usize,
    },
}

impl Node {
    fn new_dir() -> Node {
        Node::Dir {
            children: HashMap::new(),
            total_size: 0,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {}

    #[test]
    fn example_2() {}
}
