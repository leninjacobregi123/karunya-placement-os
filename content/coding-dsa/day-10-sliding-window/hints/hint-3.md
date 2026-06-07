# Hint 3

current = sum(arr[:k])
for i in range(k, n):
    current += arr[i] - arr[i-k]
    max_sum = max(max_sum, current)

Complete: O(n) time, O(1) space.
