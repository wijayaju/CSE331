import solution
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.multi_string_search(
                "this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]
            ),
            [True, False, True, True, False, True, False],
        )

    def test_case_2_basic_match(self):
        self.assertEqual(
            solution.multi_string_search(
                "abcde", ["a", "ab", "e", "de", "xyz"]
            ),
            [True, True, True, True, False],
        )

    def test_case_3_overlapping_matches(self):
        self.assertEqual(
            solution.multi_string_search(
                "abababa", ["aba", "bab", "ab", "ba"]
            ),
            [True, True, True, True],
        )

    def test_case_4_repeated_queries(self):
        self.assertEqual(
            solution.multi_string_search(
                "repeatrepeat", ["repeat", "repeat", "eat", "rep"]
            ),
            [True, True, True, True],
        )

    def test_case_5_empty_string_list(self):
        self.assertEqual(
            solution.multi_string_search("nonempty", []),
            [],
        )

    def test_case_6_empty_big_string(self):
        self.assertEqual(
            solution.multi_string_search("", ["a", "b", ""]),
            [False, False, True],
        )

    def test_case_7_case_sensitivity(self):
        self.assertEqual(
            solution.multi_string_search("CaseSensitive", ["case", "Case", "Sensitive", "sensitive"]),
            [False, True, True, False],
        )


if __name__ == "__main__":
    unittest.main()
