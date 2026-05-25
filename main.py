from textnode import TextNode, TextType
import os
import shutil

def copy_path(path,to_path):
   if os.path.exists(path):
    contents=os.listdir(path)
    for content in contents:
      file_path=os.path.join(path,content)
      des_path=os.path.join(to_path,content)
      if os.path.isfile(file_path):
        shutil.copy(file_path,des_path)
      else:
        os.mkdir(des_path)
        copy_path(file_path,des_path)

def main():
  if os.path.exists("public"):
    shutil.rmtree("public")
  os.mkdir("public")
  copy_path("static","public")

main()
