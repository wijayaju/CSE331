from solution import DisjointSet

#from solution1 import DisjointSet
#from solution2 import DisjointSet
import unittest





class TestProgram(unittest.TestCase):
    def test_case_1(self):
        disjoint_set = DisjointSet()
        self.assertTrue(disjoint_set.find_representative(1) is None)
        disjoint_set.add_set(1)
        self.assertTrue(disjoint_set.find_representative(1) == 1)
        disjoint_set.add_set(5)
        self.assertTrue(disjoint_set.find_representative(1) == 1)
        self.assertTrue(disjoint_set.find_representative(5) == 5)
        disjoint_set.merge_sets(5, 1)
        self.assertTrue(disjoint_set.find_representative(5) == disjoint_set.find_representative(1))


    def test_case_2(self):
        disjoint_set = DisjointSet()

        # Add sets
        disjoint_set.add_set(5)
        self.assertTrue(disjoint_set.find_representative(5) == 5)

        disjoint_set.add_set(10)
        self.assertTrue(disjoint_set.find_representative(10) == 10)

        # Merge sets
        disjoint_set.merge_sets(5, 10)
        self.assertTrue(disjoint_set.find_representative(5) == disjoint_set.find_representative(10))

        # Add another set
        disjoint_set.add_set(20)
        self.assertTrue(disjoint_set.find_representative(20) == 20)

        # Merge the new set with existing set
        disjoint_set.merge_sets(20, 10)
        self.assertTrue(disjoint_set.find_representative(20) == disjoint_set.find_representative(5))
        self.assertTrue(disjoint_set.find_representative(10) == disjoint_set.find_representative(5))


if __name__ == '__main__':
    unittest.main()