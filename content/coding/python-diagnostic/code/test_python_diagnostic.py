import unittest

from starter import count_eligible


class TestEligibilityCounter(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_eligible([40, 72, 65, 29], 60), 2)

    def test_all_pass(self):
        self.assertEqual(count_eligible([80, 90, 85], 50), 3)

    def test_none_pass(self):
        self.assertEqual(count_eligible([20, 30, 40], 60), 0)

    def test_empty_list(self):
        self.assertEqual(count_eligible([], 50), 0)

    def test_boundary_exact(self):
        self.assertEqual(count_eligible([60, 59, 61], 60), 2)

    def test_single_element_pass(self):
        self.assertEqual(count_eligible([100], 100), 1)

    def test_single_element_fail(self):
        self.assertEqual(count_eligible([50], 100), 0)


if __name__ == "__main__":
    unittest.main()
