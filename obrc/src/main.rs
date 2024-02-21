use std::fs::{read_to_string, File};
use std::io::prelude::*;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

const FILENAME: &'static str = "../../1brc/measurements3.txt";
//const FILENAME: &'static str = "data.csv";

struct Measurment<'a> {
    name: &'a str,
    temp: f64,
}

struct Station {
    temps: Vec<f64>,
}

fn parse_line(line: &str) -> Result<Measurment, String> {
    match line.find(';') {
	Some(pos) => {
	    Ok(Measurment {
		name: &line[0..pos],
		temp: line[pos+1..].parse::<f64>().unwrap(),
	    })
	},
	_ => Err(String::from(format!("Malformed line: {}", line))),
    }
}

fn main() -> std::io::Result<()>{
    let f = File::open(FILENAME)?;
    let reader = BufReader::new(f);
    let mut stations: HashMap<String, Station> = HashMap::new();

    for line in reader.lines() {
	if let Ok(line) = line {
	    let measure = parse_line(&line).unwrap();

	    if let Some(s) = stations.get_mut(measure.name) {
		s.temps.push(measure.temp);
	    } else {
		let s = Station {
		    temps: vec![measure.temp]
		};
		stations.insert(String::from(measure.name), s);
	    }
	    
	} else {
	    panic!("reader err");
	}
    }

    for (n, d) in stations.iter() {
	let temps = &d.temps;
	let min = temps.iter().fold(f64::MAX, |a, &b| f64::min(a, b));
	let max = temps.iter().fold(f64::MIN, |a, &b| f64::max(a, b));
	let avg = temps.iter().fold(0.0, |a, &b| a + b) / temps.len() as f64;

	println!("{n} min {min}, max: {max}, avg {avg}");
    }

    Ok(())
}
