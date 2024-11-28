import time


def checkMagazine(magazine, note):
    magazine_dict = {}
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1
    for word in note:
        if word in magazine_dict and magazine_dict[word] > 0:
            magazine_dict[word] -= 1
        else:
            return "No"
    return "Yes"
    


if __name__ == "__main__":
    start_time = time.time()
    magazine = "give me one grand today night".split()
    note = "give one grand today".split()
    result = checkMagazine(magazine, note)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
