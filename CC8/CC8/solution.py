# This is an input class. Do not edit.
class BST:
    """
    Represents a node in a Binary Search Tree (BST).

    Attributes:
        value (int): The integer value of the node.
        left (BST, optional): The left child of the node. Defaults to None.
        right (BST, optional): The right child of the node. Defaults to None.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeData:
    """
    Helper class to track the number of nodes visited and the latest node value visited
    during reverse in-order traversal.

    Attributes:
        nodes_visited (int): Count of nodes visited so far.
        latest_node_value (int): Value of the latest visited node that contributes to the kth largest calculation.
    """
    def __init__(self, nodes_visited, latest_node_value):
        self.nodes_visited = nodes_visited
        self.latest_node_value = latest_node_value



def get_kth_largest_value(tree, k):
    """
    Finds the kth largest value in a Binary Search Tree (BST).

    Args:
        tree (BST): The root node of the Binary Search Tree.
        k (int): The rank of the largest value to find in the BST.

    Returns:
        int: The kth largest value in the BST.
    """
    tree_history = TreeData(0, tree.value)
    traverse_reverse_in_order(tree, k, tree_history)
    return tree_history.latest_node_value


def traverse_reverse_in_order(node, k, tree_data):
    """
    Performs a reverse in-order traversal on the BST to find the kth largest value.

    This function recursively traverses the right subtree, then the current node,
    then the left subtree. It keeps track of the number of nodes visited so far
    and updates the latest node value when the kth largest node is reached.

    Args:
        node (BST): The current node in the BST.
        k (int): The rank of the largest value to find in the BST.
        tree_data (TreeData): An instance of TreeData to track nodes visited and the latest node value.
    """
    if node is None:
        return

    if node.right:
        traverse_reverse_in_order(node.right, k, tree_data)

    tree_data.nodes_visited += 1
    if tree_data.nodes_visited == k:
        tree_data.latest_node_value = node.value
        return

    if node.left:
        traverse_reverse_in_order(node.left, k, tree_data)

    return
