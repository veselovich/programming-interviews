import time
from memory_profiler import profile


@profile
def search_first_of_k(A, k):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    left, right, result = 0, len(A) - 1, -1
    # A[left:right + 1] is the candidate set.
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1 # Nothing to the right of mid can be solution.
        else: # A[mid] < k.
            left = mid + 1
    return result


def main():
    start_time = time.time()

    #test case
    print(search_first_of_k([-14,-10,2,108,108,243,285,285,285,401], 108))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()