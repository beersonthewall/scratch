/// Returns a new program with run-length encoding
/// Examples:
///
/// "+ + + + * /" -> "+4 * /"
fn rl_encode_program(program: &str) -> Vec<(char, usize)> {
    let mut i = 0;
    let mut encoded_prog = Vec::new();

    let chars = program.chars();
    for tkn in chars.clone() {
	let mut lookahead = chars.clone();
	let _ = lookahead.next(); // toss whitespace
	let mut snd = lookahead.next();
	let mut ct = 1;
	while snd.is_some() && snd.unwrap() == tkn {
	    ct += 1;
	    lookahead.next(); // toss whitespace
	    snd = lookahead.next();
	}
	encoded_prog.push((tkn, ct));
    }
	
    encoded_prog
}

fn run_program(program: &str) -> usize {
    let mut acc = 0;

    for t in program.chars() {
	match t {
	    '+' => acc += 1,
	    '-' => acc -= 1,
	    '*' => acc *= 2,
	    '/' => acc /= 2,
	    _ => {},
	}
    }
    acc
}

fn main() {
    let program = "+ + * - /";
    let result = run_program(program);
    println!("program: {} calculates {}", program, result);
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_basic_program() {
	let program = "+ + * - /";
	let result = run_program(program);
	assert_eq!(result, 1);
    }

    fn test_rl_encoding_prog() {}
}
