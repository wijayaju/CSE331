from array_stack import ArrayStack, Empty

import unittest

class TestArrayStack(unittest.TestCase):

    def test_push_different_data_types(self):
        stack = ArrayStack()
        stack.push(5)
        stack.push("hello")
        stack.push([1, 2, 3])
        stack.push({'key': 'value'})
        self.assertEqual(len(stack), 4)
        self.assertEqual(stack.top(), {'key': 'value'})

    def test_push_large_number_of_elements(self):
        stack = ArrayStack()
        for i in range(10000):
            stack.push(i)
        self.assertEqual(len(stack), 10000)
        self.assertEqual(stack.top(), 9999)
        for i in range(10000):
            self.assertEqual(stack.pop(), 9999 - i)
        self.assertTrue(stack.is_empty())

    def test_stack_initialization(self):
        stack = ArrayStack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)

    def test_push(self):
        stack = ArrayStack()
        stack.push(5)
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 1)
        stack.push(10)
        self.assertEqual(len(stack), 2)

    def test_top(self):
        stack = ArrayStack()
        with self.assertRaises(Empty):
            stack.top()
        stack.push(5)
        self.assertEqual(stack.top(), 5)
        stack.push(10)
        self.assertEqual(stack.top(), 10)  # Should now be 10

    def test_pop(self):
        stack = ArrayStack()
        with self.assertRaises(Empty):
            stack.pop()
        stack.push(5)
        stack.push(10)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.pop(), 5)
        self.assertTrue(stack.is_empty())

    def test_len(self):
        stack = ArrayStack()
        self.assertEqual(len(stack), 0)
        stack.push(5)
        stack.push(10)
        self.assertEqual(len(stack), 2)
        stack.pop()
        self.assertEqual(len(stack), 1)
        stack.pop()
        self.assertEqual(len(stack), 0)

    def test_is_empty(self):
        stack = ArrayStack()
        self.assertTrue(stack.is_empty())
        stack.push(5)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_something(self):
        stack = []
        for i in range(10 ** 6):
            stack.append(i)

        for i in range(10 ** 6):
            stack.pop()


# Necessary if running the test file directly
if __name__ == '__main__':
    unittest.main()
