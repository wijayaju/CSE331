"""
Project 5
CSE 331 S21 (Onsay)
Andrew McDonald & Bank Premsri
Inspired by Brandon Field and Anna DeBiasi's implementation
tests.py
"""
import unittest
import random
import types
from solution import Node,  BinarySearchTree


class BSTTests(unittest.TestCase):

    def test_insert_bst(self):
        """
        (1) Test inserting to empty tree
        final structure:
            1
        """
        bst = BinarySearchTree()
        bst.insert(bst.origin, 1)
        self.assertEqual(1, bst.size)
        self.assertEqual(1, bst.origin.value)
        self.assertEqual(0, bst.origin.height)
        self.assertEqual(None, bst.origin.left)
        self.assertEqual(None, bst.origin.right)

        """
        (2) Test inserting to cause imbalance tree on left
        final structure:
               10
              /
             5
            /
           1
          /
        -1
        """
        bst = BinarySearchTree()
        for value in [10, 5, 1, -1]:
            bst.insert(bst.origin, value)
        self.assertEqual(4, bst.size)
        self.assertEqual(10, bst.origin.value)
        self.assertEqual(3, bst.origin.height)
        self.assertEqual(5, bst.origin.left.value)
        self.assertEqual(2, bst.origin.left.height)
        self.assertEqual(1, bst.origin.left.left.value)
        self.assertEqual(1, bst.origin.left.left.height)
        self.assertEqual(-1, bst.origin.left.left.left.value)
        self.assertEqual(0, bst.origin.left.left.left.height)
        self.assertEqual(None, bst.origin.right)
        """
        (3) Test inserting to cause imbalance tree on left
        final structure:
             10
            /  \
           1    12
                 \
                  13
                   \
                   14
                    \
                    15
        """
        bst = BinarySearchTree()
        for value in [10, 12, 13, 14, 15, 1]:
            bst.insert(bst.origin, value)
        self.assertEqual(6, bst.size)
        self.assertEqual(10, bst.origin.value)
        self.assertEqual(4, bst.origin.height)
        self.assertEqual(1, bst.origin.left.value)
        self.assertEqual(0, bst.origin.left.height)

        self.assertEqual(12, bst.origin.right.value)
        self.assertEqual(3, bst.origin.right.height)
        self.assertEqual(13, bst.origin.right.right.value)
        self.assertEqual(2, bst.origin.right.right.height)
        self.assertEqual(14, bst.origin.right.right.right.value)
        self.assertEqual(1, bst.origin.right.right.right.height)
        self.assertEqual(15, bst.origin.right.right.right.right.value)
        self.assertEqual(0, bst.origin.right.right.right.right.height)

        """
        (4) Test inserting to complex tree (no rotating)
        final structure:
                        10
                    /        \
                  7           19
                /             / \
               4            13   35
              /  \           \   /   
             1    6          17 25
        """
        bst = BinarySearchTree()
        for value in [10, 7, 4, 19, 35, 25, 13, 17, 1, 6]:
            bst.insert(bst.origin, value)

        self.assertEqual(10, bst.size)
        # Height 3
        self.assertEqual(10, bst.origin.value)
        self.assertEqual(3, bst.origin.height)

        # Height 2
        self.assertEqual(7, bst.origin.left.value)
        self.assertEqual(2, bst.origin.left.height)
        self.assertEqual(19, bst.origin.right.value)
        self.assertEqual(2, bst.origin.right.height)

        # Height 1
        self.assertEqual(4, bst.origin.left.left.value)
        self.assertEqual(1, bst.origin.left.left.height)
        self.assertEqual(13, bst.origin.right.left.value)
        self.assertEqual(1, bst.origin.right.left.height)
        self.assertEqual(35, bst.origin.right.right.value)
        self.assertEqual(1, bst.origin.right.right.height)

        # Height 0
        self.assertEqual(1, bst.origin.left.left.left.value)
        self.assertEqual(0, bst.origin.left.left.left.height)
        self.assertEqual(6, bst.origin.left.left.right.value)
        self.assertEqual(0, bst.origin.left.left.right.height)
        self.assertEqual(17, bst.origin.right.left.right.value)
        self.assertEqual(0, bst.origin.right.left.right.height)
        self.assertEqual(25, bst.origin.right.right.left.value)
        self.assertEqual(0, bst.origin.right.right.left.height)

    def test_remove_bst(self):
        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        # ensure empty tree is properly handled
        bst = BinarySearchTree()
        self.assertIsNone(bst.remove(bst.origin, 0))

        """
        (1) test removal all left side (not trigger rotation)
        initial structure:
            2
           / \
          1   3
         /     \
        0       4
        final structure (removing 1, 0):
            2
             \
              3
               \
                4
        """
        bst = BinarySearchTree()
        for value in [2, 1, 3, 0, 4]:
            bst.insert(bst.origin, value)
        self.assertEqual(5, bst.size)

        bst.remove(bst.origin, 1)  # one child removal
        self.assertEqual(0, bst.origin.left.value)

        bst.remove(bst.origin, 0)  # zero child removal, will need rebalancing
        self.assertEqual(3, bst.size)
        self.assertEqual(2, bst.origin.value)
        self.assertEqual(2, bst.origin.height)
        self.assertEqual(3, bst.origin.right.value)
        self.assertEqual(1, bst.origin.right.height)
        self.assertEqual(4, bst.origin.right.right.value)
        self.assertEqual(0, bst.origin.right.right.height)
        self.assertIsNone(bst.origin.left)

        """
        (2) test removal all right side (not trigger rotation)
        initial structure:
            3
           / \
          2   4
         /     \
        1       5
        final structure (removing 4, 5):
            3
           /
          2   
         /     
        1       
        """
        bst = BinarySearchTree()
        for value in [3, 2, 4, 1, 5]:
            bst.insert(bst.origin, value)

        bst.remove(bst.origin, 4)  # one child removal
        self.assertEqual(5, bst.origin.right.value)

        bst.remove(bst.origin, 5)  # zero child removal, will need rebalancing
        self.assertEqual(3, bst.size)
        self.assertEqual(3, bst.origin.value)
        self.assertEqual(2, bst.origin.height)
        self.assertEqual(2, bst.origin.left.value)
        self.assertEqual(1, bst.origin.left.height)
        self.assertEqual(1, bst.origin.left.left.value)
        self.assertEqual(0, bst.origin.left.left.height)
        self.assertIsNone(bst.origin.right)

        """
        (3) test simple 2-child removal
        initial structure:
          2
         / \
        1   3
        final structure (removing 2):
         1 
          \
           3
        """
        bst = BinarySearchTree()
        for value in [2, 1, 3]:
            bst.insert(bst.origin, value)

        # two child removal (predecessor is in the left subtree)
        bst.remove(bst.origin, 2)
        self.assertEqual(2, bst.size)
        self.assertEqual(1, bst.origin.value)
        self.assertEqual(1, bst.origin.height)
        self.assertEqual(3, bst.origin.right.value)
        self.assertEqual(0, bst.origin.right.height)
        self.assertIsNone(bst.origin.left)

        """
        (4) Removing from a tree with a single node:
           5
        final structure (removing 5):
           Nothing
        """
        bst = BinarySearchTree()
        bst.insert(bst.origin, 5)

        bst.remove(bst.origin, 5)
        self.assertEqual(0, bst.size)
        self.assertIsNone(bst.origin)

        """
        (5) test compounded 2-child removal
        initial structure:
              4
           /     \
          2       6
         / \     / \
        1   3   5   7
        intermediate structure (removing 2, 6):
            4
           / \
          1   5
           \   \
            3   7
        final structure (removing 4)
            3
           / \
          1   5
               \
                7        
        """
        bst = BinarySearchTree()
        for i in [4, 2, 6, 1, 3, 5, 7]:
            bst.insert(bst.origin, i)
        bst.remove(bst.origin, 2)  # two child removal
        self.assertEqual(1, bst.origin.left.value)

        bst.remove(bst.origin, 6)  # two child removal
        self.assertEqual(5, bst.origin.right.value)

        bst.remove(bst.origin, 4)  # two child removal
        self.assertEqual(4, bst.size)
        self.assertEqual(3, bst.origin.value)
        self.assertEqual(2, bst.origin.height)
        self.assertEqual(1, bst.origin.left.value)
        self.assertEqual(0, bst.origin.left.height)
        self.assertEqual(5, bst.origin.right.value)
        self.assertEqual(1, bst.origin.right.height)
        self.assertEqual(7, bst.origin.right.right.value)
        self.assertEqual(0, bst.origin.right.right.height)

        """
        (6) test removal of intermediate node with 1 children
        Initial structure:
                4
               / \
              3   6
             /   / \
            2   5   7
           / 
          0   
        Final structure (removing 3):
                4
               / \
              2   6
             /   / \
            0   5   7          
        """
        bst = BinarySearchTree()
        for i in [4, 6, 3, 2, 0, 5, 7]:
            bst.insert(bst.origin, i)
        bst.remove(bst.origin, 3)

        self.assertEqual(6, bst.size)
        self.assertEqual(4, bst.origin.value)
        self.assertEqual(2, bst.origin.height)

        self.assertEqual(2, bst.origin.left.value)
        self.assertEqual(1, bst.origin.left.height)
        self.assertEqual(4, bst.origin.left.parent.value)

        self.assertEqual(0, bst.origin.left.left.value)
        self.assertEqual(0, bst.origin.left.left.height)
        self.assertEqual(2, bst.origin.left.left.parent.value)

        self.assertEqual(6, bst.origin.right.value)
        self.assertEqual(1, bst.origin.right.height)
        self.assertEqual(4, bst.origin.right.parent.value)

        self.assertEqual(5, bst.origin.right.left.value)
        self.assertEqual(0, bst.origin.right.left.height)
        self.assertEqual(6, bst.origin.right.left.parent.value)

        self.assertEqual(7, bst.origin.right.right.value)
        self.assertEqual(0, bst.origin.right.right.height)
        self.assertEqual(6, bst.origin.right.right.parent.value)

        """
        (7) test removal of intermediate node with 2 children
        Initial structure:
                 7  
               /   \
              4     9
             / \   / \
            2  5   8  10
           / \  \        
          1   3  6
        Final structure (removing 4):
                  7  
               /    \
              3      9
             / \    / \
            2   5   8  10
           /     \
          1       6
        """
        bst = BinarySearchTree()
        for i in [7, 4, 9, 2, 5, 8, 10, 1, 3, 6]:
            bst.insert(bst.origin, i)
        a = str(bst)
        bst.remove(bst.origin, 4)

        self.assertEqual(9, bst.size)
        self.assertEqual(7, bst.origin.value)
        self.assertEqual(3, bst.origin.height)

        self.assertEqual(3, bst.origin.left.value)
        self.assertEqual(2, bst.origin.left.height)
        self.assertEqual(7, bst.origin.left.parent.value)

        self.assertEqual(2, bst.origin.left.left.value)
        self.assertEqual(1, bst.origin.left.left.height)
        self.assertEqual(3, bst.origin.left.left.parent.value)

        self.assertEqual(1, bst.origin.left.left.left.value)
        self.assertEqual(0, bst.origin.left.left.left.height)
        self.assertEqual(2, bst.origin.left.left.left.parent.value)

        self.assertEqual(5, bst.origin.left.right.value)
        self.assertEqual(1, bst.origin.left.right.height)
        self.assertEqual(3, bst.origin.left.right.parent.value)

        self.assertEqual(6, bst.origin.left.right.right.value)
        self.assertEqual(0, bst.origin.left.right.right.height)
        self.assertEqual(5, bst.origin.left.right.right.parent.value)

        self.assertEqual(9, bst.origin.right.value)
        self.assertEqual(1, bst.origin.right.height)
        self.assertEqual(7, bst.origin.right.parent.value)

        self.assertEqual(8, bst.origin.right.left.value)
        self.assertEqual(0, bst.origin.right.left.height)
        self.assertEqual(9, bst.origin.right.left.parent.value)

        self.assertEqual(10, bst.origin.right.right.value)
        self.assertEqual(0, bst.origin.right.right.height)
        self.assertEqual(9, bst.origin.right.right.parent.value)

    def test_search(self):

        # ensure empty tree is properly handled
        bst = BinarySearchTree()
        self.assertIsNone(bst.search(bst.origin, 0))

        """
        (1) search small basic tree
        tree structure
          1
         / \
        0   3
           / \
          2   4
        """
        bst = BinarySearchTree()
        numbers = [1, 0, 3, 2, 4]
        for num in numbers:
            bst.insert(bst.origin, num)
        # search existing numbers
        for num in numbers:
            node = bst.search(bst.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        # search non-existing numbers and ensure parent of where value would go is returned
        pairs = [(-1, 0), (0.5, 0), (5, 4), (2.5, 2),
                 (3.5, 4), (-1e5, 0), (1e5, 4)]
        for target, closest in pairs:
            node = bst.search(bst.origin, target)
            self.assertIsInstance(node, Node)
            self.assertEqual(closest, node.value)

        """(2) search large random tree"""
        random.seed(331)
        bst = BinarySearchTree()
        numbers = {random.randint(-1000, 1000) for _ in range(1000)}
        for num in numbers:
            bst.insert(bst.origin, num)
        for num in numbers:
            # search existing number
            node = bst.search(bst.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)

            # if this node is a leaf, search non-existing numbers around it
            # to ensure it is returned as the parent of where new insertions would go
            if node.left is None and node.right is None:
                node = bst.search(bst.origin, num + 0.1)
                self.assertIsInstance(node, Node)
                self.assertEqual(num, node.value)
                node = bst.search(bst.origin, num - 0.1)
                self.assertIsInstance(node, Node)
                self.assertEqual(num, node.value)




if __name__ == '__main__':
    unittest.main(verbosity=2)
