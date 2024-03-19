import time

from nodes import *


def stable_sort_list(L):
    # Base cases: L is empty or a single node, nothing to do.
    if not L or not L.next:
        return L

    # Find the midpoint of L using a slow and a fast pointer.
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next
    pre_slow.next = None # Splits the list into two equal-sized lists.
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


def main():
    start_time = time.time()

    #test case
    print_list(stable_sort_list(L1))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()