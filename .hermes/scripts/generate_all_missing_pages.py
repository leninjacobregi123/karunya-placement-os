#!/usr/bin/env python3
"""Generate all missing path content for coding-dsa days 6-10 and aptitude-reasoning days 6-10."""
import os
import json

BASE = "/home/ewards/workspace/kpos/hermes/kpos_hermes_build_pack/repo_seed/karunya-placement-os"

# ============== CODING-DAY DAYS 6-10 ==============
CODING_DAYS_DATA = [
    {
        "num": 6,
        "dir": "day-06-time-complexity",
        "topic": "Time Complexity",
        "slug": "time-complexity",
        "description": "Understand Big-O notation - the language used to measure how an algorithm runtime grows with input size.",
        "module": "modules/coding-foundations/time-complexity/01-simple.md",
        "warmup": "If I have a loop inside a loop, each going from 0 to n-1, how many times does the inner statement execute?",
        "must_do_title": "Analyze loop complexity",
        "test_name": "test_day_06.py",
        "starter": '''def count_iterations(n, m):
    """Count total iterations of: for i in range(n): for j in range(m).

    Args:
        n: outer loop size
        m: inner loop size

    Returns:
        int: total inner iterations

    Example:
        >>> count_iterations(3, 2)
        6
    """
    # Complete this function
    pass
''',
        "tests": '''import unittest
from starter import count_iterations

class TestDay06(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_iterations(3, 4), 12)

    def test_zero(self):
        self.assertEqual(count_iterations(0, 7), 0)
        self.assertEqual(count_iterations(7, 0), 0)

    def test_equal(self):
        self.assertEqual(count_iterations(5, 5), 25)

    def test_large(self):
        self.assertEqual(count_iterations(100, 100), 10000)

if __name__ == "__main__":
    unittest.main()
''',
        "hint1": "# Hint 1\n\nCount the iterations. Outer runs n times, inner runs m times each.\nTotal = n * m.\n\nAsk yourself: trace with n=3, m=2 manually.\n",
        "hint2": "# Hint 2\n\nTotal is n * m. In Big-O: O(n * m).\nIf n == m, it becomes O(n^2) - quadratic time.\n",
        "hint3": "# Hint 3\n\nAnswer: n * m.\n\nKey insight: nested loops multiply their bounds.\nAlways count iterations first, then simplify to Big-O.\n",
        "questions": [
            {"q": "What is the time complexity of iterating over a list of size n once?", "c": ["O(1)", "O(n)", "O(n^2)", "O(log n)"], "a": 1, "e": "We n elements once: O(n)."},
            {"q": "Nested loops both 0 to n-1, complexity?", "c": ["O(n)", "O(2n)", "O(n^2)", "O(n log n)"], "a": 2, "e": "n * n = n^2. Quadratic."},
            {"q": "Binary search on sorted array of size n?", "c": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "a": 1, "e": "Halves search space each step: log2(n) steps."},
            {"q": "faster for large n: O(n) or O(n^2)?", "c": ["O(n^2)", "O(n)", "Equal", "Unknown"], "a": 1, "e": "For n=10^6: O(n)=10^6, O(n^2)=10^12. O(n) is faster."},
            {"q": "Access list element by index?", "c": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "a": 0, "e": "Direct computation: constant time."}
        ],
        "quiz_qs": [
            {"q": "Basic iteration time?", "c": ["O(1)", "O(n)", "O(n^2)", "O(log n)"], "a": 1, "e": "One pass: O(n)."},
            {"q": "If process each item with O(1) work?", "c": ["O(1)", "O(n)", "O(n^2)", "O(n log n)"], "a": 1, "e": "n * O(1) = O(n)."},
            {"q": "Nested loops 0..n-1 complexity?", "c": ["O(n)", "O(2n)", "O(n^2)", "O(n+n)"], "a": 2, "e": "n * n = n^2."},
            {"q": "faster for large n: O(n) or O(n^2)?", "c": ["O(n^2)", "O(n)", "Equal", "Unknown"], "a": 1, "e": "O(n) grows much slower than O(n^2)."},
            {"q": "List access by index time?", "c": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "a": 0, "e": "Direct index: O(1)."}
        ]
    },
    {
        "num": 7,
        "dir": "day-07-arrays-frequency",
        "topic": "Arrays and Frequency Maps",
        "slug": "arrays-frequency",
        "description": "Learn how to count elements using dictionaries (hash maps) - the fastest way to track occurrences.",
        "module": "modules/coding-foundations/arrays-frequency/01-simple.md",
        "warmup": "How would you count how many times each number appears in [1,2,3,1,2,1,4] without using a library?",
        "must_do_title": "Build a frequency map",
        "test_name": "test_day_07.py",
        "starter": '''def frequency_map(arr):
    """Build a frequency map: {element: count} for all elements.

    Args:
        arr: list of integers

    Returns:
        dict: frequency map

    Example:
        >>> frequency_map([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}
    """
    # Complete this function
    pass

def most_frequent(arr):
    """Return the element that appears most often in arr.

    Args:
        arr: list of integers (assume non-empty)

    Returns:
        the most frequent element
    """
    # Complete this function
    pass
''',
        "tests": '''import unittest
from starter import frequency_map, most_frequent

class TestDay07(unittest.TestCase):
    def test_frequency_basic(self):
        self.assertEqual(frequency_map([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_all_same(self):
        self.assertEqual(frequency_map([5, 5]), {5: 2})

    def test_all_different(self):
        self.assertEqual(frequency_map([1, 2, 3]), {1: 1, 2: 1, 3: 1})

    def test_most_frequent(self):
        self.assertEqual(most_frequent([1, 2, 2, 3, 3, 3]), 3)

    def test_tie(self):
        result = most_frequent([1, 1, 2, 2])
        self.assertIn(result, [1, 2])

if __name__ == "__main__":
    unittest.main()
''',
        "hint1": "# Hint 1\n\nA dictionary is a box where key = number, value = count.\nIterate the array and increment each key's counter.\n",
        "hint2": "# Hint 2\n\nUse counts.get(key, 0) + 1 to safely increment.\n\nThis is the standard frequency map: O(n) time, O(n) space.\n",
        "hint3": "# Hint 3\n\nPattern:\ncounts = {}\nfor x in arr:\n    counts[x] = counts.get(x, 0) + 1\n\nThe key with highest value is the answer.\n",
        "questions": [
            {"q": "Minimum time to count frequencies of n elements?", "c": ["O(1)", "O(n)", "O(n log n)", "O(n^2)"], "a": 1, "e": "One pass through array: O(n)."},
            {"q": "Best Python structure for counting frequencies?", "c": ["List", "Dictionary", "Tuple", "Set"], "a": 1, "e": "dict gives O(1) lookup/update."},
            {"q": "Space for frequency map of n distinct elements?", "c": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "a": 2, "e": "Each distinct element gets a key-value pair."},
            {"q": "Find majority element with frequency map?", "c": ["O(n) time, O(n) space", "O(n log n) time, O(1) space", "O(1) time, O(n) space", "O(n^2) time"], "a": 0, "e": "Iterate once (O(n) time), store up to n entries (O(n) space)."},
            {"q": "When would you use frequency map vs manual counting?", "c": ["When performance matters", "When you need counts for ALL elements", "When array is sorted", "Never"], "a": 1, "e": "Frequency maps give counts for every element simultaneously."}
        ],
        "quiz_qs": [
            {"q": "Minimum time to count n elements?", "c": ["O(1)", "O(n)", "O(n log n)", "O(n^2)"], "a": 1, "e": "One pass through array: O(n)."},
            {"q": "Best Python structure for frequencies?", "c": ["List", "Dictionary", "Tuple", "Set"], "a": 1, "e": "dict gives O(1) lookup."},
            {"q": "Space for n distinct elements?", "c": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "a": 2, "e": "Each distinct element gets a bucket."},
            {"q": "Find majority element with frequency map?", "c": ["O(n) time, O(n) space", "O(n log n) time, O(1) space", "O(1) time", "O(n^2) time"], "a": 0, "e": "Iterate once (O(n)), store n entries (O(n) space)."},
            {"q": "When use frequency map vs manual?", "c": ["When performance matters", "When need counts for ALL elements", "When sorted", "Never"], "a": 1, "e": "Frequency maps give counts for every element at once."}
        ]
    },
    {
        "num": 8,
        "dir": "day-08-prefix-sum",
        "topic": "Prefix Sum",
        "slug": "prefix-sum",
        "description": "Precompute running sums to answer range queries in O(1). Build in O(n), query in O(1).",
        "module": "modules/coding-foundations/prefix-sum/01-simple.md",
        "warmup": "If you need the sum of elements from index i to j in an array, what is the naive approach? How could pre-sums help?",
        "must_do_title": "Range sum queries",
        "test_name": "test_day_08.py",
        "starter": '''def build_prefix_sum(arr):
    """Build a prefix sum array. prefix[0] = 0.

    Args:
        arr: list of integers

    Returns:
        list: prefix sum array of len(arr)+1

    Example:
        >>> build_prefix_sum([1, 2, 3, 4])
        [0, 1, 3, 6, 10]
    """
    # Complete this function
    pass

def range_sum(prefix, left, right):
    """Answer a subarray sum query in O(1).

    Args:
        prefix: the prefix sum array
        left: start index (inclusive)
        right: end index (inclusive)

    Returns:
        sum of arr[left...right]
    """
    # Complete this function
    pass
''',
        "tests": '''import unittest
from starter import build_prefix_sum, range_sum

class TestDay08(unittest.TestCase):
    def test_build_basic(self):
        self.assertEqual(build_prefix_sum([1, 2, 3, 4]), [0, 1, 3, 6, 10])

    def test_build_empty(self):
        self.assertEqual(build_prefix_sum([]), [0])

    def test_range_single(self):
        p = build_prefix_sum([1, 2, 3, 4])
        self.assertEqual(range_sum(p, 0, 0), 1)
        self.assertEqual(range_sum(p, 1, 3), 9)

    def test_range_full(self):
        p = build_prefix_sum([1, 2, 3, 4])
        self.assertEqual(range_sum(p, 0, 3), 10)

    def test_negative(self):
        p = build_prefix_sum([-1, 2, -3, 4])
        self.assertEqual(range_sum(p, 0, 3), 2)

if __name__ == "__main__":
    unittest.main()
''',
        "hint1": "# Hint 1\n\nPrefix array has length n+1. prefix[0] = 0 (zero elements).\nprefix[i] = prefix[i-1] + arr[i-1] for i >= 1.\nOne pass through the array.\n",
        "hint2": "# Hint 2\n\nTo find sum of arr[left...right]:\nprefix[right+1] - prefix[left]\n\nTwo lookups, one subtraction = O(1).\n",
        "hint3": "# Hint 3\n\nBuild: prefix = [0]*(n+1)\nfor i in range(n): prefix[i+1] = prefix[i] + arr[i]\n\nQuery: prefix[j+1] - prefix[i]\n\nO(n) build, O(1) query.\n",
        "questions": [
            {"q": "Time to build prefix sum array of size n?", "c": ["O(1)", "O(n)", "O(n log n)", "O(n^2)"], "a": 1, "e": "One run: prefix[i] = prefix[i-1] + arr[i]. All in O(n)."},
            {"q": "After building, how fast to answer a subarray query?", "c": ["O(1)", "O(n)", "O(log n)", "O(n log n)"], "a": 0, "e": "prefix[right+1] - prefix[left]: two lookups."},
            {"q": "Total time for k range queries using prefix sums?", "c": ["O(n + k)", "O(n * k)", "O(n log n + k)", "O(k log n)"], "a": 0, "e": "Build takes O(n). Each of k queries takes O(1). Total: O(n + k)."},
            {"q": "If all elements are negative, does prefix-sum still work?", "c": ["No", "Yes, same way", "Only if sum = 0", "Depends on values"], "a": 1, "e": "Prefix sums handle negative values fine."},
            {"q": "Can prefix sums extend to 2D arrays? Query time for sub-rectangle?", "c": ["No, only 1D", "Yes, O(1) query", "Yes, but O(n) query", "Yes, O(log n) query"], "a": 1, "e": "A 2D prefix sum grid lets you query any sub-rectangle in O(1)."}
        ],
        "quiz_qs": [
            {"q": "Time to build prefix sum array of size n?", "c": ["O(1)", "O(n)", "O(n log n)", "O(n^2)"], "a": 1, "e": "One run through array: O(n)."},
            {"q": "After building, how fast for a subarray query?", "c": ["O(1)", "O(n)", "O(log n)", "O(n log n)"], "a": 0, "e": "Two lookups, one subtraction: O(1)."},
            {"q": "Total time for k range queries?", "c": ["O(n + k)", "O(n * k)", "O(n log n + k)", "O(k log n)"], "a": 0, "e": "Build O(n), each query O(1): O(n + k). Total."},
            {"q": "If all elements are negative, does prefix work?", "c": ["No", "Yes, same way", "Only if sum = 0", "Depends"], "a": 1, "e": "Prefix sums handle negative values just fine."},
            {"q": "Can prefix sums extend to 2D? Query time?", "c": ["No, only 1D", "Yes, O(1)", "Yes, O(n)", "Yes, O(log n)"], "a": 1, "e": "Yes - 2D prefix grid: O(1) for sub-rectangle query."}
        ]
    },
    {
        "num": 9,
        "dir": "day-09-two-pointers",
        "topic": "Two Pointers",
        "slug": "two-pointers",
        "description": "Use two indices moving toward or away from each other. Ideal for sorted arrays, searching pairs, and modifications.",
        "module": "modules/coding-foundations/two-pointers/01-simple.md",
        "warmup": "How would you check if an array is sorted in O(n)? Could two moving indices help find a pair with a specific sum?",
        "must_do_title": "Pair sum in sorted array",
        "test_name": "test_day_09.py",
        "starter": '''def pair_with_target(sorted_nums, target):
    """Find two numbers in a sorted array that add to target.

    Uses two-pointer technique.

    Args:
        sorted_nums: sorted list of integers
        target: the sum to find

    Returns:
        tuple (a, b) if found, else None

    Example:
        >>> pair_with_target([1, 3, 5, 7, 9], 10)
        (1, 9)
    """
    # Complete this function
    pass

def is_palindrome_two_pointer(s):
    """Check if string is a palindrome.

    Args:
        s: string to check

    Returns:
        True if palindrome, False otherwise
    """
    # Complete this function
    pass
''',
        "tests": '''import unittest
from starter import pair_with_target, is_palindrome_two_pointer

class TestDay09(unittest.TestCase):
    def test_pair_found(self):
        result = pair_with_target([1, 3, 5, 7, 9], 10)
        self.assertIn(result, [(1, 9), (3, 7)])

    def test_pair_not_found(self):
        self.assertIsNone(pair_with_target([1, 3, 5], 100))

    def test_pair_same(self):
        self.assertEqual(pair_with_target([5, 5, 5], 10), (5, 5))

    def test_palindrome_yes(self):
        self.assertTrue(is_palindrome_two_pointer("racecar"))
        self.assertTrue(is_palindrome_two_pointer("madam"))

    def test_palindrome_no(self):
        self.assertFalse(is_palindrome_two_pointer("hello"))

if __name__ == "__main__":
    unittest.main()
''',
        "hint1": "# Hint 1\n\nStart with left = 0 and right = len(nums) - 1.\n\nIf sum < target: move left forward (increase).\nIf sum > target: move right backward (decrease).\n",
        "hint2": "# Hint 2\n\nWhy? Array is sorted. Moving left forward increases the sum.\nMoving right backward decreases the sum.\n\nKey insight: sorted means we decide which pointer to move.\n",
        "hint3": "# Hint 3\n\nleft, right = 0, len(nums) - 1\nwhile left < right:\n    s = nums[left] + nums[right]\n    if s == target: return (nums[left], nums[right])\n    elif s < target: left += 1\n    else: right -= 1\n\nTime: O(n). Space: O(1).\n",
        "questions": [
            {"q": "In two-pointer technique for sorted array, where do we start?", "c": ["Both at beginning", "Both at end", "Left at 0, right at last index", "Randomly"], "a": 2, "e": "One pointer at smallest, one at largest value."},
            {"q": "If sum of two pointer values > target, what to do?", "c": ["Move left forward", "Move right backward", "Move both", "Stop"], "a": 1, "e": "Moving right backward reduces the sum."},
            {"q": "Time complexity of two-pointer search in sorted array of size n?", "c": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "a": 2, "e": "Each step moves one pointer. Total: O(n)."},
            {"q": "What is slow/fast pointer useful for?", "c": ["Sorting", "Detecting cycles and finding middle", "Searching unsorted arrays", "Merging"], "a": 1, "e": "Fast moves 2 steps while slow moves 1."},
            {"q": "Can two pointers work on unsorted array?", "c": ["No", "Only after sorting", "Yes, with same O(n) benefit", "Only for specific problems"], "a": 0, "e": "Sort is key property that lets us decide which pointer to move."}
        ],
        "quiz_qs": [
            {"q": "In two-pointer technique for sorted array, where do we start?", "c": ["Both at 0", "Both at last", "Left at 0, right at last", "Random"], "a": 2, "e": "One at start, one at end."},
            {"q": "If sum > target, what do?", "c": ["Move left", "Move right backward", "Both", "Stop"], "a": 1, "e": "Moves right toward smaller values."},
            {"q": "Time complexity of two-pointer search in sorted array of size n?", "c": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "a": 2, "e": "Total steps: O(n)."},
            {"q": "What is slow/fast pointer useful for?", "c": ["Sorting", "Detecting cycles and finding middle", "Searching unsorted", "Merging"], "a": 1, "e": "Detects cycles and finds middle efficiently."},
            {"q": "Can two pointers work on unsorted array?", "c": ["No", "Only after sorting", "Yes, with O(n)", "Only for some"], "a": 0, "e": "Sort is needed to decide pointer direction."}
        ]
    },
    {
        "num": 10,
        "dir": "day-10-sliding-window",
        "topic": "Sliding Window",
        "slug": "sliding-window",
        "description": "Maintain a window of k consecutive elements and slide it one step at a time. More efficient than re-computing for each window position.",
        "module": "modules/coding-foundations/sliding-window/01-simple.md",
        "warmup": "To find the maximum sum of any 3 consecutive elements, what is the naive approach? How could you slide the window to avoid re-computing?",
        "must_do_title": "Max sum of k consecutive elements",
        "test_name": "test_day_10.py",
        "starter": '''def max_subarray_sum(arr, k):
    """Find the maximum sum of any k consecutive elements.

    Uses sliding window technique.

    Args:
        arr: list of integers (non-empty)
        k: window size (1 <= k <= len(arr))

    Returns:
        int: maximum sum

    Example:
        >>> max_subarray_sum([2, 5, 1, 8, 3, 7], 3)
        18  # from [8, 3, 7]
    """
    # Complete this function
    pass

def longest_onessub_array(arr, k):
    """Find longest contiguous subarray with at most k zeros flipped to 1s.

    Uses variable-size sliding window.

    Args:
        arr: list of 0s and 1s
        k: max zeros allowed

    Returns:
        int: length of longest valid subarray
    """
    # Complete this function
    pass
''',
        "tests": '''import unittest
from starter import max_subarray_sum, longest_onessub_array

class Testday10(unittest.TestCase):
    def test_max_sub_basic(self):
        self.assertEqual(max_subarray_sum([2, 5, 1, 8, 3, 7], 3), 18)

    def test_max_sub_k_equals_n(self):
        self.assertEqual(max_subarray_sum([1, 2, 3]), 6)

    def test_max_sub_k_equals_1(self):
        self.assertEqual(max_subarray_sum([4, 1, 7, 3]), 7)

    def test_longest_sub_with_zeros(self):
        result = longest_onessub_array([1, 0, 1, 1, 0, 1], 1)
        self.assertEqual(result, 6)  # we can flip one 0 to 1

    def test_longest_sub_all_zeros(self):
        self.assertEqual(longest_onessub_array([0, 0, 0], 2), 2)

if __name__ == "__main__":
    unittest.main()
''',
        "hint1": "# Hint 1\n\nFirst window: sum(arr[0:k]).\nSlide: add arr[idx], subtract arr[idx-k].\n\nnew_sum = old_sum + arr[right] - arr[left]\n",
        "hint2": "# Hint 2\n\nEach slide takes O(1) instead of O(k).\nFor k=n/2, this changes from O(n*k) to just O(n).\n",
        "hint3": "# Hint 3\n\nSlide:\ncurrent = sum(arr[:k])\nfor i in range(k, n):\n    current += arr[i] - arr[i-k]\n    max_sum = max(max_sum, current)\n\nComplexity: O(n) time, O(1) space.\n",
        "questions": [
            {"q": "Naive way to find max sum of k consecutive elements?", "c": ["Check each window: O(n*k)", "Two pointers: O(n)", "Sort first: O(n log n)", "Frequency map: O(n)"], "a": 0, "e": "For each window, sum k elements: O(n*k). Sliding window improves to O(n)."},
            {"q": "In sliding window, how update sum when window slides right?", "c": ["Add new and subtract old element", "Recompute sum from scratch", "Add all new elements", "Subtract all old elements"], "a": 0, "e": "new_sum = old_sum + arr[right] - arr[left]. Two operations."},
            {"q": "Complexity of sliding window for max sum of k consecutive?", "c": ["O(1)", "O(n)", "O(n log n)", "O(n*k)"], "a": 1, "e": "Slide window across (n-k+1) positions. Each slide O(1). Total: O(n)."},
            {"q": "When use variable-size sliding window instead of fixed-size?", "c": ["Always, more efficient", "When constraint depends on condition (e.g., sum >= target)", "Only when sorted", "Never"], "a": 1, "e": "Dynamic windows grow/shrink based on conditions."},
            {"q": "Space complexity of basic sliding window approach?", "c": ["O(k) if store elements", "O(1) if only track running sum/min/max", "O(n) always", "O(log n)"], "a": 1, "e": "If only need result and update incrementally, O(1) extra space."}
        ],
        "quiz_qs": [
            {"q": "Naive way to find max sum of k consecutive elements?", "c": ["Check each window: O(n*k)", "Two pointers: O(n)", "Sort first: O(n log n)", "Frequency map: O(n)"], "a": 0, "e": "For each window, sum k elements: O(n*k). Sliding window improves it to O(n)."},
            {"q": "In sliding window, how update sum when window slides right?", "c": ["Add new and subtract old", "Recompute from scratch", "Add all new", "Subtract all old"], "a": 0, "e": "new sum = old sum + arr[right] - arr[left]."},
            {"q": "Complexity of sliding window for max sum of k consecutive?", "c": ["O(1)", "O(n)", "O(n log n)", "O(n*k)"], "a": 1, "e": "Slide window across (n-k+1) positions. Each slide O(1). Total: O(n)."},
            {"q": "When use variable-size sliding window instead of fixed-size?", "c": ["Always, more efficient", "When constraint depends on condition", "Only when sorted", "Never"], "a": 1, "e": "Dynamic windows grow/ shrink based on conditions."},
            {"q": "Space complexity of basic sliding window approach?", "c": ["O(k)", "O(1)", "O(n)", "O(log n)"], "a": 1, "e": "If only need result, update incrementally: O(1) extra space."}
        ]
    }
]

# ============== APTITUDE-DAY DAYS 6-10 ==============
APT_DAYS_DATA = [
    {
        "num": 6,
        "dir": "day-06-simple-interest",
        "topic": "Simple and Compound Interest", 
        "slug": "simple-interest",
        "description": "Learn SI and CI formulas and their applications. SI = PRT/100. CI = P(1+r/100)^t - P. Understand when each applies and key differences.",
        "warmup": "What is the simple interest on Rs. 1000 at 5% per annum for 3 years? How is it different from compound interest?",
        "must_do": "Calculate simple interest"
    },
    {
        "num": 7,
        "dir": "day-07-time-work",
        "topic": "Time and Work",
        "slug": "time-work",
        "description": "Work = Rate x Time. If A takes 'a' days alone and B takes 'b' days, together they take ab/(a+b) days.",
        "warmup": "If person A can finish a task in 6 days and person B in 8 days, how long will it take them working together?",
        "must_do": "Find combined work time"
    },
    {
        "num": 8,
        "dir": "day-08-pipes-cisterns",
        "topic": "Pipes and Cisterns",
        "slug": "pipes-cisterns",
        "description": "Filling pipes add work; emptying pipes subtract. Rate of filling = 1/t. Net rate = sum of all rates.",
        "warmup": "If a pipe fills a tank in 4 hours and another empties it in 6 hours, what is the net rate of filling?",
        "must_do": "Net filling time with pipes"
    },
    {
        "num": 9,
        "dir": "day-09-speed-distance",
        "topic": "Speed, Time, and Distance",
        "slug": "speed-distance",
        "description": "Speed = Distance / Time. Average speed = total distance / total time. Relative speed changes when objects move toward or away.",
        "warmup": "A car travels 120 km at 60 km/h and returns at 40 km/h. What is the average speed for the round trip?",
        "must_do": "Find average speed"
    },
    {
        "num": 10,
        "dir": "day-10-trains",
        "topic": "Trains and Boats",
        "slug": "trains",
        "description": "Train problems: crossing poles, platforms, and other trains. Speed = distance/time. Relative speed when two trains meet.",
        "warmup": "A 150 m long train crosses a pole in 12 seconds. What is its speed in km/h?",
        "must_do": "Train speed from crossing time"
    }
]

# ============== HELPER FUNCTIONS ==============

def make_readme_template(day_info):
    return f"""# Day {day_info['num']:02d}: {day_info['topic']}

## Today's Goal

{day_info['description']}

## Time: 30 minutes

## Warm Up (2 min)

{day_info['warmup']}

## Learn (8 min)

Read the module: [`{day_info['module']}`](../../{day_info['module']})

## Practice (12 min)

### Must-Do: {day_info['must_do']}

Open `code/starter.py` and implement the function. Then run:

```bash
python -m unittest code/" + (day_info.get('test_name', '') or 'test_day.py') + """
```

## Check

```bash
python scripts/kpos.py check --path coding-dsa --day {day_info['num']}
```

## Quiz (5 min)

Open `quiz.json` and answer 5 questions. Then record:

```bash
python scripts/kpos.py quiz --path coding-dsa --day {day_info['num']} --score YOUR_SCORE --total 5
```

## Reflect (3 min)

Read `reflection.md` and write your answers somewhere you can revisit them.

## Hints

If you get stuck, read:

- [Hint 1](hints/hint-1.md)
- [Hint 2](hints/hint-2.md)
- [Hint 3](hints/hint-3.md)

## AI Help

Read [ai-help.md](ai-help.md) before asking AI for help.

## Complete the Day

```bash
python scripts/kpos.py complete-day --path coding-dsa --day {day_info['num']}
```

"""

def make_readme_apt_template(day_info):
    return f"""# Day {day_info['num']:02d}: {day_info['topic']}

## Today's Goal

{day_info['description']}

## Time: 30 minutes

## Warm Up (2 min)

{day_info['warmup']}

## Learn (8 min)

Study the key concepts and formulas in the module.

## Practice (12 min)

### Must-Do: {day_info['must_do']}

Open `answers.json` and solve the practice problem. Then check your answer.

## Check

```bash
python scripts/kpos.py check --path aptitude-reasoning --day {day_info['num']}
```

## Quiz (5 min)

Open `quiz.json` and answer 5 questions. Then record:

```bash
python scripts/kpos.py quiz --path aptitude-reasoning --day {day_info['num']} --score YOUR_SCORE --total 5
```

## Reflect (3 min)

Read `reflection.md` and write your answers somewhere you can revisit them.

## Hints

If you get stuck, read:

- [Hint 1](hints/hint-1.md)
- [Hint 2](hints/hint-2.md)
- [Hint 3](hints/hint-3.md)

## AI Help

Read [ai-help.md](ai-help.md) before asking AI for help.

## Complete the Day

```bash
python scripts/kpos.py complete-day --path aptitude-reasoning --day {day_info['num']}
```

"""

def make_ai_help(heading, topic, questions, pro_tip):
    return f"""# AI Help: {topic}

**Goal:** Help the student understand {topic} - a key pattern for solving {topic.split(',')[0].split(' and ')[0]}.

**Do not solve the problem directly.**

**Ask one question at a time.**

**Maximum response:** 180 words.

**Before hinting, ask:** {questions}

**Guiding questions:**
- What information is given vs. what needs to be found?
- Which formula connects them?
- Can you explain the key insight in one sentence?

**Pro tip:** {pro_tip}\n
"""

def make_reflection(num, topic):
    return f"""# Day {num:02d} Reflection: {topic}

Take 3 minutes. Answer these honestly - no one else will see them.

- Which concept was hardest to grasp? Why?
- Can you explain the key insight in one sentence to a classmate?
- Give an example from your practice where this pattern would apply.
- What is one question you still want to practice more?

---

Write one thing you learned today in one sentence:

>
"""

def make_quiz(num, topic):
    return {"day": num, "topic": topic, "questions": []}

# ============== MAIN GENERATION ==============

def main():
    files_written = 0

    # Generate coding days 6-10
    for data in CODING_DAYS_DATA:
        dpath = os.path.join(BASE, "paths/coding-dsa", data["dir"])
        os.makedirs(os.path.join(dpath, "code", "hints"), exist_ok=True)

        # README.md
        readme = f"""# Day {data['num']:02d}: {data['topic']}

## Today's Goal

{data['description']}

## Time: 30 minutes

## Warm Up (2 min)

{data['warmup']}

## Learn (8 min)

Read the module: [`{data['module']}`](../../{data['module']})

## Practice (12 min)

### Must-Do: {data['must_do_title']}

Open `code/starter.py` and implement the function. Then run:

```bash
python -m unittest code/{data['test_name']}
```

## Check

```bash
python scripts/kpos.py check --path coding-dsa --day {data['num']}
```

## Quiz (5 min)

Open `quiz.json` and answer 5 questions. Then record:

```bash
python scripts/kpos.py quiz --path coding-dsa --day {data['num']} --score YOUR_SCORE --total 5
```

## Reflect (3 min)

Read `reflection.md` and write your answers somewhere you can revisit them.

## Hints

If you get stuck, read:

- [Hint 1](hints/hint-1.md)
- [Hint 2](hints/hint-2.md)
- [Hint 3](hints/hint-3.md)

## AI Help

Read [ai-help.md](ai-help.md) before asking AI for help.

## Complete the Day

```bash
python scripts/kpos.py complete-day --path coding-dsa --day {data['num']}
```
"""
        with open(os.path.join(dpath, "README.md"), "w") as fout:
            fout.write(readme)
        files_written += 1

        # ai-help.md
        ai_help = f"""# AI Help: {data['topic']}

**Goal:** Help the student understand {data['topic']} - a key pattern for solving {data['topic'].split(',')[0].split(' and ')[0]} problems efficiently.

**Do not solve the problem directly.**

**Ask one question at a time.**

**Maximum response:** 180 words.

**Before hinting, ask:** What pattern does this problem remind you of?

**Guiding questions:**
- Can you identify the input size and the operations needed?
- What is the brute-force approach? Can you improve on it?

**Pro tip:** For {data['topic']} problems, think about how to process data in a single pass or use a data structure to speed up lookups.\n
"""
        with open(os.path.join(dpath, "ai-help.md"), "w") as fout:
            fout.write(ai_help)
        files_written += 1

        # quiz.json
        quiz = {"day": data["num"], "topic": data["topic"], "questions": data["quiz_qs"]}
        with open(os.path.join(dpath, "quiz.json"), "w") as fout:
            json.dump(quiz, fout, indent=2)
        files_written += 1

        # reflection.md
        reflection = make_reflection(data["num"], data["topic"])
        with open(os.path.join(dpath, "reflection.md"), "w") as fout:
            fout.write(reflection)
        files_written += 1

        # tasks.json
        tasks = {"day": data["num"], "topic": data["topic"], "slug": data["slug"], 
                "path": "coding-dsa", "time_minutes": 30, "warmup": data["warmup"],
                "read": data["module"],
                "practice": [{"type": "must_do", "title": data["must_do_title"], "file": "code/starter.py"}],
                "quiz_file": "quiz.json", "timed_drill_file": "timed-drill.json",
                "reflection_file": "reflection.md"}
        with open(os.path.join(dpath, "tasks.json"), "w") as fout:
            json.dump(tasks, fout, indent=2)
        files_written += 1

        # timed-drill.json
        timed_qs = [
            {"question": "Which complexity class grows fastest for large n?", "choices": ["O(log n)", "O(n)", "O(n log n)", "O(n^2)"], "answer": 3},
            {"question": "If an algorithm takes 1 second for input 1000, about how long for input 2000 with O(n)?", "choices": ["0.5 seconds", "1 second", "2 seconds", "4 seconds"], "answer": 2},
            {"question": "Can any algorithm that inspects every element be faster than O(n)?", "choices": ["Yes, always", "No, not if all data matters", "Yes, with O(1)", "It depends on the hardware"], "answer": 1},
            {"question": "For O(n^2) vs O(n log n), which wins for n = 10^6?", "choices": ["O(n^2) because it is simpler", "O(n log n) because it grows slower", "They are the same", "Cannot compare without constants"], "answer": 1},
            {"question": "What does Big-O describe?", "choices": ["Exact runtime", "Best case only", "Growth rate of the worst case", "Average case only"], "answer": 2}
        ]
        timed = {"day": data["num"], "topic": data["topic"], "time_limit_seconds": 120, "questions": timed_qs}
        with open(os.path.join(dpath, "timed-drill.json"), "w") as fout:
            json.dump(timed, fout, indent=2)
        files_written += 1

        # code/starter.py
        with open(os.path.join(dpath, "code", "starter.py"), "w") as fout:
            fout.write(data["starter"])
        files_written += 1

        # code/test_day_XX.py
        with open(os.path.join(dpath, "code", data["test_name"]), "w") as fout:
            fout.write(data["tests"])
        files_written += 1

        # hints
        for i, hint_text in enumerate([data["hint1"], data["hint2"], data["hint3"]], 1):
            with open(os.path.join(dpath, "hints", f"hint-{i}.md"), "w") as fout:
                fout.write(hint_text)
        files_written += 3

        print(f"Coding Day {data['num']:02d} ({data['topic']}): 8 files")

    # Generate aptitude days 6-10
    for data in APT_DAYS_DATA:
        dpath = os.path.join(BASE, "paths/aptitude-reasoning", data["dir"])
        os.makedirs(os.path.join(dpath, "hints"), exist_ok=True)

        # README.md
        readme = f"""# Day {data['num']:02d}: {data['topic']}

## Today's Goal

{data['description']}

## Time: 30 minutes

## Warm Up (2 min)

{data['warmup']}

## Learn (8 min)

Study the key concepts and formulas in the module.

## Practice (12 min)

### Must-Do: {data['must_do']}

Open `answers.json` and solve the practice problem. Then check your answer.

## Check

```bash
python scripts/kpos.py check --path aptitude-reasoning --day {data['num']}
```

## Quiz (5 min)

Open `quiz.json` and answer 5 questions. Then record:

```bash
python scripts/kpos.py quiz --path aptitude-reasoning --day {data['num']} --score YOUR_SCORE --total 5
```

## Reflect (3 min)

Read `reflection.md` and write your answers somewhere you can revisit them.

## Hints

If you get stuck, read:

- [Hint 1](hints/hint-1.md)
- [Hint 2](hints/hint-2.md)
- [Hint 3](hints/hint-3.md)

## AI Help

Read [ai-help.md](ai-help.md) before asking AI for help.

## Complete the Day

```bash
python scripts/kpos.py complete-day --path aptitude-reasoning --day {data['num']}
```
"""
        with open(os.path.join(dpath, "README.md"), "w") as fout:
            fout.write(readme)
        files_written += 1

        # ai-help.md
        ai_help = f"""# AI Help: {data['topic']}

**Goal:** Help the student understand {data['topic']} - a key pattern for solving {data['topic'].split(',')[0].split(' and ')[0]} problems.

**Do not solve the problem directly.**

**Ask one question at a time.**

**Maximum response:** 180 words.

**Before hinting, ask:** What formula or pattern applies to this problem?

**Guiding questions:**
- What information is given vs. what needs to be found?
- Which formula connects them?
- Can you explain the key insight in one sentence to a classmate?

**Pro tip:** Always write down given values before picking a formula. Identify what changes and what stays constant.\n
"""
        with open(os.path.join(dpath, "ai-help.md"), "w") as fout:
            fout.write(ai_help)
        files_written += 1

        # answer-key.md
        answer_key = f"""# Answer Key for Day {data['num']}

## Quiz Answers

### Q1
Practice with the basic formula.

### Q2
Apply the concept to a new scenario.

### Q3
Compare two different approaches.

### Q4
Work through an edge case.

### Q5
Generalize the result for any values.

## Tips
- Always write down your known values first
- Check units before calculating
- Show your work step by step
"""
        with open(os.path.join(dpath, "answer-key.md"), "w") as fout:
            fout.write(answer_key)
        files_written += 1

        # reflection.md
        reflection = make_reflection(data["num"], data["topic"])
        with open(os.path.join(dpath, "reflection.md"), "w") as fout:
            fout.write(reflection)
        files_written += 1

        # quiz.json - 5 questions
        quiz_qs = [
            {"question": f"What is the basic formula for {data['topic'].split(',')[0].split(' and ')[0]}?", "choices": ["Formula A", "Formula B", "Formula C", "Formula D"], "answer": 0},
            {"question": "If given rate and time, find work:", "choices": ["Rate x Time", "Rate + Time", "Rate / Time", "Rate - Time"], "answer": 0},
            {"question": "What does average speed always mean?", "choices": ["Total distance/total time", "Average of speeds", "Median of speeds", "Sum of speeds"], "answer": 0},
            {"question": "Most common mistake in {} problems?".format(data['topic'].split(',')[0].split(' and ')[0]), "choices": ["Using wrong formula", "Unit errors", "Sign mistakes", "Calculation"], "answer": 0},
            {"question": "How verify your answer?", "choices": ["All of the above", "Only check units", "Only plug back", "Only compare"], "answer": 0}
        ]
        if len(quiz_qs[3]) > 4:
            quiz_qs[3] = {"question": f"Most common mistake in {data['topic']} problems?", "choices": ["Using wrong formula", "Unit errors", "Sign mistakes", "Arithmetic errors"], "answer": 0}
        quiz = {"day": data["num"], "topic": data["topic"], "questions": quiz_qs}
        with open(os.path.join(dpath, "quiz.json"), "w") as fout:
            json.dump(quiz, fout, indent=2)
        files_written += 1

        # tasks.json
        tasks = {"day": data["num"], "topic": data["topic"], "slug": data["slug"],
                 "path": "aptitude-reasoning", "time_minutes": 30, "warmup": data["warmup"],
                 "read": "modules/aptitude-foundations/{}/01-simple.md".format(data['num']),
                 "practice": [{"type": "must_do", "title": data["must_do"], "file": "answers.json"}],
                 "quiz_file": "quiz.json", "timed_drill_file": "timed-drill.json",
                 "reflection_file": "reflection.md"}
        with open(os.path.join(dpath, "tasks.json"), "w") as fout:
            json.dump(tasks, fout, indent=2)
        files_written += 1

        # timed-drill.json
        timed_qs = [
            {"question": "Basic SI formula?", "choices": ["PRT/100", "P(1+r)^t", "P*r*t", "P*t/r"], "answer": 0},
            {"question": "If work = rate * time, work =", "choices": ["Rate x Time", "Rate + Time", "Rate / Time", "Rate - Time"], "answer": 0},
            {"question": "Relative speed toward each other:", "choices": ["v1+v2", "|v1-v2|", "v1*v2", "sqrt(v1*v2)"], "answer": 0},
            {"question": "What is most common mistake in {}?".format(data['topic'].split(',')[0].split(' and ')[0][0]), "choices": ["Wrong formula", "Units", "Signs", "Arithmetic"], "answer": 0},
            {"question": "How verify answer?", "choices": ["Everything", "Only units", "Only plug back", "Only compare"], "answer": 0}
        ]
        timed = {"day": data["num"], "topic": data["topic"], "time_limit_seconds": 120, "questions": timed_qs}
        with open(os.path.join(dpath, "timed-drill.json"), "w") as fout:
            json.dump(timed, fout, indent=2)
        files_written += 1

        # hints
        for i, hint_text in enumerate([
            "# Hint 1\n\nAlways write down the formula you need before plugging in values.\nStart with: What do I know? What do I need to find?\n",
            "# Hint 2\n\nIdentify the key relationship between given values and the unknown.\nTry substituting in the formula step by step.\n",
            "# Hint 3\n\nCheck your answer by plugging it back in.\nDoes it make sense? Try an estimate first.\n"
        ], 1):
            with open(os.path.join(dpath, "hints", f"hint-{i}.md"), "w") as fout:
                fout.write(hint_text)
        files_written += 3

        # answers.json placeholder
        answers = {"day": data["num"], "topic": data["topic"],
                   "must_do_question": "Solve: apply {} concepts to a real scenario.".format(data['topic'].lower()),
                   "answers": [{"q": "Practice 1", "my_answer": "", "is_correct": False},
                                {"q": "Practice 2", "my_answer": "", "is_correct": False},
                                {"q": "Practice 3", "my_answer": "", "is_correct": False},
                                {"q": "Practice 4", "my_answer": "", "is_correct": False},
                                {"q": "Practice 5", "my_answer": "", "is_correct": False}]}
        with open(os.path.join(dpath, "answers.json"), "w") as fout:
            json.dump(answers, fout, indent=2)
        files_written += 1

        print(f"Aptitude Day {data['num']:02d} ({data['topic']}): 6 files")

    print(f"\nTotal files: {files_written}")

if __name__ == "__main__":
    main()
