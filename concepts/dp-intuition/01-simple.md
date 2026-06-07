# Dynamic Programming — The Core Idea

## The Core Idea

Dynamic Programming solves a hard problem by breaking it into **overlapping subproblems** and **reusing** the answers instead of recomputing them.

## Think of it as a four-step pattern

### 1. Write the brute force recursion

Don't optimize yet. Just capture the choices.

Example: You climb stairs — you can take 1 or 2 steps at a time. How many ways to reach step *n*?

```
climb(0) = 1              # at the top
climb(1) = climb(0) = 1
climb(2) = climb(1) + climb(0) = 2
climb(3) = climb(2) + climb(1) = 3
```

Each call branches into 2. For n=10, that's 177 calls — but only 11 unique inputs.

### 2. Find the overlap

Trace with small inputs. Watch how many times the same state repeats.

```
climb(4) → climb(3) and climb(2)
climb(3) → climb(2) and climb(1)
→ climb(2) appears TWICE with the same input!
```

### 3. Add a cache

```python
memo = {}
def climb(n):
    if n in memo: return memo[n]
    if n <= 1: return 1
    memo[n] = climb(n-1) + climb(n-2)
    return memo[n]
```

Same recurrence. Same logic. Now 10 calls instead of 177.

### 4. Convert to a table (iterative)

If states are just 0, 1, 2, ..., n → turn into an array.

```python
def climb_table(n):
    if n <= 1: return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## When to use DP (three yes/no questions)

1. **Overlapping subproblems?** — Can we reach the same state via different paths? → YES
2. **Optimal substructure?** — Is the big answer built from smaller answers? → YES
3. **Brute force repeats work?** — Will the same function be called many times with the same args? → YES

If all three → DP.

## Four core patterns you'll encounter

| Pattern | What it looks like | Key state |
|---|-|---|
| **Linear** | "Maximum sum" or "number of ways" in a sequence | dp[i] = f(dp[i-1], dp[i-2]) |
| **Knapsack** | "Choose or skip" items with a constraint | (item, remaining_capacity) |
| **Grid** | Move from start to end on a board | (row, col) |
| **LIS/LCS** | "Longest subsequence" matching a condition | (i, j) across two sequences |

We'll cover each pattern in the deeper lesson with full code.

## Before you code: the interview checklist

1. Write brute-force recursion on paper first — get the pattern
2. Trace on n=4 or n=5 — watch the overlap
3. Define the state clearly (what variables capture everything needed?)
4. Set base cases: dp[0] = ? Usually 0, 1, or depends on the problem
5. Code iterative with a table — interviewers prefer this
6. Ask: "Can this space be optimized?" (2D → 1D is often possible)

## Stretch problem (after the basics)

**Edit Distance** — transform one word to another. Operations: insert, delete, or replace (cost 1 each).

- State: `dp[i][j]` = cost to make `word1[0..i]` = `word2[0..j]`
- If chars match → dp[i][j] = dp[i-1][j-1]
- If not → 1 + min(delete, insert, replace)
- Time: O(m × n), Space: O(m × n)
