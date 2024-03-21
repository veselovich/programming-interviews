import time

from nodes import *

def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None
    
    transition_point = next((i for i, a in enumerate(preorder_sequence)
                             if a > preorder_sequence[0]),
                             len(preorder_sequence))
    return TreeNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
        rebuild_bst_from_preorder(preorder_sequence[transition_point:]))


def main():
    start_time = time.time()

    #test case
    print_tree(rebuild_bst_from_preorder([43,23,37,29,31,41,47,53]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()