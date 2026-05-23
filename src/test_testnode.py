import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is not a text node", TextType.BOLD)
        node4 = TextNode("This is not a text node", TextType.TEXT)
        node5 = TextNode("This is not a text node", TextType.TEXT)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)
        self.assertEqual(node4, node5)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a  node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        html_node2 = text_node_to_html_node(node2)
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is a text node")
        self.assertEqual(html_node3.tag, "code")
        self.assertEqual(html_node3.value, "This is a  node")

if __name__ == "__main__":
    unittest.main()
