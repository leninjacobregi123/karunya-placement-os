import unittest
from starter import count_iterations

class TestDay06(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_iterations(3, 4), 12)

    def test_zero(self):
        self.assertEqual(count_iterations(0, 7), 0)

    def test_equal(self):
        self.assertEqual(count_iterations(5, 5), 25)

    def test_large(self):
        self.assertEqual(count_iterations(100, 100), 10000)

if __name__ == "__main__":
    unittest.main()
