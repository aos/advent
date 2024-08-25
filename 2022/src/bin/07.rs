use std::collections::HashMap;
use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let f = fs::read_to_string("./in/day07_in.txt")?;
    let mut root = parse(&f);
    let total_dir_size = root.calculate_dir_sizes();

    let total_sizes = root.find_dirs_size_most(100_000);
    println!("part 1: {total_sizes}");

    let mut dir_sizes = Vec::new();
    root.collect_dir_sizes(&mut dir_sizes);
    println!("part 2: {}", part2(dir_sizes, total_dir_size));

    Ok(())
}

fn part2(dir_sizes: Vec<usize>, total_dir_size: usize) -> usize {
    let required = 30_000_000 - (70_000_000 - total_dir_size);
    let min = dir_sizes.iter().filter(|v| **v >= required).min().unwrap();
    *min
}

fn parse(inp: &str) -> Node {
    let lines: Vec<&str> = inp.trim().split("\n").collect();
    let mut root = Node::new_dir();
    let mut current_path = Vec::new();

    for line in &lines {
        if line.starts_with('$') {
            let line = line.trim_start_matches('$').trim();
            if line.starts_with("cd") {
                match line.split_whitespace().nth(1).unwrap() {
                    "/" => {
                        current_path.clear();
                    }
                    ".." => {
                        current_path.pop();
                    }
                    dir => {
                        current_path.push(dir);
                    }
                }
            }
        } else {
            let (first, name) = line.split_once(' ').unwrap();
            let node = match first {
                "dir" => Node::new_dir(),
                size => Node::File {
                    size: size.parse().unwrap(),
                },
            };
            root.children_at(&current_path)
                .entry(name.to_string())
                .or_insert(node);
        }
    }

    root
}

#[derive(Clone, Debug)]
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

    fn children(&mut self) -> &mut HashMap<String, Node> {
        match self {
            Node::Dir { children, .. } => children,
            Node::File { .. } => panic!("files have no children"),
        }
    }

    fn children_at(&mut self, path: &[&str]) -> &mut HashMap<String, Node> {
        if let Some((&first, rest)) = path.split_first() {
            self.children()
                .entry(first.to_owned())
                .or_insert_with(Node::new_dir)
                .children_at(rest)
        } else {
            self.children()
        }
    }

    fn calculate_dir_sizes(&mut self) -> usize {
        match *self {
            Node::File { size } => size,
            Node::Dir {
                ref mut total_size,
                ref mut children,
            } => {
                for (_name, node) in children.iter_mut() {
                    *total_size += node.calculate_dir_sizes();
                }
                *total_size
            }
        }
    }

    fn collect_dir_sizes(&self, dirs: &mut Vec<usize>) {
        match *self {
            Node::Dir {
                ref children,
                total_size,
            } => {
                dirs.push(total_size);
                children
                    .values()
                    .for_each(|node| node.collect_dir_sizes(dirs));
            }
            Node::File { .. } => {}
        }
    }

    fn find_dirs_size_most(&self, most: usize) -> usize {
        match *self {
            Node::Dir {
                total_size,
                ref children,
            } => {
                let mut total = 0;
                if total_size <= most {
                    total += total_size;
                };
                for (_name, node) in children.iter() {
                    total += node.find_dirs_size_most(most);
                }

                total
            }
            Node::File { .. } => 0,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    static EX: &str = "$ cd /
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

    #[test]
    fn example_1() {
        let mut root = parse(EX);
        root.calculate_dir_sizes();
        let total_sizes = root.find_dirs_size_most(100_000);
        assert_eq!(total_sizes, 95437);
    }

    #[test]
    fn example_2() {
        let mut root = parse(EX);
        let total_dir_size = root.calculate_dir_sizes();
        let mut dir_sizes = Vec::new();
        root.collect_dir_sizes(&mut dir_sizes);
        let min = part2(dir_sizes, total_dir_size);
        assert_eq!(min, 24933642);
    }
}
