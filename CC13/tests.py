import unittest
from solution import number_of_ways_to_get_to_end, number_of_ways_to_get_to_end_permutation


class CC13(unittest.TestCase):
    def test_number_of_ways_traverse(self):
        width = 4
        height = 3
        expected = 10
        actual = number_of_ways_to_get_to_end(width, height)
        self.assertEqual(actual, expected)

    def test_number_of_ways_traverse_permutations(self):
        width = 4
        height = 3
        expected = 10
        actual = number_of_ways_to_get_to_end_permutation(width, height)
        self.assertEqual(actual, expected)


    def test_square_grid(self):
        self.assertEqual(number_of_ways_to_get_to_end(3, 3), 6)

    def test_one_direction_only(self):
        self.assertEqual(number_of_ways_to_get_to_end(1, 5), 1)
        self.assertEqual(number_of_ways_to_get_to_end(5, 1), 1)

    def test_small_grid(self):
        self.assertEqual(number_of_ways_to_get_to_end(2, 2), 2)


if __name__ == '__main__':
    unittest.main()
