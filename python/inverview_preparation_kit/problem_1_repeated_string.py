import time


def repeatedString(string, length):
    a_count_in_pattern = string.count("a")
    num_full_repeats, remaining_length = divmod(length, len(string))
    total_repeats = num_full_repeats * a_count_in_pattern + string[
        :remaining_length
    ].count("a")
    return total_repeats


if __name__ == "__main__":
    pattern_string = "a"
    total_length = 1000000000000
    start_time = time.time()
    result = repeatedString(pattern_string, total_length)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
