# Problem: Greedy Algorithms - Marc's Cakewalk
# Link: https://www.hackerrank.com/challenges/marcs-cakewalk/problem

import time


def marcsCakewalk(calorie):
    calories_total = len(calorie)
    sorted_calorie = sorted(calorie, reverse=True)
    miles = 0
    for i in range(calories_total):
        miles += (2**i) * sorted_calorie[i]
    return miles


if __name__ == "__main__":
    calorie = [7, 4, 9, 6]
    start_time = time.time()
    result = marcsCakewalk(calorie=calorie)
    print(f"result: {result}")
    elapsed_time = time.time() - start_time
    print(f"--- elapsed time {elapsed_time:.4f} seconds---")
