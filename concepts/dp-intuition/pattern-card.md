# Pattern Card: Dynamic Programming

## Use when:
- "Maximum/minimum" of a subset or arrangement
- "Number of ways" to reach a target
- Choose-or-skip with weight/constraint
- Moving on a grid with step constraints

## Core question:
"How do I split this problem into smaller versions where the answer = function of smaller answers?"

## Common mistakes:
- Wrong base case: dp[0] = 0 (cost), dp[0] = 1 (count) — depends on the problem
- Wrong state: missing a variable (e.g., item index in knapsack)
- Not checking greedy first: DP is O(n·m); greedy is O(n log n)
- Space errors: backwards for knapsack to avoid overwriting needed values

## Interview sentence:
"I'll define dp[i] as the answer for the first i items, build a table bottom-up, and optimize space to O(1) by tracking only the last two values."

## Time/Space Analysis:
| Pattern | States | Time | Space |
|---|-|---|-|
| Linear | n | O(n) | O(1) |
| Knapsack | n·W | O(n·W) | O(W) |
| Grid | R·C | O(R·C) | O(C) |
| LIS/LCS | m·n | O(m·n) | O(m·n) |
