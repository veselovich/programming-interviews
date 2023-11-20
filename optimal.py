import time
from memory_profiler import profile


@profile
def delete_duplicates(A) :
    """
    Delete all duplicates from sorted array in place
    Example: [2,3,5,5,7,11,11,11,13] -> [2,3,5,7,11,13,any,any,any]
    
    :type A: list
    :rtype: int
    """
    if not A:
        return 0
    write_index = 1
    for i in range (1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


def main():
    start_time = time.time()
    
    #test case
    A = [2,3,5,5,7,11,11,11,13]
    print(delete_duplicates(A))
    print(A)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()