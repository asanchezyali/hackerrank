use std::time::Instant;

fn jumping_on_clouds(c: &[i32]) -> i32 {
    let mut jumps = 0;
    let mut i = 0;
    let n = c.len();
    while i < n - 1 {
        if i + 2 < c.len() && c[i + 2] == 0 {
            i += 2;
        } else {
            i += 1;
        }
        jumps += 1;
    }
    jumps
}

fn main() {
    let c = [0, 0, 1, 0, 0, 1, 0];
    let start = Instant::now();
    let result = jumping_on_clouds(&c);
    println!("Result: {}", result);
    println!("Elapsed time: {:?}", start.elapsed());
}
