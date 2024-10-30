use std::time::Instant;

fn counting_valleys(steps: i32, path: &str) -> i32 {
    let mut level = 0;
    let mut valley_count = 0;
    for (i, step) in path.chars().enumerate() {
        if i as i32 >= steps {
            break;
        }

        if step == 'U' {
            level += 1;
            if level == 0 {
                valley_count += 1;
            }
        } else {
            level -= 1;
        }
    }

    valley_count
}

fn main() {
    let steps = 8;
    let path = "UDDDUDUU";
    let start = Instant::now();
    let result = counting_valleys(steps, path);
    println!("Result: {}", result);
    println!("Elapsed time: {:?}", start.elapsed());
}
