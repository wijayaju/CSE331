import unittest
from solution import balanced_brackets


class TestBalancedBrackets(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balanced_brackets("([])(){}(())()()"), True)

    def test_case_2(self):
        self.assertEqual(balanced_brackets("([)]"), False)

    def test_case_3(self):
        self.assertEqual(balanced_brackets("(({{[[[]]]}}))"), True)

    def test_case_4(self):
        self.assertEqual(balanced_brackets("({[})"), False)


if __name__ == "__main__":
    unittest.main()
