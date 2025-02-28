def radix_sort(array):
    """
    Sorts an array of non-negative integers using Radix Sort algorithm.

    Parameters:
    array (list): List of non-negative integers to be sorted.

    Returns:
    list: Sorted list of integers.
    """
    def get_max_length(array):
        """
        Finds the maximum length (number of digits) among all elements in the array.

        Parameters:
        array (list): List of integers.

        Returns:
        int: Maximum number of digits in the largest number.
        """
        max_digit = 0
        for i in range(len(array)):
            digit_count = get_length(array[i])
            if digit_count > max_digit:
                max_digit = digit_count
        return max_digit

    def get_length(value):
        """
        Returns the number of digits in a given value.

        Parameters:
        value (int): The number whose digits are to be counted.

        Returns:
        int: Number of digits in the value.
        """
        if value == 0:
            return 1
        digits = 0
        while value != 0:
            digits += 1
            value /= 10
        return digits

    digits = get_max_length(array)
    pow10 = 1
    for i in range(digits):
        buckets = [[],[],[],[],[],[],[],[],[],[]]
        for k in array:
            buckets[((k//pow10)%10)].append(k)
        array = []
        for j in range(10):
            for k in buckets[j]:
                array.append(k)
        pow10 *= 10
    return array