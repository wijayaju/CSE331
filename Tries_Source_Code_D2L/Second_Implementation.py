"""https://repl.it/@np_tutoring/Trie#main.py """

import unittest


class TrieNode:
    """
    Represents a single node in a Trie.
    Each node contains a letter, a dictionary of child nodes, and a flag indicating if it marks the end of a word.
    """

    def __init__(self, letter: str):
        """
        Initializes a TrieNode.

        Args:
            letter (str): The character represented by the node.
        """
        self.letter = letter  # Character stored at this node
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Boolean flag indicating if this node represents the end of a word


class Trie:
    """
    A Trie (Prefix Tree) data structure for efficient string storage and lookup.
    """

    def __init__(self):
        """
        Initializes the Trie with a root node represented by '*'.
        """
        self.root = TrieNode("*")  # Root node does not store a meaningful character

    def add_word(self, word: str):
        """
        Adds a word to the Trie.

        Args:
            word (str): The word to be added.
        """
        curr_node = self.root  # Start from the root
        for letter in word:  # Iterate through each character in the word
            if letter not in curr_node.children:  # If the letter is not present, create a new node
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]  # Move to the next node
        curr_node.is_end_of_word = True  # Mark the last node as the end of a valid word

    def does_word_exist(self, word: str) -> bool:
        """
        Checks if a given word exists in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists, False otherwise.
        """
        if word == "":  # An empty string is always considered to exist
            return True

        curr_node = self.root  # Start from the root node
        for letter in word:
            if letter not in curr_node.children:  # If letter is missing, word doesn't exist
                return False
            curr_node = curr_node.children[letter]  # Move to the next node
        return curr_node.is_end_of_word  # Return True only if it's marked as the end of a word


# Unit Tests
class TestTrie(unittest.TestCase):
    def setUp(self):
        """Set up a Trie instance before each test."""
        self.trie = Trie()
        words = ["wait", "waiter", "shop", "shopper"]
        for word in words:
            self.trie.add_word(word)

    def test_word_existence(self):
        """Test words that exist in the Trie."""
        self.assertTrue(self.trie.does_word_exist("wait"))
        self.assertTrue(self.trie.does_word_exist("waiter"))
        self.assertTrue(self.trie.does_word_exist("shop"))
        self.assertTrue(self.trie.does_word_exist("shopper"))

    def test_partial_word(self):
        """Test substrings that are only prefixes and not complete words."""
        self.assertFalse(self.trie.does_word_exist("waite"))  # Exists as prefix but not as a word
        self.assertFalse(self.trie.does_word_exist("shopp"))  # Exists as prefix but not as a word

    def test_non_existent_words(self):
        """Test words that do not exist in the Trie."""
        self.assertFalse(self.trie.does_word_exist("waits"))
        self.assertFalse(self.trie.does_word_exist("shoppers"))
        self.assertFalse(self.trie.does_word_exist("random"))

    def test_empty_string(self):
        """Test searching for an empty string, which should return True."""
        self.assertTrue(self.trie.does_word_exist(""))

    def test_add_new_word(self):
        """Test adding a new word and verifying its existence."""
        self.trie.add_word("waiting")
        self.assertTrue(self.trie.does_word_exist("waiting"))


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
