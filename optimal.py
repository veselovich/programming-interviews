import time
from memory_profiler import profile


@profile
def search_smallest(A):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            # Minimum must be in A[mid + 1: right + 1].
            left = mid + 1
        else: # A[mid] < A[right].
            # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid + 1].
            right = mid
    # Loop ends when left == right.
    return left


def main():
    start_time = time.time()

    #test case
    print(search_smallest([378,478,550,631,103,203,220,234,279,368]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()