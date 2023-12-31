import time
from memory_profiler import profile

from nodes import *


@profile
def reverse_sublist(L, start, finish):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range (1, start):
        sublist_head = sublist_head.next

    # Reverses sublist.
    sublist_iter = sublist_head.next
    for _ in range (finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp
    return dummy_head.next


def main():
    start_time = time.time()

    #test case
    print_list(reverse_sublist(L, 2, 6))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()