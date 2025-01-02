# Problem: Merge Sort: Counting Inversions
# Link: https://www.hackerrank.com/challenges/ctci-merge-sort/problem
import time


def merge_and_count_inversions(left, right):
    merged = list()
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions


def count_inversions(arr):
    if len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    left, inversions_left = count_inversions(arr[:mid])
    right, inversions_right = count_inversions(arr[mid:])
    merged, inversions = merge_and_count_inversions(left, right)

    return merged, inversions + inversions_left + inversions_right


def countInversions(arr):
    _, inversions = count_inversions(arr)
    return inversions


if __name__ == "__main__":
    start_time = time.time()
    arr = [2, 1, 3, 1, 2]
    result = countInversions(arr)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
