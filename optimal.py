import time
from memory_profiler import profile
from nodes import *


@profile
def remove_duplicates(L):
    """
    Remove duplicate
    
    :type x: ListNode
    :rtype: None
    """
    it = L
    while it:
        # Uses next_distinct to find the next distinct value.
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L


def main():
    start_time = time.time()

    #test case
    remove_duplicates(L1)
    print_list(L1)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()