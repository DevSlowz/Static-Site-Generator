import os

# Expand the tilde character to the user's home directory
directory_path = os.path.expanduser("~/Workspace/Development/github.com/DevSlowz/Static-Site-Generator")

# List the contents of the directory with full paths
contents_with_paths = [os.path.join(directory_path, item) for item in os.listdir(directory_path)]

# Print the contents with full paths
# print("Contents of the directory with full paths:")
# for item_with_path in contents_with_paths:
#     print(item_with_path)

# For each directory found we need to search throuh it for files and directories 
# We can try to iterate over each path to see if it is a directoy and if it is we make it 
# the avtive path and search it  

# For all the file paths found
for content in contents_with_paths :
    # If a file path is a directory list is contents
    if os.path.isdir(content):
        # List each item found but its complete path
        contents_with_paths = [os.path.join(content, item) for item in os.listdir(content)]
        print(contents_with_paths)
        break


