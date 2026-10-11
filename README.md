# Maternal Family Tree

ITSC 2214 Project 1: Recursive Structure Engine. A Python tree that models one side of a family, with recursive traversals, search, and tests.

Portfolio page: https://conveniencestorelovefor298yen.github.io/data-structures-portfolio/projects/project-1-maternal-family-tree.html

## Requirements

Python 3. No packages to install.

## How to run

```
python main.py
```

This prints the family tree, the traversals, the operation results, and all test results.

To run only the tests, from the `project-1` folder:

```
python -m tests.test_maternal_family
```

## Example output

```
Maternal family tree:
Rosa (78) + Ed
    Ana (52) + Carlos
        Mia (24)
            Leo (2)
        Sam (19)
    Luis (49) + Grace
        Eva (15)
    Clara (45)

Traversals:
Preorder:  ['Rosa', 'Ana', 'Mia', 'Leo', 'Sam', 'Luis', 'Eva', 'Clara']
Postorder: ['Leo', 'Mia', 'Sam', 'Ana', 'Eva', 'Luis', 'Clara', 'Rosa']
```

Full output is in [`docs/sample_output.txt`](docs/sample_output.txt).

## Project structure

```
main.py                     runs everything
maternal_family/
    person_node.py          PersonNode: name, age, spouse, children
    maternal_family_tree.py MaternalFamilyTree: traversals and operations
tests/
    test_maternal_family.py normal, edge, and failure tests
docs/
    explanation.md          project write-up
    sample_output.txt       full program output
```
