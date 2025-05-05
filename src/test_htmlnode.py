import unittest
from htmlnode import HTMLNode
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", [], [])
        node2 = HTMLNode("div", "This is a div", [], [])
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("div", "This is a div", [], [])
        node2 = HTMLNode("span", "This is a div", [], [])
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", "This is a div", [], ["class='container'"])