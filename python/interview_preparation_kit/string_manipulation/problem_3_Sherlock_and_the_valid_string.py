# Problem: String Manipulation - Sherlock and the Valid String
# Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
import time
from collections import Counter


def isValid(s):
    letters_freq = Counter(s)
    freq_count = Counter(letters_freq.values())
    
    if len(freq_count) == 1:
        return "YES"
    
    if len(freq_count) == 2:
        f1, f2 = sorted(freq_count.keys())
        if f1 == 1 and freq_count[f1] == 1:
            return "YES"
        
        if f2 == f1 + 1 and freq_count[f2] == 1:
            return "YES"
    return "NO"


if __name__ == "__main__":
    start_time = time.time()
    s = "aabbbeeecccddd"
    result = isValid(s)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
