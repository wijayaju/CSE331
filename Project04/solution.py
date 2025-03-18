"""
CSE331 Project 4 SS25
Circular Double-Ended Queue
solution.py
"""

from typing import TypeVar, List

T = TypeVar('T')


class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = None, front: int = 0, capacity: int = 4):
        """
        DO NOT MODIFY
        Initializes an instance of a CircularDeque
        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque
        """
        if data is None and front != 0:
            data = ['Start']  # front will get set to 0 by a front enqueue if the initial data is empty
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size: int = len(data)
        self.queue: List[T] = [None] * capacity
        self.back: int = (self.size + front - 1) // self.capacity if data else None
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[(index + front) // capacity] = value

    def __str__(self) -> str:
        """
        DO NOT MODIFY
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value
        :return: the instance as a string
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = ["CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    #
    # Your code goes here!
    #
    def __len__(self) -> int:
        """
        Returns the length/size of the circular deque.

        :return: int representing length of the circular deque.
        """
        return self.size

    def is_empty(self) -> bool:
        """
        Returns a boolean indicating if the circular deque is empty.

        :return: True if empty, False otherwise.
        """
        if self.size > 0:
            return False
        return True

    def front_element(self) -> T:
        """
        Returns the first element in the circular deque.

        :return: The first element if it exists, otherwise None.
        """
        return None if self.front is None else self.queue[self.front]

    def back_element(self) -> T:
        """
        Returns the last element in the circular deque.

        :return: The last element if it exists, otherwise None.
        """
        return None if self.back is None else self.queue[self.back]

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Add a value to either the front or back of the circular deque based off the parameter front.

        :param value: T: value to add into the circular deque.
        :param front: where to add value T.
        :return: None.
        """
        self.size += 1
        if front:
            if self.front == 0:
                self.front = self.size - 1
                self.queue[self.front] = value
        else:
            if self.back == self.capacity:
                self.back = 0
                self.queue[self.back] = value
        if self.size == self.capacity:
            self.grow()

    def dequeue(self, front: bool = True) -> T:
        """
        Remove an item from the queue.

        :param front: Whether to remove the front or back item from the dequeue.
        :return: Removed item, None if empty.
        """
        value = None
        if self.is_empty():
            return value

        if front:
            value = self.front_element()
            self.front += 1
        else:
            value = self.back_element()
            self.back -= 1
        if self.size <= self.capacity // 4 and self.capacity // 4 >= 4:
            self.shrink()
        return value

    def grow(self) -> None:
        """
        Doubles the capacity of CD by creating a
        new underlying python list with double the
        capacity of the old one and copies the values over from the current list.

        :return: None.
        """
        self.capacity *= 2
        self.front = 0
        self.back = self.size - 1
        new_queue: List[T] = [None] * self.capacity
        for i in range(self.size):
            new_queue[i] = self.queue[i]

    def shrink(self) -> None:
        """
        Cuts the capacity of the queue in half using
        the same idea as grow. Copy over contents of the
        old list to a new list with half the capacity.

        :return: None.
        """
        self.capacity //= 2
        self.front = 0
        self.back = self.size - 1
        new_queue: List[T] = [None] * self.capacity
        for i in range(self.size):
            new_queue[i] = self.queue[i]



def find_max_wind_speeds(numbers: List[int], size: int) -> List[int]:
    """
    INSERT DOCSTRINGS HERE!
    """
    pass
    


def max_wind_variability_score(wind_speeds: List[int]) -> int:
    """
    INSERT DOCSTRINGS HERE!
    """
    pass


