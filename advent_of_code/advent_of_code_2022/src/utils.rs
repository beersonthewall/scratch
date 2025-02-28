use std::io::Read;

pub fn input_as_string(input_path: &str) -> String {
    let mut f = std::fs::File::open(input_path).unwrap();
    let file_len = f.metadata().unwrap().len() as usize;
    let mut input = String::with_capacity(file_len);
    f.read_to_string(&mut input).unwrap();
    input
}
