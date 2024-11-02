use std::time::Instant;

fn hourglass_sum(arr: &[Vec<i32>]) -> i32 {
    let mut max_sum = std::i32::MIN;
    for i in 1..5 {
        for j in 1..5 {
            let sum = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1]
                + arr[i][j]
                + arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1];
            if sum > max_sum {
                max_sum = sum;
            }
        }
    }
    max_sum
}

fn main() {
    let arr = vec![
        vec![1, 1, 1, 0, 0, 0],
        vec![0, 1, 0, 0, 0, 0],
        vec![1, 1, 1, 0, 0, 0],
        vec![0, 0, 2, 4, 4, 0],
        vec![0, 0, 0, 2, 0, 0],
        vec![0, 0, 1, 2, 4, 0],
    ];
    let start = Instant::now();
    let result = hourglass_sum(&arr);
    println!("Result: {}", result);
    println!("Elapsed time: {:?}", start.elapsed());
}
