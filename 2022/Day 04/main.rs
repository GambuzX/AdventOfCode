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

fn is_contained(l1: u32, h1: u32, l2: u32, h2: u32) -> bool {
    return l1 >= l2 && h1 <= h2;
}

fn overlaps(l1: u32, h1: u32, l2: u32, h2: u32) -> bool {
    return !(h1 < l2 || l1 > h2);
}

fn star1(lines: &Vec<String>) {
    let mut total = 0u32;
    for line in lines {        
        let split = line.split(',');
        let sections = split.collect::<Vec<&str>>();

        let split2 = sections[0].split('-');
        let s1 = split2.collect::<Vec<&str>>();
        let split3 = sections[1].split('-');
        let s2 = split3.collect::<Vec<&str>>();

        let l1 = s1[0].parse::<u32>().unwrap();
        let h1 = s1[1].parse::<u32>().unwrap();
        let l2 = s2[0].parse::<u32>().unwrap();
        let h2 = s2[1].parse::<u32>().unwrap();

        if is_contained(l1,h1,l2,h2) || is_contained(l2,h2,l1,h1) {
            total += 1;
        }
    }
    println!("Star 1: {}", total);
}

fn star2(lines: &Vec<String>) {
    let mut total = 0u32;
    for line in lines {        
        let split = line.split(',');
        let sections = split.collect::<Vec<&str>>();

        let split2 = sections[0].split('-');
        let s1 = split2.collect::<Vec<&str>>();
        let split3 = sections[1].split('-');
        let s2 = split3.collect::<Vec<&str>>();

        let l1 = s1[0].parse::<u32>().unwrap();
        let h1 = s1[1].parse::<u32>().unwrap();
        let l2 = s2[0].parse::<u32>().unwrap();
        let h2 = s2[1].parse::<u32>().unwrap();

        if overlaps(l1,h1,l2,h2) {
            total += 1;
        }
    }
    println!("Star 2: {}", total);
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
    star1(&lines);
    star2(&lines);
}
