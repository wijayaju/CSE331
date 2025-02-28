import unittest
from probe_hash_map import ProbeHashMap


class TestProbeHashMap(unittest.TestCase):

    def setUp(self):
        """Set up the hash map for testing with a small capacity."""
        self.probe_map = ProbeHashMap(cap=5)  # Small table size to force collisions

    def test_set_and_get_items(self):
        """Test setting and getting items in the hash map."""
        self.probe_map[1] = 'A'
        self.probe_map[6] = 'B'  # Should collide with 1 if hash is mod 5
        self.probe_map[11] = 'C'  # Another collision in the same slot sequence

        self.assertEqual(self.probe_map[1], 'A')
        self.assertEqual(self.probe_map[6], 'B')
        self.assertEqual(self.probe_map[11], 'C')

    def test_collision_resolution(self):
        """Test that linear probing handles collisions correctly."""
        key1 = 2
        key2 = 7  # Will collide with key1 if table size is 5
        key3 = 12  # Will also collide and use linear probing

        self.probe_map[key1] = 'X'
        self.probe_map[key2] = 'Y'
        self.probe_map[key3] = 'Z'

        self.assertEqual(self.probe_map[key1], 'X')
        self.assertEqual(self.probe_map[key2], 'Y')
        self.assertEqual(self.probe_map[key3], 'Z')

    def test_update_item(self):
        """Test updating an existing item."""
        self.probe_map[1] = 'OldValue'
        self.probe_map[1] = 'NewValue'
        self.assertEqual(self.probe_map[1], 'NewValue')

    def test_delete_and_probe_reuse(self):
        """Test that deleting an item allows for reusing the slot in linear probing."""
        self.probe_map[3] = 'Alpha'
        self.probe_map[8] = 'Beta'  # Collides with 3
        del self.probe_map[3]  # Mark slot as available
        self.probe_map[13] = 'Gamma'  # Should reuse slot from key 3

        self.assertEqual(self.probe_map[8], 'Beta')
        self.assertEqual(self.probe_map[13], 'Gamma')
        with self.assertRaises(KeyError):
            _ = self.probe_map[3]  # Key 3 should no longer exist


if __name__ == '__main__':
    unittest.main()
