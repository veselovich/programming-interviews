import time
from memory_profiler import profile

from nodes import root_tree

@profile
def create_list_of_leaves(tree):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    # First do the left subtree, and then do the right subtree.
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)


def main():
    start_time = time.time()

    #test case
    print(create_list_of_leaves(root_tree))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()