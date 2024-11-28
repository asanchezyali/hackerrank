import time


def countTriplets(arr, r):
    total_sequences = 0
    looking_for_second_number = dict()
    looking_for_third_number = dict()

    for current_num in arr:
        if current_num in looking_for_third_number:
            total_sequences += looking_for_third_number[current_num]

        if current_num in looking_for_second_number:
            next_num = current_num * r

            if next_num in looking_for_third_number:
                looking_for_third_number[next_num] += looking_for_second_number[current_num]
            else: 
                looking_for_third_number[next_num] = looking_for_second_number[current_num]

        next_num = current_num * r

        if next_num in looking_for_second_number:
            looking_for_second_number[next_num] += 1
        else:
            looking_for_second_number[next_num] = 1
    return total_sequences
    



if __name__ == "__main__":
    start_time = time.time()
    arr = [1, 2, 2, 2, 2,  4, 8, 16]
    result = countTriplets(arr, 2)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
