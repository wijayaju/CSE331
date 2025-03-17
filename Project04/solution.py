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
        self.back: int = (self.size + front - 1) % self.capacity if data else None
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[(index + front) % capacity] = value

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
        INSERT DOCSTRINGS HERE!
        """
        pass

    def is_empty(self) -> bool:
        """
        INSERT DOCSTRINGS HERE!
        """
        pass

    def front_element(self) -> T:
        """
        INSERT DOCSTRINGS HERE!
        """
        pass

    def back_element(self) -> T:
        """
        INSERT DOCSTRINGS HERE!
        """
        pass

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        pass

    def dequeue(self, front: bool = True) -> T:
        """
        INSERT DOCSTRINGS HERE!
        """
        pass

    def grow(self) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        pass

    def shrink(self) -> None:
        """
        INSERT DOCSTRINGS HERE!
        """
        pass


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


