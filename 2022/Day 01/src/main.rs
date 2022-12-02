extern crate priority_queue;

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use priority_queue::PriorityQueue;

fn main() {
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("./input.txt") {
        
        let mut id = 0;
        let mut curr = 0;
        let mut pq = PriorityQueue::new();

        // Consumes the iterator, returns an (Optional) String
        for res in lines {
            if let Ok(line) = res {
                if line == "" || line == "\n" {
                    pq.push(id, curr);
                    id += 1;
                    curr = 0;
                    continue;
                }

                curr += line.parse::<i32>().unwrap();
            }
        }

        let m1 = pq.pop().unwrap();
        let m2 = pq.pop().unwrap();
        let m3 = pq.pop().unwrap();
        println!("The max value is {}", m1.1);
        println!("The top3 total is {}", m1.1+m2.1+m3.1);
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
