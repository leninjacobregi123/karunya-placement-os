import unittest
from starter import build_prefix_sum, range_sum

class TestDay08(unittest.TestCase):
    def test_build(self):
        self.assertEqual(build_prefix_sum([1, 2, 3, 4]), [0, 1, 3, 6, 10])

    def test_build_empty(self):
        self.assertEqual(build_prefix_sum([]), [0])

    def test_range_sum(self):
        p = build_prefix_sum([1, 2, 3, 4])
        self.assertEqual(range_sum(p, 0, 0), 1)
        self.assertEqual(range_sum(p, 1, 3), 9)
        self.assertEqual(range_sum(p, 0, 3), 10)

    def test_negative(self):
        p = build_prefix_sum([-1, 2, -3, 4])
        self.assertEqual(range_sum(p, 0, 3), 2)

if __name__ == "__main__":
    unittest.main()
