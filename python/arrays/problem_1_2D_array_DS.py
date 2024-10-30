import time
import math


def hourglassSum(arr):
    max_hourglass = -math.inf
    for i in range(1, 5):
        for j in range(1, 5):
            current_hourglass = (
                arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] +
                arr[i][j] +
                arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            )
            max_hourglass = max(max_hourglass, current_hourglass)
    return max_hourglass

if __name__ == "__main__":
    start_time = time.time()
    arr = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    result = hourglassSum(arr)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
