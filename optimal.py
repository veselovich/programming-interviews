import time
from memory_profiler import profile

from nodes import *


@profile
def has_cycle(head):
    """
    Test if there is cyclicity in a linked list
   
    :type head: ListNode
    :rtype: ListNode[None]
    """
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
        
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # Finds the start of the cycle.
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # Both iterators advance in tandem.
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it # iter is the start of cycle.
    return None # No cycle.


def main():
    start_time = time.time()

    #test case
    print(has_cycle(L1))
    print(has_cycle(L2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()