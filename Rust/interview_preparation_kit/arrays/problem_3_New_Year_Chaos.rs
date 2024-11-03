use std::time::Instant;

fn minimum_bribes(q:&[i32]) {
    let mut bribes = 0;
    for i in (0..q.len()).rev() {
        let pos = i + 1;
        let expected = pos as i32;
        let actual = q[i];
        if actual - expected > 2 {
            println!("Too chaotic");
            return;
        }
        let start = if actual - 2 > 0 { actual - 2 } else { 0 };
        let end = i as i32;
        for j in start..end {
            if q[j as usize] > actual {
                bribes += 1;
            }
        }
    }
    println!("{}", bribes);
}

fn main() {
    let q = [2, 1, 5, 3, 4];
    let start = Instant::now();
    minimum_bribes(&q);
    println!("Elapsed time: {:?}", start.elapsed());
}
