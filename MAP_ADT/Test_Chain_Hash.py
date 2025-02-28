# Let's create some test cases for chain_hash_map.py
import unittest

from chain_hash_map import ChainHashMap
from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap


class TestChainHashMap(unittest.TestCase):

    def setUp(self):
        """Set up the hash map for testing."""
        self.chain_map = ChainHashMap()

    def test_set_and_get_items(self):
        """Test setting and getting items in the hash map."""
        self.chain_map[13] = 1
        self.chain_map[26] = 2
        self.chain_map[5] = 3
        self.chain_map[11] = 3
        self.assertEqual(self.chain_map[13], 1)
        self.assertEqual(self.chain_map[26], 2)
        self.assertEqual(self.chain_map[5], 3)

    def test_update_item(self):
        """Test updating an existing item."""
        self.chain_map[13] = 1
        self.chain_map[13] = 10
        self.assertEqual(self.chain_map[13], 10)

    def test_key_error_on_getitem(self):
        """Test that KeyError is raised for a missing key."""
        with self.assertRaises(KeyError):
            self.chain_map[99]

    def test_delete_item(self):
        """Test deleting an item."""
        self.chain_map[13] = 1
        self.chain_map[26] = 2
        del self.chain_map[13]
        with self.assertRaises(KeyError):
            self.chain_map[13]

    def test_key_error_on_delete(self):
        """Test that KeyError is raised when deleting a missing key."""
        with self.assertRaises(KeyError):
            del self.chain_map[99]


# Assuming the unittest module will be used to run these tests outside of this environment.

# To run these tests, you would typically use the following in a Python environment:
if __name__ == '__main__':
    unittest.main()
