import time
from memory_profiler import profile
from nodes import *


@profile
def remove_kth_last(L, k):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    # Assumes L has at least k nodes, deletes the k-th last node in L.
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next
    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return dummy_head.next


def main():
    start_time = time.time()

    #test case
    remove_kth_last(L1, 2)
    print_list(L1)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()