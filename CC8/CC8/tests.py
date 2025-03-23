import unittest
from solution import BST, get_kth_largest_value  # Import BST class and function


def build_tree_from_list(nodes, root_id):
    node_dict = {}
    for node in nodes:
        node_dict[node["id"]] = BST(node["value"])

    for node in nodes:
        current_node = node_dict[node["id"]]
        if node["left"]:
            current_node.left = node_dict[node["left"]]
        if node["right"]:
            current_node.right = node_dict[node["right"]]

    return node_dict[root_id]


class TestKthLargestInBST(unittest.TestCase):
    def test_kth_largest(self):
        # Build the tree
        nodes = [
            {"id": "15", "left": "5", "right": "20", "value": 15},
            {"id": "20", "left": "17", "right": "22", "value": 20},
            {"id": "22", "left": None, "right": None, "value": 22},
            {"id": "17", "left": None, "right": None, "value": 17},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": "3", "value": 2},
            {"id": "3", "left": None, "right": None, "value": 3},
            {"id": "1", "left": None, "right": None, "value": 1}
        ]
        tree = build_tree_from_list(nodes, "15")

        # Test cases
        self.assertEqual(get_kth_largest_value(tree, 1), 22)  # 1st largest value
        self.assertEqual(get_kth_largest_value(tree, 2), 20)  # 2nd largest value
        self.assertEqual(get_kth_largest_value(tree, 3), 17)  # 3rd largest value
        self.assertEqual(get_kth_largest_value(tree, 4), 15)  # 4th largest value
        self.assertEqual(get_kth_largest_value(tree, 5), 5)  # 5th largest value
        self.assertEqual(get_kth_largest_value(tree, 6), 5)  # 6th largest value (duplicate 5)
        self.assertEqual(get_kth_largest_value(tree, 7), 3)  # 7th largest value
        self.assertEqual(get_kth_largest_value(tree, 8), 2)  # 8th largest value
        self.assertEqual(get_kth_largest_value(tree, 9), 1)  # 9th largest value


if __name__ == "__main__":
    unittest.main()
