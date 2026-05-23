import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None,"This is a text node",None , {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode(None,"This is a text node",None , {"href": "https://www.google.com","target": "_blank",})
        node3 = HTMLNode(None,"This is not a text node")
        node4 = HTMLNode(None,"This is not a text node")
        node5 = HTMLNode(None,"This is not a text node")
        self.assertEqual(node.props_to_html(), node2.props_to_html())
        self.assertNotEqual(node.props_to_html(), node3.props_to_html())
        self.assertNotEqual(node2.props_to_html(), node4.props_to_html())
        self.assertEqual(node4.props_to_html(), node5.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("b", "ON THE WAY?")
        node3 = LeafNode("a","this is a trap", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "<b>ON THE WAY?</b>")
        self.assertEqual(node3.to_html(), '<a href="https://www.google.com" target="_blank">this is a trap</a>')
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()

