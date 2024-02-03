import collections
import time
from memory_profiler import profile

from nodes import *


@profile
def lca(tree, node0, node1):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))
    # Returns an object consisting of an int and a node. The int field is o,
    # 1, or 2 depending on how many of {node0, node1} are present in tree. If
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the LCA.
    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)
        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree.
            return right_result
        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes + int(
                tree is node0) + int(tree is node1))
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)
    return lca_helper(tree, node0, node1).ancestor


def main():
    start_time = time.time()

    #test case
    print(lca(root_tree, root_tree.left.left, root_tree.left.right))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()