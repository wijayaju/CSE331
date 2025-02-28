import unittest
from probe_hash_map import ProbeHashMap


class TestProbeHashMap(unittest.TestCase):

    def setUp(self):
        """Set up the hash map for testing."""
        self.probe_map = ProbeHashMap()

    def test_set_and_get_items(self):
        """Test setting and getting items in the hash map."""
        self.probe_map[13] = 1
        self.probe_map[26] = 2
        self.probe_map[5] = 3
        self.assertEqual(self.probe_map[13], 1)
        self.assertEqual(self.probe_map[26], 2)
        self.assertEqual(self.probe_map[5], 3)

    def test_update_item(self):
        """Test updating an existing item."""
        self.probe_map[13] = 1
        self.probe_map[13] = 10
        self.assertEqual(self.probe_map[13], 10)

    def test_key_error_on_getitem(self):
        """Test that KeyError is raised for a missing key."""
        with self.assertRaises(KeyError):
            self.probe_map[99]

    def test_delete_item(self):
        """Test deleting an item."""
        self.probe_map[13] = 1
        self.probe_map[26] = 2
        del self.probe_map[13]
        with self.assertRaises(KeyError):
            self.probe_map[13]

    def test_key_error_on_delete(self):
        """Test that KeyError is raised when deleting a missing key."""
        with self.assertRaises(KeyError):
            del self.probe_map[99]


# To run these tests, you would typically use:
if __name__ == '__main__':
     unittest.main()

