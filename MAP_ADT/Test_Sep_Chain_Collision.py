# # Let's create some test cases for chain_hash_map.py
# import unittest
#
# from chain_hash_map import ChainHashMap
# from hash_map_base import HashMapBase
# from unsorted_table_map import UnsortedTableMap
#
#
# class TestChainHashMap(unittest.TestCase):
#
#     def setUp(self):
#         """Set up the hash map for testing."""
#         self.chain_map = ChainHashMap()
#
#     def test_set_and_get_items(self):
#         """Test setting and getting items in the hash map."""
#         self.chain_map[13] = 1
#         self.chain_map[27] = 2  # Assuming same bucket as 13 in a small table
#         self.assertEqual(self.chain_map[13], 1)
#         self.assertEqual(self.chain_map[27], 2)
#
#     def test_collision_handling(self):
#         """Test that multiple keys mapping to the same bucket are handled correctly."""
#         # Assuming the hash function places these keys in the same bucket
#         key1 = 5
#         key2 = key1 + self.chain_map._capacity  # Forces collision by offsetting by table size
#         key3 = key1 + 2 * self.chain_map._capacity  # Another collision key
#
#         self.chain_map[key1] = 'A'
#         self.chain_map[key2] = 'B'
#         self.chain_map[key3] = 'C'
#
#         self.assertEqual(self.chain_map[key1], 'A')
#         self.assertEqual(self.chain_map[key2], 'B')
#         self.assertEqual(self.chain_map[key3], 'C')
#
#         # Ensure they don't overwrite each other
#         self.chain_map[key2] = 'D'
#         self.assertEqual(self.chain_map[key1], 'A')
#         self.assertEqual(self.chain_map[key2], 'D')
#         self.assertEqual(self.chain_map[key3], 'C')
#
#
# if __name__ == '__main__':
#     unittest.main()
# Let's create some test cases for chain_hash_map.py
import unittest

from chain_hash_map import ChainHashMap
from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap


class TestChainHashMap(unittest.TestCase):

    def setUp(self):
        """Set up the hash map for testing."""
        self.chain_map = ChainHashMap(cap=5)  # Small capacity to force collisions

    def test_set_and_get_items(self):
        """Test setting and getting items in the hash map."""
        self.chain_map[13] = 1
        self.chain_map[27] = 2  # Assuming same bucket as 13 in a small table
        self.assertEqual(self.chain_map[13], 1)
        self.assertEqual(self.chain_map[27], 2)

    def test_collision_handling(self):
        """Test that multiple keys mapping to the same bucket are handled correctly."""
        # With the simplified hash function and capacity=5, these should collide
        key1 = 1
        key2 = 6  # Both keys will hash to the same bucket if hash function is mod 5
        key3 = 11 # Another key that collides with the first two

        self.chain_map[key1] = 'A'
        self.chain_map[key2] = 'B'
        self.chain_map[key3] = 'C'

        self.assertEqual(self.chain_map[key1], 'A')
        self.assertEqual(self.chain_map[key2], 'B')
        self.assertEqual(self.chain_map[key3], 'C')

        # Ensure they don't overwrite each other
        self.chain_map[key2] = 'D'
        self.assertEqual(self.chain_map[key1], 'A')
        self.assertEqual(self.chain_map[key2], 'D')
        self.assertEqual(self.chain_map[key3], 'C')

if __name__ == '__main__':
    unittest.main()
