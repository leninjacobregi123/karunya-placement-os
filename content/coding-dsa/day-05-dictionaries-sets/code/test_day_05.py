import unittest

from starter import gradebook_stats


class TestGradebook(unittest.TestCase):
    def test_single_student(self):
        result = gradebook_stats({"Alice": [90, 85, 92]})
        self.assertEqual(result["Alice"]["average"], 89.0)
        self.assertEqual(result["Alice"]["highest"], 92)
        self.assertEqual(result["Alice"]["lowest"], 85)

    def test_multiple_students(self):
        result = gradebook_stats({
            "Alice": [80, 90],
            "Bob": [70, 60]
        })
        self.assertEqual(result["Alice"]["average"], 85.0)
        self.assertEqual(result["Bob"]["average"], 65.0)

    def test_single_grade(self):
        result = gradebook_stats({"Carol": [100]})
        self.assertEqual(result["Carol"]["average"], 100.0)
        self.assertEqual(result["Carol"]["highest"], 100)
        self.assertEqual(result["Carol"]["lowest"], 100)

    def test_empty_gradebook(self):
        self.assertEqual(gradebook_stats({}), {})

    def test_same_grades(self):
        result = gradebook_stats({"Dan": [80, 80, 80]})
        self.assertEqual(result["Dan"]["highest"], 80)
        self.assertEqual(result["Dan"]["lowest"], 80)
        self.assertEqual(result["Dan"]["average"], 80.0)


if __name__ == "__main__":
    unittest.main()
