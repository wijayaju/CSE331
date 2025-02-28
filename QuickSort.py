import unittest
from typing import List, TypeVar

T = TypeVar('T', int, float)


def quicksort(data: List[T]) -> None:
    """
        Sorts a list in place using quicksort
        :param data: Data to sort
        """

    def quicksort_inner(first: int, last: int) -> None:
        """
            Sorts portion of list at indices in interval [first, last] using quicksort

            :param first: first index of portion of data to sort
            :param last: last index of portion of data to sort
            """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


class TestQuickSort(unittest.TestCase):

    def test_empty_list(self):
        data = []
        quicksort(data)
        self.assertEqual(data, [])

    def test_single_element(self):
        data = [1]
        quicksort(data)
        self.assertEqual(data, [1])

    def test_sorted_list(self):
        data = [1, 2, 3, 4, 5]
        quicksort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        data = [5, 4, 3, 2, 1]
        quicksort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        data = [3, 6, 2, 7, 5, 8, 4, 1]
        quicksort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_unsorted_list2(self):
        data = [8, 2, 91, 22, 55, 1, 7, 6]
        quicksort(data)
        self.assertEqual(data, [1, 2, 6,7,8,22,55, 91 ])

    def test_duplicate_elements(self):
        data = [3, 6, 2, 7, 2, 8, 4, 2]
        quicksort(data)
        self.assertEqual(data, [2, 2, 2, 3, 4, 6, 7, 8])

    def test_all_equal_elements(self):
        data = [5, 5, 5, 5, 5]
        quicksort(data)
        self.assertEqual(data, [5, 5, 5, 5, 5])

    def test_negative_elements(self):
        data = [-3, -6, -2, -7, -5, -8, -4, -1]
        quicksort(data)
        self.assertEqual(data, [-8, -7, -6, -5, -4, -3, -2, -1])

    def test_mixed_positive_negative(self):
        data = [3, -6, 2, -7, 5, -8, 4, -1]
        quicksort(data)
        self.assertEqual(data, [-8, -7, -6, -1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
