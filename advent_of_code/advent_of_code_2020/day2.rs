use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

struct Password {
    lower: u32,
    upper: u32,
    c: char,
    value: String,
}

fn main() {
    let f = File::open("input/day2.txt").expect("Error opening input file.");
    let reader = BufReader::new(f);

    let passwords: Vec<Password> = reader
        .lines()
        .filter_map(|line_result| match line_result {
            Ok(line) => Some(line),
            _ => None,
        })
        .map(|line| {
             let itr = line.chars();
             let mut c = itr.next();
             let mut lower = 0;
             let mut tens = 1;
             // General format is 100-120 a: <variable-length-password>
             while c.is_digit() {
                 lower = lower + c.to_digit(10).unwrap() * tens;
                 tens = tens * 10;
                 c = itr.next();
             }

             if c == '-' {
                 c = itr.next();
             }

             let mut upper = 0;
             tens = 1;
             while c.is_digit() {
                 upper = upper + c.to_digit(10).unwrap() * tens;
                 tens = tens * 10;
                 c = itr.next();
             }

             if c.is_whitespace() {
                 c = itr.next();
             }

             let character = c;
             c = itr.next();

             if c = ':' {
                 c = itr.next();
             }

             if c.is_whitespace() {
                 c = itr.next();
             }

             let mut pword = String::new();
             while !c.is_whitespace() {
                 pword.push(c);
                 c = itr.next();
             }

             Password {
                 lower: lower,
                 upper: upper,
                 c: character,
                 value: pword,
             }
        }).collect();


    let valid_count = passwords.iter().fold(0, |ct, i| {
        ct + 1
    });
    println!("Part 1: {}", valid_count);
}
