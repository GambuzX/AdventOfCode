use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn star1() {
    let mut points = 0i32;
    if let Ok(lines) = read_lines("./input.txt") {
        for res in lines {
            if let Ok(line) = res {
                let split = line.split(' ');
                let vec = split.collect::<Vec<&str>>();

                match vec[0] {
                    "A" => match vec[1] {
                        "X" => points += 1+3,
                        "Y" => points += 2+6,
                        "Z" => points += 3+0,
                        _ => points += 0,
                    },
                    "B" => match vec[1] {
                        "X" => points += 1+0,
                        "Y" => points += 2+3,
                        "Z" => points += 3+6,
                        _ => points += 0,
                    },
                    "C" => match vec[1] {
                        "X" => points += 1+6,
                        "Y" => points += 2+0,
                        "Z" => points += 3+3,
                        _ => points += 0,
                    },
                    _ => points += 0,
                }
            }
        }
    }
    println!("Star 1: {}", points);
}

fn star2() {
    let mut points = 0i32;
    if let Ok(lines) = read_lines("./input.txt") {
        for res in lines {
            if let Ok(line) = res {
                let split = line.split(' ');
                let vec = split.collect::<Vec<&str>>();

                match vec[0] {
                    "A" => match vec[1] {
                        "X" => points += 3+0,
                        "Y" => points += 1+3,
                        "Z" => points += 2+6,
                        _ => points += 0,
                    },
                    "B" => match vec[1] {
                        "X" => points += 1+0,
                        "Y" => points += 2+3,
                        "Z" => points += 3+6,
                        _ => points += 0,
                    },
                    "C" => match vec[1] {
                        "X" => points += 2+0,
                        "Y" => points += 3+3,
                        "Z" => points += 1+6,
                        _ => points += 0,
                    },
                    _ => points += 0,
                }
            }
        }
    }
    println!("Star 2: {}", points);
}

fn main() {
    star1();
    star2();
}
