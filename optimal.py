import time
from memory_profiler import profile
from nodes import *


@profile
def even_odd_merge(L):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    if not L:
        return L
    
    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1 # Alternate between even and odd.
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next


def main():
    start_time = time.time()

    #test case
    print_list(even_odd_merge(L1))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()