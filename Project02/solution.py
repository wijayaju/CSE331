"""
Project 2 - Hybrid Sorting
CSE 331 Spring 2025
"""

from datetime import date
from typing import Callable, Literal, List, TypeVar

T = TypeVar("T")  # represents generic type


# This is an optional helper function but HIGHLY recommended, especially for the application problem!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Decides if `first` should come before `second` in sorted list

    :param first: an element to be compared
    :param second: next element to compare to
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :return: True if left input should be before right input, False otherwise
    """
    if not descending:  # if ascending order
        return comparator(first, second)
    else:  # if descending order
        return comparator(second, first)


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sort list using selection sort

    :param data: List of items to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :return: None
    """
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if do_comparison(data[j], data[min_idx], comparator, descending):
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Sort list using bubble sort

    :param data: List of items to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :return: None
    """
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if not do_comparison(data[j], data[j + 1], comparator, descending):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        # If no two elements were swapped by inner loop, the list is sorted
        if not swapped:
            break


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sort list using insertion sort

    :param data: List of items to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :return: None
    """
    for index in range(1, len(data)):
        key = data[index]
        j = index - 1
        while j >= 0 and do_comparison(key, data[j], comparator, descending):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sort list using a hybrid of mergesort and insertion sort

    :param data: List of items to be sorted
    :param threshold: Maximum size at which insertion sort will be used instead of merge sort
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :return: None
    """
    n = len(data)
    if n < 2:
        return
    mid = n // 2
    S1 = data[0:mid]
    S2 = data[mid:n]
    hybrid_merge_sort(S1, threshold=threshold, comparator=comparator, descending=descending)
    hybrid_merge_sort(S2, threshold=threshold, comparator=comparator, descending=descending)
    if n <= threshold:  # Insertion
        insertion_sort(data, comparator=comparator, descending=descending)
    else:  # Merge
        i = j = 0  # Merge
        while i + j < len(data):
            if j == len(S2) or (i < len(S1) and do_comparison(S1[i], S2[j], comparator, descending)) or (i < len(S1) and not do_comparison(S2[j], S1[i], comparator, descending)):  # includes tie case
                data[i + j] = S1[i]
                i = i + 1
            else:
                data[i + j] = S2[j]
                j = j + 1


def quicksort(data: List[T]) -> None:
    """
    Sorts a list in place using quicksort
    :param data: List of items to be sorted
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


###########################################################
# DO NOT MODIFY
###########################################################
class Song:
    """
    Class that represents songs.
    """
    __slots__ = ['rock', 'pop', 'rap', 'jazz', 'date_published']

    def __init__(self, rock: float, pop: float, rap: float, jazz: float, date_published: date) -> None:
        """
        Constructor for the Song class.

        :param rock: value to assign as rock relevance.
        :param pop: value to assign as pop relevance.
        :param rap: value to assign as rap relevance.
        :param jazz: value to assign as jazz relevance.
        :param date_published: value to assign as date published.
        :return: None
        """
        self.rock = rock
        self.pop = pop
        self.rap = rap
        self.jazz = jazz
        self.date_published = date_published

    def __repr__(self) -> str:
        """
        Represent the song as a string.

        :return: Representation of the song.
        """
        return str(self)

    def __str__(self) -> str:
        """
        Convert the Song to a string.

        :return: String representation of the Song.
        """
        return f'<date_published: {self.date_published.month}/{self.date_published.day}/{self.date_published.year}, rock: {self.rock}, pop: {self.pop}, rap: {self.rap}, jazz: {self.jazz}>'

    def __eq__(self, other) -> bool:
        """
        Compare two Song objects for equality.

        :param other: The other Song to compare with.
        :return: True if songs are equal, False otherwise.
        """
        return self.date_published == other.date_published and self.rock == other.rock and self.pop == other.pop and \
            self.rap == other.rap and self.jazz == other.jazz


###########################################################
# MODIFY BELOW
###########################################################
def get_relevant_songs(songs: List[Song], genres_user: List[Literal['rock', 'pop', 'rap', 'jazz']],
                       order_by: Literal['newest', 'oldest']) -> List[Song]:
    """
    Selects the top 10 songs based on relevance and sorts them according to order_by

    :param songs: A list of songs
    :param genres_user: The genres to sort by. For example, if genres_user = ["pop","rock"], then sort by pop, and afterward rock.
    :param order_by: A string object representing which the order in which to return the songs. If order_by = "newest", then return the songs in order of last date published to first, and if order_by = "oldest", return the songs in order of first song published to last.
    :return: Sorted list of relevant songs
    """
    if len(songs) < 1:
        return []
    order = False
    if order_by == 'newest':
        order = True
    for genre in genres_user:  # since genres_user can only be 1-4, shouldn't affect overall runtime complexity
        if genre == 'rock':
            hybrid_merge_sort(songs, threshold=0, comparator= lambda x, y: x.rock < y.rock, descending=True)
        elif genre == 'pop':
            hybrid_merge_sort(songs, threshold=0, comparator=lambda x, y: x.pop < y.pop, descending=True)
        elif genre == 'rap':
            hybrid_merge_sort(songs, threshold=0, comparator=lambda x, y: x.rap < y.rap, descending=True)
        else:
            hybrid_merge_sort(songs, threshold=0, comparator=lambda x, y: x.jazz < y.jazz, descending=True)
    if len(songs) > 10:
        songs = songs[0:10]
    hybrid_merge_sort(songs, threshold=0, comparator=lambda x, y: x.date_published < y.date_published, descending=order)
    return songs
