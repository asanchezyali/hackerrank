import time


def arrayManipulation(n, queries):
    array = [0] * n
    for query in queries:
        star_index, end_index, increment = query
        array[star_index - 1] += increment
        if end_index < n:
            array[end_index] -= increment
    max_value = 0
    cumulative_sum = 0
    for value in array:
        cumulative_sum += value
        max_value = max(max_value, cumulative_sum)
    return max_value
    


if __name__ == "__main__":
    start_time = time.time()
    n = 5
    array = [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100],
    ]
    result = arrayManipulation(n, array)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
