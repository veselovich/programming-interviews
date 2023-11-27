import time
from memory_profiler import profile


@profile
def next_permutation(perm):
    """
    Compute next permutation according to odometer-style increase
    Example: [0,1,2,3] -> [0,1,3,2]
    
    :type perm: list
    :rtype: list
    """
    # Find the first entry from the right that is smaller than the entry
    # immediately after it.
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return [] # perm is the last permutation.

    # Swap the smallest entry after index inversion point that is greater tha
    # perminversion point]. Since entries in perm are decreasing after
    # inversion point, if we search in reverse order, the first entry that is
    # greater than perm[inversion point] is the entry to swap with.
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break
    # Entries in perm must appear in decreasing order after inversion point,
    # so we simply reverse these entries to get the smallest dictionary order.
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


def main():
    start_time = time.time()

    #test case
    perm = [6,2,1,5,4,3,0]
    print(next_permutation(perm))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()