# Problem: Greedy Algorithms - Luck Balance
# Link: https://www.hackerrank.com/challenges/luck-balance/problem
import time


# O(n log n) time complexity due to sorting
def luckBalance(k, contests):
    important_contests = sorted([luck for luck, importance in contests if importance == 1], reverse=True)
    unimportant_contests = [luck for luck, importance in contests if importance == 0]
    max_luck = sum(unimportant_contests) + sum(important_contests[:k]) - sum(important_contests[k:])
    return max_luck


# Example usage:
if __name__ == "__main__":
    k = 3
    contests = [(5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0)]
    start_time = time.time()
    result = luckBalance(k, contests)
    print(result)  # Output: 29
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
