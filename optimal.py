import time
from memory_profiler import profile

from nodes import *


@profile
def sum_root_to_leaf(tree, partial_path_sum=0):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    if not tree:
        return 0
    
    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right: # Leaf.
        return partial_path_sum
    # Non-leaf.
    return (sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(
        tree.right, partial_path_sum))


def main():
    start_time = time.time()

    #test case
    print(sum_root_to_leaf(root_tree))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()