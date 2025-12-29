import os
import shutil
f = os.listdir("FILES")
os.makedirs("FILES/python_files", exist_ok=True)
os.makedirs("FILES/text_files", exist_ok=True)
os.makedirs("FILES/image_files", exist_ok=True)
for name in f:

    source = os.path.join("FILES", name)
    if os.path.isdir(source):
        continue
    elif name.endswith(".py"):
        shutil.move(source, "FILES/python_files")
    elif name.endswith(".txt"):
        shutil.move(source , "FILES/text_files")
    elif name.endswith((".jpg", ".png", ".jpeg")):
        shutil.move(source , "FILES/image_files")        
    else:
        pass

x = os.listdir("FILES/python_files")        
y = os.listdir("FILES/text_files")
z = os.listdir("FILES/image_files")

print("Python Files: ", x)
print("Text Files: ", y)
print("Image Files: ", z)