pub fn solve_part_1(input_path: &str) -> usize {
    let mut index = 0;
    let mut sums: Vec<usize> = vec![0];
    let mut max = 0;

    // Split on newline, empty lines are preserved as ""
    for e in super::utils::input_as_string(input_path).split('\n') {
	// Sum each elf while not an empty line
	if !e.is_empty() {
	    sums[index] += e.parse::<usize>().unwrap();
	    continue;
	}

	// Keep a running maximum so we don't traverse twice
	if sums[index] > max {
	    max = sums[index];
	}

	// ensure next vec entry exists
	sums.push(0);
	index += 1;
    }

    max
}

pub fn solve_part_2(input_path: &str) -> usize {
    let mut index = 0;
    let mut sums: Vec<usize> = vec![0];

    // Split on newline, empty lines are preserved as ""
    for e in super::utils::input_as_string(input_path).split('\n') {
	// Sum each elf while not an empty line
	if !e.is_empty() {
	    sums[index] += e.parse::<usize>().unwrap();
	    continue;
	}

	// ensure next vec entry exists
	sums.push(0);
	index += 1;
    }

    sums.sort();
    sums[sums.len() - 1] + sums[sums.len() - 2] + sums[sums.len() - 3]
}
