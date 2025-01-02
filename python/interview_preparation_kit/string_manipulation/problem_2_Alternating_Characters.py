# Problem: String Manipulation - Alternating Characters
# Link: https://www.hackerrank.com/challenges/alternating-characters/problem
import time


def alternatingCharacters(s):
    deletions = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletions += 1
    return deletions


if __name__ == "__main__":
    start_time = time.time()
    a = "cde"
    b = "abc"
    result = alternatingCharacters(a)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
