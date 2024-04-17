from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image
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

# Example Output :
# # [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")]

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

# Example Output :
# [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
def extract_markdown_links(text) :
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    # Create an empty list to store the result after processing
    new_nodes = []

    # Iterate over each old_node in the list of old_nodes
    for old_node in old_nodes:
        # Check if the current node is not of type 'text'
        # If so, append it as is to new_nodes and skip further processing for this node
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        # Assign the text content of the current node to a variable
        original_text = old_node.text

        # Use a custom function to find all markdown image syntax in the text
        images = extract_markdown_images(original_text)

        # If no images are found, append the current node as is and skip further processing
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        # If images are found, iterate over each image
        for image in images:
            # Split the text into two parts around the first occurrence of the current image markdown
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)

            # If split operation didn't result in exactly two parts, something went wrong
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")

            # If the text before the image is not empty, create a new TextNode with this text and append it
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))

            # Create a new TextNode for the image itself and append it
            new_nodes.append(
                TextNode(
                    image[0],  # The alt text of the image
                    text_type_image,  # The type of this node is set to 'image'
                    image[1],  # The URL of the image
                )
            )

            # Update original_text to be the remaining text after the first image
            original_text = sections[1]
            

        # If there is any text left after processing all images, create a new TextNode with it
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    # Return the final list of processed nodes
    return new_nodes




def split_nodes_link(old_nodes):
    pass