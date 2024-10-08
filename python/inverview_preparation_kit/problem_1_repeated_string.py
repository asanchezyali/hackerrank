import time

def repeatedString(pattern_string, total_length):
    a_count_in_pattern = pattern_string.count("a")
    num_full_repeats, remaining_length = divmod(total_length, len(pattern_string))
    total_a_in_length = num_full_repeats * a_count_in_pattern + pattern_string[:remaining_length].count("a")
    return total_a_in_length

if __name__ == "__main__":
    pattern_string = "a"
    total_length = 1000000000000
    start_time = time.time()
    result = repeatedString(pattern_string, total_length)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
