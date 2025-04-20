import solution
import unittest


class TestProgram(unittest.TestCase):
    """Unit tests for the Dijkstra's shortest path algorithm."""

    def test_case_1(self):
        """
        Test case with a reachable graph where some nodes are connected
        through direct and indirect paths. Also includes an unreachable node (index 5).
        """
        start = 0
        edges = [
            [[1, 7]],
            [[2, 6], [3, 20], [4, 3]],
            [[3, 14]],
            [[4, 2]],
            [],
            []
        ]
        expected = [0, 7, 13, 27, 10, -1]
        actual = solution.dijkstras_algorithm(start, edges)
        self.assertEqual(actual, expected)

    def test_disconnected_node(self):
        """
        Graph with disconnected components. Nodes 3, 4, and 5 are not reachable
        from the start node (0).
        """
        start = 0
        edges = [
            [[1, 1]],
            [[2, 2]],
            [],
            [[4, 1]],
            [],
            []
        ]
        expected = [0, 1, 3, -1, -1, -1]
        actual = solution.dijkstras_algorithm(start, edges)
        self.assertEqual(actual, expected)

    def test_all_reachable(self):
        """
        All nodes are reachable from the start node (2). The graph includes
        both direct and indirect connections, ensuring multiple path options.
        """
        start = 2
        edges = [
            [[1, 2]],
            [[3, 3]],
            [[0, 4], [1, 1]],
            [[4, 5]],
            []
        ]
        expected = [4, 1, 0, 4, 9]
        actual = solution.dijkstras_algorithm(start, edges)
        self.assertEqual(actual, expected)



class TestAStarAlgorithm(unittest.TestCase):
    """Unit tests for A* shortest path algorithm in a grid."""

    def test_astar_case_1(self):
        """Basic path through open cells with obstacles around."""
        start_row = 0
        start_col = 1
        end_row = 4
        end_col = 3
        graph = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        expected = [[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]
        actual = solution.a_star_algorithm(start_row, start_col, end_row, end_col, graph)
        self.assertEqual(actual, expected)

    def test_astar_no_path(self):
        """Case with no available path due to blockage by obstacles."""
        start_row = 0
        start_col = 0
        end_row = 2
        end_col = 2
        graph = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ]
        expected = []
        actual = solution.a_star_algorithm(start_row, start_col, end_row, end_col, graph)
        self.assertEqual(actual, expected)

    def test_astar_single_step(self):
        """Start and end are adjacent with a clear path."""
        start_row = 0
        start_col = 0
        end_row = 0
        end_col = 1
        graph = [
            [0, 0],
        ]
        expected = [[0, 0], [0, 1]]
        actual = solution.a_star_algorithm(start_row, start_col, end_row, end_col, graph)
        self.assertEqual(actual, expected)

    def test_astar_start_equals_end(self):
        """Start and end positions are the same."""
        start_row = 1
        start_col = 1
        end_row = 1
        end_col = 1
        graph = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        expected = [[1, 1]]
        actual = solution.a_star_algorithm(start_row, start_col, end_row, end_col, graph)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
