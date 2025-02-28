import unittest
from array_stack import ArrayStack


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))  # we will re-insert newlines when writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')  # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')  # re-insert newline characters
    output.close()


class TestReverseFile(unittest.TestCase):

    def setUp(self):
        # Sample file content for testing
        self.sample_content = "Line 1\nLine 2\nLine 3"
        self.reversed_content = "Line 3\nLine 2\nLine 1"
        self.test_file = "test_sample_file.rtf"

        # Create a sample .rtf file for testing
        with open(self.test_file, 'w') as file:
            file.write(self.sample_content)

    def tearDown(self):
        import os
        os.remove(self.test_file)  # Clean up after test

    def test_reverse_file(self):

        print("sample content: " )
        print(self.sample_content)
        #Call the reverse_file function
        reverse_file(self.test_file)
        # Check if the file content is reversed
        with open(self.test_file, 'r') as file:
            content = file.read().strip()
        print("after the call for reverse_file:")
        print(content)
        self.assertEqual(content, self.reversed_content)


if __name__ == '__main__':
    unittest.main()
