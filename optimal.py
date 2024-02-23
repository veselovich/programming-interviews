import time
from memory_profiler import profile


@profile
def square_root(k):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    left, right = 0, k
    # Candidate interval [left, right] where everything before left has square
    # <= k, everything after right has square > k.
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


def main():
    start_time = time.time()

    #test case
    print(square_root(1000))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()