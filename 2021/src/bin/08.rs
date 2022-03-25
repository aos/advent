use aoc2021::Result;

fn main() -> Result<()> {
    let input = include_str!("../../in/day08_in.txt");
    Ok(())
}

fn parse(input: &str) -> Result<Vec<(Vec<&str>, Vec<&str>)>> {
    Ok(input
        .lines()
        .map(|l| l.split_once(" | ")
                    .ok_or("no line")?.map(|(sig_raw, out_raw)|
                        (sig_raw.split_whitespace().collect(), out_raw.split_whitespace().collect()))))
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX: &str = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce";

    #[test]
    fn example1_() {
    }
}
