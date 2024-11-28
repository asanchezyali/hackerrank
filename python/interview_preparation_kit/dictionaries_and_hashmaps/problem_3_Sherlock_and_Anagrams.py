#Problem: Sherlock and Anagrams
#Link: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
import time


def sherlockAndAnagrams(s):
    anagram_dict = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sorted_substring = "".join(sorted(s[i:j]))
            if sorted_substring in anagram_dict:
                anagram_dict[sorted_substring] += 1
            else:
                anagram_dict[sorted_substring] = 1
    anagram_count = 0
    for key in anagram_dict:
        anagram_count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return anagram_count
    


if __name__ == "__main__":
    start_time = time.time()
    magazine = "give me one grand today night".split()
    note = "give one grand today".split()
    result = sherlockAndAnagrams(magazine, note)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
