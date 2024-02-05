import time
from memory_profiler import profile

from nodes import *


@profile
def preorder_traversal(tree):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    path, result = [tree], []
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result


def main():
    start_time = time.time()

    #test case
    print(preorder_traversal(root_tree))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()