import time


def countingValleys(steps, path):
    level = 0
    valleys = 0
    for i in range(steps):
        if path[i] == "U":
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys


if __name__ == "__main__":
    steps = 8
    string = "UDDDUDUU"
    start_time = time.time()
    result = countingValleys(steps, string)
    print(result)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")
