import unittest

from starter import execute_and_verify


class TestDryRunThinking(unittest.TestCase):
    """Each test case describes a code snippet to trace manually."""

    def test_simple_addition(self):
        """Trace: x = 10; y = 20; result = x + y"""
        # Final value: result = 30
        result = execute_and_verify("x = 10; y = 20; result = 30", 30)
        self.assertTrue(result)

    def test_loop_accumulator(self):
        """Trace: total = 0; for i in [1,2,3]: total += i"""
        # Final value: total = 6
        result = execute_and_verify("total = 0; for i in [1,2,3]: total += i; result = total", 6)
        self.assertTrue(result)

    def test_while_loop(self):
        """Trace: n = 10; while n > 0: n -= 2"""
        # Final value: n = 0 (10->8->6->4->2->0, exits at 0)
        result = execute_and_verify("n = 10; while n > 0: n -= 2; result = n", 0)
        self.assertTrue(result)

    def test_condition_branch(self):
        """Trace: x = 5; if x > 3: x = x * 2 else: x = x + 1"""
        # x > 3 is True, so x = 5 * 2 = 10
        result = execute_and_verify("x = 5; if x > 3: x = x * 2; else: x = x + 1; result = x", 10)
        self.assertTrue(result)

    def test_list_access(self):
        """Trace: items = [10, 20, 30]; last = items[-1]"""
        # items[-1] = 30
        result = execute_and_verify("items = [10, 20, 30]; last = items[-1]", 30)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
