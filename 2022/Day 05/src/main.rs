use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex::Regex;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

struct Op {
    n: u32,
    from: usize,
    to: usize,
}

fn get_res(stacks: Vec<Vec<char>>) -> String {
    let mut res : String = String::from("xxxxxxxxx");
    for (i, e) in stacks.iter().enumerate() {
        res.replace_range(i..i+1, &e.last().unwrap().to_string());
    }
    return res;
}

fn star1(ops: &Vec<Op>, originalstacks: &Vec<Vec<char>>) {
    let mut stacks = originalstacks.clone();

    for op in ops {
        for _ in 0..op.n {
            let last = stacks[op.from].pop().unwrap();
            stacks[op.to].push(last);
        }
    }

    println!("Star 1: {}", get_res(stacks));
}

fn star2(ops: &Vec<Op>, originalstacks: &Vec<Vec<char>>) {
    let mut stacks = originalstacks.clone();
    
    for op in ops {
        let mut helper: Vec<char> = Vec::new();
        for _ in 0..op.n {
            let last = stacks[op.from].pop().unwrap();
            helper.push(last);
        }
        for _ in 0..op.n {
            let last = helper.pop().unwrap();
            stacks[op.to].push(last);
        }
    }
    println!("Star 2: {}", get_res(stacks));
}

fn main() {
    let mut lines: Vec<String> = Vec::new();
    if let Ok(lines_inp) = read_lines("./input.txt") {
        for res in lines_inp {
            if let Ok(line) = res {
                lines.push(line);
            }
        }
    }

    let mut ops: Vec<Op> = Vec::new();
    let re = Regex::new(r"move (\d+) from (\d+) to (\d+)").unwrap(); 
    for line in lines {
        for cap in re.captures_iter(&line) {
            ops.push(Op {
                n: cap[1].parse::<u32>().unwrap(),
                from: cap[2].parse::<usize>().unwrap()-1,
                to: cap[3].parse::<usize>().unwrap()-1,
            });
        }
    }

    let stacks: Vec<Vec<char>> = vec![
        vec!['R', 'S', 'L', 'F', 'Q'],
        vec!['N', 'Z', 'Q', 'G', 'P', 'T'],
        vec!['S', 'M', 'Q', 'B'],
        vec!['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'],
        vec!['P', 'H', 'M', 'B', 'N', 'F', 'S'],
        vec!['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'],
        vec!['W', 'C', 'F'],
        vec!['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'],
        vec!['G', 'Z', 'D', 'L', 'C', 'N', 'R'],
    ];

    star1(&ops, &stacks);
    star2(&ops, &stacks);
}
