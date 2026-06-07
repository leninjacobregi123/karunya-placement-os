# Dynamic Programming — Going Deeper

## The Four Patterns with Full Code

### Pattern 1: Linear DP (Fibonacci-style)

Each state depends on the previous 1-2 (or few) states. This is the simplest form.

**Example: House Robber**

You are a robber. Each house has money. Steal from two adjacent houses = alert the police. Maximize.

```python
def house_robber(nums):
    if not nums: return 0
    prev2, prev1 = 0, 0  # dp[i-2], dp[i-1]
    for money in nums:
        dp[i] = max(prev1, prev2 + money)
        prev2, prev1 = prev1, dp[i]
    return prev1
```

**Key insight:** At each house, you either skip it (take prev1's best) or rob it (add to prev2). No 2D table needed — just two rolling variables.

```python
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
```

**Time: O(n), Space: O(1)** — can use rolling variables because only the last 2 states matter.

---

### Pattern 2: Knapsack-Style DP

Choose or skip items under a constraint. State: `(item_index, remaining_capacity)`.

**Example: 0/1 Knapsack**

You have n items with weights and values. A bag holds capacity W. Maximize total value.

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i-1][w]  # skip item i
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], values[i-1] + dp[i-1][w-weights[i-1]])
    return dp[n][W]
```

**Space optimization (2D → 1D):** Use a single array. Iterate **backwards** to avoid overwriting values you still need.

```python
def knapsack_1d(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):  # backwards!
            dp[w] = max(dp[w], values[i] + dp[w-weights[i]])
    return dp[W]
```

```python
dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
```

**Time: O(n × W), Space: O(W)**

---

### Pattern 3: Grid DP

Move on a 2D board from start to end. State: `(row, col)`.

**Example: Minimum Path Sum**

Find the path from top-left to bottom-right with minimum cost. You can only move right or down.

```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j > 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0 and i > 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]
```

**Space optimization:** Use a single row. Update left-to-right.

```python
dp = [0] * n
dp[0] = grid[0][0]
for j in range(1, n):
    dp[j] = dp[j-1] + grid[0][j]
for i in range(1, m):
    dp[0] += grid[i][0]
    for j in range(1, n):
        dp[j] = grid[i][j] + min(dp[j], dp[j-1])
```

**Time: O(m × n), Space: O(n)**

---

### Pattern 4: LIS / LCS (Two-Sequence DP)

Compare two sequences. State: `(i, j)` — index in each sequence.

**Example: Longest Common Subsequence**

Find the longest subsequence that appears in both strings (not necessarily contiguous).

```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]  # match!
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])  # skip one
    return dp[m][n]
```

**Can this be optimized to 1D?** No — the recurrence needs both `dp[i]` and `dp[i-1]` from different columns, so a full table is required.

**Time: O(m × n), Space: O(m × n)**

---

## How to Choose the Right Pattern

Look at the problem description:

| Problem clues → | You want → | Pattern |
|---|-|---|
| "Maximum/minimum something" | choose or skip items | Knapsack |
| "Number of ways to reach" | build up linearly | Linear DP |
| "Move on a grid/board" | step-by-step movement | Grid DP |
| "Longest subsequence" | compare two sequences | LIS/LCS |
| "Cut/arrange items" | try all cut positions | Linear DP |

## Complex Problem: Edit Distance

Combines patterns 2 and 1. Transform word1 into word2.

State: `dp[i][j]` = minimum operations to make `word1[0..i]` = `word2[0..j]`.

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i  # delete all from word1
    for j in range(n + 1):
        dp[0][j] = j  # insert all for word2
    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = 1 + min(
                    dp[i][j+1],      # delete from word1
                    dp[i+1][j],      # insert into word1
                    dp[i][j]         # replace
                )
    return dp[m][n]
```

**Time: O(m × n), Space: O(m × n)**

## Common Mistakes

**Mistake 1: Wrong base case**
- dp[0] = 0 or dp[0] = 1? For "count ways," dp[0] = 1. For "min cost," dp[0] = 0.
- A wrong base case cascades through the entire solution.

**Mistake 2: Wrong state definition**
- If you miss even one variable, the states are incomplete and the answer is wrong.
- Example: For knapsack, you need BOTH item index AND remaining capacity. Without both, you can't distinguish different subproblems.

**Mistake 3: Using DP when greedy works**
- Some problems look like DP but have a simpler greedy solution.
- Ask: "Can I prove that my local choice is always optimal?" If yes → greedy. If no → DP.

**Mistake 4: Space optimization errors**
- When converting 2D to 1D, the iteration order matters.
- Forward iteration overwrites data you still need (like unvisited states).
- Backward iteration (like knapsack) preserves it.

## Interview Tips

1. **Don't jump to DP** — always confirm by checking if the problem has overlapping subproblems.
2. **Write the brute-force first** — it reveals the state and transition naturally.
3. **Define state explicitly** — "dp[i] represents the answer for the first i elements."
4. **Iterative over recursive** — safer in interviews (no stack overflow, easier to explain).
5. **Always test edge cases** — empty input, single element, already-sorted input.
