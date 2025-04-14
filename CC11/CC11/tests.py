import unittest
from solution import Node, has_single_cycle



class TestDepthFirstSearch(unittest.TestCase):

    def test_example_1_original(self):
        graph = Node("A")
        graph.children = [Node("B"), Node("C"), Node("D")]
        graph.children[0].children = [Node("E"), Node("F")]
        graph.children[0].children[1].children = [Node("I"), Node("J")]
        graph.children[2].children = [Node("G"), Node("H")]
        graph.children[2].children[0].children = [Node("K")]

        result = graph.depth_first_search([])
        expected = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
        self.assertEqual(result, expected)

    def test_example_2(self):
        graph = Node("X")
        graph.children = [Node("Y"), Node("Z")]
        graph.children[0].children = [Node("P"), Node("Q")]

        result = graph.depth_first_search([])
        expected = ["X", "Y", "P", "Q", "Z"]
        self.assertEqual(result, expected)

    def test_example_3(self):
        graph = Node("M")
        graph.children = [Node("N")]
        graph.children[0].children = [Node("O"), Node("P")]
        graph.children[0].children[1].children = [Node("Q")]

        result = graph.depth_first_search([])
        expected = ["M", "N", "O", "P", "Q"]
        self.assertEqual(result, expected)

    def test_example_4(self):
        graph = Node("R")
        graph.children = [Node("S"), Node("T"), Node("U")]
        graph.children[1].children = [Node("V")]
        graph.children[1].children[0].children = [Node("W"), Node("X")]

        result = graph.depth_first_search([])
        expected = ["R", "S", "T", "V", "W", "X", "U"]
        self.assertEqual(result, expected)





class TestSingleCycleCheck(unittest.TestCase):

    def test_single_cycle_true(self):
        array = [2, 3, 1, -4, -4, 2]
        self.assertTrue(has_single_cycle(array))

    def test_single_cycle_false_revisits_start(self):
        array = [1, 1, 1, 1, 2]
        self.assertFalse(has_single_cycle(array))

    def test_single_cycle_false_incomplete(self):
        array = [1, 1, 0, 1, 1]
        self.assertFalse(has_single_cycle(array))

    def test_single_cycle_exact_jump(self):
        array = [1, 1, 1, 1, -4]
        self.assertTrue(has_single_cycle(array))

    def test_single_element_true(self):
        array = [0]
        self.assertTrue(has_single_cycle(array))

    def test_single_element_true_case2(self):
        array = [1]
        self.assertTrue(has_single_cycle(array))


if __name__ == '__main__':
    unittest.main()
