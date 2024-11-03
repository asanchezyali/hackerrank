import time


def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1, -1, -1):
        # Verifiy if the person has bribed more than 2 people
        if q[i] - (i + 1) > 2:
            return "Too chaotic"
        # Count how many times the current person has been bribed.
        # Check only the range from max(0, q.get(i) - 2) to i
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    return bribes


if __name__ == "__main__":
    start_time = time.time()
    a = [2, 1, 5, 3, 4]
    result = minimumBribes(a)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
