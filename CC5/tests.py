import solution
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        employees = [[0, 1], [1, 0]]
        projects = [[1, 0], [1, 0]]
        expected = [[0, 0], [1, 1]]
        actual = solution.stable_assignments(employees, projects)
        self.assertTrue(len(actual) == len(expected))
        for match in expected:
            self.assertIn(match, actual)

    def test_case_2(self):
        employees = [[0, 1, 2], [0, 2, 1], [1, 2, 0]]
        projects = [[2, 1, 0], [0, 1, 2], [0, 1, 2]]
        expected = [[0, 1], [1, 0], [2, 2]]
        actual = solution.stable_assignments(employees, projects)
        self.assertTrue(len(actual) == len(expected))
        for match in expected:
            self.assertIn(match, actual)

    def test_case_3(self):
        employees = [
            [0, 1, 2],
            [1, 0, 2],
            [1, 2, 0]
        ]
        projects = [
            [2, 1, 0],
            [1, 2, 0],
            [0, 2, 1]
        ]
        expected = [
            [0, 0],
            [1, 1],
            [2, 2]
        ]
        actual = solution.stable_assignments(employees, projects)
        self.assertTrue(len(actual) == len(expected))
        for match in expected:
            self.assertIn(match, actual)

    def test_case_4(self):
        employees = [
            [2, 0, 1, 3],
            [1, 3, 2, 0],
            [0, 1, 2, 3],
            [3, 2, 1, 0]
        ]
        projects = [
            [1, 2, 0, 3],
            [0, 3, 2, 1],
            [2, 1, 3, 0],
            [3, 0, 1, 2]
        ]
        expected = [
            [0, 2],
            [1, 1],
            [2, 0],
            [3, 3]
        ]
        actual = solution.stable_assignments(employees, projects)
        self.assertTrue(len(actual) == len(expected))
        for match in expected:
            self.assertIn(match, actual)

    def test_case_5(self):
        employees = [
            [1, 0, 2],
            [0, 2, 1],
            [2, 1, 0]
        ]
        projects = [
            [1, 0, 2],
            [0, 2, 1],
            [2, 1, 0]
        ]
        expected = [
            [0, 1],
            [1, 0],
            [2, 2]
        ]
        actual = solution.stable_assignments(employees, projects)
        self.assertTrue(len(actual) == len(expected))
        for match in expected:
            self.assertIn(match, actual)


if __name__ == "__main__":
    unittest.main()
