# Problem: Repeated String
# Link:https://www.hackerrank.com/challenges/repeated-string/problem

import time


def repeatedString(s, n):
    a_count_in_string = s.count("a")
    num_full_repeats, remaining_length = divmod(n, len(s))
    total_repeats = num_full_repeats * a_count_in_string + s[:remaining_length].count("a")
    return total_repeats


if __name__ == "__main__":
    string = "a"
    length = 1000000000000
    start_time = time.time()
    result = repeatedString(string, length)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
