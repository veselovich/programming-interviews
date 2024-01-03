import time
from memory_profiler import profile

from nodes import *


@profile
def overlapping_lists(L1, L2):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    # Store the start of cycle if any.
    root1, root2 = has_cycle(L1), has_cycle(L2)

    if not root1 and not root2:
        # Both lists don't have cycles.
        return overlapping_no_cycle_lists(L1, L2)
    elif (root1 and not root2) or (not root1 and root2):
        # One list has cycle, one list has no cycle.
        return None
    # Both lists have cycles.
    temp = root2
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break

    # L1 and L2 do not end in the same cycle.
    if temp is not root1:
        return None # Cycles are disjoint.
    
    # Calculates the distance between a and b.
    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis
    
    # L1 and L2 end in the same cycle, locate the overlapping node if they
    # first overlap before cycle starts.
    stem1_length, stem2_length = distance(L1, root1), distance(L2, root2)
    if stem1_length > stem2_length:
        L2, L1 = L1, L2
        root1, root2 = root2, root1
    for _ in range(abs(stem1_length - stem2_length)) :
        L2 = L2.next
    while L1 is not L2 and L1 is not root1 and L2 is not root2:
        L1, L2 = L1.next, L2.next

    # If L1 = L2 before reaching root1, it means the overlap first occurs
    # before the cycle starts; otherwise, the first overlapping node is not
    # unique, we can return any node on the cycle.
    return L1 if L1 is L2 else root1


def main():
    start_time = time.time()

    #test case
    print(overlapping_lists(L1, L2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()