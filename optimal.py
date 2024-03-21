import time
from memory_profiler import profile

from nodes import *


@profile
def find_k_largest_in_bst(tree, k):
    def find_k_largest_in_bst_helper(tree):
        # Perform reverse inorder traversal.
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements


def main():
    start_time = time.time()

    #test case
    print(find_k_largest_in_bst(root_tree2, 3))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()