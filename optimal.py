import time
from memory_profiler import profile

from nodes import TreeNode, print_tree

@profile
def reconstruct_preorder(preorder):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None
        # Note that reconstruct-preorder helper updates preorder iter. So the
        # order of following two calls are critical.
        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)
        return TreeNode(subtree_key, left_subtree, right_subtree)
    return reconstruct_preorder_helper(iter(preorder))


def main():
    start_time = time.time()

    #test case
    print_tree(reconstruct_preorder(['H','B','F',None,None,'E','A',None,None,None,'C',None,'D',None,'G','I',None,None,None]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()