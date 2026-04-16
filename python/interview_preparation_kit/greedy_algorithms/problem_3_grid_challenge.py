# Problem: Greedy Algorithms - Grid Challenge
# Link: https://www.hackerrank.com/challenges/grid-challenge/problem

import time


def gridChallenge(grid):
    new_grid = [sorted("".join(column)) for column in zip(*grid)]
    for c in new_grid:
        if c != sorted(c):
            return "NO"
    return "YES"


if __name__ == "__main__":
    grid = ["ebacd", "aghij", "olmkn", "trpqs", "xywuv"]
    start_time = time.time()
    result = gridChallenge(grid)
    print(f"result: {result}")
    elapsed_time = time.time() - start_time
    print(f"--- elapsed time {elapsed_time:.4f} seconds ---")
