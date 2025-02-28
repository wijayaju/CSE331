class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def remove_duplicates_from_linked_list(linked_list):
    # Function to be implemented by students
    current_node = linked_list
    while current_node is not None:
        next_node = current_node.next
        while next_node is not None and next_node.value == current_node:
            current_node.next = next_node.next
    return current_node


# Unit test cases
import unittest

class TestRemoveDuplicatesFromLinkedList(unittest.TestCase):
    def build_linked_list(self, values):
        if not values:
            return None
        head = LinkedList(values[0])
        current = head
        for value in values[1:]:
            current.next = LinkedList(value)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        values = []
        while head is not None:
            values.append(head.value)
            head = head.next
        return values

    def test_remove_duplicates(self):
        # Test case 1
        values = [1, 1, 3, 4, 4, 5, 6, 6]
        linked_list = self.build_linked_list(values)
        expected = [1, 3, 4, 5, 6]
        result = remove_duplicates_from_linked_list(linked_list)
        self.assertEqual(self.linked_list_to_list(result), expected)

        # Test case 2
        values = [1, 1, 1, 1, 1]
        linked_list = self.build_linked_list(values)
        expected = [1]
        result = remove_duplicates_from_linked_list(linked_list)
        self.assertEqual(self.linked_list_to_list(result), expected)

        # Test case 3
        values = [1, 2, 3, 4, 5]
        linked_list = self.build_linked_list(values)
        expected = [1, 2, 3, 4, 5]
        result = remove_duplicates_from_linked_list(linked_list)
        self.assertEqual(self.linked_list_to_list(result), expected)

        # Test case 4
        values = []
        linked_list = self.build_linked_list(values)
        expected = []
        result = remove_duplicates_from_linked_list(linked_list)
        self.assertEqual(self.linked_list_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
