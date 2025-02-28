from linked_queue import LinkedQueue


def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return  # list is already sorted
    # divide
    p = S.first()  # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():  # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:  # S.first() must equal pivot
            E.enqueue(S.dequeue())
    # conquer (with recursion)
    quick_sort(L)  # sort elements less than p
    quick_sort(G)  # sort elements greater than p
    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


import unittest


class TestQuickSortLinkedQueue(unittest.TestCase):

    def queue_to_list(self, queue):
        """Convert queue to list for easier comparison."""
        result = []
        while not queue.is_empty():
            result.append(queue.dequeue())
        return result

    def test_sort_unsorted(self):
        """Test sorting an unsorted queue."""
        lq = LinkedQueue()
        lq.enqueue(6)
        lq.enqueue(3)
        lq.enqueue(1)
        lq.enqueue(4)
        lq.enqueue(2)
        quick_sort(lq)
        self.assertEqual(self.queue_to_list(lq), [1, 2, 3, 4, 6])

    def test_sort_duplicates(self):
        """Test sorting a queue with duplicate elements."""
        lq = LinkedQueue()
        lq.enqueue(4)
        lq.enqueue(2)
        lq.enqueue(2)
        lq.enqueue(3)
        quick_sort(lq)
        self.assertEqual(self.queue_to_list(lq), [2, 2, 3, 4])

    def test_sort_sorted(self):
        """Test sorting an already sorted queue."""
        lq = LinkedQueue()
        lq.enqueue(1)
        lq.enqueue(2)
        lq.enqueue(3)
        lq.enqueue(4)
        quick_sort(lq)
        self.assertEqual(self.queue_to_list(lq), [1, 2, 3, 4])

    def test_sort_reverse(self):
        """Test sorting a reverse sorted queue."""
        lq = LinkedQueue()
        lq.enqueue(5)
        lq.enqueue(4)
        lq.enqueue(3)
        lq.enqueue(2)
        lq.enqueue(1)
        quick_sort(lq)
        self.assertEqual(self.queue_to_list(lq), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        """Test sorting a single element queue."""
        lq = LinkedQueue()
        lq.enqueue(1)
        quick_sort(lq)
        self.assertEqual(self.queue_to_list(lq), [1])

    def test_sort_empty(self):
        """Test sorting an empty queue."""
        lq = LinkedQueue()
        quick_sort(lq)
        self.assertEqual(self.queue_to_list(lq), [])


if __name__ == '__main__':
    unittest.main()
