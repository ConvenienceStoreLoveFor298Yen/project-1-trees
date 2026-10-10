"""PersonNode: one person in the maternal family tree, with references to their children."""


class PersonNode:
    def __init__(self, name, age, spouse=None):
        """Store name, age, and spouse. Children initially an empty list."""
        self.name = name
        self.age = age
        self.spouse = spouse      # just a name for display, not part of the tree
        self.children = []        # list of PersonNode
