import unittest
from solution import MinHeap


class MyTestCase(unittest.TestCase):
    def test_top_minheap(self):
        # (1) Zero Element Heap
        heap = MinHeap()
        self.assertEqual(None, heap.top())  # (1)

        # (2) One Element Heap
        heap.data = [4]
        self.assertEqual(4, heap.top())  # (2)

        # (3) Three Element Heap
        heap.data = [1, 4, 7]
        self.assertEqual(1, heap.top())  # (3)

        # (4) Many Element Heap
        heap.data = [2, 3, 4, 5]
        self.assertEqual(2, heap.top())  # (4)

        # (5) Many Element Heap (Out of Order)
        heap.data = [0, 3, 4, 8, 5, 6, 9]
        self.assertEqual(0, heap.top())  # (5)

    def test_add(self):
        heap = MinHeap()
        heap.add(1)
        heap.add(2)
        heap.add(3)
        heap.add(5)
        heap.add(7)
        heap.add(9)

        self.assertEqual(6, len(heap.data))  # (1) Length of heap is 6
        self.assertEqual({1, 2, 3, 5, 7, 9}, set(heap.data))  # (1) Heap has correct elements
        self.assertEqual(heap.data[0], min(heap.data[:6]))  # (1) Top of the heap is the minimum element
        self.assertLess(heap.data[1], heap.data[3])  # (1) Ensure less than children
        self.assertLess(heap.data[1], heap.data[4])  # (1) Ensure less than children
        self.assertLess(heap.data[2], heap.data[5])  # (1) Node at index 2 is less than Node at index 5

        # (2) Simple Case (Percolate)
        heap = MinHeap()
        heap.add(5)
        heap.add(4)
        heap.add(3)
        self.assertEqual(3, len(heap.data))  # (2) Length of heap is 3
        self.assertEqual({3, 4, 5}, set(heap.data))  # (2) Heap has correct elements
        self.assertEqual(heap.data[0], min(heap.data[:3]))  # (2) Top of the heap is the minimum element
        self.assertEqual(3, heap.data[0])  # (2) Top of the heap is the minimum element

    def test_remove(self):
        heap = MinHeap()
        heap.remove()  # Test popping from empty heap doesn't crash

        heap.data = [5]
        self.assertEqual(5, heap.remove())  # (1)
        self.assertEqual(0, len(heap))  # (1)
        self.assertEqual([], heap.data)  # (1)

        heap = MinHeap()
        heap.data = [3, 5, 4]
        self.assertEqual(3, heap.remove())  # (2)
        self.assertEqual(2, len(heap))  # (2)
        self.assertEqual([4, 5], heap.data)  # (2)

        heap = MinHeap()
        heap.data = [3, 4, 5]
        self.assertEqual(3, heap.remove())  # (3)
        self.assertEqual(2, len(heap))  # (3)
        self.assertEqual([4, 5], heap.data)  # (3)

    def test_build_heap_and_is_min_heap(self):
        minHeap = MinHeap()
        minHeap.data = [51, 22, 45, 30, 20, 33, 14, 13]
        self.assertFalse(minHeap.is_min_heap())
        minHeap.build_heap()
        self.assertTrue(minHeap.is_min_heap())

        minHeap = MinHeap()
        minHeap.data = [3, 4, 5]
        minHeap.build_heap()
        self.assertTrue(minHeap.is_min_heap())

        minHeap = MinHeap()
        minHeap.data = [49, 62, 88, 73, 20, 94, 68]
        self.assertFalse(minHeap.is_min_heap())
        minHeap.build_heap()
        self.assertTrue(minHeap.is_min_heap())


if __name__ == '__main__':
    unittest.main()
# Unit tests
