"""
Project 5
CSE 331 SS25 (Liu, Onsay)
tests.py
"""

import random
import types
import unittest

from solution import Node, AVLTree, KNNClassifier


class AVLTreeTests(unittest.TestCase):

    def test_rotate(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.right_rotate(avl.origin))
        self.assertIsNone(avl.left_rotate(avl.origin))

        """
        (1) test basic right
        initial structure:
            3
           /
          2
         /
        1
        final structure:
          2
         / \
        1   3
        """
        avl.origin = Node(3)
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.size = 3

        node = avl.right_rotate(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(2, node.value)

        # root has no parent
        self.assertEqual(2, avl.origin.value)
        self.assertIsNone(avl.origin.parent)

        # root left value and parent
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(avl.origin, avl.origin.left.parent)

        # left leaf should have no children
        self.assertIsNone(avl.origin.left.left)
        self.assertIsNone(avl.origin.left.right)

        # root right value and parent
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(avl.origin, avl.origin.right.parent)

        # right leaf should have no children
        self.assertIsNone(avl.origin.right.right)
        self.assertIsNone(avl.origin.right.left)

        """
        (2) test basic left
        initial structure:
        1
         \
          2
           \
            3
        final structure:
          2
         / \
        1   3
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.right = Node(2, parent=avl.origin)
        avl.origin.right.right = Node(3, parent=avl.origin.right)
        avl.size = 3

        node = avl.left_rotate(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(2, node.value)

        # root has no parent
        self.assertEqual(2, avl.origin.value)
        self.assertIsNone(avl.origin.parent)

        # root left value and parent
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(avl.origin, avl.origin.left.parent)

        # left leaf should have no children
        self.assertIsNone(avl.origin.left.left)
        self.assertIsNone(avl.origin.left.right)

        # root right value and parent
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(avl.origin, avl.origin.right.parent)

        # right leaf should have no children
        self.assertIsNone(avl.origin.right.right)
        self.assertIsNone(avl.origin.right.left)

        """
        (3) test intermediate right, rotating at origin
        initial structure:
              7
             / \
            3   10
           / \
          2   4
         /
        1 
        final structure:
            3
           / \
          2   7
         /   / \
        1   4   10
        """
        avl = AVLTree()
        avl.origin = Node(7)
        avl.origin.left = Node(3, parent=avl.origin)
        avl.origin.left.left = Node(2, parent=avl.origin.left)
        avl.origin.left.left.left = Node(1, parent=avl.origin.left.left)
        avl.origin.left.right = Node(4, parent=avl.origin.left)
        avl.origin.right = Node(10, parent=avl.origin)

        node = avl.right_rotate(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(3, node.value)

        self.assertEqual(3, avl.origin.value)
        self.assertIsNone(avl.origin.parent)

        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(avl.origin, avl.origin.left.parent)
        self.assertIsNone(avl.origin.left.right)

        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(avl.origin.left, avl.origin.left.left.parent)
        self.assertIsNone(avl.origin.left.left.left)
        self.assertIsNone(avl.origin.left.left.right)

        self.assertEqual(7, avl.origin.right.value)
        self.assertEqual(avl.origin, avl.origin.right.parent)

        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(avl.origin.right, avl.origin.right.left.parent)
        self.assertIsNone(avl.origin.right.left.left)
        self.assertIsNone(avl.origin.right.left.right)

        self.assertEqual(10, avl.origin.right.right.value)
        self.assertEqual(avl.origin.right, avl.origin.right.right.parent)
        self.assertIsNone(avl.origin.right.right.left)
        self.assertIsNone(avl.origin.right.right.right)

        """
        (4) test intermediate left, rotating at origin
        initial structure:
          7
         /  \
        3   10
           /   \
          9    11
                 \
                  12
        final structure:
        	10
           /  \
          7   11
         / \    \
        3   9    12
        """
        avl = AVLTree()
        avl.origin = Node(7)
        avl.origin.left = Node(3, parent=avl.origin)
        avl.origin.right = Node(10, parent=avl.origin)
        avl.origin.right.left = Node(9, parent=avl.origin.right)
        avl.origin.right.right = Node(11, parent=avl.origin.right)
        avl.origin.right.right.right = Node(12, parent=avl.origin.right.right)

        node = avl.left_rotate(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(10, node.value)

        self.assertEqual(10, avl.origin.value)
        self.assertIsNone(avl.origin.parent)
        # assert node10.value == 10 and not node10.parent

        self.assertEqual(7, avl.origin.left.value)
        self.assertEqual(avl.origin, avl.origin.left.parent)
        # assert node7.value == 7 and node7.parent == node10

        self.assertEqual(3, avl.origin.left.left.value)
        self.assertEqual(avl.origin.left, avl.origin.left.left.parent)
        self.assertIsNone(avl.origin.left.left.left)
        self.assertIsNone(avl.origin.left.left.right)
        # assert node3.value == 3 and node3.parent == node7 and not (
        #     node3.left or node3.right)

        self.assertEqual(9, avl.origin.left.right.value)
        self.assertEqual(avl.origin.left, avl.origin.left.right.parent)
        self.assertIsNone(avl.origin.left.right.left)
        self.assertIsNone(avl.origin.left.right.right)
        # assert node9.value == 9 and node9.parent == node7 and not (
        #     node9.left or node9.right)

        self.assertEqual(11, avl.origin.right.value)
        self.assertEqual(avl.origin, avl.origin.right.parent)
        self.assertIsNone(avl.origin.right.left)
        # assert node11.value == 11 and node11.parent == node10 and not node11.left

        self.assertEqual(12, avl.origin.right.right.value)
        self.assertEqual(avl.origin.right, avl.origin.right.right.parent)
        self.assertIsNone(avl.origin.right.right.left)
        self.assertIsNone(avl.origin.right.right.right)
        # assert node12.value == 12 and node12.parent == node11 and not (
        #     node12.left or node12.right)

        """
        (5) test advanced right, rotating not at origin
        initial structure:
        		10
        	   /  \
        	  5	   11
        	 / \     \
        	3	7    12
           / \
          2   4
         /
        1
        final structure:
              10
             /  \
            3    11
           / \     \
          2   5     12
         /   / \
        1   4   7
        """
        avl = AVLTree()
        avl.origin = Node(10)
        avl.origin.right = Node(11, parent=avl.origin)
        avl.origin.right.right = Node(12, parent=avl.origin.right)
        avl.origin.left = Node(5, parent=avl.origin)
        avl.origin.left.right = Node(7, parent=avl.origin.left)
        avl.origin.left.left = Node(3, parent=avl.origin.left)
        avl.origin.left.left.right = Node(4, parent=avl.origin.left.left)
        avl.origin.left.left.left = Node(2, parent=avl.origin.left.left)
        avl.origin.left.left.left.left = Node(
            1, parent=avl.origin.left.left.left)

        node = avl.right_rotate(avl.origin.left)
        self.assertIsInstance(node, Node)
        self.assertEqual(3, node.value)
        # checking origin of balanced tree to be 3

        self.assertEqual(10, avl.origin.value)
        self.assertIsNone(avl.origin.parent)
        # parent of node3 == node10

        self.assertEqual(3, avl.origin.left.value)
        self.assertEqual(avl.origin, avl.origin.left.parent)
        # checking node10 left child == node3

        self.assertEqual(2, avl.origin.left.left.value)
        self.assertEqual(avl.origin.left, avl.origin.left.left.parent)
        self.assertIsNone(avl.origin.left.left.right)
        # checking node3 left child == node2 and node2 parent == node3
        # node2.right == None

        self.assertEqual(5, avl.origin.left.right.value)
        self.assertEqual(avl.origin.left, avl.origin.left.right.parent)
        # checking node3 right child == node5 and node5 parent == node3

        self.assertEqual(1, avl.origin.left.left.left.value)
        self.assertEqual(avl.origin.left.left,
                         avl.origin.left.left.left.parent)
        self.assertIsNone(avl.origin.left.left.left.left)
        self.assertIsNone(avl.origin.left.left.left.right)
        # checking node1 == node2 left child and node1 parent == node2
        # checking if node1 is a leaf node

        self.assertEqual(4, avl.origin.left.right.left.value)
        self.assertEqual(avl.origin.left.right,
                         avl.origin.left.right.left.parent)
        self.assertIsNone(avl.origin.left.right.left.left)
        self.assertIsNone(avl.origin.left.right.left.right)
        # checking node4 == node5 left child and node4 parent == node 5
        # checking if node4 is a leaf node

        self.assertEqual(7, avl.origin.left.right.right.value)
        self.assertEqual(avl.origin.left.right,
                         avl.origin.left.right.right.parent)
        self.assertIsNone(avl.origin.left.right.right.left)
        self.assertIsNone(avl.origin.left.right.right.right)
        # checking node7 == node5 right child and node7 parent == node 5
        # checking if node7 is a leaf node

        self.assertEqual(11, avl.origin.right.value)
        self.assertEqual(avl.origin, avl.origin.right.parent)
        self.assertIsNone(avl.origin.right.left)
        # checking the node11 stayed in place with node11 parent == origin (node10)
        # checking node11 has no left child


        self.assertEqual(12, avl.origin.right.right.value)
        self.assertEqual(avl.origin.right, avl.origin.right.right.parent)
        self.assertIsNone(avl.origin.right.right.left)
        self.assertIsNone(avl.origin.right.right.right)
        # checking that node12 stayed in place with node12 parent == node11
        # checking that node12 is still a leaf node

        """
        (6) test advanced left, rotating not at origin
        initial structure:
        	3
           / \
          2   10
         /   /  \
        1   5   12
               /  \
              11   13
                     \
                      14
        final structure:
        	3
           / \
          2   12
         /   /  \
        1   10   13
           /  \    \
          5   11   14
        """
        avl = AVLTree()
        avl.origin = Node(3)
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.right = Node(10, parent=avl.origin)
        avl.origin.right.left = Node(5, parent=avl.origin.right)
        avl.origin.right.right = Node(12, parent=avl.origin.right)
        avl.origin.right.right.left = Node(11, parent=avl.origin.right.right)
        avl.origin.right.right.right = Node(13, parent=avl.origin.right.right)
        avl.origin.right.right.right.right = Node(
            14, parent=avl.origin.right.right.right)


        node = avl.left_rotate(avl.origin.right)
        self.assertIsInstance(node, Node)
        self.assertEqual(12, node.value)
        # check after the rotation that the node given back is node12

        self.assertEqual(3, avl.origin.value)
        self.assertIsNone(avl.origin.parent)
        # check that the origin remains node3

        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(avl.origin, avl.origin.left.parent)
        self.assertIsNone(avl.origin.left.right)
        # check that node2 did not move
        # node2 == origin left child and node2 parent == origin
        # check that node2 should not have a right child

        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(avl.origin.left, avl.origin.left.left.parent)
        self.assertIsNone(avl.origin.left.left.left)
        self.assertIsNone(avl.origin.left.left.right)
        # check that node1 did not move either
        # node1 == node2 left child and node1 parent == node2
        # check that node1 is a leaf node as well

        self.assertEqual(12, avl.origin.right.value)
        self.assertEqual(avl.origin, avl.origin.right.parent)
        # check that origin right == node12

        self.assertEqual(10, avl.origin.right.left.value)
        self.assertEqual(avl.origin.right, avl.origin.right.left.parent)
        # check that node12 left == node10

        self.assertEqual(5, avl.origin.right.left.left.value)
        self.assertEqual(avl.origin.right.left,
                         avl.origin.right.left.left.parent)
        self.assertIsNone(avl.origin.right.left.left.left)
        self.assertIsNone(avl.origin.right.left.left.right)
        # check that node5 == node10 left child
        # node5 should also be a leaf node

        self.assertEqual(11, avl.origin.right.left.right.value)
        self.assertEqual(avl.origin.right.left,
                         avl.origin.right.left.right.parent)
        self.assertIsNone(avl.origin.right.left.right.left)
        self.assertIsNone(avl.origin.right.left.right.right)
        # check that node11 == node10 right child
        # node11 should also be a leaf node

        self.assertEqual(13, avl.origin.right.right.value)
        self.assertEqual(avl.origin.right, avl.origin.right.right.parent)
        self.assertIsNone(avl.origin.right.right.left)
        # check that node13 == node12 right child and should have no
        # left child

        self.assertEqual(14, avl.origin.right.right.right.value)
        self.assertEqual(avl.origin.right.right,
                         avl.origin.right.right.right.parent)
        self.assertIsNone(avl.origin.right.right.right.left)
        self.assertIsNone(avl.origin.right.right.right.right)
        # check that node14 == node13 right child
        # node14 should also be a leaf node

    def test_balance_factor(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertEqual(0, avl.balance_factor(avl.origin))

        """
        (1) test on balanced tree
        structure:
          2
         / \
        1   3
        """
        avl.origin = Node(2)
        avl.origin.height = 1
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 0
        avl.size = 3

        self.assertEqual(0, avl.balance_factor(avl.origin))
        self.assertEqual(0, avl.balance_factor(avl.origin.left))
        self.assertEqual(0, avl.balance_factor(avl.origin.right))

        """
        (2) test on unbalanced left
        structure:
            3
           /
          2
         /
        1
        """
        avl = AVLTree()
        avl.origin = Node(3)
        avl.origin.height = 2
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 1
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.size = 3

        self.assertEqual(2, avl.balance_factor(avl.origin))
        self.assertEqual(1, avl.balance_factor(avl.origin.left))
        self.assertEqual(0, avl.balance_factor(avl.origin.left.left))

        """
        (2) test on unbalanced right
        structure:
        1
         \
          2
           \
            3
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.height = 2
        avl.origin.right = Node(2, parent=avl.origin)
        avl.origin.right.height = 1
        avl.origin.right.right = Node(3, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.size = 3

        self.assertEqual(-2, avl.balance_factor(avl.origin))
        self.assertEqual(-1, avl.balance_factor(avl.origin.right))
        self.assertEqual(0, avl.balance_factor(avl.origin.right.right))

    def test_rebalance(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.rebalance(avl.origin))

        """
        (1) test balanced tree (do nothing)
        initial and final structure:
          2
         / \
        1   3
        since pointers are already tested in rotation testcase, only check values and heights
        """
        avl.origin = Node(2)
        avl.origin.height = 1
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 0
        avl.size = 3

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(2, node.value)

        self.assertEqual(2, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (2) test left-left rebalance
        initial structure:
            4
           /
          2
         / \
        1   3
        final structure:
          2
         / \
        1   4
           /
          3
        """
        avl = AVLTree()
        avl.origin = Node(4)
        avl.origin.height = 2
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 1
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.origin.left.right = Node(3, parent=avl.origin.left)
        avl.origin.left.right.height = 0
        avl.size = 4

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(2, node.value)

        self.assertEqual(2, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(3, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)

        """
        (3) test right-right rebalance
        initial structure:
        1
         \
          3
         /  \
        2    4
        final structure:
          3
         / \
        1   4
         \
          2
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.height = 2
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 1
        avl.origin.right.right = Node(4, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.origin.right.left = Node(2, parent=avl.origin.right)
        avl.origin.right.left.height = 0
        avl.size = 4

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(3, node.value)

        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.assertEqual(2, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        """
        (4) test left-right rebalance
        initial structure:
            5
           / \
          2   6
         / \
        1   3
             \
              4
        intermediate structure:
              5
             / \
            3   6
           / \
          2   4
         /
        1
        final structure:
            3 
           / \
          2   5
         /   / \
        1   4   6
        """
        avl = AVLTree()
        avl.origin = Node(5)
        avl.origin.height = 3
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 2
        avl.origin.right = Node(6, parent=avl.origin)
        avl.origin.right.height = 0
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.origin.left.right = Node(3, parent=avl.origin.left)
        avl.origin.left.right.height = 1
        avl.origin.left.right.right = Node(4, parent=avl.origin.left.right)
        avl.origin.left.right.right.height = 0

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(3, node.value)

        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (5) test right-left rebalance
        initial structure:
          2
         / \
        1   5
           / \
          4   6
         /
        3
        intermediate structure:
          2
         / \
        1   4
           / \
          3   5
               \
                6
        final structure:
            4 
           / \
          2   5
         / \   \
        1   3   6
        """
        avl = AVLTree()
        avl.origin = Node(2)
        avl.origin.height = 3
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(5, parent=avl.origin)
        avl.origin.right.height = 2
        avl.origin.right.left = Node(4, parent=avl.origin.right)
        avl.origin.right.left.height = 1
        avl.origin.right.right = Node(6, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.origin.right.left.left = Node(3, parent=avl.origin.right.left)
        avl.origin.right.left.left.height = 0

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)
        self.assertEqual(4, node.value)

        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

    def check_parent_relation(self, current: Node, isRoot: bool = False):
        if current is None:
            return
        # Check correct assigning of parents
        if isRoot:
            self.assertIs(current.parent, None)
        if current.left:
            self.assertIs(current, current.left.parent)
            self.check_parent_relation(current.left)
        if current.right:
            self.assertIs(current, current.right.parent)
            self.check_parent_relation(current.right)

    def test_insert(self):

        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        avl = AVLTree()
        """
        (1) test insertion causing right-right rotation
        final structure
          1
         / \
        0   3
           / \
          2   4
        """
        for value in range(5):
            node = avl.insert(avl.origin, value)
            self.assertIsInstance(node, Node)

        self.assertEqual(5, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(0, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(2, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(4, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.check_parent_relation(avl.origin, True)

        """
        (2) test insertion with a value already existing in the tree.
        """
        for value in range(4, -1, -1):
            node = avl.insert(avl.origin, value)
            self.assertIsInstance(node, Node)
        self.assertEqual(5, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(0, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(2, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(4, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.assertIsNone(avl.origin.left.left)
        self.assertIsNone(avl.origin.left.right)
        self.assertIsNone(avl.origin.right.left.left)
        self.assertIsNone(avl.origin.right.left.right)
        self.assertIsNone(avl.origin.right.right.left)
        self.assertIsNone(avl.origin.right.right.right)
        self.check_parent_relation(avl.origin, True)

        """
        (3) test insertion causing left-left rotation
        final structure
            3
           / \
          1   4
         / \
        0   2
        """
        avl = AVLTree()
        for value in range(4, -1, -1):
            node = avl.insert(avl.origin, value)
            self.assertIsInstance(node, Node)
        self.assertEqual(5, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(2, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.check_parent_relation(avl.origin, True)

        """
        (4) test insertion (with duplicates) causing left-right rotation
        initial structure:
            5
           / \
          2   6
         / \
        1   3
             \
              4
        final structure:
            3 
           / \
          2   5
         /   / \
        1   4   6
        """
        avl = AVLTree()
        for value in [5, 2, 6, 1, 3] * 2 + [4]:
            node = avl.insert(avl.origin, value)
            self.assertIsInstance(node, Node)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.check_parent_relation(avl.origin, True)

        """
        (5) test insertion (with duplicates) causing right-left rotation
        initial structure:
          2
         / \
        1   5
           / \
          4   6
         /
        3
        final structure:
            4 
           / \
          2   5
         / \   \
        1   3   6
        """
        avl = AVLTree()
        for value in [2, 1, 5, 4, 6] * 2 + [3]:
            node = avl.insert(avl.origin, value)
            self.assertIsInstance(node, Node)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.check_parent_relation(avl.origin, True)

    def test_height(self):

        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        avl = AVLTree()
        """
        (1) test height after causing right-right rotation
        final structure
          1
         / \
        0   3
           / \
          2   4
        """
        for value in range(5):
            node = avl.insert(avl.origin, value)
            self.assertIsInstance(node, Node)

        self.assertEqual(2, avl.height(avl.origin))
        self.assertEqual(0, avl.height(avl.origin.left))
        self.assertEqual(1, avl.height(avl.origin.right))
        self.assertEqual(0, avl.height(avl.origin.right.left))
        self.assertEqual(0, avl.height(avl.origin.right.right))

        """
        (2) test height with a value already existing in the tree.
        """
        for value in range(4, -1, -1):
            node = avl.insert(avl.origin, value)
            self.assertIsInstance(node, Node)
        self.assertEqual(2, avl.height(avl.origin))
        self.assertEqual(0, avl.height(avl.origin.left))
        self.assertEqual(1, avl.height(avl.origin.right))
        self.assertEqual(0, avl.height(avl.origin.right.left))
        self.assertEqual(0, avl.height(avl.origin.right.right))

        """
        (3) test height after removal causing left-right rotation
        initial structure:
              5
             / \
            2   6
           / \   \
          1   3   7
         /     \
        0       4
        final structure (removing 1, 6):
            3 
           / \
          2   5
         /   / \
        0   4   7
        """
        avl = AVLTree()
        for value in [5, 2, 6, 1, 3, 7, 0, 4]:
            avl.insert(avl.origin, value)

        avl.remove(avl.origin, 1)  # one child removal
        self.assertEqual(0, avl.origin.left.left.value)

        avl.remove(avl.origin, 6)  # one child removal, will need rebalancing

        self.assertEqual(2, avl.height(avl.origin))
        self.assertEqual(1, avl.height(avl.origin.left))
        self.assertEqual(1, avl.height(avl.origin.right))
        self.assertEqual(0, avl.height(avl.origin.left.left))
        self.assertEqual(0, avl.height(avl.origin.right.left))
        self.assertEqual(0, avl.height(avl.origin.right.right))

    def test_remove(self):
        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.remove(avl.origin, 0))

        """
        (1) test removal causing right-right rotation
        initial structure:
            2
           / \
          1   3
         /     \
        0       4
        final structure (removing 1, 0):
          3 
         / \
        2   4
        """
        avl = AVLTree()
        for value in [2, 1, 3, 0, 4]:
            avl.insert(avl.origin, value)

        avl.remove(avl.origin, 1)  # one child removal
        self.assertEqual(0, avl.origin.left.value)

        avl.remove(avl.origin, 0)  # zero child removal, will need rebalancing
        self.assertEqual(3, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.check_parent_relation(avl.origin, True)

        """
        (2) test removal causing left-left rotation
        initial structure:
            3
           / \
          2   4
         /     \
        1       5
        final structure (removing 4, 5):
          2 
         / \
        1   3
        """
        avl = AVLTree()
        for value in [3, 2, 4, 1, 5]:
            avl.insert(avl.origin, value)

        avl.remove(avl.origin, 4)  # one child removal
        self.assertEqual(5, avl.origin.right.value)

        avl.remove(avl.origin, 5)  # zero child removal, will need rebalancing
        self.assertEqual(3, avl.size)
        self.assertEqual(2, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.check_parent_relation(avl.origin, True)


        """
        (3) test removal causing left-right rotation
        initial structure:
              5
             / \
            2   6
           / \   \
          1   3   7
         /     \
        0       4
        final structure (removing 1, 6):
            3 
           / \
          2   5
         /   / \
        0   4   7
        """
        avl = AVLTree()
        for value in [5, 2, 6, 1, 3, 7, 0, 4]:
            avl.insert(avl.origin, value)

        avl.remove(avl.origin, 1)  # one child removal
        self.assertEqual(0, avl.origin.left.left.value)

        avl.remove(avl.origin, 6)  # one child removal, will need rebalancing

        self.assertEqual(6, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        self.assertIs(avl.origin.parent, None)
        self.assertIs(avl.origin, avl.origin.left.parent)
        self.assertIs(avl.origin, avl.origin.right.parent)
        self.check_parent_relation(avl.origin, True)

        """
        (4) test removal causing right-left rotation
        initial structure:
            2
           / \
          1   5
         /   / \
        0   4   6
           /     \
          3       7
        final structure (removing 6, 1):
            4 
           / \
          2   5
         / \   \
        0   3   7
        """
        avl = AVLTree()
        for value in [2, 1, 5, 0, 4, 6, 3, 7]:
            avl.insert(avl.origin, value)

        avl.remove(avl.origin, 6)  # one child removal
        self.assertEqual(7, avl.origin.right.right.value)

        avl.remove(avl.origin, 1)  # one child removal, will need rebalancing
        self.assertEqual(6, avl.size)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.check_parent_relation(avl.origin, True)

        """
        (5) test simple 2-child removal
        initial structure:
          2
         / \
        1   3
        final structure (removing 2):
         1 
          \
           3
        """
        avl = AVLTree()
        for value in [2, 1, 3]:
            avl.insert(avl.origin, value)
        avl.remove(avl.origin, 2)  # two child removal
        self.assertEqual(2, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.check_parent_relation(avl.origin, True)

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
        avl = AVLTree()
        for value in [4, 2, 6, 1, 3, 5, 7]:
            avl.insert(avl.origin, value)

        avl.remove(avl.origin, 2)  # two child removal
        self.assertEqual(1, avl.origin.left.value)

        avl.remove(avl.origin, 6)  # two child removal
        self.assertEqual(5, avl.origin.right.value)

        avl.remove(avl.origin, 4)  # two child removal
        self.assertEqual(4, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.check_parent_relation(avl.origin, True)

        """
        (6) Removing from a tree with a single node:
           5
        final structure (removing 5):
           Nothing
        """
        avl = AVLTree()
        avl.insert(avl.origin, 5)

        avl.remove(avl.origin, 5)
        self.assertEqual(0, avl.size)
        self.assertIsNone(avl.origin)
        self.check_parent_relation(avl.origin, True)

    def test_min(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.min(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        min_node = avl.min(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertEqual(0, min_node.value)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        min_node = avl.min(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertEqual(-100, min_node.value)

        """(3) large random tree"""
        random.seed(331)
        avl = AVLTree()
        numbers = [random.randint(-1000, 1000) for _ in range(1000)]
        for num in numbers:
            avl.insert(avl.origin, num)
        min_node = avl.min(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertEqual(min(numbers), min_node.value)

    def test_max(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.max(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        max_node = avl.max(avl.origin)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(9, max_node.value)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        max_node = avl.max(avl.origin)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(100, max_node.value)

        """(3) large random tree"""
        random.seed(331)
        avl = AVLTree()
        numbers = [random.randint(-1000, 1000) for _ in range(1000)]
        for num in numbers:
            avl.insert(avl.origin, num)
        max_node = avl.max(avl.origin)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(max(numbers), max_node.value)

    def test_search(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.search(avl.origin, 0))

        """
        (1) search small basic tree
        tree structure
          1
         / \
        0   3
           / \
          2   4
        """
        avl = AVLTree()
        numbers = [1, 0, 3, 2, 4]
        for num in numbers:
            avl.insert(avl.origin, num)
        # search existing numbers
        for num in numbers:
            node = avl.search(avl.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        # search non-existing numbers and ensure parent of where value would go is returned
        pairs = [(-1, 0), (0.5, 0), (5, 4), (2.5, 2),
                 (3.5, 4), (-1e5, 0), (1e5, 4)]
        for target, closest in pairs:
            node = avl.search(avl.origin, target)
            self.assertIsInstance(node, Node)
            self.assertEqual(closest, node.value)

        """(2) search large random tree"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(1000)}
        for num in numbers:
            avl.insert(avl.origin, num)
        for num in numbers:
            # search existing number
            node = avl.search(avl.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)

            # if this node is a leaf, search non-existing numbers around it
            # to ensure it is returned as the parent of where new insertions would go
            if node.left is None and node.right is None:
                node = avl.search(avl.origin, num + 0.1)
                self.assertIsInstance(node, Node)
                self.assertEqual(num, node.value)
                node = avl.search(avl.origin, num - 0.1)
                self.assertIsInstance(node, Node)
                self.assertEqual(num, node.value)

    def test_inorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.inorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(10))
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(-100, 101))
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(80)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = sorted(numbers)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(4) Testing tree is iterable. Hint: Implement the __iter__ function."""
        for expected_val, actual in zip(expected, avl):
            self.assertEqual(expected_val, actual.value)

    def test_preorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.preorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [3, 1, 0, 2, 7, 5, 4, 6, 8, 9]
        # avl.visualize("test2.svg")
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 21):
            avl.insert(avl.origin, i)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-5, -13, -17, -19, -20, -18, -15, -16, -14, -9, -11,
                    -12, -10, -7, -8, -6, 11, 3, -1, -3, -4, -2, 1, 0, 2,
                    7, 5, 4, 6, 9, 8, 10, 15, 13, 12, 14, 17, 16, 19, 18,
                    20]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(80)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [527, 33, -493, -834, -933, -954, -918, -655, -720,
                    -789, -705, -650, -529, -165, -343, -422, -434,
                    -359, -312, -324, -269, -113, -142, -148, -116, -43,
                    -89, -26, 327, 220, 108, 77, 44, 101, 193, 113,
                    194, 274, 251, 224, 268, 294, 283, 316, 454, 362, 358,
                    333, 360, 431, 411, 446, 486, 485, 498, 503,
                    711, 574, 565, 529, 571, 675, 641, 687, 832, 776, 733,
                    720, 775, 784, 782, 802, 914, 860, 843, 888,
                    966, 944, 975]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_postorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.postorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [0, 2, 1, 4, 6, 5, 9, 8, 7, 3]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 20):
            avl.insert(avl.origin, i)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-20, -18, -19, -16, -14, -15, -17, -12, -10, -11, -8, -6, -7, -9,
                    -13, -4, -2, -3, 0, 2, 1, -1, 4, 6, 5, 8, 10, 9, 7, 3, 12, 14, 13,
                    16, 19, 18, 17, 15, 11, -5]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(80)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-954, -918, -933, -789, -705, -720, -529, -650, -655, -834, -434, -359, -422, -324, -269, -312,
                    -343, -148, -116, -142, -89, -26, -43, -113, -
                    165, -493, 44, 101, 77, 113, 194, 193, 108, 224,
                    268, 251, 283, 316, 294, 274, 220, 333, 360, 358, 411, 446, 431, 362, 485, 503, 498, 486, 454,
                    327, 33, 529, 571, 565, 641, 687, 675, 574, 720, 775, 733, 782, 802, 784, 776, 843, 888, 860,
                    944, 975, 966, 914, 832, 711, 527]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_levelorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.levelorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [3, 1, 7, 0, 2, 5, 8, 4, 6, 9]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 20):
            avl.insert(avl.origin, i)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-5, -13, 11, -17, -9, 3, 15, -19, -15, -11, -7, -1, 7, 13, 17, -20, -18,
                    -16, -14, -12, -10, -8, -6, -3, 1, 5, 9, 12, 14, 16, 18, -4, -2, 0, 2,
                    4, 6, 8, 10, 19]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(80)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [527, 33, 711, -493, 327, 574, 832, -834, -165, 220, 454,
                    565, 675, 776, 914, -933, -655, -343, -113, 108, 274,
                    362, 486, 529, 571, 641, 687, 733, 784, 860, 966, -954,
                    -918, -720, -650, -422, -312, -142, -43, 77, 193, 251,
                    294, 358, 431, 485, 498, 720, 775, 782, 802, 843, 888,
                    944, 975, -789, -705, -529, -434, -359, -324, -269, -148,
                    -116, -89, -26, 44, 101, 113, 194, 224, 268, 283, 316, 333,
                    360, 411, 446, 503]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_AVL_comprehensive(self):

        # visualize some of test in this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        # ensure empty tree is properly handled
        """
        First part, inserting and removing without rotation

        insert without any rotation (inserting 5, 0, 10):
          5
         / \
        1   10
        """

        def check_node_properties(current: Node, value: int = 0, height: int = 0, balance: int = 0):
            if value is None:
                self.assertIsNone(current)
                return
            self.assertEqual(value, current.value)
            self.assertEqual(height, current.height)
            self.assertEqual(balance, avl.balance_factor(current))

        avl = AVLTree()
        avl.insert(avl.origin, 5)
        avl.insert(avl.origin, 1)
        avl.insert(avl.origin, 10)
        self.assertEqual(3, avl.size)
        self.assertEqual(1, avl.min(avl.origin).value)
        self.assertEqual(10, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=5, height=1, balance=0)
        check_node_properties(avl.origin.left, value=1, height=0, balance=0)
        check_node_properties(avl.origin.right, value=10, height=0, balance=0)
        """
        Current AVL tree:
          5
         / \
        1   10
        After Removing 5:
          1
           \
            10
        """
        avl.remove(avl.origin, 5)
        self.assertEqual(2, avl.size)
        self.assertEqual(1, avl.min(avl.origin).value)
        self.assertEqual(10, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=1, height=1, balance=-1)
        check_node_properties(avl.origin.left, value=None)
        check_node_properties(avl.origin.right, value=10, height=0, balance=0)
        """
        Current AVL tree:
          1
            \
            10
        After inserting 0, 20:
          1
         /  \
        0   10
              \
               20
        """
        avl.insert(avl.origin, 0)
        avl.insert(avl.origin, 20)
        self.assertEqual(4, avl.size)
        self.assertEqual(0, avl.min(avl.origin).value)
        self.assertEqual(20, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=1, height=2, balance=-1)
        check_node_properties(avl.origin.left, value=0, height=0, balance=0)
        check_node_properties(avl.origin.right, value=10, height=1, balance=-1)
        check_node_properties(avl.origin.right.right,
                              value=20, height=0, balance=0)

        """
        Current AVL tree:
          1
         /  \
        0   10
              \
               20
        After removing 20, inserting -20 and inserting 5
             1
            /  \
           0   10
          /   /
        -20  5
        """
        avl.remove(avl.origin, 20)
        avl.insert(avl.origin, -20)
        avl.insert(avl.origin, 5)
        self.assertEqual(5, avl.size)
        self.assertEqual(-20, avl.min(avl.origin).value)
        self.assertEqual(10, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=1, height=2, balance=0)
        check_node_properties(avl.origin.left, value=0, height=1, balance=1)
        check_node_properties(avl.origin.left.left,
                              value=-20, height=0, balance=0)
        check_node_properties(avl.origin.right, value=10, height=1, balance=1)
        check_node_properties(avl.origin.right.left,
                              value=5, height=0, balance=0)

        """
        Second part, inserting and removing with rotation

        inserting 5, 10:
          5
           \
            10
        """
        avl = AVLTree()
        avl.insert(avl.origin, 5)
        avl.insert(avl.origin, 10)
        self.assertEqual(2, avl.size)
        self.assertEqual(5, avl.min(avl.origin).value)
        self.assertEqual(10, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=5, height=1, balance=-1)
        check_node_properties(avl.origin.right, value=10, height=0, balance=0)
        """
        Current AVL tree:
          5
           \
            10
        After inserting 8, 9, 12
           8
         /   \
        5    10
            /  \
           9   12
        """
        avl.insert(avl.origin, 8)
        avl.insert(avl.origin, 9)
        avl.insert(avl.origin, 12)
        self.assertEqual(5, avl.size)
        self.assertEqual(5, avl.min(avl.origin).value)
        self.assertEqual(12, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=2, balance=-1)
        check_node_properties(avl.origin.right, value=10, height=1, balance=0)
        check_node_properties(avl.origin.right.left,
                              value=9, height=0, balance=0)
        check_node_properties(avl.origin.right.right,
                              value=12, height=0, balance=0)
        check_node_properties(avl.origin.left, value=5, height=0, balance=0)

        """
        Current AVL tree:
           8
         /   \
        5    10
            /  \
           9   12
        After inserting 3, 1, 2
               8
           /       \
          3        10
         /  \     /   \
        1    5   9    12
          \
           2
        """
        avl.insert(avl.origin, 3)
        avl.insert(avl.origin, 1)
        avl.insert(avl.origin, 2)
        self.assertEqual(8, avl.size)
        self.assertEqual(1, avl.min(avl.origin).value)
        self.assertEqual(12, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=3, balance=1)
        check_node_properties(avl.origin.right, value=10, height=1, balance=0)
        check_node_properties(avl.origin.right.left,
                              value=9, height=0, balance=0)
        check_node_properties(avl.origin.right.right,
                              value=12, height=0, balance=0)
        check_node_properties(avl.origin.left, value=3, height=2, balance=1)
        check_node_properties(avl.origin.left.left,
                              value=1, height=1, balance=-1)
        check_node_properties(avl.origin.left.left.right,
                              value=2, height=0, balance=0)
        check_node_properties(avl.origin.left.right,
                              value=5, height=0, balance=0)
        """
        Current AVL tree:
               8
           /       \
          3        10
         /  \     /   \
        1    5   9    12
          \
           2
        After removing 5
               8
           /       \
          2        10
         /  \     /   \
        1    3   9    12
        """
        avl.remove(avl.origin, 5)
        self.assertEqual(7, avl.size)
        self.assertEqual(1, avl.min(avl.origin).value)
        self.assertEqual(12, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=2, balance=0)
        check_node_properties(avl.origin.right, value=10, height=1, balance=0)
        check_node_properties(avl.origin.right.left,
                              value=9, height=0, balance=0)
        check_node_properties(avl.origin.right.right,
                              value=12, height=0, balance=0)
        check_node_properties(avl.origin.left, value=2, height=1, balance=0)
        check_node_properties(avl.origin.left.left,
                              value=1, height=0, balance=0)
        check_node_properties(avl.origin.left.right,
                              value=3, height=0, balance=0)
        """
        Current AVL tree:
              8
           /     \
          2      10
         /  \   /   \
        1    3 9    12
        After inserting 5, 13, 0, 7, 20
               8
            /       \
           2         10
          /  \      /   \
         1    5     9    13
        /    / \        /  \
        0   3   7     12    20
        """
        avl.insert(avl.origin, 5)
        avl.insert(avl.origin, 13)
        avl.insert(avl.origin, 0)
        avl.insert(avl.origin, 7)
        avl.insert(avl.origin, 20)
        self.assertEqual(12, avl.size)
        self.assertEqual(0, avl.min(avl.origin).value)
        self.assertEqual(20, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=3, balance=0)

        check_node_properties(avl.origin.right, value=10, height=2, balance=-1)
        check_node_properties(avl.origin.right.left,
                              value=9, height=0, balance=0)
        check_node_properties(avl.origin.right.right,
                              value=13, height=1, balance=0)
        check_node_properties(avl.origin.right.right.right,
                              value=20, height=0, balance=0)
        check_node_properties(avl.origin.right.right.left,
                              value=12, height=0, balance=0)

        check_node_properties(avl.origin.left, value=2, height=2, balance=0)
        check_node_properties(avl.origin.left.left,
                              value=1, height=1, balance=1)
        check_node_properties(avl.origin.left.left.left,
                              value=0, height=0, balance=0)
        check_node_properties(avl.origin.left.right,
                              value=5, height=1, balance=-0)
        check_node_properties(avl.origin.left.right.right,
                              value=7, height=0, balance=0)
        check_node_properties(avl.origin.left.right.left,
                              value=3, height=0, balance=0)

        """
        Current AVL tree:
               8
            /       \
           2         10
          /  \      /   \
         1    5     9    13
        /    / \        /  \
        0   3   7     12    20
        After removing 1, 9
               8
            /       \
           2         13
          /  \      /   \
         0    5   10     20
             / \     \    
             3   7    12
        """
        avl.remove(avl.origin, 1)
        avl.remove(avl.origin, 9)
        self.assertEqual(10, avl.size)
        self.assertEqual(0, avl.min(avl.origin).value)
        self.assertEqual(20, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=3, balance=0)

        check_node_properties(avl.origin.right, value=13, height=2, balance=1)
        check_node_properties(avl.origin.right.left,
                              value=10, height=1, balance=-1)
        check_node_properties(avl.origin.right.left.right,
                              value=12, height=0, balance=0)
        check_node_properties(avl.origin.right.right,
                              value=20, height=0, balance=0)

        check_node_properties(avl.origin.left, value=2, height=2, balance=-1)
        check_node_properties(avl.origin.left.left,
                              value=0, height=0, balance=0)
        check_node_properties(avl.origin.left.right,
                              value=5, height=1, balance=-0)
        check_node_properties(avl.origin.left.right.right,
                              value=7, height=0, balance=0)
        check_node_properties(avl.origin.left.right.left,
                              value=3, height=0, balance=0)

class KNNClassifierTests(unittest.TestCase):
    def test_train(self):
        """(1) Test basic scenario"""
        data = [(0.1, "L"), (0.2, "L"), (0.6, "W"), (0.7, "W"), (0.5, "W")]
        classifier = KNNClassifier(k=2)
        classifier.train(data)
        self.assertEqual(2, classifier.tree.height(classifier.tree.origin))
        self.assertEqual([value[0] for value in sorted(data)], [node.value for node in classifier.tree], )
        self.assertEqual(
            [value[1] for value in sorted(data)],
            [node.data for node in classifier.tree],
        )

        """(2) Test tied nodes should still be added in train"""
        points = [i/10 for i in range(0,11) if i != 5]
        labels = ["W"] * 5 + ["L"]*5
        data = list(zip(points, labels))
        classifier = KNNClassifier()
        classifier.train(data)
        self.assertEqual(3, classifier.tree.height(classifier.tree.origin))
        self.assertEqual([value[0] for value in sorted(data)], [node.value for node in classifier.tree])
        self.assertEqual(
            [value[1] for value in sorted(data)],
            [node.data for node in classifier.tree],
        )

        """(3) Testing empty test data"""
        data = []
        classifier = KNNClassifier(k=2)
        classifier.train(data)
        self.assertEqual(-1, classifier.tree.height(classifier.tree.origin), )
        self.assertEqual([value[0] for value in sorted(data)], [node.value for node in classifier.tree])
        self.assertEqual(
            [value[1] for value in sorted(data)],
            [node.data for node in classifier.tree],
        )

    def test_get_k_neighbors(self):
        # Getting empty neighbors should not break
        data = []
        classifier = KNNClassifier(k=2)
        classifier.train(data)
        neighbors = classifier.get_k_neighbors(0.45)
        self.assertEqual([], neighbors)

        # Test basic scenario
        data = [(0.1, "L"), (0.2, "L"), (0.6, "W"), (0.7, "W"), (0.5, "W")]

        # A 0 neighbor scenario should not break
        classifier = KNNClassifier(k=0)
        classifier.train(data)
        neighbors = classifier.get_k_neighbors(0.1)
        self.assertEqual([], neighbors)

        # Simple scenario
        classifier = KNNClassifier(k=2)
        classifier.train(data)
        neighbors = classifier.get_k_neighbors(0.1)
        self.assertEqual([(0.1, 'L'), (0.2, 'L')], neighbors)

        neighbors = classifier.get_k_neighbors(0.45)
        self.assertEqual([(0.5, 'W'), (0.6, 'W')], neighbors)

        # Tied values should be ignored
        neighbors = classifier.get_k_neighbors(0.6)
        self.assertEqual([(0.6, 'W'), (0.2, 'L')], neighbors)

        # A k greater than the number of data points should not be a problem
        classifier = KNNClassifier(k=10)
        classifier.train(data)
        neighbors = classifier.get_k_neighbors(0.1)
        self.assertEqual([(0.1, 'L'), (0.2, 'L'), (0.5, 'W'), (0.6, 'W'), (0.7, 'W')], neighbors)

        # A more complex tie scenario
        points = [i/10 for i in range(0,11) if i != 5]
        labels = ["W"] * 5 + ["L"]*5
        data = list(zip(points, labels))
        classifier = KNNClassifier(5)
        classifier.train(data)
        neighbors = classifier.get_k_neighbors(0.5)
        # In this case all neighbors are tied, so should ignore them
        self.assertEqual([], neighbors)

        # Some of the outer neighbors should still be ignored as they are tied
        neighbors = classifier.get_k_neighbors(0.4)
        self.assertEqual([(0.4, 'W'), (0.3, 'W'), (0.9, 'L'), (1.0, 'L')], neighbors, )

        # Reversed sorted input
        data = [(0.7, "W"), (0.6, "W"), (0.5, "W"), (0.2, "L"), (0.1, "L")]
        classifier = KNNClassifier(k=2)
        classifier.train(data)
        neighbors = classifier.get_k_neighbors(0.61)
        self.assertEqual([(0.6, 'W'), (0.7, 'W')], neighbors)

    def test_calculate_best_fit(self):
        classifier = KNNClassifier(k=2)

        # Empty neighbors should return None
        neighbors = []
        result = classifier.calculate_best_fit(neighbors, 0.5)
        self.assertIsNone(result)

        # Single neighbor
        neighbors = [(0.3, "L")]
        result = classifier.calculate_best_fit(neighbors, 0.5)
        self.assertEqual("L", result)

        # Multiple neighbors with clear best fit
        neighbors = [(0.3, "L"), (0.4, "L"), (0.7, "W")]
        result = classifier.calculate_best_fit(neighbors, 0.5)
        self.assertEqual("L", result)

        # Multiple neighbors with different weights
        neighbors = [(0.2, "L"), (0.6, "W"), (0.9, "W")]
        result = classifier.calculate_best_fit(neighbors, 0.5)
        self.assertEqual("W", result)  # Higher weight due to proximity of both W's

        # Large dataset of neighbors
        neighbors = [(i / 100, "L" if i % 2 == 0 else "W") for i in range(1, 20)]
        result = classifier.calculate_best_fit(neighbors, 0.55)
        self.assertIn(result, ["L", "W"])  # Ensures stability for larger input

    def test_knn(self):
        """
        Testing specs examples
        """
        # Example 1
        data = [(0.1, "L"), (0.2, "L"), (0.6, "W"), (0.7, "W"), (0.5, "W")]
        classifier = KNNClassifier(k=2)
        classifier.train(data)
        self.assertEqual("W", classifier.classify(0.55))

        # Example 2
        data = [(0.1, "L"), (0.2, "L"), (0.6, "W"), (0.7, "W")]
        classifier = KNNClassifier()
        classifier.train(data)
        self.assertIsNone(classifier.classify(0.4))

        # Example 3
        data = [(0.1, "L"), (0.2, "L"), (0.6, "W"), (0.7, "W"), (0.5, "L")]
        classifier = KNNClassifier()
        classifier.train(data)
        self.assertEqual("L", classifier.classify(0.4))

        # Testing 4 closest neighbor
        data = [(0.18, "L"), (0.21, "L"), (0.29, "L"), (0.46, "L"),
        (0.49, "L"), (0.51, "W"), (0.53, "W"),
        (0.97, "W"), (0.98, "W"), (0.99, "W")]
        classifier = KNNClassifier()
        classifier.train(data)
        test_predictions = [0.1, 0.2, 0.5, 0.8, 0.9]
        expected = ["L", "L", "W", "W", "W"]
        actual = [classifier.classify(i) for i in test_predictions]
        self.assertEqual(expected, actual)

        # Testing 5 closest neighbors
        classifier = KNNClassifier(k=2)
        classifier.train(data)
        test_predictions = [0.1, 0.2, 0.5, 0.8, 0.9]
        expected = ["L", "L", "W", "W", "W"]
        actual = [classifier.classify(i) for i in test_predictions]
        self.assertEqual(expected, actual)

        # Testing 6 closest neighbors, weights make a difference here. Even if there are more neighbors for one classification.
        classifier = KNNClassifier(k=3)
        classifier.train(data)
        test_predictions = [0.1, 0.2, 0.5, 0.8, 0.9]
        expected = ["L", "L", "W", "W", "W"]
        actual = [classifier.classify(i) for i in test_predictions]
        self.assertEqual(expected, actual)

        # Testing 7 changing weights to affect classification
        data[2] = (0.43, "L")
        classifier = KNNClassifier(k=3)
        classifier.train(data)
        test_predictions = [0.1, 0.2, 0.5, 0.8, 0.9]
        expected = ["L", "L", "L", "W", "W"]
        actual = [classifier.classify(i) for i in test_predictions]
        self.assertEqual(expected, actual)
    
        # Testing 8 Test tied weights/distances
        points = [i/10 for i in range(0,11) if i != 5]
        labels = ["W"] * 5 + ["L"]*5
        data = list(zip(points, labels))
        classifier = KNNClassifier()
        classifier.train(data)
        self.assertIsNone(classifier.classify(0.5))

        classifier = KNNClassifier(k=3)
        classifier.train(data)
        self.assertIsNone(classifier.classify(0.5))

        classifier = KNNClassifier(k=4)
        classifier.train(data)
        self.assertIsNone(classifier.classify(0.5))

        # Testing 9 test from previous projects
        random.seed(331)
        L_images = [(random.random() / 2, "L") for _ in range(50)]
        W_images = [(random.random() / 2 + 0.5, "W") for _ in range(50)]
        data = L_images + W_images

        classifier = KNNClassifier()
        classifier.train(data)
        test_images = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]
        expected = ["L"] * 4 + ["W"] * 4
        actual = [classifier.classify(image) for image in test_images]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)
