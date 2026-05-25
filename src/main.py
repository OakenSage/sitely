import os
import shutil
from block_code import markdown_to_html_node, extract_title

def generate_recurse(from_path, template_path, dest_path):
  files=os.listdir(from_path)
  for file in files:
      file_path=os.path.join(from_path,file)
      des_path=os.path.join(dest_path,file)
      if os.path.isfile(file_path):
        new_path= os.path.splitext(des_path)[0]+".html"
        generate_page(file_path, template_path, new_path)
      else:
        os.mkdir(des_path)
        generate_recurse(file_path,template_path,des_path)

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  from_=open(from_path)
  template=open(template_path)
  md=from_.read()
  temp=template.read()
  html=markdown_to_html_node(md)
  file=html.to_html()
  title=extract_title(md)
  temp=temp.replace("{{ Title }}",title)
  temp=temp.replace("{{ Content }}",file)
  direct=os.path.dirname(dest_path)
  os.makedirs(direct,exist_ok=True)
  with open(dest_path,"w") as f:
    f.write(temp)

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
  generate_recurse("content","template.html","public")

main()




