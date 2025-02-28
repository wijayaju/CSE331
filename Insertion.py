import unittest


def insertion_sort(data):
    for index in range(1, len(data)):
        key = data[index]
        j = index - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


class TestInsertionSort(unittest.TestCase):

    def test_sort(self):
        test_data = [64, 34, 25, 12, 22, 11, 90]
        insertion_sort(test_data)
        self.assertEqual(test_data, [11, 12, 22, 25, 34, 64, 90])

    def test_empty_list(self):
        test_data = []
        insertion_sort(test_data)
        self.assertEqual(test_data, [])

    def test_single_element(self):
        test_data = [5]
        insertion_sort(test_data)
        self.assertEqual(test_data, [5])

    def test_already_sorted(self):
        test_data = [1, 2, 3, 4, 5]
        insertion_sort(test_data)
        self.assertEqual(test_data, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        test_data = [5, 4, 3, 2, 1]
        insertion_sort(test_data)
        self.assertEqual(test_data, [1, 2, 3, 4, 5])

    def test_q(self):
        test_data = [6, 3, 5, 7, 2, 4]
        insertion_sort(test_data)
        self.assertEqual(test_data, [2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
