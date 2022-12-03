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

fn priority(c: char) -> u32 {
    if c.is_lowercase() {
        return c as u32 - 'a' as u32 + 1;
    }
    return c as u32 - 'A' as u32 + 27;
}

fn star1() {
    let mut total = 0u32;
    if let Ok(lines) = read_lines("./input.txt") {
        for res in lines {
            if let Ok(line) = res {
                let l = line.len();
                let mut first_compartment = HashSet::new();
                for i in 0..l/2 {
                    first_compartment.insert(line.chars().nth(i).unwrap());
                }

                for i in l/2..l {
                    let c = line.chars().nth(i).unwrap();
                    //println!("{}", c);
                    if first_compartment.contains(&c) {
                        total += priority(c);
                        break;
                    }
                }
            }
        }
    }
    println!("Star 1: {}", total);
}

fn star2() {
    let mut total = 0u32;
    let mut first_group = HashSet::new();
    let mut second_group = HashSet::new();
    let mut iter = 0;
    if let Ok(lines) = read_lines("./input.txt") {
        for res in lines {
            if let Ok(line) = res {
                
                if iter % 3 == 0 {
                    for c in line.chars() {
                        first_group.insert(c);
                    }
                }
                else if iter % 3 == 1 {
                    for c in line.chars() {
                        if first_group.contains(&c) {
                            second_group.insert(c);
                        }
                    }
                }
                else if iter % 3 == 2 {
                    for c in line.chars() {
                        if second_group.contains(&c) {
                            total += priority(c);
                            break;
                        }
                    }
                    first_group.clear();
                    second_group.clear();
                }
                iter += 1;
            }
        }
    }
    println!("Star 2: {}", total);
}

fn main() {
    star1();
    star2();
}
