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
    for i in range(len(A)) :
        # Look for a smaller element.
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(A))) :
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


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