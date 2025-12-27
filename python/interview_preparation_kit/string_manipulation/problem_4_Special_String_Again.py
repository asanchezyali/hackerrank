# Problem: String Manipulation - Special String Again
# Link: https://www.hackerrank.com/challenges/special-palindrome-again/problem
import time


def substrCount(n, s):
    count = n
    for i in range(n):
        j = i
        while j < n - 1:
            j += 1
            if s[j] == s[i]:
                count += 1
            else:
                if s[i:j] == s[j + 1 : 2 * j - i + 1]:
                    count += 1
                break
    return count


if __name__ == "__main__":
    start_time = time.time()
    s = "asasd"
    n = len(s)
    result = substrCount(n, s)
    print(f"Result: {result}")
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time}")
