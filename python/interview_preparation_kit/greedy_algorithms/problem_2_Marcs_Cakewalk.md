# Marc's Cakewalk - Tutorial

## Problem Statement

Marc loves cupcakes, but he also worries about his weight. He wants to walk off the calories from eating cupcakes. The number of miles he must walk to burn off the calories from cupcake `i` eaten as the `j`-th cupcake is:

**miles = 2^j x calorie[i]**

Given a list of calorie values for each cupcake, determine the **minimum number of miles** Marc must walk to maintain his weight.

**Link:** [HackerRank - Marc's Cakewalk](https://www.hackerrank.com/challenges/marcs-cakewalk/problem)

---

## Understanding the Problem

| Parameter | Description |
|-----------|-------------|
| `calorie` | Array of calorie values for each cupcake |
| `j` | Order in which a cupcake is eaten (0-indexed) |
| `2^j` | Multiplier that grows exponentially with eating order |
| **Goal** | Minimize total miles = sum of `2^j * calorie[j]` |

The key observation: **the multiplier doubles with each cupcake eaten**. Eating a high-calorie cupcake later means it gets multiplied by a much larger power of 2.

---

## Example Walkthrough

```
calorie = [7, 4, 9, 6]
```

**Step 1:** Sort calories in descending order

```
sorted = [9, 7, 6, 4]
```

**Step 2:** Assign powers of 2 in increasing order

| Order (j) | Multiplier (2^j) | Calorie | Miles |
|------------|-------------------|---------|-------|
| 0 | 1 | 9 | 9 |
| 1 | 2 | 7 | 14 |
| 2 | 4 | 6 | 24 |
| 3 | 8 | 4 | 32 |

**Result:** 9 + 14 + 24 + 32 = **79**

**Why not unsorted?** With original order `[7, 4, 9, 6]`:
`1*7 + 2*4 + 4*9 + 8*6 = 7 + 8 + 36 + 48 = 99` (worse!)

---

## The Greedy Insight

To minimize total miles:
1. **Eat** the highest-calorie cupcake **first** (smallest multiplier `2^0 = 1`)
2. **Eat** the lowest-calorie cupcake **last** (largest multiplier)

This is greedy because larger multipliers grow exponentially, so pairing them with smaller calorie values always produces the optimal result. The property `2^j > 2^0 + 2^1 + ... + 2^(j-1)` guarantees that reducing the calorie at position `j` matters more than all previous positions combined.

---

## Current Solution Analysis

```python
def marcsCakewalk(calorie):
    calories_total = len(calorie)
    sorted_calorie = sorted(calorie, reverse=True)
    miles = 0
    for i in range(calories_total):
        miles += (2**i) * sorted_calorie[i]
    return miles
```

### How It Works

1. Sort calories in descending order
2. Iterate with index `i` as the eating order
3. Accumulate `2^i * calorie[i]` for each cupcake

### Complexity

| Metric | Value | Notes |
|--------|-------|-------|
| **Time** | O(n log n) | Dominated by sorting |
| **Space** | O(n) | Sorted copy of the array |

---

## Alternative Solutions

### 1. One-liner with `enumerate`

A compact Pythonic version using a generator expression:

```python
def marcsCakewalk(calorie):
    return sum(2**i * c for i, c in enumerate(sorted(calorie, reverse=True)))
```

- Same complexity: O(n log n) time, O(n) space
- More readable for those comfortable with Python idioms

---

### 2. Bit Shifting

Since `2^i` is equivalent to `1 << i` (left bit shift), we can avoid the exponentiation operator:

```python
def marcsCakewalk(calorie):
    return sum((1 << i) * c for i, c in enumerate(sorted(calorie, reverse=True)))
```

- Bit shifting is a single CPU instruction vs. exponentiation
- Minor performance improvement, same complexity

---

### 3. Doubling Multiplier (No Exponentiation)

Instead of computing `2^i` at each step, maintain a running multiplier that doubles:

```python
def marcsCakewalk(calorie):
    miles = 0
    power = 1
    for c in sorted(calorie, reverse=True):
        miles += power * c
        power *= 2
    return miles
```

### Why This Is Better

- Avoids recomputing powers entirely
- Uses only multiplication (O(1) per step)
- The summation loop is O(n) with constant-factor improvement
- Still O(n log n) overall due to sorting

---

## Complexity Comparison

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Original (loop + `2**i`) | O(n log n) | O(n) | Clear, straightforward |
| One-liner (`enumerate`) | O(n log n) | O(n) | Compact, Pythonic |
| Bit shifting (`1 << i`) | O(n log n) | O(n) | Faster exponentiation |
| **Doubling multiplier** | **O(n log n)** | **O(n)** | **No exponentiation at all** |

All solutions share the same asymptotic complexity because sorting dominates. The differences are constant-factor improvements in the summation step.

---

## Common Mistakes

1. **Sorting in ascending order** - Pairing high calories with large multipliers gives the maximum, not the minimum
2. **Using 1-indexed powers** - The problem uses 0-indexed eating order, so the first cupcake has multiplier `2^0 = 1`, not `2^1 = 2`
3. **Ignoring the exponential growth** - Because `2^j` grows so fast, no clever reordering of lower positions can compensate for a bad choice at a high position
4. **Overlooking integer overflow** - In languages without arbitrary precision, `2^n` overflows quickly (Python handles this natively)

---

## Test Cases

```python
# Basic example
assert marcsCakewalk([7, 4, 9, 6]) == 79

# Single cupcake
assert marcsCakewalk([10]) == 10

# Already sorted descending
assert marcsCakewalk([5, 3, 1]) == 1*5 + 2*3 + 4*1  # 15

# All same calories
assert marcsCakewalk([4, 4, 4]) == 1*4 + 2*4 + 4*4  # 28

# Two cupcakes
assert marcsCakewalk([1, 100]) == 1*100 + 2*1  # 102
```

---

## Key Takeaways

1. **Greedy pattern:** When multipliers grow exponentially, always pair the largest value with the smallest multiplier
2. **Exponential dominance:** `2^j` grows so fast that the last position matters more than all others combined
3. **Avoid recomputation:** Use a doubling multiplier instead of recomputing `2^i` at each step
4. **Bit shifting:** `1 << i` is a constant-time alternative to `2**i`

---

## Related Problems

- [Luck Balance](https://www.hackerrank.com/challenges/luck-balance)
- [Greedy Florist](https://www.hackerrank.com/challenges/greedy-florist)
- [Minimum Absolute Difference in an Array](https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array)
