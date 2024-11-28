import time


def twoString(s1, s2):
    s1_dict = {}
    for word in s1:
        if word in s1_dict:
            s1_dict[word] += 1
        else:
            s1_dict[word] = 1
    for word in s2:
        if word in s1_dict:
            return "YES"
    return "NO"
    


if __name__ == "__main__":
    start_time = time.time()
    magazine = "give me one grand today night".split()
    note = "give one grand today".split()
    result = twoString(magazine, note)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
