def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]


# unittest for selection sort
import unittest


class TestSelectionSort(unittest.TestCase):

    def test_sort(self):
        test_data = [64, 34, 25, 12, 22, 11, 90]
        selection_sort(test_data)
        self.assertEqual(test_data, [11, 12, 22, 25, 34, 64, 90])

    def test_empty_list(self):
        test_data = []
        selection_sort(test_data)
        self.assertEqual(test_data, [])

    def test_single_element(self):
        test_data = [5]
        selection_sort(test_data)
        self.assertEqual(test_data, [5])

    def test_already_sorted(self):
        test_data = [1, 2, 3, 4, 5]
        selection_sort(test_data)
        self.assertEqual(test_data, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        test_data = [5, 4, 3, 2, 1]
        selection_sort(test_data)
        self.assertEqual(test_data, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
