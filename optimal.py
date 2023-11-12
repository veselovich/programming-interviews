import time
from memory_profiler import profile


@profile
def even_odd(A):
    """
    Sorts array: even first, than odds
    Example: [1,2,3,4,5,6] -> [6,2,4,5,3,1]
    
    :type A: list
    :rtype: list
    """
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


def main():
    start_time = time.time()

    #test case
    A = [1,2,3,4,5,6]
    even_odd(A)
    print(A)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()