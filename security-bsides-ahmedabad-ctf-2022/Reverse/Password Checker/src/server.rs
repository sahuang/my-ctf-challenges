use std::io::{self, BufRead};

// Bsides{X0R_15_345y_2_D3BUG?}
fn main() {
    let mut password = String::new();
    let stdin = io::stdin();
    stdin.lock().read_line(&mut password).unwrap();
    password = password.trim().to_string();

    if password.len() != 28 {
        println!("Nope.");
        return;
    }

    let result = [396, 870, 667, 761, 645, 866, 789, 545, 282, 629, 725, 282, 317, 726, 309, 317, 289, 796, 717, 267, 719, 395, 317, 407, 521, 426, 485, 822];
    let mut curr = 0x42;
    for i in 0..28 {
        let c = password.chars().nth(i).unwrap() as u32;
        if ((c * 7) ^ curr) != result[i] {
            println!("Nope.");
            return;
        }
        curr += 1;
    }
    println!("Got it.");
    return;
}