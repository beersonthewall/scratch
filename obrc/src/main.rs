use std::fs::File;
use std::io::{prelude::*, BufWriter};
use std::io::{BufReader, stdout};
use std::collections::HashMap;
use std::sync::{Arc, Mutex};

const FILENAME: &'static str = "../../1brc/measurements3.txt";
const NUM_WORKERS: usize = 20;
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

fn worker(input: Arc<Vec<String>>, start: usize, sz: usize, shared_stations: Arc<Mutex<HashMap<String, Station>>>) {
    let mut stations = HashMap::new();
    let input = &input[start..start + sz];
    for line in input {
	let measure = parse_line(&line).unwrap();
	let s = stations.entry(String::from(measure.name)).or_insert_with(|| Station { temps: vec![] });
	s.temps.push(measure.temp);
    }
    let mut results = shared_stations.lock().unwrap();
    (*results).extend(stations);
}

fn main() -> std::io::Result<()>{
    let f = File::open(FILENAME)?;
    let reader = BufReader::new(f);
    let stations = Arc::new(Mutex::new(HashMap::new()));

    let raw: Arc<Vec<String>> = Arc::new(reader.lines().filter(|l| l.is_ok()).map(|ok| ok.unwrap()).collect());
    let chunks_sz = raw.len() / NUM_WORKERS;

    let mut handles = Vec::new();

    for offset in (0..raw.len()).step_by(chunks_sz) {
	let stations = stations.clone();
	let raw = raw.clone();
	handles.push(std::thread::spawn(move || {
	    worker(raw, offset, chunks_sz, stations)
	}));
    }

    for h in handles {
	h.join().unwrap();
    }

    let stations = stations.lock().unwrap();
    let stdout = stdout().lock();
    let mut stream = BufWriter::new(stdout);
    write!(stream, "{}", "{")?;
    let mut itr = stations.iter().peekable();
    while let Some((n,d)) = itr.next() {
	let temps = &d.temps;
	let min = temps.iter().fold(f64::MAX, |a, &b| f64::min(a, b));
	let max = temps.iter().fold(f64::MIN, |a, &b| f64::max(a, b));
	let avg = temps.iter().fold(0.0, |a, &b| a + b) / temps.len() as f64;

	write!(stream, "{n}={min}/{avg}/{max}")?;
	if let Some(_) = itr.peek() {
	    write!(stream, ",")?;
	}
    }
    write!(stream, "{}", '}')?;
    stream.flush()?;

    Ok(())
}
