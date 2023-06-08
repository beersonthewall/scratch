fn popcount(num: usize) -> usize {
    let mut num = num;
    let mut count = 0;
    while num > 0 {
	// Kernighan's trick: num - 1 unsets the least significant bit.
	// This causes us to loop only once for every set bit.
	num = num & (num - 1);
	count += 1;
    }
    return count;
}

fn main() {
    println!("{}", popcount(110123));
}
