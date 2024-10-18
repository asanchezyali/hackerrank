import time

def sockMerchant(n, ar):
    sock_count = {}
    matching_pairs = 0
    for i in range(n):
        if ar[i] in sock_count:
            sock_count[ar[i]] += 1
            if sock_count[ar[i]] % 2 == 0:
                matching_pairs += 1
        else:
            sock_count[ar[i]] = 1
    return matching_pairs

# This is the first solution I came up with. It is not the most efficient one, but it works.
""" 
def sockMerchant(n, ar):
    matching_pairs = 0
    for i in range(n):
        if ar[i] !=0:
            for j in range(i+1, n):
                if ar[i] == ar[j]:
                    matching_pairs += 1
                    ar[j] = 0
                    break
    return matching_pairs
"""

if __name__ == "__main__":
    start_time = time.time()
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")



