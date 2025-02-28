def mergeSort(S):
    """Sort the elements of Python list S using the merge sort algorithm."""
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    mergeSort(S1)
    mergeSort(S2)
    merge(S1, S2, S)


def merge(S1, S2, S):
    """Merge two sorted Python Lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i = i + 1
        else:
            S[i + j] = S2[j]
            j = j + 1


# Unit tests
import unittest


class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        data = []
        mergeSort(data)
        self.assertEqual(data, [])

    def test_single_element(self):
        data = [1]
        mergeSort(data)
        self.assertEqual(data, [1])

    def test_sorted_list(self):
        data = [1, 2, 3, 4, 5]
        mergeSort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        data = [4, 2, 5, 1, 3]
        mergeSort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        data = [4, 2, 5, 2, 3]
        mergeSort(data)
        self.assertEqual(data, [2, 2, 3, 4, 5])

    def test_negative_numbers(self):
        data = [-3, -1, -2, -4, 0]
        mergeSort(data)
        self.assertEqual(data, [-4, -3, -2, -1, 0])

    def test_large_numbers(self):
        data = [1000, 500, 1500, 2000, 100]
        mergeSort(data)
        self.assertEqual(data, [100, 500, 1000, 1500, 2000])


if __name__ == '__main__':
    unittest.main()

