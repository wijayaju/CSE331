import math
from typing import TypeVar, Generator, List, Tuple, Optional, Dict
from collections import deque
import json
from queue import SimpleQueue
import heapq

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
# represents a Node object (forward-declare to use in Node __init__)
Node = TypeVar("Node")
# represents a custom type used in application
AVLWrappedDictionary = TypeVar("AVLWrappedDictionary")


class Node:
    """
    Implementation of an BST and AVL tree node.
    Do not modify.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["value", "parent", "left", "right", "height", "data"]

    def __init__(self, value: T, parent: Node = None,
                 left: Node = None, right: Node = None, data: str = None) -> None:
        """
        Construct an AVL tree node.

        :param value: value held by the node object
        :param parent: ref to parent node of which this node is a child
        :param left: ref to left child node of this node
        :param right: ref to right child node of this node
        """
        self.value = value
        self.parent, self.left, self.right = parent, left, right
        self.height = 0
        self.data = data

    def __repr__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return f"<{str(self.value)}>"

    def __str__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return repr(self)


####################################################################################################

class BinarySearchTree:
    """
    Implementation of an BSTree.
    Modify only below indicated line.
    """

    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["origin", "size"]

    def __init__(self) -> None:
        """
        Construct an empty BST tree.
        """
        self.origin = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the BSTree as a string.

        :return: string representation of the BST tree
        """
        if self.origin is None:
            return "Empty BST Tree"

        lines = pretty_print_binary_tree(self.origin, 0, False, '-')[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

    def __str__(self) -> str:
        """
        Represent the BSTree as a string.

        :return: string representation of the BSTree
        """
        return repr(self)

    ########################################
    # Implement functions below this line. #
    ########################################

    def height(self, root: Node) -> int:
        """
        Return the height of a subtree in the BSTree, or -1 if the tree is empty.
        :param root: the root of the subtree
        :return: the height of the subtree
        """
        return root.height if root else -1

    def insert(self, root: Node, val: T) -> None:
        """
        Insert a value into the BSTree at the correct location starting at root.
        :param root: root of subtree in BSTree
        :param val: the value to insert
        """
        if not self.origin:
            self.origin = Node(val)
            self.size += 1

        if root:
            if root.value == val:
                return

            if val < root.value:
                if not root.left:
                    root.left = Node(val, root)
                    self.size += 1
                else:
                    self.insert(root.left, val)
            else:
                if not root.right:
                    root.right = Node(val, root)
                    self.size += 1
                else:
                    self.insert(root.right, val)





            root.height = 1 + max(self.height(root.left),
                                  self.height(root.right))

    def remove(self, root: Node, val: T) -> Node:
        """
        Remove a value from the BSTree starting at root.
        :param root: root of subtree in BSTree
        :param val: the value to remove
        :return: the new root of the subtree
        """
        if not self.origin:
            return

        if root:
            # (1) Case where value is found at this root
            if root.value == val:
                # (1a) Case where root has no children -> decrease size, and return None
                if not root.left and not root.right:
                    root = None
                    self.size -= 1
                    if self.size == 0:
                        self.origin = None
                    return root

                # (1b) Case where root has only a left child -> pull up child and set parent
                elif root.right is None:
                    self.size -= 1
                    root.left.parent = root.parent
                    root = root.left
                    return root

                # (1c) Case where root has only a right child -> pull up child and set parent
                elif root.left is None:
                    self.size -= 1
                    root.right.parent = root.parent
                    root = root.right
                    return root

                # (1d) Case where root has two children -> swap with predecessor and remove predecessor
                else:
                    pred = root.left
                    while pred.right:
                        pred = pred.right
                    root.value = pred.value
                    root.left = self.remove(root.left, pred.value)

            # (2) Search left or right
            elif val < root.value:
                root.left = self.remove(root.left, val)

            else:
                root.right = self.remove(root.right, val)

            # (3) Update height after removal
            root.height = 1 + max(self.height(root.left), self.height(root.right))
            return root

    def search(self, root: Node, val: T) -> Optional[Node]:
        """
        Search for a value in the BSTree starting at root.
        :param root: root of subtree in BSTree
        :param val: the value to search for
        :return: the node containing the value, or its potential parent if it is not found
        """
        if not self.origin:
            return

        if root:
            if root.value == val:
                return root
            elif val < root.value:
                if not root.left:
                    return root
                return self.search(root.left, val)
            else:
                if not root.right:
                    return root
                return self.search(root.right, val)




def pretty_print_binary_tree(root: Node, curr_index: int, include_index: bool = False,
                             delimiter: str = "-", ) -> \
        Tuple[List[str], int, int, int]:
    """
    Taken from: https://github.com/joowani/binarytree

    Recursively walk down the binary tree and build a pretty-print string.
    In each recursive call, a "box" of characters visually representing the
    current (sub)tree is constructed line by line. Each line is padded with
    whitespaces to ensure all lines in the box have the same length. Then the
    box, its width, and start-end positions of its root node value repr string
    (required for drawing branches) are sent up to the parent call. The parent
    call then combines its left and right sub-boxes to build a larger box etc.
    :param root: Root node of the binary tree.
    :type root: binarytree.Node | None
    :param curr_index: Level-order_ index of the current node (root node is 0).
    :type curr_index: int
    :param include_index: If set to True, include the level-order_ node indexes using
        the following format: ``{index}{delimiter}{value}`` (default: False).
    :type include_index: bool
    :param delimiter: Delimiter character between the node index and the node
        value (default: '-').
    :type delimiter:
    :return: Box of characters visually representing the current subtree, width
        of the box, and start-end positions of the repr string of the new root
        node value.
    :rtype: ([str], int, int, int)
    .. _Level-order:
        https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
    """
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if include_index:
        node_repr = "{}{}{}".format(curr_index, delimiter, root.value)
    else:
        node_repr = f'{root.value},h={root.height},' \
                    f'⬆{str(root.parent.value) if root.parent else "None"}'

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = pretty_print_binary_tree(
        root.left, 2 * curr_index + 1, include_index, delimiter
    )
    r_box, r_box_width, r_root_start, r_root_end = pretty_print_binary_tree(
        root.right, 2 * curr_index + 2, include_index, delimiter
    )

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(" " * (l_root + 1))
        line1.append("_" * (l_box_width - l_root))
        line2.append(" " * l_root + "/")
        line2.append(" " * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(" " * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append("_" * r_root)
        line1.append(" " * (r_box_width - r_root + 1))
        line2.append(" " * r_root + "\\")
        line2.append(" " * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = " " * gap_size
    new_box = ["".join(line1), "".join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else " " * l_box_width
        r_line = r_box[i] if i < len(r_box) else " " * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end
