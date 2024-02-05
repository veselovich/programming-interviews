import time
from memory_profiler import profile

from nodes import *


@profile
def has_path_sum(tree, remaining_weight):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    if not tree:
        return False
    if not tree.left and not tree.right: # Leaf.
        return remaining_weight == tree.data
    # Non-leaf.
    return (has_path_sum(tree.left, remaining_weight - tree.data)
            or has_path_sum(tree.right, remaining_weight - tree.data))


def main():
    start_time = time.time()

    #test case
    print(has_path_sum(root_tree, 10))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()