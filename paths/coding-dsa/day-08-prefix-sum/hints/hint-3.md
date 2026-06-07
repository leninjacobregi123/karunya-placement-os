# Hint 3

Build: prefix = [0]*(n+1)
for i in range(n): prefix[i+1] = prefix[i] + arr[i]

Query: prefix[j+1] - prefix[i]

O(n) build, O(1) query.
