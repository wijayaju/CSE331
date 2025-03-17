class BinaryTree:
    """
    A class representing a node in a binary tree.

    Attributes:
        value (int): The value stored in the node.
        left (BinaryTree): The left child of the node, which is either another BinaryTree node or None.
        right (BinaryTree): The right child of the node, which is either another BinaryTree node or None.
    """

    def __init__(self, value):
        """
        Initializes a BinaryTree node with a value and no children.

        Args:
            value (int): The value to be assigned to the node.
        """
        self.value = value
        self.left, self.right = None, None


# O(n) time | O(n) space – where n is the number of nodes in the Binary Tree
def branch_sums(root):
    """
    Computes the sum of values for all branches in a binary tree.

    A branch sum is the total value of all nodes from the root to a leaf node.
    The function returns a list of branch sums ordered from the leftmost to the rightmost branch.

    Args:
        root (BinaryTree): The root node of the binary tree.

    Returns:
        list: A list of integers representing the sums of each branch.
    """
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums



def calculate_branch_sums(node, running_sum, sums):
    """
    Recursively traverses the binary tree to calculate the sum of each branch.

    If the node is a leaf node (no children), the running sum is appended to the sums list.
    Otherwise, the function continues traversing the left and right subtrees.

    Args:
        node (BinaryTree): The current node being traversed.
        running_sum (int): The sum of values from the root to the current node.
        sums (list): A list of sums of all branches found so far.
    """
    if node is None:
        return

    running_sum += node.value

    if node.left is None and node.right is None:
        sums.append(running_sum)
        return

    calculate_branch_sums(node.left, running_sum, sums)
    calculate_branch_sums(node.right, running_sum, sums)