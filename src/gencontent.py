import os
import re
from pathlib import Path
from markdown_blocks import markdown_to_html_node

# Grab the h1 text from the markdown file and return it 
def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")


# Generate a single HTML page
def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    # Open file from 'from_path' -> read the contents -> store in variable
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    # Open file from 'template_path' -> read the contents -> store in variable
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    # Convert markdown document to html nodes
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Grab title from file 
    title = extract_title(markdown_content)

    # Replace template placeholders with real data
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, 'w')
    to_file.write(template)


# Recursively generate HTML pages for markdown files in a directory
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    # Crawl entries in dir_path_content
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        # Generate a new .html page for each markdown file
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            # Write to the dest_dir_path using the template_path template
            generate_page(from_path, template_path, dest_path)
        else:
            # Write to the dest_dir_path using the template_path template
            generate_pages_recursive(from_path, template_path, dest_path)
