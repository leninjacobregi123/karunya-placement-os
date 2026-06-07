# Hint 1

First window: sum(arr[0:k]).
Slide: add arr[idx], subtract arr[idx-k].
new_sum = old_sum + arr[right] - arr[left]
