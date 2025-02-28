from importlib.metadata import pass_none
from typing import TypeVar  # For use in type hinting

# Type declarations
T = TypeVar('T')        # generic type
SLL = TypeVar('SLL')    # forward declared Singly Linked List type
Node = TypeVar('Node')  # forward declared Node type


class SLLNode:
    """
    Node implementation
    Do not modify
    """

    __slots__ = ['data', 'next']

    def __init__(self, data: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param data: data value held by the node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method, casts SLL nodes to strings
        :return: string representation of node
        """
        return '(Node: ' + str(self.data) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        :return: string representation of node
        """
        return '(Node: ' + str(self.data) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: True if the nodes are ==, else False
        """
        return self is other if other is not None else False


class SinglyLinkedList:
    """
    SLL implementation
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        return: None
        DO NOT MODIFY THIS FUNCTION
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        DO NOT MODIFY THIS FUNCTION
        :return: string representation of SLL
        """
        return self.to_string()

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right operand of `==`
        :return: True if equal, else False
        DO NOT MODIFY THIS FUNCTION
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ========== Modify below ========== #

    def append(self, data: T) -> None:
        """
        Append an SLLNode to the end of the SLL
        :param data: data to append
        :return: None
        """
        if self.head is None:
            self.head = self.tail = SLLNode(data)
        else:
            self.tail.next = SLLNode(data)
            self.tail = self.tail.next

    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of SLL
        """
        if self.head is None:
            return "None"
        SLL_string = ""
        current_node = self.head
        while current_node is not self.tail:
            SLL_string += current_node.data + " --> "
            current_node = current_node.next
        SLL_string += current_node.data
        return SLL_string

    def length(self) -> int:
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def total(self) -> T:
        """
        Sums up the values in the list
        :return: total sum of values in the list
        """
        total = None
        if self.head is None:
            return total
        current_node = self.head
        total = current_node.data
        current_node = current_node.next
        while current_node is not None:
            total = total + current_node.data
            current_node = current_node.next
        return total

    def delete(self, data: T) -> bool:
        """
        Deletes the first node containing `data` from the SLL
        :param data: data to remove
        :return: True if a node was removed, else False
        """
        if self.head is None:
            return False

        if self.head.data is data:
            if self.head is self.tail:
                self.tail = self.tail.next
            self.head = self.head.next
            return True

        current_node = self.head
        while current_node.next and current_node.next.data is not data:
            current_node = current_node.next

        if current_node.next is None:
            return False

        if current_node.next is self.tail:
            self.tail = current_node

        current_node.next = current_node.next.next

        return True

    def delete_all(self, data: T) -> bool:
        """
        Deletes all instances of a node containing `data` from the SLL
        :param data: data to remove
        :return: True if a node was removed, else False
        """
        out = False

        if self.head is None:
            return False

        while self.head and self.head.data is data:
            if self.head is self.tail:
                self.tail = self.tail.next
            self.head = self.head.next
            out = True

        current_node = self.head
        while current_node and current_node.next:
            if current_node.next.data is not data:
                current_node = current_node.next
            else:
                if current_node.next is self.tail:
                    self.tail = current_node
                current_node.next = current_node.next.next
                out = True

        return out


    def find(self, data: T) -> bool:
        """
        Looks through the SLL for a node containing `data`
        :param data: data to search for
        :return: True if found, else False
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data is data:
                return True
            current_node = current_node.next
        return False

    def find_sum(self, data: T) -> int:
        """
        Returns the number of occurrences of `data` in this list
        :param data: data to find and sum up
        :return: number of times the data occurred
        """
        total = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data is data:
                total += 1
            current_node = current_node.next
        return total


def help_mario(roster: SLL, ally: str) -> bool:
    """
    Updates the roster of racers to put Mario's ally at the front
    Preserves relative order of racers around ally
    :param roster: initial order of racers
    :param ally: the racer that needs to go first
    :return: True if the roster was changed, else False
    """
    if roster.head is None:
        return False
    if roster.head.data is ally:
        return False
    if roster.head.next is None:
        return False
    racer = roster.head.next
    prev_racer = roster.head
    while racer:
        if racer.data is ally:
            roster.tail.next = roster.head
            prev_racer.next = None
            roster.tail = prev_racer
            roster.head = racer
            return True
        racer = racer.next
        prev_racer = prev_racer.next
    return False