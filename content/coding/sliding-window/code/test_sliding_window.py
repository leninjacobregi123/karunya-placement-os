import unittest
from starter import max_subarray_sum, longest_onessub_array

class TestDay10(unittest.TestCase):
    def test_max_sub(self):
        self.assertEqual(max_subarray_sum([2, 5, 1, 8, 3, 7], 3), 18)

    def test_k_equals_n(self):
        self.assertEqual(max_subarray_sum([1, 2, 3]), 6)

    def test_longest_sub(self):
        self.assertEqual(longest_onessub_array([1, 0, 1, 1, 0, 1], 1), 6)

    def test_all_zeros(self):
        self.assertEqual(longest_onessub_array([0, 0, 0], 2), 2)

if __name__ == "__main__":
    unittest.main()
