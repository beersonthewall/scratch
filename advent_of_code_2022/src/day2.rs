enum RPS {
    Rock,
    Paper,
    Scissors,
}

impl RPS {
    fn new(s: &str) -> Self {
	match s {
	    "A" | "X" => RPS::Rock,
	    "B" | "Y" => RPS::Paper,
	    "C" | "Z" => RPS::Scissors,
	    _ => panic!("Unknown Rock-Paper-Scissors choice"),
	}
    }
}
/// A Rock-Paper-Scissors round is scored as followed:
/// Points for which play you made:
/// Playing rock = 1
/// Playing paper = 2
/// Playing scissors = 3
///
/// plus points for the result:
/// win = 6
/// draw = 3
/// loss = 0
fn score(me: RPS, villan: RPS) -> usize {
    match (me, villan) {
        (RPS::Rock, RPS::Rock) => 1 + 3,
	(RPS::Rock, RPS::Paper) => 1 + 0,
	(RPS::Rock, RPS::Scissors) => 1 + 6,

	(RPS::Paper, RPS::Paper) => 2 + 3,
	(RPS::Paper, RPS::Rock) => 2 + 6,
	(RPS::Paper, RPS::Scissors) => 2 + 0,

	(RPS::Scissors, RPS::Scissors) => 3 + 3,
	(RPS::Scissors, RPS::Rock) => 3 + 0,
	(RPS::Scissors, RPS::Paper) => 3 + 6,
    }
}

pub fn solve_part_1(input_path: &str) -> usize {
    let input = super::utils::input_as_string(input_path);
    let mut total_score = 0;
    for round in input.split('\n') {
	let choices: Vec<_> = round.split(' ').collect();
	if choices.len() == 2 {
	    let me = choices[1];
	    let villan = choices[0];
	    total_score += score(RPS::new(me), RPS::new(villan));
	}
    }
    total_score
}

enum RpsResult {
    Win,
    Draw,
    Loss
}

impl RpsResult {
    fn new(s: &str) -> Self {
	match s {
	    "X" => RpsResult::Loss,
	    "Y" => RpsResult::Draw,
	    "Z" => RpsResult::Win,
	    _ => panic!("Unknown result input"),
	}
    }
}

fn make_choice(target_result: RpsResult, villan: &RPS) -> RPS {
    match (target_result, villan) {
	(RpsResult::Win, RPS::Rock) => RPS::Paper,
	(RpsResult::Win, RPS::Paper) => RPS::Scissors,
	(RpsResult::Win, RPS::Scissors) => RPS::Rock,

	(RpsResult::Draw, RPS::Rock) => RPS::Rock,
	(RpsResult::Draw, RPS::Paper) => RPS::Paper,
	(RpsResult::Draw, RPS::Scissors) => RPS::Scissors,

	(RpsResult::Loss, RPS::Rock) => RPS::Scissors,
	(RpsResult::Loss, RPS::Paper) => RPS::Rock,
	(RpsResult::Loss, RPS::Scissors) => RPS::Paper,
    }
}

pub fn solve_part_2(input_path: &str) -> usize {
    let input = super::utils::input_as_string(input_path);
    let mut total_score = 0;
    for round in input.split('\n') {
	let choices: Vec<_> = round.split(' ').collect();
	if choices.len() == 2 {
	    let target_result = RpsResult::new(choices[1]);
	    let villan = RPS::new(choices[0]);
	    let me = make_choice(target_result, &villan);
	    total_score += score(me, villan);
	}
    }
    total_score
}
