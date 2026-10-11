"""Entry point: builds the sample maternal family tree, prints it, runs operations and tests."""
from maternal_family.maternal_family_tree import MaternalFamilyTree
from tests.test_maternal_family import run_all_tests


def build_sample_family():
    family = MaternalFamilyTree()
    rosa = family.set_matriarch("Rosa", 78, spouse="Ed")
    ana = family.add_child(rosa, "Ana", 52, spouse="Carlos")
    luis = family.add_child(rosa, "Luis", 49, spouse="Grace")
    family.add_child(rosa, "Clara", 45)
    mia = family.add_child(ana, "Mia", 24)
    family.add_child(ana, "Sam", 19)
    family.add_child(luis, "Eva", 15)
    family.add_child(mia, "Leo", 2)
    return family


def main():
    family = build_sample_family()

    print("Maternal family tree:")
    for line in family.display():
        print(line)
    print()

    print("Traversals:")
    print("Preorder: ", family.preorder())
    print("Postorder:", family.postorder())
    print()

    print("Operations:")
    print("Members:", family.count_members())
    print("Tree Height (generations below the matriarch):", family.height())
    print("Path to Leo:", family.find_path("Leo"))
    print("Find Eva (recursive):", family.find_person("Eva").name)
    print("Find Eva (iterative):", family.find_person_iterative("Eva").name)
    print()

    print("Tests:")
    run_all_tests()


if __name__ == "__main__":
    main()
