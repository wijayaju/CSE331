"""
Project 2 - Hybrid Sorting - Tests
CSE 331 Spring 2025
"""

from collections.abc import MutableSequence
from collections import defaultdict
from datetime import date, timedelta
from random import randrange, random, seed, shuffle
import unittest

from solution import selection_sort, bubble_sort, insertion_sort, hybrid_merge_sort, get_relevant_songs, Song

seed(331)


# Custom comparator used in all comprehensive testcases
def sum_digits(n: int):
    """Computes the sum of all digits in a number"""
    return sum(int(digit) for digit in str(n))


# Custom comparator used in all comprehensive testcases
def comp_sum_digits(x: int, y: int):
    """Compares two numbers by the sum of their digits"""
    return sum_digits(x) < sum_digits(y)


class Project2Tests(unittest.TestCase):

    def test_selection_sort_basic(self):
        # (1) test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        selection_sort(data)
        self.assertEqual(expected, data)

        # (2) test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        selection_sort(data)
        self.assertEqual(expected, data)

        # (3) test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        selection_sort(data)
        self.assertEqual(expected, data)

        # (4) test empty
        data = []
        selection_sort(data)
        self.assertEqual([], data)

        # (5) check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(selection_sort(data))

    def test_selection_sort_comparator(self):
        # (1) sort powers of ten by number of digits, in reverse
        data = [10 ** i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: -1 * len(str(x)))
        selection_sort(data, comparator=lambda x, y: len(str(x)) > len(str(y)))
        self.assertEqual(expected, data)

        # (2) sort strings by length
        data = ['a' * i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(x))
        selection_sort(data, comparator=lambda x, y: len(x) < len(y))
        self.assertEqual(expected, data)

    def test_selection_sort_descending(self):
        # (1) sort powers of ten by number of digits, in reverse
        data = [10 ** i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(str(x)), reverse=True)
        selection_sort(data, comparator=lambda x, y: len(str(x)) < len(str(y)), descending=True)
        self.assertEqual(expected, data)

        # (2) sort strings by length
        data = ['a' * i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(x), reverse=True)
        selection_sort(data, comparator=lambda x, y: len(x) < len(y), descending=True)
        self.assertEqual(expected, data)

    def test_selection_sort_comprehensive(self):
        # (1) sort a lot of integers
        data = list(range(1500))
        shuffle(data)
        expected = sorted(data)
        selection_sort(data)
        self.assertEqual(expected, data)

        # (2) sort a lot of integers with alternative comparator
        # this comparator compares values as follows:
        #   x < y
        #   if and only if
        #   sum(digits(x)) < sum(digits(y))
        # ex: 12 < 15 since 1 + 2 = 3 < 6 = 1 + 5
        data = list(range(1500))
        expected_data = sorted(data, key=sum_digits)
        selection_sort(data, comparator=comp_sum_digits)
        # there are multiple possible orderings, thus we must compare via sums of digits
        for expected, actual in zip(expected_data, data):
            expected_sum = sum_digits(expected)
            actual_sum = sum_digits(actual)
            self.assertEqual(expected_sum, actual_sum)

    def test_bubble_sort_basic(self):
        # (1) test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        bubble_sort(data)
        self.assertEqual(expected, data)

        # (2) test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        bubble_sort(data)
        self.assertEqual(expected, data)

        # (3) test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        bubble_sort(data)
        self.assertEqual(expected, data)

        # (4) test empty
        data = []
        bubble_sort(data)
        self.assertEqual([], data)

        # (5) check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(bubble_sort(data))

    def test_bubble_sort_comparator(self):
        # (1) sort powers of ten by number of digits, in reverse
        data = [10 ** i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: -1 * len(str(x)))
        bubble_sort(data, comparator=lambda x, y: len(str(x)) > len(str(y)))
        self.assertEqual(expected, data)

        # (2) sort strings by length
        data = ['a' * i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(x))
        bubble_sort(data, comparator=lambda x, y: len(x) < len(y))
        self.assertEqual(expected, data)

    def test_bubble_sort_descending(self):
        # (1) sort powers of ten by number of digits, in reverse
        data = [10 ** i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(str(x)), reverse=True)
        bubble_sort(data, comparator=lambda x, y: len(str(x)) < len(str(y)), descending=True)
        self.assertEqual(expected, data)

        # (2) sort strings by length
        data = ['a' * i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(x), reverse=True)
        bubble_sort(data, comparator=lambda x, y: len(x) < len(y), descending=True)
        self.assertEqual(expected, data)

    def test_bubble_sort_comprehensive(self):
        # (1) sort a lot of integers
        # Smaller than the other comprehensive tests; bubble sort is slow!
        data = list(range(500))
        shuffle(data)
        expected = sorted(data)
        bubble_sort(data)
        self.assertEqual(expected, data)

        # (2) sort a lot of integers with alternative comparator
        # this comparator compares values as follows:
        #   x < y
        #   if and only if
        #   sum(digits(x)) < sum(digits(y))
        # ex: 12 < 15 since 1 + 2 = 3 < 6 = 1 + 5
        data = list(range(500))
        expected_data = sorted(data, key=sum_digits)
        bubble_sort(data, comparator=comp_sum_digits)
        # there are multiple possible orderings, thus we must compare via sums of digits
        for expected, actual in zip(expected_data, data):
            expected_sum = sum_digits(expected)
            actual_sum = sum_digits(actual)
            self.assertEqual(expected_sum, actual_sum)

    def test_insertion_sort_basic(self):
        # (1) test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # (2) test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # (3) test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # (4) test empty
        data = []
        insertion_sort(data)
        self.assertEqual([], data)

        # (5) check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(insertion_sort(data))

    def test_insertion_sort_comparator(self):
        # (1) sort powers of ten by number of digits, in reverse
        data = [10 ** i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: -1 * len(str(x)))
        insertion_sort(data, comparator=lambda x, y: len(str(x)) > len(str(y)))
        self.assertEqual(expected, data)

        # (2) sort strings by length
        data = ['a' * i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(x))
        insertion_sort(data, comparator=lambda x, y: len(x) < len(y))
        self.assertEqual(expected, data)

    def test_insertion_sort_descending(self):
        # (1) sort powers of ten by number of digits, in reverse
        data = [10 ** i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(str(x)), reverse=True)
        insertion_sort(data, comparator=lambda x, y: len(str(x)) < len(str(y)), descending=True)
        self.assertEqual(expected, data)

        # (2) sort strings by length
        data = ['a' * i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(x), reverse=True)
        insertion_sort(data, comparator=lambda x, y: len(x) < len(y), descending=True)
        self.assertEqual(expected, data)

    def test_insertion_sort_comprehensive(self):
        # (1) sort a lot of integers
        data = list(range(1500))
        shuffle(data)
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # (2) sort a lot of integers with alternative comparator
        # this comparator compares values as follows:
        #   x < y
        #   if and only if
        #   sum(digits(x)) < sum(digits(y))
        # ex: 12 < 15 since 1 + 2 = 3 < 6 = 1 + 5
        data = list(range(1500))
        expected_data = sorted(data, key=sum_digits)
        insertion_sort(data, comparator=comp_sum_digits)
        # there are multiple possible orderings, thus we must compare via sums of digits
        for expected, actual in zip(expected_data, data):
            expected_sum = sum_digits(expected)
            actual_sum = sum_digits(actual)
            self.assertEqual(expected_sum, actual_sum)

    def test_hybrid_merge_sort_basic(self):
        # (1) test with basic list of integers - default comparator and threshold
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        hybrid_merge_sort(data)
        self.assertEqual(expected, data)

        # (2) test with basic set of strings - default comparator and threshold
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        hybrid_merge_sort(data)
        self.assertEqual(expected, data)

        # (3) test with already sorted data - default comparator and threshold
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        hybrid_merge_sort(data)
        self.assertEqual(expected, data)

        # (4) test empty - default comparator and threshold
        data = []
        hybrid_merge_sort(data)
        self.assertEqual([], data)

        # (5) check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(hybrid_merge_sort(data, threshold=0))

    def test_hybrid_merge_sort_threshold(self):
        # first, all the tests from basic should work with higher thresholds

        # (1) test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        hybrid_merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        # (2) test with basic set of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        hybrid_merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        # (3) test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        hybrid_merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        # (4) now, for a longer test - a bunch of thresholds
        data = list(range(25))
        expected = sorted(data)
        for t in range(11):
            shuffle(data)
            hybrid_merge_sort(data, threshold=t)
            self.assertEqual(expected, data)

    def test_hybrid_merge_sort_comparator(self):
        # (1) sort powers of ten by number of digits, in reverse
        data = [10 ** i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: -1 * len(str(x)))
        hybrid_merge_sort(data, comparator=lambda x, y: len(str(x)) > len(str(y)))
        self.assertEqual(expected, data)

        # (2) sort strings by length
        data = ['a' * i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key=lambda x: len(x))
        hybrid_merge_sort(data, comparator=lambda x, y: len(x) < len(y))
        self.assertEqual(expected, data)

    def test_hybrid_merge_sort_descending(self):
        # (1) test with basic list of integers - default comparator, threshold of zero
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data, reverse=True)
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual(expected, data)

        # (2) test with basic list of strings - default comparator, threshold
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data, reverse=True)
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual(expected, data)

        # (3) test with already sorted data - default comparator, threshold
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data, reverse=True)
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual(expected, data)

        # (4) test empty
        data = []
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual([], data)

        # (5) check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(hybrid_merge_sort(data, threshold=0, descending=True))

        # (6) now let's test with multiple thresholds
        data = list(range(50))
        expected = sorted(data, reverse=True)
        for t in range(20):
            shuffle(data)
            hybrid_merge_sort(data, threshold=t, descending=True)
            self.assertEqual(expected, data)

    def test_hybrid_merge_sort_comprehensive(self):
        # (1) sort a lot of integers, with a lot of thresholds
        data = list(range(500))
        for t in range(100):
            shuffle(data)
            expected = sorted(data)
            hybrid_merge_sort(data, threshold=t)
            self.assertEqual(expected, data)

        # (2) sort a lot of integers with alternative comparator, threshold of 8
        # this comparator compares values as follows:
        #   x < y
        #   if and only if
        #   sum(digits(x)) < sum(digits(y))
        # ex: 12 < 15 since 1 + 2 = 3 < 6 = 1 + 5
        data = list(range(1500))
        expected_data = sorted(data, key=sum_digits)
        hybrid_merge_sort(data, threshold=8, comparator=comp_sum_digits)
        # there are multiple possible orderings, thus we must compare via sums of digits
        for expected, actual in zip(expected_data, data):
            expected_sum = sum_digits(expected)
            actual_sum = sum_digits(actual)
            self.assertEqual(expected_sum, actual_sum)

        # (3) sort a lot of integers with same comparator as above, thresholds in [1, ..., 49]
        # this comparator compares values as follows:
        #   x < y
        #   if and only if
        #   sum(digits(x)) < sum(digits(y))
        # ex: 12 < 15 since 1 + 2 = 3 < 6 = 1 + 5
        data = list(range(1000))
        expected_data = sorted(data, key=sum_digits)
        for t in range(50):
            shuffle(data)
            hybrid_merge_sort(data, threshold=t, comparator=comp_sum_digits)
            for expected, actual in zip(expected_data, data):
                expected_sum = sum_digits(expected)
                actual_sum = sum_digits(actual)
                self.assertEqual(expected_sum, actual_sum)

    def test_hybrid_merge_sort_speed(self):
        # *********************************************************
        # ***WORTH NO POINTS, FOR PERSONAL TESTING PURPOSES ONLY***
        # *********************************************************
        # the point of this sort is to be fast, right?
        # this (probably) won't finish if you're not careful with time complexity,
        # but it isn't guaranteed
        data = list(range(300000))
        expected = data[:]
        shuffle(data)
        hybrid_merge_sort(data)
        self.assertEqual(expected, data)

    def test_hybrid_merge_actually_hybrid(self):
        # *********************************************************
        # ***WORTH NO POINTS, FOR PERSONAL TESTING PURPOSES ONLY***
        # *********************************************************
        # this test is to make sure that the hybrid merge sort is actually
        # hybrid by calling insertion sort when appropriate

        calling_functions = defaultdict(set)

        class MyList(MutableSequence):
            # This class was taken from
            # https://stackoverflow.com/questions/6560354/how-would-i-create-a-custom-list-class-in-python
            def __init__(self, data=None):
                super(MyList, self).__init__()
                self._list = list(data)

            def __delitem__(self, ii):
                """Delete an item"""
                del self._list[ii]

            def __setitem__(self, ii, val):
                self._list[ii] = val

            def insert(self, ii, val):
                self._list.insert(ii, val)

            def __len__(self):
                """List length"""
                return len(self._list)

            def __getitem__(self, ii):
                import inspect
                calling_functions[inspect.stack()[1].function].add(len(self))
                if isinstance(ii, slice):
                    return self.__class__(self._list[ii])
                else:
                    return self._list[ii]

        data = MyList(range(50))
        hybrid_merge_sort(data, threshold=2)
        self.assertIn('insertion_sort', calling_functions)
        self.assertIn('hybrid_merge_sort', calling_functions)
        self.assertTrue(all(length <= 2 for length in calling_functions['insertion_sort']))
        self.assertAlmostEqual(len(calling_functions['hybrid_merge_sort']), 10, delta=2)

    def test_relevant_songs(self):
        # (1) Empty songs list.
        products = []
        expected = []
        actual = get_relevant_songs(products, ["pop"], "newest")
        self.assertEqual(expected, actual)
        actual = get_relevant_songs(products, ["rock"], "oldest")
        self.assertEqual(expected, actual)

        # (2) Less than 10 items
        # newest
        songs = [
            Song(0.1, 0.3, 0.4, 0.99, date(2000, 4, 19)),
            Song(0.6, 0.21, 0.53, 0.64, date(2005, 8, 15)),
            Song(0.2, 0.45, 0.32, 0.87, date(2010, 3, 10)),
            Song(0.78, 0.12, 0.56, 0.43, date(2015, 11, 25)),
            Song(0.33, 0.77, 0.89, 0.15, date(2020, 7, 5)),
            Song(0.51, 0.61, 0.41, 0.92, date(2023, 2, 14)),
            Song(0.29, 0.58, 0.74, 0.68, date(2024, 12, 19))
        ]
        expected = [
            Song(0.29, 0.58, 0.74, 0.68, date(2024, 12, 19)),
            Song(0.51, 0.61, 0.41, 0.92, date(2023, 2, 14)),
            Song(0.33, 0.77, 0.89, 0.15, date(2020, 7, 5)),
            Song(0.78, 0.12, 0.56, 0.43, date(2015, 11, 25)),
            Song(0.2, 0.45, 0.32, 0.87, date(2010, 3, 10)),
            Song(0.6, 0.21, 0.53, 0.64, date(2005, 8, 15)),
            Song(0.1, 0.3, 0.4, 0.99, date(2000, 4, 19))
        ]
        actual = get_relevant_songs(songs, ["pop", "jazz", "rock"], "newest")
        self.assertEqual(expected, actual)

        # (3) oldest
        songs = [
            Song(0.35, 0.29, 0.47, 0.82, date(1999, 12, 15)),
            Song(0.61, 0.18, 0.59, 0.75, date(2003, 6, 30)),
            Song(0.42, 0.41, 0.34, 0.89, date(2007, 4, 10)),
            Song(0.57, 0.62, 0.73, 0.58, date(2012, 9, 25)),
            Song(0.49, 0.33, 0.66, 0.79, date(2016, 3, 14)),
            Song(0.71, 0.56, 0.44, 0.68, date(2019, 11, 8)),
            Song(0.28, 0.24, 0.51, 0.92, date(2021, 7, 21)),
            Song(0.64, 0.45, 0.38, 0.73, date(2024, 1, 3)),
            Song(0.37, 0.51, 0.42, 0.67, date(2025, 5, 15)),
            Song(0.53, 0.39, 0.49, 0.85, date(2027, 8, 19))
        ]
        expected = [
            Song(0.35, 0.29, 0.47, 0.82, date(1999, 12, 15)),
            Song(0.61, 0.18, 0.59, 0.75, date(2003, 6, 30)),
            Song(0.42, 0.41, 0.34, 0.89, date(2007, 4, 10)),
            Song(0.57, 0.62, 0.73, 0.58, date(2012, 9, 25)),
            Song(0.49, 0.33, 0.66, 0.79, date(2016, 3, 14)),
            Song(0.71, 0.56, 0.44, 0.68, date(2019, 11, 8)),
            Song(0.28, 0.24, 0.51, 0.92, date(2021, 7, 21)),
            Song(0.64, 0.45, 0.38, 0.73, date(2024, 1, 3)),
            Song(0.37, 0.51, 0.42, 0.67, date(2025, 5, 15)),
            Song(0.53, 0.39, 0.49, 0.85, date(2027, 8, 19))
        ]
        actual = get_relevant_songs(songs, ["rock", "jazz"], "oldest")
        self.assertEqual(expected, actual)

        # (4) two songs have the same rating and date
        # (4a) newest simple example (from specs)
        songs = [
            Song(0.56, 0.17, 0.95, 0.24, date(2003, 12, 17)),
            Song(0.93, 0.23, 0.52, 0.96, date(2024, 7, 5)),
            Song(0.93, 0.63, 0.755, 0.96, date(2024, 7, 5)),
            Song(0.27, 0.05, 0.12, 0.34, date(2019, 4, 21)),
        ]

        expected = [
            Song(0.93, 0.23, 0.52, 0.96, date(2024, 7, 5)),
            Song(0.93, 0.63, 0.755, 0.96, date(2024, 7, 5)),
            Song(0.27, 0.05, 0.12, 0.34, date(2019, 4, 21)),
            Song(0.56, 0.17, 0.95, 0.24, date(2003, 12, 17)),
        ]
        actual = get_relevant_songs(songs, ["jazz", "rock"], "newest")
        self.assertEqual(expected, actual)

        # (4b) newest
        songs = [
            Song(0.9, 0.37, 0.41, 0.88, date(2010, 5, 15)),
            Song(0.55, 0.37, 0.42, 0.88, date(2010, 5, 15)),
            Song(0.61, 0.22, 0.43, 0.81, date(2012, 8, 10)),
            Song(0.58, 0.29, 0.72, 0.73, date(2015, 3, 20)),
            Song(0.44, 0.35, 0.64, 0.76, date(2017, 6, 30)),
            Song(0.50, 0.42, 0.49, 0.72, date(2020, 2, 14)),
            Song(0.62, 0.25, 0.53, 0.85, date(2023, 9, 19)),
            Song(0.57, 0.38, 0.62, 0.78, date(2025, 11, 25))
        ]
        expected = [
            Song(0.57, 0.38, 0.62, 0.78, date(2025, 11, 25)),
            Song(0.62, 0.25, 0.53, 0.85, date(2023, 9, 19)),
            Song(0.50, 0.42, 0.49, 0.72, date(2020, 2, 14)),
            Song(0.44, 0.35, 0.64, 0.76, date(2017, 6, 30)),
            Song(0.58, 0.29, 0.72, 0.73, date(2015, 3, 20)),
            Song(0.61, 0.22, 0.43, 0.81, date(2012, 8, 10)),
            # These two remain in their original order because of stable sorting
            Song(0.9, 0.37, 0.41, 0.88, date(2010, 5, 15)),
            Song(0.55, 0.37, 0.42, 0.88, date(2010, 5, 15))
        ]
        actual = get_relevant_songs(songs, ["pop", "jazz"], "newest")
        self.assertEqual(expected, actual)

        # (4c) oldest
        songs = [
            Song(0.75, 0.20, 0.55, 0.90, date(2022, 1, 10)),
            Song(0.82, 0.35, 0.40, 0.75, date(2024, 5, 2)),
            Song(0.60, 0.50, 0.65, 0.80, date(2023, 11, 15)),
            Song(0.95, 0.42, 0.30, 0.68, date(2025, 3, 8)),
            Song(0.70, 0.28, 0.78, 0.92, date(2022, 8, 22)),
            Song(0.88, 0.55, 0.45, 0.72, date(2024, 12, 28)),
            Song(0.65, 0.32, 0.52, 0.85, date(2023, 6, 5))
        ]
        expected = [
            Song(0.75, 0.20, 0.55, 0.90, date(2022, 1, 10)),
            Song(0.70, 0.28, 0.78, 0.92, date(2022, 8, 22)),
            Song(0.65, 0.32, 0.52, 0.85, date(2023, 6, 5)),
            Song(0.60, 0.50, 0.65, 0.80, date(2023, 11, 15)),
            Song(0.82, 0.35, 0.40, 0.75, date(2024, 5, 2)),
            Song(0.88, 0.55, 0.45, 0.72, date(2024, 12, 28)),
            Song(0.95, 0.42, 0.30, 0.68, date(2025, 3, 8))
        ]
        actual = get_relevant_songs(songs, ["pop", "jazz"], "oldest")
        self.assertEqual(expected, actual)

        # (5) > 10 items
        songs = [
            Song(0.35, 0.29, 0.47, 0.82, date(1999, 12, 15)),
            Song(0.61, 0.18, 0.59, 0.75, date(2003, 6, 30)),
            Song(0.42, 0.41, 0.34, 0.89, date(2007, 4, 10)),
            Song(0.57, 0.62, 0.73, 0.58, date(2012, 9, 25)),
            Song(0.49, 0.33, 0.66, 0.79, date(2016, 3, 14)),
            Song(0.71, 0.56, 0.44, 0.68, date(2019, 11, 8)),
            Song(0.28, 0.24, 0.51, 0.92, date(2021, 7, 21)),
            Song(0.64, 0.45, 0.38, 0.73, date(2024, 1, 3)),
            Song(0.37, 0.51, 0.42, 0.67, date(2025, 5, 15)),
            Song(0.53, 0.39, 0.49, 0.85, date(2027, 8, 19)),
            Song(0.91, 0.22, 0.33, 0.70, date(2001, 4, 5)),  # Added
            Song(0.44, 0.66, 0.55, 0.81, date(2011, 10, 22))  # Added

        ]
        expected = [  # rock and jazz, oldest
            Song(0.35, 0.29, 0.47, 0.82, date(1999, 12, 15)),
            Song(0.91, 0.22, 0.33, 0.70, date(2001, 4, 5)),
            Song(0.61, 0.18, 0.59, 0.75, date(2003, 6, 30)),
            Song(0.42, 0.41, 0.34, 0.89, date(2007, 4, 10)),
            Song(0.44, 0.66, 0.55, 0.81, date(2011, 10, 22)),
            Song(0.49, 0.33, 0.66, 0.79, date(2016, 3, 14)),
            Song(0.71, 0.56, 0.44, 0.68, date(2019, 11, 8)),
            Song(0.28, 0.24, 0.51, 0.92, date(2021, 7, 21)),
            Song(0.64, 0.45, 0.38, 0.73, date(2024, 1, 3)),
            Song(0.53, 0.39, 0.49, 0.85, date(2027, 8, 19)),
        ]
        actual = get_relevant_songs(songs, ["rock", "jazz"], "oldest")
        self.assertEqual(expected, actual)

        # (6) > 10 items
        songs = [
            Song(0.54, 0.25, 0.47,0.52,date(2024,2,2)),
            Song(0.54,0.1,0.27,0.53,date(2024,2,2)),
            Song(0.24, 0.23, 0.65, 0.48, date(2025, 1, 5)),
            #Song(0.1, 0.68, 0.38, 0.58, date(2023, 4, 12)),
            Song(0.99, 0.68, 0.58, 0.26, date(2022, 12,6)),
            Song(0.3, 0.4, 0.5, 0.6, date(2023, 1, 1)),
            #Song(0.1, 0.2, 0.3, 0.4, date(2021, 5, 12)),
            Song(0.3,0.6,0.6,0.27, date(2023,1,1)),
            #Song(0.24, 0.21, 0.52, 0.48, date(2025, 1, 5)),
            Song(0.99, 0.24, 0.34, 0.42, date(2025,1,5)),
            Song(0.43, 0.47, 0.74, 0.21, date(1999, 7, 18)),
            Song(0.63, 0.56, 0.34, 0.52, date(1979, 3, 23)),
            Song(0.62, 0.24, 0.47, 0.23, date(2014, 4, 21))
        ]

        expected = [
            Song(0.99, 0.24, 0.34, 0.42, date(2025, 1, 5)),
            Song(0.24, 0.23, 0.65, 0.48, date(2025,1,5)),
            Song(0.54, 0.25, 0.47, 0.52, date(2024,2,2)),
            Song(0.54, 0.1, 0.27, 0.53, date(2024,2,2)),
            Song(0.3, 0.4, 0.5, 0.6, date(2023, 1, 1)),
            Song(0.3, 0.6, 0.6, 0.27, date(2023,1,1)),
            Song(0.99, 0.68, 0.58, 0.26, date(2022,12,6)),
            Song(0.62, 0.24, 0.47, 0.23, date(2014, 4, 21)),
            Song(0.43, 0.47, 0.74, 0.21, date(1999, 7, 18)),
            Song(0.63, 0.56, 0.34, 0.52, date(1979, 3, 23)),

        ]
        actual = get_relevant_songs(songs, ["rock"], "newest")
        self.assertEqual(expected, actual)


        # (7) random large test case of 1000 songs.
        num_songs = 1000
        songs = []
        start_date = date(1950, 1, 1)
        end_date = date(2024, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        for _ in range(num_songs):
            random_number_of_days = randrange(days_between_dates)
            random_date = start_date + timedelta(days=random_number_of_days)
            songs.append(Song(random(), random(), random(), random(), random_date))

        shuffle(songs)

        genres_newest = ["rock", "pop", "jazz", "rap"]
        expected_newest = sorted(sorted(songs, key=lambda x: tuple(reversed([getattr(x, g) for g in genres_newest])),reverse=True
                                 )[:10],key=lambda x: x.date_published, reverse=True)
        actual_newest = get_relevant_songs(songs, genres_newest, "newest")
        self.assertEqual(expected_newest, actual_newest)

        genres_oldest = ["rap", "jazz", "pop", "rock"]
        expected_oldest = sorted(sorted(songs, key=lambda x: tuple(reversed([getattr(x, g) for g in genres_oldest])),reverse=True
                                 )[:10],key=lambda x: x.date_published)
        actual_oldest = get_relevant_songs(songs, genres_oldest, "oldest")
        self.assertEqual(expected_oldest, actual_oldest)


if __name__ == '__main__':
    unittest.main()
