import time


def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr):
        correct_pos = arr[i] - 1
        if arr[i] != arr[correct_pos]:
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
            swaps += 1
        else:
            i += 1
    return swaps


if __name__ == "__main__":
    start_time = time.time()
    a = [2, 1, 5, 3, 4]
    result = minimumSwaps(a)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
