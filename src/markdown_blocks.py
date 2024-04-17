import re

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

