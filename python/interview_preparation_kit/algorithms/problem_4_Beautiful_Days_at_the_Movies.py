# Problem: Beautiful Days at the Movies
# Link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem


import math
import time


def get_reverse_number(n):
    reverse_number = 0
    while n != 0:
        reverse_number = reverse_number * 10 + n % 10
        n = math.floor(n / 10)
    return reverse_number


def is_beautiful_number(n, k):
    return abs(n - get_reverse_number(n)) % k == 0


def beautifulDays(i, j, k):
    return sum(1 if is_beautiful_number(number, k) else 0 for number in range(i, j + 1))


if __name__ == "__main__":
    start_time = time.time()
    i = 20
    j = 23
    k = 6
    result = beautifulDays(i, j, k)
    print("Result: ", result)
    elapsed_time = start_time - time.time()
    print("Spent time: ", elapsed_time)
