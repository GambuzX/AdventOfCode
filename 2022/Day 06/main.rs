use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn star1(inp: &String) {
    let mut res = 0;
    for i in 3..inp.len() {
        let c1 = inp.chars().nth(i-3).unwrap();
        let c2 = inp.chars().nth(i-2).unwrap();
        let c3 = inp.chars().nth(i-1).unwrap();
        let c4 = inp.chars().nth(i).unwrap();
        
        let mut s = HashSet::new();
        s.insert(c1);
        s.insert(c2);
        s.insert(c3);
        s.insert(c4);

        if s.len() == 4 {
            res = i+1;
            break;
        }

    }
    println!("Star 1: {}", res);
}

fn star2(inp: &String) {
    let mut res = 0;
    let wsize = 14;
    for i in wsize..inp.len() {
        let mut s = HashSet::new();

        for j in 0..wsize {
            s.insert(inp.chars().nth(i-j).unwrap());
        }

        if s.len() == wsize {
            res = i+1;
            break;
        }

    }
    println!("Star 2: {}", res);
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
    star1(&lines[0]);
    star2(&lines[0]);
}
