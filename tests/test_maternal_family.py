"""Test cases"""
from maternal_family.maternal_family_tree import MaternalFamilyTree

results = []


def check(test_name, expected, actual):
    """Print one test case with its expected and actual results, and record PASS/FAIL."""
    passed = expected == actual
    results.append(passed)
    print(f"TEST {len(results)}: {test_name}")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}")
    print(f"  Result:   {'PASS' if passed else 'FAIL'}")
    print()


def build_test_family():
    tree = MaternalFamilyTree()
    rosa = tree.set_matriarch("Rosa", 78)
    ana = tree.add_child(rosa, "Ana", 52)
    tree.add_child(rosa, "Luis", 49)
    mia = tree.add_child(ana, "Mia", 24)
    tree.add_child(mia, "Leo", 2)
    return tree


def name_or_none(person):
    return person.name if person is not None else None


def error_message(action):
    """Run action and return its ValueError message, or 'no error' if it didn't raise."""
    try:
        action()
    except ValueError as error:
        return str(error)
    return "no error"


def test_set_matriarch():
    tree = MaternalFamilyTree()
    check("get the matriarch of a new tree (edge)",
          None, tree.get_matriarch())
    tree.set_matriarch("Rosa", 78)
    check("set and get the matriarch (normal)",
          "Rosa", name_or_none(tree.get_matriarch()))
    check("set a second matriarch (failure)",
          "Matriarch already exists.", error_message(lambda: tree.set_matriarch("Ana", 52)))


def test_add_child():
    tree = build_test_family()
    check("children of Rosa in the sample family (normal)",
          ["Ana", "Luis"], [child.name for child in tree.get_matriarch().children])
    check("add a second child named Ana under Rosa (failure)",
          "Rosa already has a child named Ana.",
          error_message(lambda: tree.add_child(tree.get_matriarch(), "Ana", 50)))


def test_display():
    tree = build_test_family()
    check("display the sample family (normal)",
          ["Rosa (78)", "    Ana (52)", "        Mia (24)", "            Leo (2)", "    Luis (49)"],
          tree.display())
    check("display an empty tree (edge)",
          [], MaternalFamilyTree().display())


def test_preorder():
    tree = build_test_family()
    check("preorder of the sample family (normal)",
          ["Rosa", "Ana", "Mia", "Leo", "Luis"], tree.preorder())
    check("preorder of an empty tree (edge)",
          [], MaternalFamilyTree().preorder())


def test_postorder():
    tree = build_test_family()
    check("postorder of the sample family (normal)",
          ["Leo", "Mia", "Ana", "Luis", "Rosa"], tree.postorder())
    check("postorder of an empty tree (edge)",
          [], MaternalFamilyTree().postorder())


def test_find_person():
    tree = build_test_family()
    check("find Leo, 4 generations deep, recursive (normal)",
          "Leo", name_or_none(tree.find_person("Leo")))
    check("search an empty tree, recursive (edge)",
          None, MaternalFamilyTree().find_person("Rosa"))
    check("search for Zed, who is not in the tree, recursive (failure)",
          None, tree.find_person("Zed"))


def test_find_person_iterative():
    tree = build_test_family()
    check("find Leo, 4 generations deep, iterative (normal)",
          "Leo", name_or_none(tree.find_person_iterative("Leo")))
    check("search an empty tree, iterative (edge)",
          None, MaternalFamilyTree().find_person_iterative("Rosa"))
    check("search for Zed, who is not in the tree, iterative (failure)",
          None, tree.find_person_iterative("Zed"))


def test_find_path():
    tree = build_test_family()
    check("path from the matriarch to Leo (normal)",
          ["Rosa", "Ana", "Mia", "Leo"], tree.find_path("Leo"))
    check("path to Zed, who is not in the tree (failure)",
          None, tree.find_path("Zed"))


def test_count_members():
    check("count members of the sample family (normal)",
          5, build_test_family().count_members())
    check("count members of an empty tree (edge)",
          0, MaternalFamilyTree().count_members())
    tree = MaternalFamilyTree()
    tree.set_matriarch("Rosa", 78)
    check("count members of a matriarch-only tree (edge)",
          1, tree.count_members())


def run_all_tests():
    results.clear()
    test_set_matriarch()
    test_add_child()
    test_display()
    test_preorder()
    test_postorder()
    test_find_person()
    test_find_person_iterative()
    test_find_path()
    test_count_members()
    print(f"{sum(results)} / {len(results)} tests passed")


if __name__ == "__main__":
    run_all_tests()
