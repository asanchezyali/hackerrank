import time

def jumpingOnClouds(c):
    jumps = 0
    position = 0
    n = len(c)
    while position < n -1:
        if position + 2 < n and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        jumps += 1
    return jumps


if __name__ == "__main__":
    start_time = time.time()
    clouds = [0, 0, 0, 0, 0, 0, 1, 0, 0]
    result = jumpingOnClouds(clouds)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
