# Hint 3

left, right = 0, len(nums) - 1
while left < right:
    s = nums[left] + nums[right]
    if s == target: return (nums[left], nums[right])
    elif s < target: left += 1
    else: right -= 1

Time: O(n). Space: O(1).
