import time
from memory_profiler import profile

from nodes import *


@profile
def merge_two_sorted_lists(L1, L2):
    """
    Merges two sorted linked list into a one
    
    :type L1: ListNode
    :type L2: ListNode
    :rtype: ListNode
    """
    # Creates a placeholder for the result.
    dummy_head = tail = ListNode()
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next


def main():
    start_time = time.time()

    #test case
    print_list(merge_two_sorted_lists(L1, L2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()