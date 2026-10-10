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


def run_all_tests():
    results.clear()
    test_set_matriarch()
    print(f"{sum(results)} / {len(results)} tests passed")


if __name__ == "__main__":
    run_all_tests()
