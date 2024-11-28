# Problem: Mark and Toys
# Link: https://www.hackerrank.com/challenges/mark-and-toys/problem

import time


def maximumToys(prices, k):
    prices.sort()
    total_toys = 0
    while k > 0:
        k -= prices.pop(0)
        total_toys += 1
    return total_toys - 1


if __name__ == "__main__":
    start_time = time.time()
    prices = [1, 12, 5, 111, 200, 1000, 10]
    k = 50
    result = maximumToys(prices, k)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
