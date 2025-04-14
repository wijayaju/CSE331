class BPlusTreeNode:
    """
    B+ Tree implementation with insertion, search, and in-order traversal.

    📌 Disclaimer on Balancing and Deletion:

    This implementation is intentionally simplified for educational purposes.

    - ✅ No balancing after insertion:
        B+ trees naturally stay balanced through node splitting.
        When a node becomes full, it is split and the middle key is pushed up.
        This ensures the tree remains balanced without additional logic,
        maintaining logarithmic height and efficient operations.

    - ❌ No deletion:
        Deletion is not implemented in this version.
        In practice, B+ tree deletions are rare in most applications such as databases,
        file systems, and indexing structures. Deletions are often handled by:
            - Logical deletion (marking entries as deleted),
            - Lazy deletion (cleanup at a later time),
            - Or batch reorganization.
        This approach avoids the complexity and cost of constant rebalancing.

    - ⚙️ Typical Runtime Behavior:
        - All core operations (insert, search, traversal) run in O(log n) time.
        - In real-world systems, the dominant cost is I/O time (disk access),
          not the in-memory tree manipulation.
        - Therefore, simplified insertions with rare splits reflect actual runtime usage well.

    This class is ideal for demonstrating the structure and behavior of B+ trees
    without the added complexity of rebalancing or deletion logic.
    """

    """
    A node in a B+ Tree.

    Attributes:
    - is_leaf (bool): True if this is a leaf node, False if it's an internal node.
    - keys (list): Keys stored in the node.
    - children (list): Child pointers (to BPlusTreeNode instances).
    - next (BPlusTreeNode): Pointer to the next leaf node (only used in leaf nodes).
    """
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        self.next = None  # For leaf node chaining


class BPlusTree:
    """
    A simplified B+ Tree implementation supporting insertion and search.

    Disclaimer: This implementation is simplified for educational use.
    - No deletion is implemented.
    - No rebalancing beyond splitting full nodes is needed due to B+ tree structure.
    - Runtime remains logarithmic because the tree stays balanced by design.
    """
    def __init__(self, max_children=3):
        """
        Initializes a B+ Tree.

        Parameters:
        - max_children (int): Maximum number of children per internal node.
        """
        self.root = BPlusTreeNode(is_leaf=True)
        self.max_children = max_children
        self.max_keys = max_children - 1

    def contains(self, key):
        """
        Public method to check if a key exists in the tree.

        Parameters:
        - key: The value to search for.

        Returns:
        - True if key is found, False otherwise.
        """
        return self.search(key)

    def insert_key(self, key):
        """
        Public method to insert a key into the tree.

        Parameters:
        - key: The value to insert.
        """
        self.insert(key)

    def search(self, key):
        """
        Searches for a key in the B+ Tree.

        Parameters:
        - key: The value to search for.

        Returns:
        - True if key is found in any leaf node, False otherwise.
        """
        node = self.root
        # Traverse down to the leaf node
        while not node.is_leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        return key in node.keys

    def insert(self, key):
        """
        Inserts a key into the tree, handling root splits if necessary.

        Parameters:
        - key: The value to insert.
        """
        root = self.root
        # If root is full, split it and create a new root
        if len(root.keys) == self.max_keys:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        """
        Helper function to insert a key into a non-full node.
        Recursively descends into child nodes if needed.

        Parameters:
        - node (BPlusTreeNode): The current node.
        - key: The key to insert.
        """
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            # Split the child if it is full before descending
            if len(node.children[i].keys) == self.max_keys:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index):
        """
        Splits a full child node of a parent into two.

        Parameters:
        - parent (BPlusTreeNode): The parent node.
        - index (int): Index of the child to split.
        """
        node = parent.children[index]
        new_node = BPlusTreeNode(is_leaf=node.is_leaf)
        mid = len(node.keys) // 2

        if node.is_leaf:
            # Split leaf node: both halves keep data, maintain next pointer
            new_node.keys = node.keys[mid:]
            node.keys = node.keys[:mid]
            new_node.next = node.next
            node.next = new_node
            parent.keys.insert(index, new_node.keys[0])
        else:
            # Split internal node: push middle key up, divide children
            parent.keys.insert(index, node.keys[mid])
            new_node.keys = node.keys[mid + 1:]
            new_node.children = node.children[mid + 1:]
            node.keys = node.keys[:mid]
            node.children = node.children[:mid + 1]

        parent.children.insert(index + 1, new_node)

    def get_sorted_elements(self):
        """
        Returns all keys in the tree in sorted order.

        Returns:
        - A list of keys from all leaf nodes, in ascending order.
        """
        node = self.root
        # Traverse to the leftmost leaf
        while not node.is_leaf:
            node = node.children[0]
        result = []
        # Walk through linked leaf nodes
        while node:
            result.extend(node.keys)
            node = node.next
        return result


# Unit Tests
import unittest

class TestBPlusTree(unittest.TestCase):
    """Unit tests for basic B+ Tree functionality"""

    def test_insertion_and_sorted_output(self):
        tree = BPlusTree(max_children=3)
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            tree.insert_key(key)
        self.assertEqual(tree.get_sorted_elements(), sorted(keys))

    def test_duplicate_insertion(self):
        tree = BPlusTree(max_children=3)
        keys = [30, 30, 40, 50, 50, 60]
        for key in keys:
            tree.insert_key(key)
        self.assertEqual(tree.get_sorted_elements(), sorted(keys))

    def test_search_existing(self):
        tree = BPlusTree(max_children=3)
        keys = [25, 40, 15, 30, 10, 50]
        for key in keys:
            tree.insert_key(key)
        self.assertTrue(tree.contains(15))
        self.assertTrue(tree.contains(50))
        self.assertTrue(tree.contains(25))

    def test_search_non_existing(self):
        tree = BPlusTree(max_children=3)
        keys = [12, 24, 36]
        for key in keys:
            tree.insert_key(key)
        self.assertFalse(tree.contains(100))
        self.assertFalse(tree.contains(0))
        self.assertFalse(tree.contains(18))


if __name__ == "__main__":
    unittest.main()