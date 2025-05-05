def HTMLNode ():
    def __init__(self, tag, value, children, props):
        self.tag = None
        self.value = None
        self.children = None
        self.props = None

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return self.props.join(" ")

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


