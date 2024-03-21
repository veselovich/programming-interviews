import time

from nodes import *

def rebuild_bst_from_preorder(preorder_sequence):
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None
        
        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1
        # Note that rebuild_bst_ from_preorder_on_value_range updates root_idx [0].
        # So the order of following two calls are critical.
        left_subtree = rebuild_bst_from_preorder_on_value_range(
            lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(
            root, upper_bound)
        return TreeNode(root, left_subtree, right_subtree)
    
    root_idx = [0] # Tracks current subtree.
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))


def main():
    start_time = time.time()

    #test case
    print_tree(rebuild_bst_from_preorder([43,23,37,29,31,41,47,53]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()