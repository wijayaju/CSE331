import unittest
from solution import find_unsorted_subarray


class TestFindUnsortedSubarray(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test_already_sorted(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 3, 4]), [-1, -1])

    def test_single_element(self):
        self.assertEqual(find_unsorted_subarray([1]), [-1, -1])

    def test_unsorted_middle(self):
        self.assertEqual(find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]), [1, 5])


# Running the tests
if __name__ == '__main__':
    unittest.main()
