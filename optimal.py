import time
from memory_profiler import profile

from nodes import *


@profile
def find_kth_node_binary_tree(tree, k):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k: #k-th node must be in right subtree of tree.
            k -= left_size + 1
            tree = tree.right
        elif left_size == k - 1: #k-th is iter itself.
            return tree
        else: # k-th node must be in left subtree of iter.
            tree = tree.left

    return None # If k is between 1 and the tree size, this is unreachable.


def main():
    start_time = time.time()

    #test case
    print(find_kth_node_binary_tree(root_tree, 5))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()