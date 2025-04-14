from typing import List


class Node:
    def __init__(self, name: str):
        """
        Initializes a Node with a name and an empty list of children.

        :param name: The name of the node.
        """
        self.name = name
        self.children = []

    def add_child(self, name: str):
        """
        Adds a child node with the given name to this node.

        :param name: The name of the child node to add.
        :return: The current node instance (to allow chaining).
        """
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array: List[str]) -> List[str]:
        """
        Performs a depth-first search on the node tree starting from this node.
        Appends the name of each visited node to the provided array.

        :param array: A list that accumulates the names of visited nodes.
        :return: The updated list containing the DFS traversal order.
        """
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array



def has_single_cycle(array: List[int]) -> bool:
    """
    Determines whether the given array of jumps forms a single cycle.
    A single cycle occurs if every element is visited exactly once
    and the final jump lands back at the starting index.

    :param array: List of integers representing jump values at each index.
    :return: True if the array contains a single cycle, False otherwise.
    """
    count = 0
    index = 0
    while True:
        index = get_next_idx(index, array)
        count += 1
        if count == len(array):
            if index == 0:
                return True
            return False
        elif count > len(array):
            return False


def get_next_idx(current_idx: int, array: List[int]) -> int:
    """
    Calculates the next index to jump to, with wraparound.

    :param current_idx: The current index in the array.
    :param array: The array of jump values.
    :return: The next index to jump to.
    """
    idx = (current_idx + array[current_idx]) % len(array)
    return idx