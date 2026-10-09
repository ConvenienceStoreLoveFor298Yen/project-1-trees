"""PersonNode: one person in the maternal family tree, with references to their children."""


class PersonNode:
    def __init__(self, name, age, spouse=None):
        self.name = name
        self.age = age
        self.spouse = spouse      # just a name for display, not part of the tree
        self.children = []        # list of PersonNode

    def add_child(self, child):
        """Connect a child node under this person."""
        if child in self.children:
            raise ValueError(f"{self.name} already has {child.name} as a child!")
        self.children.append(child)
