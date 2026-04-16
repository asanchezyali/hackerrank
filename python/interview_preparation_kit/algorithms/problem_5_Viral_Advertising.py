# Problem: Viral Advertising
# Link: https://www.hackerrank.com/challenges/strange-advertising/problem


import time


def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative


if __name__ == "__main__":
    start_time = time.time()
    n = 5
    result = viralAdvertising(n)
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
    print("Result: ", result)
