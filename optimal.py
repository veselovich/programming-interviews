import time
from memory_profiler import profile

from nodes import *


@profile
def build_min_height_bst_from_sorted_array(A):
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return TreeNode(A[mid],
                       build_min_height_bst_from_sorted_subarray(start, mid),
                       build_min_height_bst_from_sorted_subarray(mid + 1, end))
    return build_min_height_bst_from_sorted_subarray(0, len(A))


def main():
    start_time = time.time()

    #test case
    print_tree(build_min_height_bst_from_sorted_array([2,3,5,7,11,13,17,19,23]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()