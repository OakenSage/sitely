from enum import Enum
from string_to_nodes import text_to_textnodes
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST="unordered"
    ORDERED_LIST="ordered"

def markdown_to_html_node(markdown):
   blocks=markdown_to_blocks(markdown)
   block_lock=[]
   for block in blocks:
     type=block_to_block_type(block)
     if type==BlockType.PARAGRAPH:
       block=block.replace("\n"," ")
       lock=ParentNode("p",text_to_children(block))
       block_lock.append(lock)
     if type==BlockType.HEADING:
       count= 0
       for char in block:
         if char == "#":
           count+=1
         else:
           break
       block=block[count+1:]
       lock=ParentNode(f"h{count}",text_to_children(block))
       block_lock.append(lock)
     if type==BlockType.QUOTE:
       lines = block.split("\n")
       cleaned_lines = []
       for line in lines:
         cleaned_lines.append(line.lstrip("> "))
       cleaned_text = "\n".join(cleaned_lines)
       lock=ParentNode("blockquote",text_to_children(cleaned_text))
       block_lock.append(lock)
     if type==BlockType.UNORDERED_LIST:
       lines=block.split("- ")
       new_block=[]
       for line in lines:
         line=ParentNode("li",text_to_children(line))
         new_block.append(line)
       lock=ParentNode("ul",new_block)
       block_lock.append(lock)
     if type==BlockType.ORDERED_LIST:
       lines=block.split("\n")
       new_block=[]
       for line in lines:
         line = line[3:]
         line=ParentNode("li",text_to_children(line))
         new_block.append(line)
       lock=ParentNode("ol",new_block)
       block_lock.append(lock)
     if type==BlockType.CODE:
       block=block[4:-3]
       texts=TextNode(block,TextType.TEXT)
       child=[text_node_to_html_node(texts)]
       code=[ParentNode("code",child)]
       lock=ParentNode("pre",code)
       block_lock.append(lock)
   nodes=ParentNode("div",block_lock)
   return nodes

def text_to_children(text):
   texts=text_to_textnodes(text)
   child=[]
   for old_text in texts:
     old_text=text_node_to_html_node(old_text)
     child.append(old_text)
   return child

def block_to_block_type(block):
   if block.startswith("#"):
     count= 0
     for char in block:
       if char == "#":
         count+=1
       else:
         break
     if count<7 and count>0 and block[count]==" ":
       return BlockType.HEADING
   if block.startswith("```\n") and block.endswith("```"):
     return BlockType.CODE
   if block.startswith(">"):
     lines=block.split("\n")
     if all(line.startswith(">") for line in lines):
       return BlockType.QUOTE
   if block.startswith("- "):
     lines=block.split("\n")
     if all(line.startswith("- ") for line in lines):
       return BlockType.UNORDERED_LIST
   if block.startswith("1."):
     lines=block.split("\n")
     count=1
     for line in lines:
       if line.startswith(f"{count}. "):
         count+=1
       else:
         break
     if count ==len(lines)+1:
       return BlockType.ORDERED_LIST
   return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
   blocks=markdown.split("\n\n")
   new_blocks=[]
   for block in blocks:
      block=block.strip()
      if block!="":
         new_blocks.append(block)
   return new_blocks
