# Problem: Bubble Sort
# Link: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

import time


def countSwaps(a):
    num_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1
    print (f"Array is sorted in {num_swaps} swaps.")
    print (f"First Element: {a[0]}")
    print (f"Last Element: {a[-1]}")

if __name__ == "__main__":
    start_time = time.time()
    a = [3, 2, 1]
    countSwaps(a)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
