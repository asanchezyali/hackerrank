pub fn repeat_string(s: &str, n: i64) -> i64 {
  let a_count_in_string = s.chars().filter(|&c| c == 'a').count() as i64;
  let (num_full_repeat, remaining_length) = (n / s.len() as i64, n % s.len() as i64);
  let total_repeats = num_full_repeat * a_count_in_string
      + s.chars()
          .take(remaining_length as usize)
          .filter(|&c| c == 'a')
          .count() as i64;
  total_repeats
}