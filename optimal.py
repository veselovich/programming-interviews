import time
from memory_profiler import profile

from nodes import *


@profile
def add_two_numbers(L1, L2):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    place_iter = dummy_head = ListNode()
    carry = 0
    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        place_iter.next = ListNode(val % 10)
        carry, place_iter = val // 10, place_iter.next
    return dummy_head.next


def main():
    start_time = time.time()

    #test case
    print_list(add_two_numbers(L1, L2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()