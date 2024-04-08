class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # String representing HTML tage name
        self.tag = tag
        # String representing the value of HTML tag
        self.value = value
        # List of HTMLNode objects 
        self.children = children
        # Dictionary of key-value pairs representing attributes of the HTML tag - <a>
        self.props = props

    def to_html(self) :
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html



    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children},{self.props} )"
