import time


def freqQuery(queries):
    values = dict()
    result = []
    for query in queries:
        operation, value = query

        if operation == 1:
            if value in values:
                values[value] += 1
            else:
                values[value] = 1

        if operation == 2:
            if value in values:
                values[value] -= 1

                if values[value] == 0:
                    del values[value]

        if operation == 3:
            if value in values.values():
                result.append(1)
            else:
                result.append(0)
    return result
            


            
   



    



if __name__ == "__main__":
    start_time = time.time()
    queries = [
        [1, 5],
        [1, 6],
        [3, 2],
        [1, 10],
        [1, 10],
        [1, 6],
        [2, 5],
        [3, 2]
    ]
    result = freqQuery(queries)
    elapsed_time = time.time() - start_time
    print(result)
    print(f"--- {elapsed_time:.4f} seconds ---")
