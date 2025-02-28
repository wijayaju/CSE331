import unittest
from solution import RecursiveSinglyLinkedList as SLL, fibonacci
import random


class MyTestCase(unittest.TestCase):

    def test_add(self):
        sll = SLL()  # SLL: Empty

        # 1. Insert into an empty list
        sll.add(3)  # SLL: 3
        self.assertEqual(3, sll.head.val)  # 1
        self.assertIs(None, sll.head.next)  # 1
        self.assertEqual(3, sll.tail.val)  # 1
        self.assertIs(sll.head, sll.tail)  # 1

        # 2. Insert into a one element list
        sll.add(2)  # SLL: 3 --> 2
        self.assertEqual(3, sll.head.val)  # 2
        self.assertEqual(2, sll.head.next.val)  # 2
        self.assertIs(None, sll.head.next.next)  # 2
        self.assertEqual(2, sll.tail.val)  # 2
        self.assertIs(sll.head.next, sll.tail)  # 2

        # 3. add into a list with multiple SLLNodes
        sll.add(1)  # SLL: 3 --> 2 --> 1
        self.assertEqual(3, sll.head.val)  # 3
        self.assertEqual(2, sll.head.next.val)  # 3
        self.assertEqual(1, sll.head.next.next.val)  # 3
        self.assertIs(None, sll.head.next.next.next)  # 3
        self.assertEqual(1, sll.tail.val)  # 3
        self.assertIs(sll.head.next.next, sll.tail)  # 3

        # 4. Front test
        sll.add(4, False)  # SLL: 4 --> 3 --> 2 --> 1
        self.assertEqual(4, sll.head.val)  # 4
        self.assertEqual(3, sll.head.next.val)  # 4
        self.assertEqual(2, sll.head.next.next.val)  # 4
        self.assertEqual(1, sll.head.next.next.next.val)  # 4
        self.assertIs(None, sll.head.next.next.next.next)  # 4
        self.assertEqual(1, sll.tail.val)  # 4
        self.assertIs(sll.head.next.next.next, sll.tail)  # 4

        # 5. Type Agnostic test
        sll = SLL()  # SLL: Empty

        sll.add('CSE331')  # SLL: CSE331
        self.assertEqual('CSE331', sll.head.val)  # 5
        self.assertIs(None, sll.head.next)  # 5
        self.assertEqual('CSE331', sll.tail.val)  # 5
        self.assertIs(sll.head, sll.tail)  # 5

        # 6. Type Agnostic test 2
        sll.add('CSE498')  # SLL: CSE331 --> CSE498
        self.assertEqual('CSE331', sll.head.val)  # 6
        self.assertEqual('CSE498', sll.head.next.val)  # 6
        self.assertIs(None, sll.head.next.next)  # 6
        self.assertEqual('CSE498', sll.tail.val)  # 6
        self.assertIs(sll.head.next, sll.tail)  # 6

    def test_to_string(self):
        sll = SLL()

        # 1. Get the string of an empty list
        self.assertEqual("None", sll.to_string(sll.head))  # 1

        # 2. Get the string of an one element list
        sll.add('C')
        self.assertEqual("C", sll.to_string(sll.head))  # 2

        # 3. Get the string of a two element list
        sll.add('S')
        self.assertEqual("C --> S", sll.to_string(sll.head))  # 3

        # 4. Get the string of a multi-element list
        sll.add('E')
        self.assertEqual("C --> S --> E", sll.to_string(sll.head))  # 4

        # 5. Get the string of another multi-element list
        sll.add("3")
        self.assertEqual("C --> S --> E --> 3", sll.to_string(sll.head))  # 5

        # 6. Get the string of another multi-element list
        sll.add("3")
        self.assertEqual("C --> S --> E --> 3 --> 3", sll.to_string(sll.head))  # 6

        # 7. Get the string of another multi-element list
        sll.add("1")
        self.assertEqual("C --> S --> E --> 3 --> 3 --> 1", sll.to_string(sll.head))  # 7

    def test_search(self):
        sll = SLL()

        # 1. Try to search an empty List
        self.assertEqual(False, sll.search(331))  # 1

        sll.add(4)
        sll.add(2)
        sll.add(0)

        # 2. Search for a SLLNode at the start of the list
        self.assertEqual(True, sll.search(4))  # 2

        # 3. Search for a value that doesn't exist in the list
        self.assertEqual(False, sll.search(3))  # 3

        # 4. Search for a SLLNode in the middle of the list
        self.assertEqual(True, sll.search(2))  # 4

        # 5. Search for a SLLNode at the end of the list
        self.assertEqual(True, sll.search(0))  # 5

        # 6. Type Agnostic test
        sll = SLL()
        sll.add('Hello')
        sll.add('World!')
        sll.add('ThereShouldBeNoSpaces')
        self.assertEqual(True, sll.search('World!'))  # 6

    def test_remove(self):
        sll = SLL()

        # 1. Removing from an empty list
        self.assertEqual(False, sll.remove(331))  # SLL: Empty
        self.assertIs(None, sll.head)  # 1
        self.assertIs(None, sll.tail)  # 1

        sll.add(3)
        sll.add(4)
        sll.add(3)
        sll.add(1)  # SLL: 3 --> 4 --> 3 --> 1

        # 2. Try to remove an element that doesn't exist in the list
        self.assertEqual(False, sll.remove(6))  # SLL: 3 --> 4 --> 3 --> 1
        self.assertEqual(3, sll.head.val)  # 2
        self.assertEqual(4, sll.head.next.val)  # 2
        self.assertEqual(3, sll.head.next.next.val)  # 2
        self.assertEqual(1, sll.head.next.next.next.val)  # 2
        self.assertIs(None, sll.head.next.next.next.next)  # 2
        self.assertEqual(1, sll.tail.val)  # 2
        self.assertIs(sll.tail, sll.head.next.next.next)  # 2

        # 3. Remove from the middle of the list
        self.assertEqual(True, sll.remove(4))  # SLL: 3 --> 3 --> 1
        self.assertEqual(3, sll.head.val)  # 3
        self.assertEqual(3, sll.head.next.val)  # 3
        self.assertEqual(1, sll.head.next.next.val)  # 3
        self.assertIs(None, sll.head.next.next.next)  # 3
        self.assertEqual(1, sll.tail.val)  # 3
        self.assertIs(sll.tail, sll.head.next.next)  # 3

        # 4. Remove from the end of the list
        self.assertEqual(True, sll.remove(1))  # SLL: 3 --> 3
        self.assertEqual(3, sll.head.val)  # 4
        self.assertEqual(3, sll.head.next.val)  # 4
        self.assertIs(None, sll.head.next.next)  # 4
        self.assertEqual(3, sll.tail.val)  # 4
        self.assertIs(None, sll.tail.next)  # 4
        self.assertEqual(sll.tail, sll.head.next)  # 4

        # 5. Remove from the front of the list
        self.assertEqual(True, sll.remove(3))  # SLL: 3 (ONLY remove the first occurrence)
        self.assertEqual(3, sll.head.val)  # 5
        self.assertIs(None, sll.head.next)  # 5
        self.assertEqual(3, sll.tail.val)  # 5
        self.assertIs(sll.head, sll.tail)  # 5

        # 6. Remove the last SLLNode in the list
        self.assertEqual(True, sll.remove(3))  # SLL: Empty
        self.assertIs(None, sll.head)  # 6
        self.assertIs(None, sll.tail)  # 6

    def test_insertion_sort(self):
        sll = SLL()

        test_list=[7,6,5,4,3,2,1]
        for i in test_list:
            sll.add(i)
        sll.insertion_sort()
        current = sll.head
        while current.next is not None:
            self.assertTrue(current.val <= current.next.val)
            current = current.next

    def test_remove_duplicates(self):
        sll = SLL()

        # Add duplicate values to the linked list
        sll.add(1)
        sll.add(2)
        sll.add(2)
        sll.add(3)
        sll.add(3)
        sll.add(4)
        sll.add(4)
        sll.add(4)

        # Call remove_duplicates()
        sll.remove_duplicates(sll.head)

        # Check that all duplicates have been removed
        current = sll.head
        while current.next is not None:
            self.assertNotEqual(current.val, current.next.val)
            current = current.next

        # Check that the length of the list is correct
        count = 0
        current = sll.head
        while current is not None:
            count += 1
            current = current.next
        self.assertEqual(count, 4)  # There should only be 4 unique elements

    def test_remove_duplicates_it(self):

        sll = SLL()

        # Add duplicate values to the linked list
        sll.add(1)
        sll.add(2)
        sll.add(2)
        sll.add(3)
        sll.add(3)
        sll.add(4)
        sll.add(4)
        sll.add(4)

        # Call remove_duplicates()
        sll.remove_duplicates_iterative(sll.head)

        # Check that all duplicates have been removed
        current = sll.head
        while current.next is not None:
            self.assertNotEqual(current.val, current.next.val)
            current = current.next

        # Check that the length of the list is correct
        count = 0
        current = sll.head
        while current is not None:
            count += 1
            current = current.next
        self.assertEqual(count, 4)  # There should only be 4 unique elements



    def test_fibonacci(self):
        cache = {}
        result = fibonacci(0, cache)
        self.assertEqual(result, 0)

        cache = {}
        result = fibonacci(1, cache)
        self.assertEqual(result, 1)

        cache = {}
        result = fibonacci(2, cache)
        self.assertEqual(result, 1)

        cache = {}
        result = fibonacci(3, cache)
        self.assertEqual(result, 2)

        cache = {}
        result = fibonacci(4, cache)
        self.assertEqual(result, 3)

        cache = {}
        result = fibonacci(6, cache)
        self.assertEqual(result, 8)

        cache = {}
        result = fibonacci(7, cache)
        self.assertEqual(result, 13)

        cache = {}
        result = fibonacci(8, cache)
        self.assertEqual(result, 21)






if __name__ == '__main__':
    unittest.main()

