import solution
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(solution.branch_sums(tree), [15, 16, 18, 10, 11])

    def test_case_2(self):
        tree = BinaryTree(5).insert([3, 8, 2, 4, 7, 9])
        self.assertEqual(solution.branch_sums(tree), [10, 12, 20, 22])


class BinaryTree(solution.BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


if __name__ == "__main__":
    unittest.main()
