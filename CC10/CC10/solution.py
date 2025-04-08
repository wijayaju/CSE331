class Trie:
    """
    A simple Trie (Prefix Tree) data structure used to store strings
    for efficient prefix-based search.
    """

    def __init__(self):
        # Root node of the trie is an empty dictionary
        self.root = {}

        # Special symbol to mark the end of a word
        self.end_symbol = "*"

    def insert(self, word):
        """
        Inserts a word into the trie.

        Args:
            word (str): The word to insert.
        """
        root = self.root
        for ch in word:
            if ch not in root:
                root[ch] = {}
            root = root[ch]
        root[self.end_symbol] = word


def multi_string_search(big_string, small_strings):
    """
    Determines which strings from small_strings are present in big_string.

    Args:
        big_string (str): The larger string to search within.
        small_strings (List[str]): A list of smaller strings to search for.

    Returns:
        List[bool]: A list of boolean values indicating whether each small string
                    is found in the big string.
    """
    # TODO: Build the trie and search for the small strings
    small_strings_trie = Trie()
    for string in small_strings:
        small_strings_trie.insert(string)

    found_strings = set()
    if not big_string:
        return [big_string == string for string in small_strings]
    for i in range(len(big_string)):
        current = small_strings_trie.root
        j = i
        while j < len(big_string):
            char = big_string[j]
            if char not in current:
                break
            current = current[char]
            j += 1
            if small_strings_trie.end_symbol in current:
                found_strings.add(current[small_strings_trie.end_symbol])
    is_found = [string in found_strings for string in small_strings]
    return is_found


def search_from_index(string, start_index, trie, found_strings):
    """
    Traverses the big string from the given start index, using the trie
    to find matching substrings that correspond to the small strings.

    Args:
        string (str): The big string.
        start_index (int): The index to start searching from.
        trie (Trie): The trie built from the small strings.
        found_strings (dict): A dictionary to record found strings.
    """
    # TODO: Traverse the trie from the start index and record matches
    current = trie.root
    j = start_index
    while j < len(string):
        char = string[j]
        if char not in current:
            break
        current = current[char]
        j += 1
        if trie.end_symbol in current:
            found_strings[trie.end_symbol] = string
