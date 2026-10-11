# Project 1: Recursive Structure Engine

## Hierarchical data

My tree represents the maternal side of a family. It starts with the matriarch, a maternal grandmother, and includes everyone descended from her. A full family tree is not really a tree, because every child has two parents. To keep it a true tree, each person only links to their children on this side of the family. Spouses are saved as a name for display, but they are not nodes in the tree.

## Tree organization

Each person is a `PersonNode` that stores a name, an age, an optional spouse name, and a list of children. I used a list instead of left and right children because a person can have any number of kids. Because of this, I did not use in-order traversal, since it only works on binary trees.

The `MaternalFamilyTree` class holds the root node, which is the matriarch, and all of the traversals and operations. `set_matriarch` creates the root, and `add_child` creates a new person, adds them to a parent's list of children, and returns them. Both raise an error if something is already there: a second matriarch, or a second child with the same name under one parent.

## How recursion is used

Each recursive operation has a public method that starts at the matriarch and a private helper method that does the recursion. Every helper has a base case that returns an empty result when the person is `None`, and a recursive case that handles the current person and then calls itself on each child.

Where the current person is handled decides the traversal order. In pre-order, the person is handled before their children. I use this for printing the tree, so a parent prints above their kids, and for searching, so the search can stop as soon as it finds a match. In post-order, the person is handled after their children. I use this for height, because a person's height is one more than their tallest child's height, so the children have to be finished first.

## Supported operations

The program can print the tree indented by generation, list everyone in pre-order and post-order, find a person by name both recursively and iteratively, find the path from the matriarch to a person, count the members, and compute the height of the tree. Searches return `None` when the person is not found, and an empty tree returns 0 members and a height of -1.

## Recursive vs. iterative comparison

I wrote the search both ways, and both versions return the same results. The recursive version follows the shape of the tree: check this person, then search each child. Python's call stack remembers which people are still left to check. The iterative version uses a list as a stack instead. It pops a person off, checks them, and pushes their children on, so the program keeps track of who is left to check itself.

For searching, both approaches work well. The recursive one is easier to read because it matches the tree. The iterative one does not have Python's recursion limit of about 1000 levels, but a family tree is never that deep, so it does not matter here. For post-order tasks like height, recursion is the better choice, because an iterative version would need extra work to remember whether each person's children are finished.

## Example output

As seen in `sample_output.txt`, this is how the program runs from start to finish with `python main.py`. It first prints the family tree indented by generation, then the pre-order and post-order traversals, then the results of the operations, such as the member count, the height, and the path from the matriarch to Leo. Finally, it runs the 25 test cases and shows what each one tests, the expected result, the actual result, and whether it passed. All 25 tests pass.
