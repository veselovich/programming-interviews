import time
from memory_profiler import profile

from nodes import root_tree

@profile
def exterior_binary_tree(tree):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    def is_leaf(node):
        return not node.left and not node.right
    
    # Computes the nodes from the root to the leftmost leaf followed by all
    # the leaves in subtree.
    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        return (([subtree] if is_boundary or is_leaf(subtree) else [])
                + left_boundary_and_leaves(subtree.left, is_boundary)
                + left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left))
    
    # Computes the leaves in left-to-right order followed by the rightmost
    # leaf to the root path in subtree.
    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        return (right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right)
                + right_boundary_and_leaves(subtree.right, is_boundary)
                + ([subtree] if is_boundary or is_leaf(subtree) else []))
    
    return ([tree]
            + left_boundary_and_leaves(tree.left, is_boundary=True)
            + right_boundary_and_leaves(tree.right, is_boundary=True)
            if tree else [])


def main():
    start_time = time.time()

    #test case
    print(exterior_binary_tree(root_tree))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()