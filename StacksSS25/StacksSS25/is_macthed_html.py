from array_stack import ArrayStack
import unittest


def is_matched_html(raw):
    """Return True if all HTML tags are properly matched; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')  # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j + 1)  # find next '>' character
        if k == -1:
            return False  # invalid tag
        tag = raw[j + 1:k]  # strip away < >
        if not tag.startswith('/'):  # this is opening tag
            S.push(tag)
        else:  # this is closing tag
            if S.is_empty():
                return False  # nothing to match with
            if tag[1:] != S.pop():
                return False  # mismatched delimiter
        j = raw.find('<', k + 1)  # find next '<' character (if any)
    return S.is_empty()  # were all opening tags matched?


class TestIsMatchedHTML(unittest.TestCase):

    def test_balanced_html(self):
        good = "<html><head><title>Hello</title></head></html>"
        good2 = "<html><head><title>Hello</title></head><body><p>This appears in the <i>browser</i>.</p></body></html>"
        self.assertTrue(is_matched_html(good))
        self.assertTrue(is_matched_html(good2))

    def test_unbalanced_html(self):
        bad = "<html>Hello</title></html>"  # unmatched opening <html> and closing </title>
        bad2 = "<html><head><title>Hello</head></html>"  # unmatched closing </title>
        self.assertFalse(is_matched_html(bad))
        self.assertFalse(is_matched_html(bad2))

    def test_no_tags(self):
        text = "This is just plain text with no HTML tags."
        self.assertTrue(is_matched_html(text))  # No tags, so it's "balanced"

    def test_empty_string(self):
        self.assertTrue(is_matched_html(""))  # Empty string should be balanced

    def test_invalid_tag_format(self):
        invalid = "<html><head><title>Hello<title></head></html>"  # Missing '/'
        self.assertFalse(is_matched_html(invalid))


if __name__ == '__main__':
    unittest.main()
