import time
from memory_profiler import profile


@profile
def search_entry_equal_to_its_index(A):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        # A[mid] == mid if and only if difference == 0.
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else: # difference ‹ 0.
            left = mid + 1
    return -1


def main():
    start_time = time.time()

    #test case
    print(search_entry_equal_to_its_index([-2,0,2,4,6,7,9]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()