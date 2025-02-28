import solution
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # Basic test case with mixed elements
        inventory = [2, 0, 0, 3, 3, 0, 2, 2]
        priority = [0, 2, 3]
        expected = [0, 0, 0, 2, 2, 2, 3, 3]
        actual = solution.sort_inventory(inventory, priority)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        # Already sorted inventory
        inventory = [0, 0, 0, 2, 2, 2, 3, 3]
        priority = [0, 2, 3]
        expected = [0, 0, 0, 2, 2, 2, 3, 3]
        actual = solution.sort_inventory(inventory, priority)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        # Inventory contains only one type of item (all first priority)
        inventory = [5, 5, 5, 5]
        priority = [5, 4, 3]
        expected = [5, 5, 5, 5]
        actual = solution.sort_inventory(inventory, priority)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        # Inventory contains only two types of items
        inventory = [4, 4, 6, 6, 6, 4, 4, 6]
        priority = [6, 4, 5]
        expected = [6, 6, 6, 6, 4, 4, 4, 4]
        actual = solution.sort_inventory(inventory, priority)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        # Edge case with an empty inventory
        inventory = []
        priority = [1, 2, 3]
        expected = []
        actual = solution.sort_inventory(inventory, priority)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        # Inventory missing one item from the priority list
        inventory = [3, 3, 2, 2, 2, 3, 3, 3]
        priority = [1, 2, 3]
        expected = [2, 2, 2, 3, 3, 3, 3, 3]  # 1 is missing, so only 2s and 3s
        actual = solution.sort_inventory(inventory, priority)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        # Large input test (Stress test)
        inventory = [3, 1, 2] * 1000
        priority = [1, 2, 3]
        expected = [1] * 1000 + [2] * 1000 + [3] * 1000
        actual = solution.sort_inventory(inventory, priority)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
