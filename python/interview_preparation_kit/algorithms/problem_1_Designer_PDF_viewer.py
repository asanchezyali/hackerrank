# Problem: Designer PDF viewer
# Link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import time


def designerPdfViewer(h, word):
    heights = []
    for char in word:
        index = int(ord(char) - 97)
        heights.append(h[index])
    max_height = max(heights)
    weight = len(word)
    return max_height * weight


if __name__ == "__main__":
    start_time = time.time()
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = "zaba"
    result = designerPdfViewer(h, word)
    print("Rectangle area: ", result)
    elapsed_time = time.time() - start_time
    print("Executed time: ", elapsed_time)
