use std::time::Instant;

fn sock_merchant(n: i32, ar: &[i32]) -> i32 {
    let mut sock_count = vec![0; 101];
    let mut pair_count = 0;
    for i in 0..n as usize {
        sock_count[ar[i] as usize] += 1;
        if sock_count[ar[i] as usize] % 2 == 0 {
            pair_count += 1;
        }
    }
    pair_count
}

fn main() {
    let n = 9;
    let ar = [10, 20, 20, 10, 10, 30, 50, 10, 20];
    let start = Instant::now();
    let result = sock_merchant(n, &ar);
    println!("Result: {}", result);
    println!("Elapsed time: {:?}", start.elapsed());
}
