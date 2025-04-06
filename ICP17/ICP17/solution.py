from typing import TypeVar, List
import unittest

T = TypeVar('T')


class MinHeap:
    """
    A MinHeap class that maintains a min-heap property, where the smallest element
    is at the root. This heap is implemented using an array.
    """

    def __init__(self):
        """
        Initializes an empty MinHeap.
        """
        self.data = []

    def __len__(self) -> int:
        """
        Returns the number of elements in the heap.

        :return: The size of the heap.
        """
        return len(self.data)

    def _swap(self, i, j):
        """
        Swaps two elements in the heap at indices i and j.

        :param i: Index of the first element.
        :param j: Index of the second element.
        """
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def empty(self) -> bool:
        """
        Checks if the heap is empty.

        :return: True if the heap is empty, False otherwise.
        """
        return len(self) == 0

    def top(self) -> T:
        """
        Returns the smallest element in the heap without removing it.

        :return: The smallest element if the heap is not empty, None otherwise.
        """
        if not self.empty():
            return self.data[0]

    def left_child_index(self, index: int) -> int:
        """
        Returns the index of the left child of a node at a given index.

        :param index: Index of the parent node.
        :return: Index of the left child if it exists, None otherwise.
        """
        return 2 * index + 1 if 2 * index + 1 < len(self.data) else None

    def right_child_index(self, index: int) -> int:
        """
        Returns the index of the right child of a node at a given index.

        :param index: Index of the parent node.
        :return: Index of the right child if it exists, None otherwise.
        """
        return 2 * index + 2 if 2 * index + 2 < len(self.data) else None

    def parent_index(self, index: int) -> int:
        """
        Returns the index of the parent of a node at a given index.

        :param index: Index of the child node.
        :return: Index of the parent if it exists, None otherwise.
        """
        return (index - 1) // 2 if index > 0 else None

    def min_child_index(self, index: int) -> int:
        """
        Finds the index of the smaller child of a node at a given index.

        :param index: Index of the parent node.
        :return: Index of the minimum child if it exists, None otherwise.
        """
        left_i = self.left_child_index(index)
        right_i = self.right_child_index(index)
        if left_i is not None and (right_i is None or self.data[left_i] < self.data[right_i]):
            return left_i
        return right_i

    def percolate_up(self, index: int) -> None:
        """
        Moves a node up the heap to restore the min-heap property.

        :param index: Index of the node to percolate up.
        """
        self._swap(index, self.parent_index(index))

    def percolate_down(self, index: int) -> None:
        """
        Moves a node down the heap to restore the min-heap property.

        :param index: Index of the node to percolate down.
        """
        self._swap(index, self.min_child_index(index))

    def add(self, key: T) -> None:
        """
        Adds a new element to the heap, restoring the min-heap property if necessary.

        :param key: The value to add to the heap.
        """
        self.data.append(key)
        index = len(self.data) - 1
        while (self.parent_index(index) or self.parent_index(index) == 0) and self.data[index] < self.data[self.parent_index(index)]:
            percolate = self.parent_index(index)
            self.percolate_up(index)
            index = percolate

    def remove(self) -> T:
        """
        Removes and returns the smallest element (root) from the heap,
        restoring the min-heap property if necessary.

        :return: The smallest element if the heap is not empty, None otherwise.
        """
        if self.empty():
            return None

        index = 0
        while self.min_child_index(index):
            percolate = self.min_child_index(index)
            self.percolate_down(index)
            index = percolate

        return self.data.pop(index)

    def build_heap(self):
        """
        Builds a min-heap from an unordered array of elements.
        """
        if self.empty():
            return

        for i in range(len(self.data) // 2 - 1, -1, -1):
            index = i
            while self.min_child_index(index) and self.data[index] > self.data[self.min_child_index(index)]:
                percolate = self.min_child_index(index)
                self.percolate_down(index)
                index = percolate

    def is_min_heap(self) -> bool:
        """
        Checks if the current structure satisfies the min-heap property.

        :return: True if the heap is a min-heap, False otherwise.
        """

        if self.empty():
            return False

        if len(self.data) == 1:
            return True

        for index in range(1, len(self.data)):
            if self.data[index] < self.data[self.parent_index(index)]:
                return False

        return True
