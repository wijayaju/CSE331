from typing import List
import unittest


def number_of_ways_to_make_change(n, denoms):
    """
    Calculates the number of distinct ways to make change for a given amount using
    unlimited coins from a list of denominations. The order of coins does not matter.

    Parameters:
    -----------
    n : int
        The target amount of money to make change for.

    denoms : List[int]
        A list of coin denominations (distinct positive integers).

    Returns:
    --------
    int
        The number of ways to make change for the target amount.

    Time Complexity: O(n * d)
    Space Complexity: O(n)
    """
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1  # One way to make 0: use no coins

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]


class TestNumberOfWaysToMakeChange(unittest.TestCase):
    def test_basic_example(self):
        self.assertEqual(number_of_ways_to_make_change(6, [1, 5]), 2)  # (1x6), (1+5)

    def test_repeat_small_denom(self):
        self.assertEqual(number_of_ways_to_make_change(4, [1, 2]), 3)

    def test_zero_amount(self):
        self.assertEqual(number_of_ways_to_make_change(0, [1, 2, 3]), 1)  # Only one way: use no coins

    def test_no_denominations(self):
        self.assertEqual(number_of_ways_to_make_change(10, []), 0)

    def test_large_denom_only(self):
        self.assertEqual(number_of_ways_to_make_change(3, [5, 10]), 0)  # Can't make 3 with larger coins


if __name__ == "__main__":
    unittest.main()
