# Problem: Comparator
# Link: https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

import time
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name} {self.score}"
        
    def comparator(a, b):
        B_GREATER_A = 1
        A_GREATER_B = -1
        A_EQUAL_B = 0
        NAME_B_GREATER_NAME_A = -1
        NAME_A_GREATER_NAME_B = 1
         
        if a.score == b.score and a.name == b.name:
            return A_EQUAL_B           
        if a.score < b.score:
            return B_GREATER_A
        if a.score > b.score:
            return A_GREATER_B
        if a.name < b.name:
            return NAME_B_GREATER_NAME_A
        if a.name > b.name:
            return NAME_A_GREATER_NAME_B



if __name__ == "__main__":
    start_time = time.time()
    n = 5
    data = []
    for i in range(n):
        name, score = ["amy", "david", "heraldo", "aakansha", "aleksa"][i], [100, 100, 50, 75, 150][i]
        score = int(score)
        player = Player(name, score)
        data.append(player)
        
    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time:.4f} seconds ---")