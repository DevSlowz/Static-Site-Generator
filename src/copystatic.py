import os
import shutil



def copy_files_recursive(source_dir_path, dest_dir_path):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # Iterate through each item in the source directory
    for filename in os.listdir(source_dir_path):
        # Create full paths for source and destination files
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        
        # Print the copy operation for each file or directory
        print(f" * {from_path} -> {dest_path}")
        
        # If the item is a file, copy it to the destination
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        # If the item is a directory, recursively copy its contents
        else:
            copy_files_recursive(from_path, dest_path)
