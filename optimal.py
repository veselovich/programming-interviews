import time

from nodes import *


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) 
            and is_binary_tree_bst(tree.right, tree.data, high_range))


def main():
    start_time = time.time()

    #test case
    print(is_binary_tree_bst(root_tree))
    print(is_binary_tree_bst(root_tree2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()