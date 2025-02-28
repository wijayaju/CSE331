import unittest

from solution import CC0


class TestFindPairSumFunction(unittest.TestCase):

    def test_case_1(self):
        subject = CC0()
        numbers = [2, 7, 4, 9, 0, 1]
        target_sum = 0
        expected = set([])
        actual = set(subject.pairwise_sum(numbers, target_sum))
        self.assertEqual(actual, expected)

    def test_case_2(self):
        subject = CC0()
        numbers = [3, 5, -4, 8, 11, 1, -1, 6]
        target_sum = 10
        expected = set([11, -1])
        actual = set(subject.pairwise_sum(numbers, target_sum))
        self.assertEqual(actual, expected)

    def test_case_3(self):
        subject = CC0()
        numbers = [3, 5]
        target_sum = 8
        expected = set([3, 5])
        actual = set(subject.pairwise_sum(numbers, target_sum))
        self.assertEqual(actual, expected)

    def test_case_4(self):
        subject = CC0()
        numbers = [4, 6, 1, -3]
        target_sum = 3
        expected = set([-3, 6])
        actual = set(subject.pairwise_sum(numbers, target_sum))
        self.assertEqual(actual, expected)

    def test_case_5(self):
        subject = CC0()
        numbers = [14]
        target_sum = 14
        expected = set([])
        actual = set(subject.pairwise_sum(numbers, target_sum))
        self.assertEqual(actual, expected)

    def test_case_6(self):
        subject = CC0()
        numbers = [4, 6, 1]
        target_sum = 5
        expected = set([4, 1])
        actual = set(subject.pairwise_sum(numbers, target_sum))
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
