import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag = 'a',value = "This is a text node",props = {"href": "https://www.google.com"})
        node2 = HTMLNode(tag = 'a',value = "This is a text node",props = {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = ParentNode(tag = 'p',children = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),]
        ,props = {"href": "https://www.google.com"})
        self.assertEqual(node.tag, "p")




if __name__ == "__main__":
    unittest.main()