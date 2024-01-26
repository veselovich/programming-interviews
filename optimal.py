import time
from memory_profiler import profile

from nodes import *


@profile
def binary_tree_depth_order(tree) :	
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree]

    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes for child in (curr.left, curr.right)
            if child
            ]
    return result


def main():
    start_time = time.time()

    #test case
    print(binary_tree_depth_order(root_tree))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()