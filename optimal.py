import collections
import time
from memory_profiler import profile

from nodes import *

Interval = collections.namedtuple('Interval', ('left', 'right'))

@profile
def range_lookup_in_bst(tree, interval):
    def range_lookup_in_bst_helper(tree):
        if tree is None:
            return
        
        if interval.left <= tree.data <= interval.right:
            # tree. data lies in the interval.
            range_lookup_in_bst_helper(tree.left)
            result.append(tree.data)
            range_lookup_in_bst_helper(tree.right)
        elif interval.left > tree.data:
            range_lookup_in_bst_helper(tree.right)
        else: # interval.right > tree.data
            range_lookup_in_bst_helper(tree.left)

    result = []
    range_lookup_in_bst_helper(tree)
    return result


def main():
    start_time = time.time()

    #test case
    print(range_lookup_in_bst(root_tree2, Interval(3,5)))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()