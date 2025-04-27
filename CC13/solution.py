from typing import List, Tuple



def number_of_ways_to_get_to_end(width, height):
    """
    Calculate the number of unique paths from the top-left corner
    to the bottom-right corner of a grid with the given width and height.

    You may only move either right or down at any point in time.

    Parameters:
    - width (int): number of columns in the grid (must be > 0)
    - height (int): number of rows in the grid (must be > 0)

    Returns:
    - int: total number of unique paths to reach the bottom-right corner

    Example:
    >>> number_of_ways_to_get_to_end(3, 3)
    6
    """
    if width <= 0 and height <= 0:  # Edge case: invalid measurements
        return 0
    elif width <= 1 < height or width > 1 >= height:  # Edge case: 1 path
        return 1

    grid = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0:
                grid[i][j] = 1
                continue
            ways_left = grid[i][j-1]
            ways_up = grid[i-1][j]
            grid[i][j] = ways_left + ways_up

    return grid[-1][-1]


# Optional challenge: implement using combinatorics
def number_of_ways_to_get_to_end_permutation(width, height):
    """
    Calculate the number of unique paths using combinatorics.

    This uses the idea that to reach the bottom-right corner,
    you must make (width - 1) right moves and (height - 1) down moves
    in some order.

    Total paths = C((width - 1 + height - 1), (width - 1)) = (m+n)! / (m! * n!)

    Parameters:
    - width (int): number of columns
    - height (int): number of rows

    Returns:
    - int: number of unique paths calculated via permutations
    """
    right = width - 1
    down = height - 1
    return factorial(right + down) / (factorial(right) * factorial(down))


def factorial(num):
    """
    Compute the factorial of a non-negative integer.

    Parameters:
    - num (int): a non-negative integer

    Returns:
    - int: factorial of num

    Example:
    >>> factorial(5)
    120
    """
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result
