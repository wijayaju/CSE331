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
        if self.size == 1:  # edge case for empty queue
            self.front, self.back = 0, 0
            self.queue[self.front] = value
        elif front:
            if self.front == 0:
                self.front = self.capacity - 1
            else:
                self.front -= 1
            self.queue[self.front] = value
        else:
            if self.back == self.capacity - 1:
                self.back = 0
            else:
                self.back += 1
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
        if self.is_empty():  # edge case for empty queue
            return value

        self.size -= 1

        if front:
            value = self.front_element()
            if self.front == self.capacity - 1:
                self.front = 0
            else:
                self.front += 1
        else:
            value = self.back_element()
            if self.back == 0:
                self.back = self.capacity - 1
            else:
                self.back -= 1

        if self.size <= self.capacity / 4 and self.capacity / 2 >= 4:
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
        new_queue: List[T] = [None] * self.capacity

        if self.is_empty():
            self.queue = new_queue
            return

        for index, value in enumerate(self.queue):
            if index >= self.front:  # if element is behind of front element
                new_queue[index - self.front] = value
            else:  # if element is in front of front element
                new_queue[self.size - self.front + index] = value

        self.front = 0
        self.back = self.size - 1
        self.queue = new_queue

    def shrink(self) -> None:
        """
        Cuts the capacity of the queue in half using
        the same idea as grow. Copy over contents of the
        old list to a new list with half the capacity.

        :return: None.
        """
        self.capacity //= 2
        new_queue: List[T] = [None] * self.capacity

        if self.is_empty():
            self.queue = new_queue
            return

        if self.front < self.back:  # if no circling
            for index in range(self.front,self.back + 1):
                new_queue[(index - self.front) % self.capacity] = self.queue[index]
        else:
            for index in range(self.front, len(self.queue)):  # loop over front to end of queue
                new_queue[(index - self.front) % self.capacity] = self.queue[index]
            for index in range(self.back + 1):  # circle back for rest of queue
                new_queue[(self.size - self.front + index) % self.capacity] = self.queue[index]

        self.front = 0
        self.back = self.size - 1
        self.queue = new_queue

def find_max_wind_speeds(numbers: List[int], size: int) -> List[int]:
    """
    Takes in a list of numbers and a sliding window size
    and returns a list containing the maximum value of the
    sliding window at each iteration step.

    :param numbers: A list of numbers that the sliding window will
        move through. Numbers can be negative or positive, including 0.
    :param size: The size of the sliding window.
    :return: A list containing the max number within the sliding window at each iteration step.
    """
    if len(numbers) < 2 or size == 1:  # edge case for empty or list with one item
        return numbers

    speeds = list()

    # brute force approach
    # for i in range(len(numbers) - size + 1):
        # window = CircularDeque(numbers[i:i+size], 0, size)
        # max_spd = None
        # for j in range(size):
        #     if not max_spd or max_spd < window.queue[j]:
        #         max_spd = window.queue[j]
        # speeds.append(max_spd)

    # sliding window approach
    window = CircularDeque(numbers[:size], 0, size)  # initialize sliding window
    if window.front < window.back: # first window, if queue doesn't circle around
        speeds.append(max(window.queue[window.front:window.back + 1]))
    else:
        speeds.append(max(window.queue[window.front:window.capacity] + window.queue[0:window.back + 1]))

    for i in range(size, len(numbers)):  # continue to slide window
        window.dequeue()
        window.enqueue(numbers[i], False)
        if window.front < window.back:
            speeds.append(max(window.queue[window.front:window.back+1]))
        else:
            speeds.append(max(window.queue[window.front:window.capacity] + window.queue[0:window.back + 1]))

    return speeds
    


def max_wind_variability_score(wind_speeds: List[int]) -> int:
    """
    Takes in a list of numbers and calculates the maximum
    wind variability score by finding the largest sum of
    non-adjacent numbers.

    :param wind_speeds: A list of wind speeds that the algorithm will be applied on.
    :return: An integer representing the maximum wind variability score.
    """
    if not wind_speeds:  # edge case for empty list
        return 0
    elif len(wind_speeds) <= 2:  # edge case for 2 or fewer items in list
        return max(wind_speeds)

    spds = [wind_speeds[0], max(wind_speeds[:2])]

    for i in range(2, len(wind_speeds)):
        # take prev spd and compare with sum of prev prev spd and cur spd
        spds.append(max(spds[-1], spds[i-2] + wind_speeds[i]))

    return spds[-1]