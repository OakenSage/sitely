import unittest
from string_to_nodes import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, text_to_textnodes
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_text_to_nodes(self):
    text="This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes=[
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD),
      TextNode(" with an ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word and a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" and an ", TextType.TEXT),
      TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
      TextNode(" and a ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://boot.dev"),]
    self.assertEqual(nodes,text_to_textnodes(text))
    text2="This is **bold** with `alot of code` and i am _tired_ now"
    nodes2=[
      TextNode("This is ", TextType.TEXT),
      TextNode("bold", TextType.BOLD),
      TextNode(" with ", TextType.TEXT),
      TextNode("alot of code", TextType.CODE),
      TextNode(" and i am ", TextType.TEXT),
      TextNode("tired", TextType.ITALIC),
      TextNode(" now", TextType.TEXT)]
    self.assertEqual(nodes2,text_to_textnodes(text2))

  def test_splits(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),])
    node2 = TextNode("This is text with a **bold block** word", TextType.TEXT)
    new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
    self.assertEqual(new_nodes2, [TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold block", TextType.BOLD),
    TextNode(" word", TextType.TEXT),])
    node3 = TextNode("This is text with a _Ity block_ word", TextType.TEXT)
    new_nodes3 = split_nodes_delimiter([node3], "_", TextType.ITALIC)
    self.assertEqual(new_nodes3, [TextNode("This is text with a ", TextType.TEXT),
    TextNode("Ity block", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),])

  def test_extract_images(self):
    matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    matches2 = extract_markdown_images("This is text with another ![image](https://i.imgur.com/zeRo.png)")
    self.assertListEqual([("image", "https://i.imgur.com/zeRo.png")], matches2)

  def test_split_images(self):
    node1 = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,)
    new_nodes1 = split_nodes_image([node1])
    self.assertListEqual([TextNode("This is text with an ", TextType.TEXT),TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.TEXT),TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),],new_nodes1,)
    node2 = TextNode(
        "This is text ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,)
    new_nodes2 = split_nodes_image([node2])
    self.assertListEqual([TextNode("This is text ", TextType.TEXT),TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.TEXT),TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),],new_nodes2,)
    node3 = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,)
    new_nodes3 = split_nodes_image([node3])
    self.assertListEqual([TextNode("This is text with an ", TextType.TEXT),TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.TEXT),TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),],new_nodes3,)

  def test_extract_links(self):
    matches = extract_markdown_links("This is text with an [link](https://i.imgur.com/zjjcJKZ.png)")
    self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)
    matches2 = extract_markdown_links("This is text with another [link](https://i.imgur.com/zeRo.png)")
    self.assertListEqual([("link", "https://i.imgur.com/zeRo.png")], matches2)
if __name__ == "__main__":
    unittest.main()

