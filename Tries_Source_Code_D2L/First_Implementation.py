import unittest


class Trie:
    """
    A Trie (Prefix Tree) implementation using a dictionary to store children nodes.
    """

    def __init__(self):
        """
        Initializes the Trie with a root node represented as a dictionary.
        The root contains a special key '*' to indicate the root itself.
        """
        self.root = {"*": "*"}  # Root node, storing child nodes dynamically

    def add_word(self, word: str):
        """
        Adds a word to the Trie.

        Args:
            word (str): The word to be added.
        """
        curr_node = self.root  # Start from the root node
        for letter in word:  # Iterate through each letter in the word
            if letter not in curr_node:  # If letter is not already a child, create a new dictionary
                curr_node[letter] = {}
            curr_node = curr_node[letter]  # Move to the next node
        curr_node["*"] = "*"  # Mark the end of the word using '*'

    def does_word_exist(self, word: str) -> bool:
        """
        Checks if a given word exists in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists, False otherwise.
        """
        curr_node = self.root  # Start from the root node
        for letter in word:  # Iterate through each letter of the word
            if letter not in curr_node:  # If the letter is not present, the word does not exist
                return False
            curr_node = curr_node[letter]  # Move to the next node
        return "*" in curr_node  # Return True if the '*' symbol is found, indicating a complete word


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
