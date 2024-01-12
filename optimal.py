import time
from memory_profiler import profile

from nodes import *


@profile
def is_linked_list_a_palindrome(L):
    """
    Check if linked list is palindrome
    
    :type L: ListNode
    :rtype: bool
    """
    # Finds the second half of L.
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    # Compares the first half and the reversed second half lists.
    first_half_iter, second_half_iter = L, reverse_linked_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = (second_half_iter.next,
                                             first_half_iter.next)
    return True


def main():
    start_time = time.time()

    #test case
    print(is_linked_list_a_palindrome(L1))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()