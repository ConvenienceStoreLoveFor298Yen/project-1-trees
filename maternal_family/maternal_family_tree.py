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

    def add_child(self, parent, name, age, spouse=None):
        """Create and return a child of parent; raise ValueError if parent already has a child with that name."""
        for child in parent.children:
            if child.name == name:
                raise ValueError(f"{parent.name} already has a child named {name}.")

        child = PersonNode(name, age, spouse)
        parent.children.append(child)
        return child

    def display(self):
        """Recursively return one line per person, indented by generation."""
        return self._display(self.matriarch, 0)

    def _display(self, person, depth):
        if person is None:
            return []

        line = "    " * depth + f"{person.name} ({person.age})"
        if person.spouse is not None:
            line += f" + {person.spouse}"

        lines = [line]
        for child in person.children:
            lines += self._display(child, depth + 1)
        return lines

    def preorder(self):
        """Recursively return names in person-then-children order."""
        return self._preorder(self.matriarch)

    def _preorder(self, person):
        if person is None:
            return []

        names = [person.name]
        for child in person.children:
            names += self._preorder(child)
        return names

    def postorder(self):
        """Recursively return names in children-then-person order."""
        return self._postorder(self.matriarch)

    def _postorder(self, person):
        if person is None:
            return []

        names = []
        for child in person.children:
            names += self._postorder(child)
        names.append(person.name)
        return names

    def find_person(self, name):
        """Recursively search (pre-order) for a person by name; return the node or None."""
        return self._find_person(self.matriarch, name)

    def _find_person(self, person, name):
        if person is None:
            return None

        if person.name == name:
            return person

        for child in person.children:
            found = self._find_person(child, name)
            if found is not None:
                return found

        return None
