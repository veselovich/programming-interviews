import time
from memory_profiler import profile

from nodes import tree

@profile
def find_successor(node):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    if node.right:
        # Successor is the leftmost element in node's right subtree.
        node = node.right
        while node.left:
            node = node.left
        return node
    
    # Find the closest ancestor whose left subtree contains node.
    while node.parent and node.parent.right is node:
        node = node.parent
    # A return value of None means node does not have successor, i.e., node is
    # the rightmost node in the tree.
    return node.parent


def main():
    start_time = time.time()

    #test case
    print(find_successor(tree.root.right.left))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()