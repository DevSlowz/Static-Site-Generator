import os

directory_path = os.path.expanduser("~/Workspace/Development/github.com/DevSlowz/Static-Site-Generator")
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)