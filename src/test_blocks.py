import unittest
from block_code import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TextBlockCode(unittest.TestCase):

  def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

  def test_block_to_block(self):
      block="""### I have a dream
a dream to be free
"""
      self.assertEqual(block_to_block_type(block),BlockType.HEADING)
      block2="""```\ncode code code```"""
      self.assertEqual(block_to_block_type(block2),BlockType.CODE)
      block3=""">Life before death
>Strength before weakness
>Journey before destination"""
      self.assertEqual(block_to_block_type(block3),BlockType.QUOTE)
      block4="""- list
- list
- list"""
      self.assertEqual(block_to_block_type(block4),BlockType.UNORDERED_LIST)
      block5="""1. eggs
2. bacon
3. toast
4. world domination"""
      self.assertEqual(block_to_block_type(block5),BlockType.ORDERED_LIST)
      block6="""This is the laws of thermodynamics..."""
      self.assertEqual(block_to_block_type(block6),BlockType.PARAGRAPH)

  def test_markdown_to_block(self):
      md =  """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
      blocks = markdown_to_blocks(md)
      self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
      mark = """
This is a paragraph

what about this paragraph
yep it is too

-this is a list of things
-things
-things
"""
      block = markdown_to_blocks(mark)
      self.assertEqual(
            block,
            [
                 "This is a paragraph",
                 "what about this paragraph\nyep it is too",
                 "-this is a list of things\n-things\n-things",
            ],
         )
