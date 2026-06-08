import unittest

from starter import word_frequency


class TestWordFrequency(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(word_frequency("hello"), {"hello": 1})

    def test_duplicate_words(self):
        self.assertEqual(word_frequency("the the the"), {"the": 3})

    def test_mixed_words(self):
        result = word_frequency("cat dog cat bird")
        self.assertEqual(result["cat"], 2)
        self.assertEqual(result["dog"], 1)
        self.assertEqual(result["bird"], 1)

    def test_case_sensitive(self):
        result = word_frequency("The the THE")
        self.assertEqual(len(result), 3)  # three different keys

    def test_empty_string(self):
        self.assertEqual(word_frequency(""), {})

    def test_multiple_spaces(self):
        result = word_frequency("hello  world")
        # Split by whitespace — two spaces produce empty string between them
        self.assertIn("hello", result)
        self.assertIn("world", result)

    def test_single_occurrence(self):
        result = word_frequency("apple banana cherry")
        for word in result.values():
            self.assertEqual(word, 1)


if __name__ == "__main__":
    unittest.main()
