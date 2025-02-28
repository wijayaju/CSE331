
import unittest
from solution import non_constructible_change


class TestNonConstructibleChange(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(non_constructible_change([1, 2, 5, 10]), 4)

    def test_empty_array(self):
        self.assertEqual(non_constructible_change([]), 1)

    def test_one_coin(self):
        self.assertEqual(non_constructible_change([5]), 1)

    def test_no_gaps(self):
        self.assertEqual(non_constructible_change([1, 1, 1, 1]), 5)

    def test_large_numbers(self):
        self.assertEqual(non_constructible_change([20, 1, 3, 5, 100]), 2)

    def test_unsorted_array(self):
        self.assertEqual(non_constructible_change([5, 7, 1, 1, 2, 3, 22]), 20)

    def test_all_same_coins(self):
        self.assertEqual(non_constructible_change([2, 2, 2, 2]), 1)


# Running the tests
if __name__ == '__main__':
    unittest.main()
