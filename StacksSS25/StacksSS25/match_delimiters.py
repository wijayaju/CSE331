
from array_stack import ArrayStack
import unittest


def is_matched(expr):
    """
    Return True if all delimiters are properly matched;
    False otherwise.
    """
    left = '({['  # opening delimiters
    right = ')}]'  # respective closing delimiters

    S = ArrayStack()
    for c in expr:
        if c in left:
            S.push(c)  # push left delimiter on stack
        elif c in right:
            if S.is_empty():
                return False  # nothing to match with
            if right.index(c) != left.index(S.pop()):
                return False  # mismatched
    return S.is_empty()  # were all symbols matched?


class TestIsMatched(unittest.TestCase):

    def test_balanced_expressions(self):
        self.assertTrue(is_matched("[(3*5)+10]/2"))
        self.assertTrue(is_matched("[(5+x)-(y+z)]"))
        self.assertTrue(is_matched("()(()){([()])}"))

    def test_unbalanced_expressions(self):
        self.assertFalse(is_matched("[(3*5)+{10]/2"))
        self.assertFalse(is_matched(")(()){([()])}"))
        self.assertFalse(is_matched("({[])}"))
        self.assertFalse(is_matched("( { [5*3 ] +2) -1}"))

    def test_empty_expression(self):
        self.assertTrue(is_matched(""))  # Empty expression should be balanced

    def test_single_delimiter(self):
        self.assertFalse(is_matched("("))  # Single open delimiter should be unbalanced
        self.assertFalse(is_matched(")"))  # Single close delimiter should be unbalanced

    def test_no_delimiters(self):
        self.assertTrue(is_matched("3 + 5 - 2"))  # No delimiters, should be considered balanced


if __name__ == '__main__':
    unittest.main()
