import heapq
import itertools
import time
from memory_profiler import profile


@profile
def sort_k_increasing_decreasing_array(A):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    # Decomposes A into a set of sorted arrays.
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or # A is ended. Adds the last subarray.
            (A[i - 1] < A[i] and subarray_type == DECREASING) or
            (A[i - 1] >= A[i] and subarray_type == INCREASING)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type ==
                                    INCREASING else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = (DECREASING
                            if subarray_type == INCREASING else INCREASING)
    return merge_sorted_arrays(sorted_subarrays)

# Pythonic solution, uses a stateful object to trace the monotonic subarrays.
def sort_k_increasing_decreasing_array_pythonic(A):
    class Monotonic:
        def __init__(self):
            self._last = float('-inf')
            
        def __call__(self, curr):
            res = curr < self._last
            self._last = curr
            return res
        
    return merge_sorted_arrays([
        list(group)[:: -1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(A, Monotonic())
        ])

def merge_sorted_arrays(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


def main():
    start_time = time.time()

    #test case
    print(sort_k_increasing_decreasing_array([57,131,493,294,221,339,418,452,442,190]))
    print(sort_k_increasing_decreasing_array_pythonic([57,131,493,294,221,339,418,452,442,190]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()