class ArrayQueue:
    DEFAULT_CAPACITY = 5  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')

        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Attempting to remove from an empty queue! ')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned





class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


import unittest


class TestArrayQueue(unittest.TestCase):
    def test_queue_initialization(self):
        queue = ArrayQueue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)

    def test_enqueue_and_length(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        self.assertEqual(len(queue), 1)
        queue.enqueue(2)
        self.assertEqual(len(queue), 2)

    def test_first(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        self.assertEqual(queue.first(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.first(), 1)  # Still the first element

    def test_dequeue(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertTrue(queue.is_empty())

    def test_empty_dequeue(self):
        queue = ArrayQueue()
        with self.assertRaises(Empty):
            queue.dequeue()

    def test_empty_first(self):
        queue = ArrayQueue()
        with self.assertRaises(Empty):
            queue.first()

    def test_resize_and_wrap_around(self):
        queue = ArrayQueue()
        for i in range(1, 7):  # Exceed the default capacity to trigger resize
            queue.enqueue(i)
        self.assertEqual(len(queue), 6)
        self.assertEqual(queue.dequeue(), 1)  # Check FIFO after resizing
        self.assertEqual(queue.dequeue(), 2)
        queue.enqueue(7)
        queue.enqueue(8)  # These operations should work correctly with wrap-around
        self.assertEqual(len(queue), 6)
        self.assertEqual(queue.first(), 3)


# Necessary if running the test file directly
if __name__ == '__main__':
    unittest.main()
