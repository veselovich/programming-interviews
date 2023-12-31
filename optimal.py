import time
from memory_profiler import profile

from nodes import *


@profile
def overlapping_no_cycle_lists(L1, L2):
    """
    Test if two linked lists overlaps
    
    :type L1: ListNode
    :type L2: ListNode
    :rtype: ListNode[None]
    """
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    
    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1 # L2 is the longer list
    # Advances the longer list to get equal length lists.
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1 # None implies there is no overlap between L1 and L2.


def main():
    start_time = time.time()

    #test case
    print(overlapping_no_cycle_lists(L1, L2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()