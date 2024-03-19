import time
from memory_profiler import profile

from nodes import *


@profile
def insertion_sort(L):
    dummy_head = ListNode(0, L)
    # The sublist consisting of nodes up to and including iter is sorted in
    # increasing order. We need to ensure that after we move to L.next this
    # property continues to hold. We do this by swapping L.next with its
    # predecessors in the list till it's in the right place.
    while L and L.next:
        if L.data > L.next.data:
            target, pre = L.next, dummy_head
            while pre.next.data < target.data:
                pre = pre.next
            temp, pre.next, L.next = pre.next, target, target.next
            target.next = temp
        else:
            L = L.next
    return dummy_head.next


def main():
    start_time = time.time()

    #test case
    print_list(insertion_sort(L1))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()