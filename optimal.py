import time
from memory_profiler import profile

from nodes import *


@profile
def inorder_traversal(tree):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    s, result = [], []
    while s or tree:
        if tree:
            s.append(tree)
            # Going left.
            tree = tree.left
        else:
            # Going up.
            tree = s.pop()
            result.append(tree.data)
            # Going right.
            tree = tree.right
    return result


def main():
    start_time = time.time()

    #test case
    print(inorder_traversal(root_tree))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()