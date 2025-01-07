fn main() {
    let program = "+ + * - /";
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

    println!("program: {} calculates {}", program, acc);
}
