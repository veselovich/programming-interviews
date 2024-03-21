import time
from memory_profiler import profile

from nodes import *


@profile
def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else: # Root and all keys in left subtree are < k, so skip them.
            subtree = subtree.right
    return first_so_far


def main():
    start_time = time.time()

    #test case
    print(find_first_greater_than_k(root_tree2, 4.5))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()