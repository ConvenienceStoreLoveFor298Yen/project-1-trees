"""MaternalFamilyTree: the maternal descendant tree, rooted at the matriarch, with its traversals and operations."""
from maternal_family.person_node import PersonNode


class MaternalFamilyTree:
    def __init__(self):
        """Initialize self.matriarch (the root node) to None."""
        self.matriarch = None

    def set_matriarch(self, name, age, spouse=None):
        """Create and return the matriarch; raise ValueError if one exists."""
        if self.matriarch is not None:
            raise ValueError("Matriarch already exists.")

        self.matriarch = PersonNode(name, age, spouse)
        return self.matriarch

    def get_matriarch(self):
        """Return the matriarch node, or None."""
        return self.matriarch
