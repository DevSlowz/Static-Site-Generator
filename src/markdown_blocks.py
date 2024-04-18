import re
from htmlnode import HTMLNode, LeafNode, ParentNode

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



    
def heading_to_htmlnode(block, type):
    heading_level = len(block) - len(block.lstrip('#'))
    if heading_level > 6 :
        raise ValueError("Heading level greater than 6")
    block = block.lstrip('# ')
    return HTMLNode(f'h{heading_level}', block)

def code_to_htmlnode(block, type):
    child_node = LeafNode('code', block)
    parent_node = ParentNode('pre', [child_node])

    return parent_node

def olist_to_htmlnode(block, type):
    pass

def ulist_to_htmlnode(block, type):
    pass

def quote_to_htmlnode(block, type):
    pass
