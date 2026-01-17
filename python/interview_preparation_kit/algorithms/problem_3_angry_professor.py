# Problem: Utopian Tree
# Link: https://www.hackerrank.com/challenges/angry-professor/problem

import time


def angryProfessor(k, a):
    return "NO" if sum(t <= 0 for t in a) >= k else "YES"


if __name__ == "__main__":
    start_time = time.time()
    k = 3
    a = [-2, -1, 0, 1, 2]
    result = angryProfessor(k, a)
    elapsed_time = time.time() - start_time
    print(result)
    print(elapsed_time)
