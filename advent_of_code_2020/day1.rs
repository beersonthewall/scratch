use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;

fn part1(nums: &[usize]) -> Option<usize> {
    for i in nums {
        for j in nums {
            if i + j == 2020 {
                return Some(i * j);
            }
        }
    }
    None
}

fn part2(nums: &[usize]) -> Option<usize> {
    for i in nums {
        for j in nums {
            for k in nums {
                if i + j + k == 2020 {
                    return Some(i * j * k);
                }
            }
        }
    }
    None
}

fn main() {
    let f = File::open("input/day1.txt").expect("Error opening file");
    let reader = BufReader::new(f);
    let mut nums: Vec<usize> = Vec::new();
    for line in reader.lines() {
        if let Ok(l) = line {
            nums.push(l.parse().expect("Not a number"));
        }
    }

    println!("Part 1: {}", part1(&nums).unwrap());
    println!("Part 2: {}", part2(&nums).unwrap());
}
