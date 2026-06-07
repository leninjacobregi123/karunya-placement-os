import unittest
from starter import frequency_map, most_frequent

class TestDay07(unittest.TestCase):
    def test_freq_basic(self):
        self.assertEqual(frequency_map([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_all_same(self):
        self.assertEqual(frequency_map([5, 5]), {5: 2})

    def test_most_freq(self):
        self.assertEqual(most_frequent([1, 2, 2, 3, 3, 3]), 3)

    def test_tie(self):
        result = most_frequent([1, 1, 2, 2])
        self.assertIn(result, [1, 2])

if __name__ == "__main__":
    unittest.main()
