from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []  # This will hold the transformed list of nodes.
    
    # Loop through each node in the provided list.
    for old_node in old_nodes:
        
        # If a node's type isn't plain text, add it to the new list as-is.
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        # For plain text nodes, prepare to split them based on the delimiter.
        split_nodes = []
        sections = old_node.text.split(delimiter)  # Split the text by the delimiter.
        
        # If the number of sections is even, a delimiter was left open.
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        # Process each section.
        for i in range(len(sections)):
            # Skip empty sections, which can happen if delimiters are adjacent.
            if sections[i] == "":
                continue
            
            # Even-index sections are outside delimiters and remain plain text.
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            # Odd-index sections are inside delimiters and take on the new text_type.
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        
        # Extend the new_nodes list with the processed nodes.
        new_nodes.extend(split_nodes)
    
    # Return the transformed list of nodes.
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text) :
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches