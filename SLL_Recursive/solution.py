from typing import TypeVar, Tuple  # For use in type hinting

# Type Declarations
T = TypeVar('T')  # generic type
SLL = TypeVar('SLL')  # forward declared
Node = TypeVar('Node')  # forward declare `Node` type


class SLLNode:
    """
    Node implementation
    Do not modify.
    """

    __slots__ = ['val', 'next']

    def __init__(self, value: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param value: value held by node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.val = value
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method to cast nodes to strings
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: bool
        """
        return self is other if other is not None else False


class RecursiveSinglyLinkedList:
    """
    Recursive implementation of an SLL
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        :return: None
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        """
        return self.to_string(self.head)

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ============ Modify below ============ #

    # def insertion_sort(self) -> None:
    #     current = self.head
    #     while current.next is not None:
    #
    #         temp = current.next
    #         if temp.val < current.val:
    #             current.next = temp.next
    #             temp.next = self.head
    #             self.head = temp
    #         else:
    #             prev = current
    #             while prev.next is not None and temp.val > prev.next.val:
    #                 prev = prev.next
    #             if prev.next != temp:
    #                 current.next = temp.next
    #                 temp.next = prev.next
    #                 prev.next = temp
    #         current = current.next
    def insertion_sort(self) -> None:
        dummy = SLLNode(None)
        current = self.head
        while current:
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            next_node = current.next
            current.next = prev.next
            prev.next = current
            current = next_node
        self.head = dummy.next

    def add(self, value: T, back: bool = True) -> None:
        """
        Pushes a `Node` with value `value` to the end of the list
        :param value: value to push to the list
        :param back: whether to push to the front or the back of the linked list
        :return: None
        """
        new_node = SLLNode(value)

        if self.head is None:
            # pushing onto brand-new list
            self.head = new_node
            self.tail = new_node
        elif back:
            # pushing onto tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            # pushing onto head
            new_node.next = self.head
            self.head = new_node

    def to_string(self, curr: Node) -> str:
        """
        Converts an SLL to a string
        :param curr: node at this recursive step
        :return: string representation up to the current node
        """

        answer = ""

        if curr and curr.next:
            answer += str(curr.val) + " --> " + self.to_string(curr.next)
        elif curr:
            answer += str(curr.val)
        else:
            return "None"

        return answer

        # return (str(curr.val) if curr else 'None') + (" --> " + self.to_string(curr.next) if (curr and curr.next) else '')

    def search(self, value: T) -> bool:
        """
        Searches the SLL for a node containing `value`
        :param value: value to search for
        :return: `True` if found, else `False`
        """

        def search_inner(curr: Node) -> bool:
            """
            Recursive helper for `search`
            :param curr: node at this recursive step
            :return bool: `True` if found, else `False`
            """
            if curr is None:
                return False

            return curr.val == value or search_inner(curr.next)

        return search_inner(self.head)

    def remove(self, value: T) -> bool:
        """
        Removes the first node containing `value` from the SLL
        :param value: value to remove
        :return: bool is anything deleted
        """

        def remove_inner(curr: Node) -> Tuple[Node, bool]:
            """
            Recursive helper for `remove`
            :param curr: node at this recursive step
            :return: Node removed node; bool was a node removed
            """
            if curr is None:
                return None, False

            if curr.val == value:
                return curr.next, True

            curr.next, is_del = remove_inner(curr.next)
            # If tail was removed, then reassign tail
            if curr.next is None:
                self.tail = curr
            return curr, is_del

        self.head, is_deleted = remove_inner(self.head)
        if self.head is None:
            self.tail = None
        return is_deleted

    # recursive
    def remove_duplicates(self, curr: Node) -> None:
        if curr is None:
            return
        if curr.next is not None and curr.val == curr.next.val:
            curr.next = curr.next.next
            self.remove_duplicates(curr)
        else:
            self.remove_duplicates(curr.next)

    # write it iteratively first to help you ease in!!!
    def remove_duplicates_iterative(self, curr: Node) -> None:

        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next


def fibonacci(n: int, cache: dict) -> int:
    if n not in cache:
        cache[0] = 0
        cache[1] = 1
    if n <= 0:
        return cache[0]
    elif n == 1:
        return cache[1]
    else:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        return cache[n]
