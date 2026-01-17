# Problem: Utopian Tree
# Link: https://www.hackerrank.com/challenges/utopian-tree/problem

import time


def utopianTree(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return utopianTree(n - 1) + 1
    else:
        return 2 * utopianTree(n - 1)


if __name__ == "__main__":
    start_time = time.time()
    n = 5
    result = utopianTree(n)
    elapsed_time = time.time() - start_time
    print("Height of the tree is: ", result)
    print("Time spent :", elapsed_time)
