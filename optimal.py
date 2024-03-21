import time
from memory_profiler import profile

from nodes import *

@profile
# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_LCA(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        # Keep searching since tree is outside of [s, b].
        while tree.data < s.data:
            tree = tree.right # LCA must be in tree's right child.
        while tree.data > b.data:
            tree = tree.left # LCA must be in tree's left child.
    # Now, s.data < tree. data && tree. data <= b. data.
    return tree


def main():
    start_time = time.time()

    #test case
    print(find_LCA(root_tree2, root_tree2.right.left, root_tree2.right.right))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()