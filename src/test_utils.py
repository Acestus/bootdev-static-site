# src/test_utils.py

import unittest
from utils import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_with_whitespace(self):
        self.assertEqual(extract_title("   #   My Title   "), "My Title")

    def test_extract_title_multiline(self):
        md = "Intro\n# Main Title\n## Subtitle"
        self.assertEqual(extract_title(md), "Main Title")

    def test_extract_title_no_h1(self):
        with self.assertRaises(Exception):
            extract_title("## No h1 here\nJust text")

if __name__ == "__main__":
    unittest.main()