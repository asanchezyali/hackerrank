# Problem: String Manipulation - Making Anagrams
# Link: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
import time


def makeAnagram(a, b):
    dict_a = dict()
    dict_b = dict()
    for char in a:
        dict_a[char] = dict_a.get(char, 0) + 1
    for char in b:
        dict_b[char] = dict_b.get(char, 0) + 1

    count = 0
    for char in dict_a:
        count += abs(dict_a[char] - dict_b.get(char, 0))
    for char in dict_b:
        if char not in dict_a:
            count += dict_b[char]
    return count


if __name__ == "__main__":
    start_time = time.time()
    a = "cde"
    b = "abc"
    result = makeAnagram(a, b)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
