import time
from memory_profiler import profile


@profile
def dutch_flag_partition(pivot_index, A):
    """
    Sort array in two parts: before pivot and after
    Example: 0, [2,1,3] -> [1,2,3]
    
    :type pivot_index: int
    :type A: list
    """
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[: smaller].
    # middle group: A[smaller: equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.,
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot.
            larger -= 1
            A [equal], A[larger] = A[larger], A[equal]


def main():
    start_time = time.time()

    #test case
    A = [3, 6, 8, 10, 1, 2, 1]
    dutch_flag_partition(0, A)
    print(A)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()