class ArrayQueue:
    DEFAULT_CAPACITY = 4  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self.front_index = 0

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

        return self._data[self.front_index]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Attempting to remove from an empty queue! ')
        answer = self._data[self.front_index]
        self._data[self.front_index] = None  # help garbage collection
        self.front_index = (self.front_index + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self.front_index + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self.front_index
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self.front_index = 0  # front has been realigned


if __name__ == '__main__':
    myQueue = ArrayQueue()  # contents: [ ]
    myQueue.enqueue(120)
    myQueue.enqueue(150)
    myQueue.enqueue(275)
    myQueue.enqueue(331)
    myQueue.enqueue(111)
    myQueue.enqueue(102)
    print("front_index after series of enqueue/dequeue operation is :", myQueue.front_index)
    if myQueue.first() < 221:
        myQueue.enqueue(468)
    else:
        myQueue.enqueue(978)
        myQueue.enqueue(1000)
    myQueue.enqueue(129)
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    print()
    print()
    print("front_index after series of enqueue/dequeue operation is :", myQueue.front_index)

    # example similar to practice exam:
    myQueue = ArrayQueue()  # contents: [ ]
    myQueue.enqueue(33)
    myQueue.enqueue(222)
    myQueue.enqueue(544)
    myQueue.enqueue(133)
    myQueue.enqueue(122)
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.enqueue(100)
    myQueue.enqueue(101)
    print()
    print()
    print("front_index after series of enqueue/dequeue operation is :", myQueue.front_index)


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass
