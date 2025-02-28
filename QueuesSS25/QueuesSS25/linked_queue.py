class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


import unittest


class TestLinkedQueue(unittest.TestCase):

    def setUp(self):
        """Set up an empty queue for testing."""
        self.queue = LinkedQueue()

    def test_is_empty_on_init(self):
        """Test if the queue is empty on initialization."""
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(len(self.queue), 0)

    def test_enqueue(self):
        """Test enqueue operation."""
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.first(), 10)

        self.queue.enqueue(20)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.first(), 10)  # First element should still be 10

    def test_dequeue(self):
        """Test dequeue operation."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)

        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.first(), 20)  # First should now be 20

        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.first(), 30)

        self.assertEqual(self.queue.dequeue(), 30)
        self.assertTrue(self.queue.is_empty())

    def test_first(self):
        """Test accessing the first element."""
        self.queue.enqueue(100)
        self.assertEqual(self.queue.first(), 100)
        self.queue.enqueue(200)
        self.assertEqual(self.queue.first(), 100)  # First element should still be 100

    def test_dequeue_empty_exception(self):
        """Test dequeueing from an empty queue raises Empty exception."""
        with self.assertRaises(Empty):
            self.queue.dequeue()

    def test_first_empty_exception(self):
        """Test accessing the first element of an empty queue raises Empty exception."""
        with self.assertRaises(Empty):
            self.queue.first()


if __name__ == '__main__':
    unittest.main()
