import time


def rotLeft(a, d):
    return a[d:] + a[:d]


if __name__ == "__main__":
    start_time = time.time()
    a = [1, 2, 3, 4, 5]
    d = 4
    result = rotLeft(a, d)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
