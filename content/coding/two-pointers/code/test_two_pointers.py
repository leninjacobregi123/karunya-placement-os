import unittest
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

    def test_palindrome_no(self):
        self.assertFalse(is_palindrome_two_pointer("hello"))

if __name__ == "__main__":
    unittest.main()
