# Luck Balance - Tutorial

## Problem Statement

Lena is preparing for an important coding competition. Before the competition, she must attend several preliminary contests. Each contest has a **luck value** and an **importance rating**.

- If Lena **loses** a contest, she gains that contest's luck value
- If Lena **wins** a contest, she loses that luck value
- She can lose at most **k important contests**
- She can lose **all unimportant contests**

**Goal:** Maximize total luck.

**Link:** [HackerRank - Luck Balance](https://www.hackerrank.com/challenges/luck-balance/problem)

---

## Understanding the Problem

```mermaid
flowchart TD
    subgraph Input["Input Parameters"]
        K["k = max important contests we can lose"]
        C["contests = [(luck, importance), ...]"]
    end

    subgraph Rules["Contest Rules"]
        R1["importance = 1 → Important contest"]
        R2["importance = 0 → Unimportant contest"]
        R3["Lose contest → +luck"]
        R4["Win contest → -luck"]
    end

    subgraph Constraints["Constraints"]
        C1["Can lose ALL unimportant contests"]
        C2["Can lose at most K important contests"]
        C3["Must WIN remaining important contests"]
    end

    Input --> Rules
    Rules --> Constraints
```

---

## Example Walkthrough

```
k = 3
contests = [(5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0)]
```

```mermaid
graph TB
    subgraph Contests["All Contests"]
        subgraph Important["Important (importance=1)"]
            I1["luck=8"]
            I2["luck=5"]
            I3["luck=2"]
            I4["luck=1"]
        end
        subgraph Unimportant["Unimportant (importance=0)"]
            U1["luck=10"]
            U2["luck=5"]
        end
    end

    subgraph Strategy["Greedy Strategy (k=3)"]
        direction TB
        S1["Lose ALL unimportant: +10 +5 = +15"]
        S2["Lose TOP 3 important: +8 +5 +2 = +15"]
        S3["Win remaining important: -1"]
    end

    subgraph Result["Total Luck"]
        R["15 + 15 - 1 = 29"]
    end

    Contests --> Strategy
    Strategy --> Result
```

---

## The Greedy Insight

```mermaid
flowchart LR
    subgraph Key["Key Insight"]
        direction TB
        K1["To MAXIMIZE luck..."]
        K2["Lose contests with HIGHEST luck values"]
        K3["Win contests with LOWEST luck values"]
    end

    subgraph Application["Applied to Important Contests"]
        direction TB
        A1["Sort by luck value (descending)"]
        A2["Lose the top K contests"]
        A3["Win the remaining contests"]
    end

    Key --> Application
```

**Why is this greedy?**
- We make the locally optimal choice at each step
- Losing high-luck contests gives us more luck
- Being forced to win should cost us the least (low-luck contests)

---

## Current Solution Analysis

```python
# O(n log n) time complexity due to sorting
def luckBalance(k, contests):
    important_contests = sorted(
        [luck for luck, importance in contests if importance == 1],
        reverse=True
    )
    unimportant_contests = [luck for luck, importance in contests if importance == 0]
    max_luck = sum(unimportant_contests) + sum(important_contests[:k]) - sum(important_contests[k:])
    return max_luck
```

### Step-by-Step Breakdown

```mermaid
flowchart TD
    A["Start: contests = [(5,1), (2,1), (1,1), (8,1), (10,0), (5,0)]"]

    B["Step 1: Filter & Sort Important Contests"]
    B1["Filter: [5, 2, 1, 8]"]
    B2["Sort descending: [8, 5, 2, 1]"]

    C["Step 2: Filter Unimportant Contests"]
    C1["[10, 5]"]

    D["Step 3: Calculate Luck"]
    D1["sum(unimportant) = 10 + 5 = 15"]
    D2["sum(important[:k]) = 8 + 5 + 2 = 15"]
    D3["sum(important[k:]) = 1"]

    E["Step 4: Final Calculation"]
    E1["15 + 15 - 1 = 29"]

    A --> B
    B --> B1 --> B2
    A --> C --> C1
    B2 --> D
    C1 --> D
    D --> D1
    D --> D2
    D --> D3
    D1 --> E
    D2 --> E
    D3 --> E
    E --> E1
```

---

## Complexity Analysis

```mermaid
graph TB
    subgraph Current["Current Solution: O(n log n)"]
        direction TB
        C1["Filter important: O(n)"]
        C2["Sort important: O(m log m)"]
        C3["Filter unimportant: O(n)"]
        C4["Sum operations: O(n)"]
        C5["Total: O(n log n)"]
    end

    subgraph Space["Space: O(n)"]
        S1["important_contests list"]
        S2["unimportant_contests list"]
    end
```

| Operation | Complexity | Notes |
|-----------|------------|-------|
| Filter important | O(n) | Single pass through contests |
| Sort important | O(m log m) | m = number of important contests |
| Filter unimportant | O(n) | Single pass through contests |
| Sum calculations | O(n) | Linear summation |
| **Total Time** | **O(n log n)** | Dominated by sorting |
| **Space** | **O(n)** | Two auxiliary lists |

---

## Optimization Recommendations

### Optimization 1: Single Pass with Heap (O(n + k log m))

When `k` is small relative to the number of important contests, we can use `heapq.nlargest()`:

```python
import heapq

def luckBalance_optimized_v1(k, contests):
    important = []
    total_luck = 0

    for luck, importance in contests:
        if importance == 0:
            total_luck += luck  # Always lose unimportant
        else:
            important.append(luck)
            total_luck += luck  # Assume we lose all initially

    # If we have more important contests than k, we must win some
    if len(important) > k:
        # Find the (len-k) smallest values we must win
        must_win = heapq.nsmallest(len(important) - k, important)
        total_luck -= 2 * sum(must_win)  # Subtract twice (undo +luck, apply -luck)

    return total_luck
```

```mermaid
flowchart TD
    subgraph Approach["Optimized Approach"]
        A["Assume we LOSE all contests"]
        B["Add all luck values to total"]
        C["Find contests we MUST win"]
        D["Subtract 2× their luck values"]
        E["(once to undo, once to penalize)"]
    end

    A --> B --> C --> D --> E

    subgraph Why["Why subtract 2×?"]
        W1["Initially: +luck (assumed loss)"]
        W2["Correction: -luck (undo the addition)"]
        W3["Reality: -luck (we actually win)"]
        W4["Net change: -2×luck"]
    end
```

### Optimization 2: Quickselect Approach (O(n) average)

For the best average-case performance, use the selection algorithm:

```python
import heapq

def luckBalance_optimized_v2(k, contests):
    important = []
    total_luck = 0

    for luck, importance in contests:
        if importance == 0:
            total_luck += luck
        else:
            important.append(luck)

    m = len(important)

    if m <= k:
        # Can lose all important contests
        return total_luck + sum(important)

    # Use nlargest for top-k (internally uses heap)
    top_k = heapq.nlargest(k, important)

    # Lose top k, win the rest
    total_luck += sum(top_k)
    total_luck -= (sum(important) - sum(top_k))

    return total_luck
```

### Optimization 3: Single Pass with Min-Heap (O(n log k))

Maintain a heap of size k for streaming data:

```python
import heapq

def luckBalance_optimized_v3(k, contests):
    min_heap = []  # Min-heap of size k for top-k important contests
    total_luck = 0
    important_sum = 0

    for luck, importance in contests:
        if importance == 0:
            total_luck += luck
        else:
            important_sum += luck
            if len(min_heap) < k:
                heapq.heappush(min_heap, luck)
            elif luck > min_heap[0]:
                heapq.heapreplace(min_heap, luck)

    # Top k important contests we can lose
    top_k_sum = sum(min_heap)
    # Rest we must win
    must_win_sum = important_sum - top_k_sum

    return total_luck + top_k_sum - must_win_sum
```

```mermaid
flowchart TD
    subgraph MinHeap["Min-Heap Strategy"]
        A["Maintain heap of size k"]
        B["Heap contains TOP k luck values"]
        C["Min-heap → smallest of top-k at root"]
        D["New value > root? Replace!"]
    end

    subgraph Process["Process Each Contest"]
        P1{"importance == 0?"}
        P1 -->|Yes| P2["Add luck to total"]
        P1 -->|No| P3{"heap size < k?"}
        P3 -->|Yes| P4["Push to heap"]
        P3 -->|No| P5{"luck > heap root?"}
        P5 -->|Yes| P6["Replace root"]
        P5 -->|No| P7["Skip (will be won)"]
    end

    A --> B --> C --> D
```

---

## Complexity Comparison

```mermaid
graph LR
    subgraph Original["Original Solution"]
        O1["Time: O(n log n)"]
        O2["Space: O(n)"]
    end

    subgraph V1["Optimization 1: nsmallest"]
        V1T["Time: O(n + (m-k) log m)"]
        V1S["Space: O(m)"]
    end

    subgraph V2["Optimization 2: nlargest"]
        V2T["Time: O(n + k log m)"]
        V2S["Space: O(m)"]
    end

    subgraph V3["Optimization 3: Min-Heap"]
        V3T["Time: O(n log k)"]
        V3S["Space: O(k)"]
    end
```

| Solution | Time Complexity | Space Complexity | Best When |
|----------|----------------|------------------|-----------|
| Original | O(n log n) | O(n) | Simple, readable |
| Optimization 1 | O(n + (m-k) log m) | O(m) | k is close to m |
| Optimization 2 | O(n + k log m) | O(m) | k << m |
| **Optimization 3** | **O(n log k)** | **O(k)** | **k << n, memory-constrained** |

---

## Complete Optimized Solution

```python
import heapq

def luckBalance(k, contests):
    """
    Maximize luck by strategically losing contests.

    Time: O(n log k) where n = total contests, k = max important losses
    Space: O(k) for the min-heap

    Args:
        k: Maximum number of important contests we can lose
        contests: List of (luck, importance) tuples

    Returns:
        Maximum possible luck value
    """
    if k == 0:
        # Must win all important contests
        return sum(luck if imp == 0 else -luck for luck, imp in contests)

    min_heap = []
    total_luck = 0
    important_total = 0

    for luck, importance in contests:
        if importance == 0:
            # Lose all unimportant contests
            total_luck += luck
        else:
            important_total += luck
            # Maintain top-k important contests in min-heap
            if len(min_heap) < k:
                heapq.heappush(min_heap, luck)
            elif luck > min_heap[0]:
                heapq.heapreplace(min_heap, luck)

    # Sum of top k important contests (we lose these)
    lose_sum = sum(min_heap)
    # Sum of remaining important contests (we must win these)
    win_sum = important_total - lose_sum

    return total_luck + lose_sum - win_sum
```

---

## Visual Summary

```mermaid
mindmap
    root((Luck Balance))
        Problem
            Maximize luck
            Lose up to k important
            Lose all unimportant
        Greedy Strategy
            Lose highest luck first
            Win lowest luck contests
        Original Solution
            Sort: O(n log n)
            Simple and readable
        Optimizations
            Min-Heap: O(n log k)
            Best for small k
            Memory efficient: O(k)
        Key Insight
            Only need top-k values
            No need to sort everything
```

---

## Common Mistakes to Avoid

```mermaid
flowchart TD
    subgraph Mistakes["Common Mistakes"]
        M1["❌ Sorting when k is very small"]
        M2["❌ Forgetting k=0 edge case"]
        M3["❌ Not handling when m ≤ k"]
        M4["❌ Using max-heap instead of min-heap for top-k"]
    end

    subgraph Correct["Correct Approaches"]
        C1["✓ Use heap when k << n"]
        C2["✓ Handle edge cases first"]
        C3["✓ When m ≤ k, lose all important"]
        C4["✓ Min-heap keeps smallest of top-k at root"]
    end

    M1 --> C1
    M2 --> C2
    M3 --> C3
    M4 --> C4
```

---

## Test Cases

```python
# Test Case 1: Basic example
k = 3
contests = [(5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0)]
# Expected: 29

# Test Case 2: Can lose all important
k = 4
contests = [(5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0)]
# Expected: 31 (lose all)

# Test Case 3: Must win all important
k = 0
contests = [(5, 1), (2, 1), (10, 0)]
# Expected: 10 - 5 - 2 = 3

# Test Case 4: No important contests
k = 2
contests = [(10, 0), (5, 0), (3, 0)]
# Expected: 18 (lose all unimportant)
```

---

## Key Takeaways for Junior Developers

1. **Recognize greedy patterns** - When you need to maximize/minimize by selecting k items, think greedy

2. **Question full sorting** - If you only need top-k elements, a heap is often better than sorting

3. **Heap selection**:
   - **Min-heap** for top-k largest (evict smallest when full)
   - **Max-heap** for top-k smallest (evict largest when full)

4. **Trade-off awareness**:
   - O(n log n) sort is simple and often fast enough
   - O(n log k) heap is better when k << n
   - Profile before optimizing!

5. **Edge cases matter** - Always handle k=0, empty lists, and m ≤ k scenarios

---

## Related Problems

- [Minimum Absolute Difference in an Array](https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array)
- [Marc's Cakewalk](https://www.hackerrank.com/challenges/marcs-cakewalk)
- [Greedy Florist](https://www.hackerrank.com/challenges/greedy-florist)
