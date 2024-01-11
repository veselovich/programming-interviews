import time
from memory_profiler import profile
from nodes import *


@profile
def cyclically_right_shift_list(L, k):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    if not L:
        return L
    
    # Computes the length of L and the tail.
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    k %= n
    if k == 0:
        return L
    
    tail.next = L # Makes a cycle by connecting the tail to the head.
    steps_to_new_head, new_tail = n - k, tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head


def main():
    start_time = time.time()

    #test case
    print_list(cyclically_right_shift_list(L1, 2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()