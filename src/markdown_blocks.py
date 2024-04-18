import re
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


# Takes an entire document as a markdown string and returns blocks
def markdown_to_blocks(markdown) :
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph


def paragraph_to_htmlnode(block, type):
    # blocks = markdown_to_blocks(markdown)
    # block_types = []
    # if len(blocks) == 0 :
    #     raise AssertionError("Invalid Markdown")
    
    # # Iterate over each block and identify it
    # for block in blocks:
    #     block_types.append()
    return f'<p>{block}</p>'

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

    
def heading_to_htmlnode(block):
    """Converts a Markdown heading block to an HTML node.

    Args:
        block (str): The Markdown heading block.

    Returns:
        ParentNode: An HTML node representing the heading.
        
    Raises:
        ValueError: If the heading level is invalid.
    """
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_htmlnode(block):
    """Converts a Markdown code block to an HTML node.

    Args:
        block (str): The Markdown code block.

    Returns:
        ParentNode: An HTML node representing the code block.
        
    Raises:
        ValueError: If the code block is invalid.
    """
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_htmlnode(block):
    if not block.startswith("<ol>") or not block.endswith("</ol>"):
        raise ValueError("Invalid code block") 

def ulist_to_htmlnode(block):
    pass

def quote_to_htmlnode(block):
    pass
