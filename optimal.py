import time
from memory_profiler import profile

from nodes import *


@profile
def list_pivoting(L, x):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()
    # Populates the three lists.
    while L:
        if L.data < x:
            less_iter.next = L
            less_iter = less_iter.next
        elif L.data == x:
            equal_iter.next = L
            equal_iter = equal_iter.next
        else: # L.data > x.
            greater_iter.next = L
            greater_iter = greater_iter.next
        L = L.next

    # Combines the three lists.
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    return less_head.next


def main():
    start_time = time.time()

    #test case
    print_list(list_pivoting(L1, 7))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()