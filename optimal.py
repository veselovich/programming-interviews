import time
from memory_profiler import profile

from nodes import TreeNode

@profile
def binary_tree_from_preorder_inorder(preorder, inorder):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder [preorder_ start: preorder_end] and
    # inorder [inorder_start: inorder_end].
    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
                                                 inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
    
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return TreeNode(
            preorder[preorder_start],
        # Recursively builds the left subtree.
        binary_tree_from_preorder_inorder_helper(
            preorder_start + 1, preorder_start + 1 + left_subtree_size,
            inorder_start, root_inorder_idx),
        # Recursively builds the right subtree.
        binary_tree_from_preorder_inorder_helper(
            preorder_start + 1 + left_subtree_size, preorder_end,
            root_inorder_idx + 1, inorder_end))
    
    return binary_tree_from_preorder_inorder_helper(0,
                                                    len(preorder), 0,
                                                    len(inorder))


def main():
    start_time = time.time()

    #test case
    print(binary_tree_from_preorder_inorder([1,2,4,5,3,6,7], [4,2,5,1,6,3,7]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()