import unittest

from starter import placement_fizzbuzz


class TestPlacementFizzBuzz(unittest.TestCase):
    def test_first_five(self):
        result = placement_fizzbuzz(5)
        self.assertEqual(result, ['1', '2', 'Placement', '4', 'Ready'])

    def test_fifteen(self):
        result = placement_fizzbuzz(15)
        self.assertEqual(result[14], 'PlacementReady')
        self.assertEqual(result[2], 'Placement')
        self.assertEqual(result[4], 'Ready')

    def test_thirty(self):
        result = placement_fizzbuzz(30)
        placement_count = result.count('Placement')
        ready_count = result.count('Ready')
        pr_count = result.count('PlacementReady')
        self.assertEqual(placement_count, 8)   # 3,6,9,12,18,21,24,27 (15,30 are PlacementReady)
        self.assertEqual(pr_count, 2)           # 15, 30
        self.assertEqual(ready_count, 4)        # 5,10,20,25 (15,30 are PlacementReady)
        self.assertEqual(result[9], 'Ready')     # index 9 = num 10 -> div by 5 -> 'Ready'
        self.assertEqual(result[12], '13')      # index 12 = num 13 -> same


    def test_single(self):
        self.assertEqual(placement_fizzbuzz(1), ['1'])

    def test_empty(self):
        self.assertEqual(placement_fizzbuzz(0), [])

    def test_all_numbers(self):
        result = placement_fizzbuzz(15)
        self.assertEqual(len(result), 15)
        for i in range(15):
            num = i + 1
            if num % 15 == 0:
                self.assertEqual(result[i], 'PlacementReady')
            elif num % 3 == 0:
                self.assertEqual(result[i], 'Placement')
            elif num % 5 == 0:
                self.assertEqual(result[i], 'Ready')
            else:
                self.assertEqual(result[i], str(num))


if __name__ == "__main__":
    unittest.main()
