from operator import truediv
import sys  # for min/max sizes

def find_unsorted_subarray(array):
    """
    Finds the shortest subarray that needs to be sorted for the entire
    array to become sorted.

    Args:
        array (list of int): The input array of integers.

    Returns:
        list: A list containing two integers representing the start and
        end indices of the shortest subarray that needs to be sorted.
        If the array is already sorted, returns [-1, -1].

    To Do:
        - Students will implement the logic to find the minimum and maximum
        out-of-order elements and determine the boundaries of the subarray
        that must be sorted.
    """
    if len(array) < 2:  # less than 2 items check
        return [-1, -1]

    left = 0
    while left < len(array) - 1 and array[left] <= array[left + 1]:
        # |o>----| left to right
        left += 1

    if left == len(array) - 1:  # already sorted check
        return [-1, -1]

    right = len(array) - 1
    while right > 0 and array[right] >= array[right - 1]:
        # |----<o| right to left
        right -= 1

    minimum = sys.maxsize
    maximum = -sys.maxsize
    for i in range(left, right + 1):
        # |-o><o-| between first left and right bound
        minimum = min(minimum, array[i])
        maximum = max(maximum, array[i])

    while left > 0 and array[left - 1] > minimum:
        # |--<o--| first left bound to left
        left -= 1

    while right < len(array) - 1 and array[right + 1] < maximum:
        # |--o>--| first right bound to right
        right += 1

    return [left, right]

def is_out_of_order(i, num, array):
    """
    Helper function to determine if an element is out of order in the array.

    Args:
        i (int): The index of the element to check.
        num (int): The element at index i.
        array (list of int): The input array of integers.

    Returns:
        bool: True if the element is out of order, False otherwise.

    This function is a suggestion  to students as a helper function.
    Students are encouraged to implement this function if they find it helpful.
    """
