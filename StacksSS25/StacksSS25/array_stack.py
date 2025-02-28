from exceptions import Empty
import unittest


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def __str__(self):
        """Return a string representation of the stack."""
        return f"Stack({self._data})"

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    """push(e):Add element e to the top of the stack."""

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)  # new item stored at end of list

    def top(self):
        """return the item at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        """pop():Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()  # remove last item from list


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


# Necessary if running the test file directly
if __name__ == '__main__':
    # unittest.main()

    my_stack = ArrayStack()  # Initial contents: [ ]
    my_stack.push(441)
    my_stack.push(756)
    my_stack.pop()
    my_stack.push(800)
    print("Top of the stack is ", my_stack.top())
    if my_stack.top() == 800:
        my_stack.push(331)

    my_stack.push(1700)
    my_stack.pop()
    my_stack.push(600)
    my_stack.pop()
    my_stack.push(1110)  # then test it with 111
    print("Top of the stack is ", my_stack.top())
    while not my_stack.is_empty() and my_stack.top() < 1000:
        my_stack.pop()

    my_stack.push(1000)
    print("Current stack is: ", my_stack)
