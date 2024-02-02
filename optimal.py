import time
from memory_profiler import profile

from nodes import *


@profile
def is_symmetric(tree):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1. right)
                    and check_symmetric(subtree_0.right, subtree_1. left))
        # One subtree is empty, and the other is not.
        return False
    return not tree or check_symmetric(tree.left, tree.right)


def main():
    start_time = time.time()

    #test case
    print(is_symmetric(root_tree))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()