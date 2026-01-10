# Making Anagrams - Tutorial

## Problem Statement

Given two strings, `a` and `b`, determine the **minimum number of character deletions** required to make them anagrams of each other.

**Link:** [HackerRank - Making Anagrams](https://www.hackerrank.com/challenges/ctci-making-anagrams/problem)

---

## What is an Anagram?

Two strings are **anagrams** if they contain the same characters with the same frequencies, regardless of order.

**Examples:**
- `"listen"` and `"silent"` → Anagrams ✓
- `"triangle"` and `"integral"` → Anagrams ✓
- `"hello"` and `"world"` → Not anagrams ✗

---

## Understanding the Problem

Given two strings, we need to find how many characters must be **deleted** (from either string) so that the remaining characters form anagrams.

### Example

```
a = "cde"
b = "abc"
```

```mermaid
graph LR
    subgraph String_A["String a = 'cde'"]
        A1((c))
        A2((d))
        A3((e))
    end

    subgraph String_B["String b = 'abc'"]
        B1((a))
        B2((b))
        B3((c))
    end

    A1 -.->|"common"| B3
    A2 -->|"delete"| X1[❌]
    A3 -->|"delete"| X2[❌]
    B1 -->|"delete"| X3[❌]
    B2 -->|"delete"| X4[❌]
```

**Answer:** 4 deletions (d, e from `a` and a, b from `b`)

---

## Solution Approach

### Key Insight

Instead of thinking about which characters to keep, we count the **frequency difference** of each character between both strings.

### Algorithm Overview

```mermaid
flowchart TD
    A[Start] --> B[Count character frequencies in string a]
    B --> C[Count character frequencies in string b]
    C --> D[For each character in dict_a]
    D --> E[Add absolute difference with dict_b]
    E --> F[For each character only in dict_b]
    F --> G[Add its frequency to count]
    G --> H[Return total count]
    H --> I[End]
```

---

## Step-by-Step Code Explanation

### Step 1: Build Frequency Dictionaries

```python
dict_a = dict()
dict_b = dict()

for char in a:
    dict_a[char] = dict_a.get(char, 0) + 1

for char in b:
    dict_b[char] = dict_b.get(char, 0) + 1
```

For `a = "cde"` and `b = "abc"`:

```mermaid
graph LR
    subgraph dict_a["dict_a"]
        direction TB
        A1["'c': 1"]
        A2["'d': 1"]
        A3["'e': 1"]
    end

    subgraph dict_b["dict_b"]
        direction TB
        B1["'a': 1"]
        B2["'b': 1"]
        B3["'c': 1"]
    end
```

### Step 2: Count Differences from String `a`

```python
count = 0
for char in dict_a:
    count += abs(dict_a[char] - dict_b.get(char, 0))
```

```mermaid
flowchart LR
    subgraph Process["Processing dict_a characters"]
        C["char 'c'"] --> C1["dict_a: 1, dict_b: 1"]
        C1 --> C2["|1-1| = 0"]

        D["char 'd'"] --> D1["dict_a: 1, dict_b: 0"]
        D1 --> D2["|1-0| = 1"]

        E["char 'e'"] --> E1["dict_a: 1, dict_b: 0"]
        E1 --> E2["|1-0| = 1"]
    end

    C2 --> SUM["count = 0+1+1 = 2"]
    D2 --> SUM
    E2 --> SUM
```

### Step 3: Count Characters Only in String `b`

```python
for char in dict_b:
    if char not in dict_a:
        count += dict_b[char]
```

```mermaid
flowchart LR
    subgraph Process["Processing dict_b characters"]
        A["char 'a'"] --> A1{"In dict_a?"}
        A1 -->|No| A2["+1"]

        B["char 'b'"] --> B1{"In dict_a?"}
        B1 -->|No| B2["+1"]

        C["char 'c'"] --> C1{"In dict_a?"}
        C1 -->|Yes| C2["skip"]
    end

    A2 --> SUM["count = 2+1+1 = 4"]
    B2 --> SUM
```

---

## Visual Walkthrough

```mermaid
graph TB
    subgraph Input["Input Strings"]
        A["a = 'cde'"]
        B["b = 'abc'"]
    end

    subgraph Step1["Step 1: Build Frequency Maps"]
        DA["dict_a = {c:1, d:1, e:1}"]
        DB["dict_b = {a:1, b:1, c:1}"]
    end

    subgraph Step2["Step 2: Compare All Characters"]
        COMP["
        a: |0-1| = 1 (only in b)
        b: |0-1| = 1 (only in b)
        c: |1-1| = 0 (common)
        d: |1-0| = 1 (only in a)
        e: |1-0| = 1 (only in a)
        "]
    end

    subgraph Result["Result"]
        R["Total Deletions = 4"]
    end

    Input --> Step1
    Step1 --> Step2
    Step2 --> Result
```

---

## Character Comparison Table

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#f0f0f0'}}}%%
graph TD
    subgraph Table["Character Frequency Comparison"]
        direction TB
        Header["| Char | In a | In b | Deletions |"]
        Row1["| a | 0 | 1 | 1 |"]
        Row2["| b | 0 | 1 | 1 |"]
        Row3["| c | 1 | 1 | 0 |"]
        Row4["| d | 1 | 0 | 1 |"]
        Row5["| e | 1 | 0 | 1 |"]
        Total["| Total | | | 4 |"]

        Header --- Row1
        Row1 --- Row2
        Row2 --- Row3
        Row3 --- Row4
        Row4 --- Row5
        Row5 --- Total
    end
```

---

## Complete Solution

```python
def makeAnagram(a, b):
    dict_a = dict()
    dict_b = dict()

    # Count character frequencies in string a
    for char in a:
        dict_a[char] = dict_a.get(char, 0) + 1

    # Count character frequencies in string b
    for char in b:
        dict_b[char] = dict_b.get(char, 0) + 1

    count = 0

    # Count differences for characters in a
    for char in dict_a:
        count += abs(dict_a[char] - dict_b.get(char, 0))

    # Count characters only in b (not in a)
    for char in dict_b:
        if char not in dict_a:
            count += dict_b[char]

    return count
```

---

## Alternative Solution Using Counter

Python's `collections.Counter` simplifies the frequency counting:

```python
from collections import Counter

def makeAnagram(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)

    # Get all unique characters from both strings
    all_chars = set(counter_a.keys()) | set(counter_b.keys())

    # Sum the absolute differences
    return sum(abs(counter_a[c] - counter_b[c]) for c in all_chars)
```

---

## Complexity Analysis

```mermaid
graph LR
    subgraph Time["Time Complexity: O(n + m)"]
        T1["Iterate string a: O(n)"]
        T2["Iterate string b: O(m)"]
        T3["Compare dictionaries: O(k)"]
    end

    subgraph Space["Space Complexity: O(k)"]
        S1["dict_a: O(k)"]
        S2["dict_b: O(k)"]
        S3["k = unique chars ≤ 26"]
    end
```

| Complexity | Value | Explanation |
|------------|-------|-------------|
| **Time**   | O(n + m) | Where `n` = len(a), `m` = len(b). We iterate through each string once |
| **Space**  | O(k) | Where `k` = number of unique characters (at most 26 for lowercase letters) |

---

## Test Cases

```mermaid
graph TB
    subgraph Test1["Test Case 1"]
        T1A["a = 'cde'"]
        T1B["b = 'abc'"]
        T1R["Expected: 4"]
    end

    subgraph Test2["Test Case 2"]
        T2A["a = 'showman'"]
        T2B["b = 'woman'"]
        T2R["Expected: 2"]
    end

    subgraph Test3["Test Case 3"]
        T3A["a = 'aab'"]
        T3B["b = 'a'"]
        T3R["Expected: 2"]
    end
```

```python
# Test Case 1
a = "cde"
b = "abc"
# Expected: 4 (delete 'd', 'e' from a; delete 'a', 'b' from b)

# Test Case 2
a = "showman"
b = "woman"
# Expected: 2 (delete 's', 'h' from a)

# Test Case 3
a = "aab"
b = "a"
# Expected: 2 (delete one 'a' and 'b' from a)
```

---

## Key Takeaways

```mermaid
mindmap
  root((Making Anagrams))
    Concepts
      Frequency Counting
      Dictionary Operations
      Set Theory
    Techniques
      dict.get with default
      Absolute differences
      Union of keys
    Complexity
      Time: O(n + m)
      Space: O(k)
    Tips
      Avoid string manipulation
      Use Counter for cleaner code
      Handle missing keys gracefully
```

---

## Related Problems

- [Sherlock and the Valid String](https://www.hackerrank.com/challenges/sherlock-and-valid-string)
- [Common Child](https://www.hackerrank.com/challenges/common-child)
- [Alternating Characters](https://www.hackerrank.com/challenges/alternating-characters)
