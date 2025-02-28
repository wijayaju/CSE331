def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True

        # If no two elements were swapped by inner loop, the list is sorted
        if not swapped:
            break


# def bubble_sort(data):
#     n = len(data)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#
#


# unittest for bubble sort
import unittest

class TestBubbleSort(unittest.TestCase):

    def test_sort(self):
        test_data = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(test_data)
        self.assertEqual(test_data, [11, 12, 22, 25, 34, 64, 90])

    def test_empty_list(self):
        test_data = []
        bubble_sort(test_data)
        self.assertEqual(test_data, [])

    def test_single_element(self):
        test_data = [5]
        bubble_sort(test_data)
        self.assertEqual(test_data, [5])

    def test_already_sorted(self):
        test_data = [1, 2, 3, 4, 5]
        bubble_sort(test_data)
        self.assertEqual(test_data, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        test_data = [5, 4, 3, 2, 1]
        bubble_sort(test_data)
        self.assertEqual(test_data, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
