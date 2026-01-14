# Designer PDF Viewer

**Difficulty:** Easy
**Link:** [HackerRank - Designer PDF Viewer](https://www.hackerrank.com/challenges/designer-pdf-viewer/problem)

## Problem Description

When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently.

You are given:
- An array `h` of 26 integers representing the heights of each letter from `a` to `z`
- A string `word` containing only lowercase English letters

The task is to find the area of the rectangle that would highlight the word. The rectangle has:
- **Width** = number of characters in the word
- **Height** = the tallest letter in the word

## Example

```
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"
```

The letters in "zaba" have heights:
- `z` → index 25 → height 7
- `a` → index 0 → height 1
- `b` → index 1 → height 3
- `a` → index 0 → height 1

Maximum height = 7
Width = 4
**Area = 7 × 4 = 28**

## Key Insight

The core insight is converting each character to its corresponding index in the height array:
- `'a'` has ASCII value 97, and should map to index 0
- `'b'` has ASCII value 98, and should map to index 1
- ...and so on

Formula: `index = ord(char) - ord('a')` or `index = ord(char) - 97`

## Solutions

### Solution 1: Basic Loop (Original)

```python
def designerPdfViewer(h, word):
    heights = []
    for char in word:
        index = int(ord(char) - 97)
        heights.append(h[index])
    max_height = max(heights)
    width = len(word)
    return max_height * width
```

**Analysis:**
- Time Complexity: O(n) where n is the length of the word
- Space Complexity: O(n) - creates an intermediate list of heights

### Solution 2: List Comprehension (Cleaner)

```python
def designerPdfViewer(h, word):
    heights = [h[ord(c) - 97] for c in word]
    return max(heights) * len(word)
```

**Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(n)
- More Pythonic and readable

### Solution 3: Generator Expression (Memory Optimized)

```python
def designerPdfViewer(h, word):
    max_height = max(h[ord(c) - 97] for c in word)
    return max_height * len(word)
```

**Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(1) - no intermediate list created
- The generator yields values one at a time to `max()`

### Solution 4: One-Liner

```python
def designerPdfViewer(h, word):
    return max(h[ord(c) - 97] for c in word) * len(word)
```

**Analysis:**
- Same as Solution 3, but condensed
- Elegant for those who prefer concise code

### Solution 5: Using `map()` Function

```python
def designerPdfViewer(h, word):
    return max(map(lambda c: h[ord(c) - 97], word)) * len(word)
```

**Analysis:**
- Time Complexity: O(n)
- Space Complexity: O(1) - `map()` returns an iterator
- Functional programming style

### Solution 6: Using `ord('a')` for Clarity

```python
def designerPdfViewer(h, word):
    base = ord('a')
    return max(h[ord(c) - base] for c in word) * len(word)
```

**Analysis:**
- More readable than magic number 97
- Self-documenting code

## Comparison

| Solution | Lines | Space | Readability | Performance |
|----------|-------|-------|-------------|-------------|
| Basic Loop | 6 | O(n) | Good | Good |
| List Comprehension | 2 | O(n) | Better | Good |
| Generator | 2 | O(1) | Better | Best |
| One-Liner | 1 | O(1) | Moderate | Best |
| Map | 1 | O(1) | Moderate | Best |

## Recommended Solution

**Solution 3 (Generator Expression)** offers the best balance:

```python
def designerPdfViewer(h, word):
    max_height = max(h[ord(c) - ord('a')] for c in word)
    return max_height * len(word)
```

**Why?**
1. **Memory efficient:** No intermediate list allocation
2. **Readable:** Clear separation of logic
3. **Pythonic:** Uses modern Python idioms
4. **Self-documenting:** `ord('a')` explains the character mapping

## Edge Cases to Consider

1. **Single character word:** `word = "a"` → area = height of 'a' × 1
2. **All same letters:** `word = "aaaa"` → area = height of 'a' × 4
3. **All different heights:** Each letter has unique height

## Complete Test Code

```python
def designerPdfViewer(h, word):
    max_height = max(h[ord(c) - ord('a')] for c in word)
    return max_height * len(word)


if __name__ == "__main__":
    # Test case 1
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = "zaba"
    assert designerPdfViewer(h, word) == 28

    # Test case 2: single character
    h2 = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    word2 = "a"
    assert designerPdfViewer(h2, word2) == 1

    # Test case 3: HackerRank sample
    h3 = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    word3 = "abc"
    assert designerPdfViewer(h3, word3) == 9  # max(1,3,1) * 3 = 9

    print("All tests passed!")
```

## Summary

This problem teaches:
- **Character to index mapping** using ASCII values
- **Finding maximum values** efficiently
- **Generator expressions** for memory optimization
- **Clean, Pythonic code** patterns

The key is recognizing that the area formula is simply `max_height × width`, and efficiently computing the maximum height among all characters in the word.
