import solution
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # Original test case: A list with multi-digit numbers in random order.
        input = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
        expected = [2, 12, 65, 87, 234, 345, 654, 3008, 8762]
        actual = solution.radix_sort(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        # Test case 2: A small list with single-digit numbers in random order.
        input = [5, 3, 8, 6, 2, 7, 4, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        actual = solution.radix_sort(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        # Test case 3: A mix of numbers with varying digits, including zero.
        input = [100, 20, 3000, 5, 50, 500, 0]
        expected = [0, 5, 20, 50, 100, 500, 3000]
        actual = solution.radix_sort(input)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        # Test case 4: A reverse-ordered list of single-digit numbers for edge case validation.
        input = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = solution.radix_sort(input)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
