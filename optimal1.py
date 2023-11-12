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
    # First pass: group elements smaller than pivot.
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    # Second pass: group elements larger than pivot.
    larger = len (A) - 1
    for i in reversed(range(len(A))) :
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


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