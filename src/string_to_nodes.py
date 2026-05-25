from textnode import TextNode, TextType
import re

def text_to_textnodes(text):
     text=[TextNode(text,TextType.TEXT)]
     text=split_nodes_delimiter(text,"**",TextType.BOLD)
     text=split_nodes_delimiter(text,"_",TextType.ITALIC)
     text=split_nodes_delimiter(text,"`",TextType.CODE)
     text=split_nodes_image(text)
     text=split_nodes_link(text)
     return text

def extract_markdown_images(text):
     image_match = re.findall(r"\!\[(.*?)\]\((.*?)\)",text)
     return image_match

def extract_markdown_links(text):
     link_match = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
     return link_match

def split_nodes_delimiter(old_nodes, delimiter, text_type):
     new_nodes=[]
     for node in old_nodes:
        if node.text_type != TextType.TEXT:
           new_nodes.append(node)
           continue
        splitted=node.text.split(delimiter)
        if len(splitted)%2==0:
           raise Exception("delimiter missing")
        results=[]
        for x, piece in enumerate(splitted):
           if x % 2 == 0:
              if splitted[x]!="":
                splitted[x]=TextNode(splitted[x],TextType.TEXT)
                results.append(splitted[x])
           else:
              splitted[x]=TextNode(splitted[x],text_type)
              results.append(splitted[x])
        new_nodes.extend(results)
     return new_nodes

def split_nodes_image(old_nodes):
     new_nodes=[]
     for node in old_nodes:
        if node.text_type != TextType.TEXT:
           new_nodes.append(node)
           continue
        images=extract_markdown_images(node.text)
        if images==[]:
           new_nodes.append(node)
           continue
        leftovers=node.text
        for image in images:
           parts=leftovers.split(f"![{image[0]}]({image[1]})",1)
           if parts[0]!="":
               parts[0]=TextNode(parts[0],TextType.TEXT)
               new_nodes.append(parts[0])
           image=TextNode(image[0],TextType.IMAGE,image[1])
           new_nodes.append(image)
           if len(parts)>=2:
              leftovers=parts[1]
        if leftovers!="":
           leftovers=TextNode(leftovers,TextType.TEXT)
           new_nodes.append(leftovers)
     return new_nodes

def split_nodes_link(old_nodes):
     new_nodes=[]
     for node in old_nodes:
        if node.text_type != TextType.TEXT:
           new_nodes.append(node)
           continue
        links=extract_markdown_links(node.text)
        if links==[]:
           new_nodes.append(node)
           continue
        leftovers=node.text
        for link in links:
           parts=leftovers.split(f"[{link[0]}]({link[1]})",1)
           if parts[0]!="":
               parts[0]=TextNode(parts[0],TextType.TEXT)
               new_nodes.append(parts[0])
           link=TextNode(link[0],TextType.LINK,link[1])
           new_nodes.append(link)
           if len(parts)>=2:
              leftovers=parts[1]
        if leftovers!="":
           leftovers=TextNode(leftovers,TextType.TEXT)
           new_nodes.append(leftovers)
     return new_nodes
