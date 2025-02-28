mod day1;
mod day2;
mod utils;

fn main() {
    println!("day 1 part 1 solution: {}", day1::solve_part_1("inputs/day1.txt"));
    println!("day 1 part 2 solution: {}", day1::solve_part_2("inputs/day1.txt"));
    println!("day 2 part 1 solution: {}", day2::solve_part_1("inputs/day2.txt"));
    println!("day 2 part 2 solution: {}", day2::solve_part_2("inputs/day2.txt"));
}
