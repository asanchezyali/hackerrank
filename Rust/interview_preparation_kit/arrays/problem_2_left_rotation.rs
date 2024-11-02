use std::time::Instant;

fn rot_left(a: &[i32], d: i32) -> Vec<i32> {
  let n = a.len() as i32;
  let d = d % n;
  let mut result = Vec::with_capacity(n as usize);
  let d = d as usize;
  result.extend_from_slice(&a[d..]);
  result.extend_from_slice(&a[..d]);
  result
}

fn main() {
    let a = [1, 2, 3, 4, 5];
    let d = 4;
    let start = Instant::now();
    let result = rot_left(&a, d);
    println!("Result: {:?}", result);
    println!("Elapsed time: {:?}", start.elapsed());
}
