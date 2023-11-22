import time
from memory_profiler import profile


@profile
def rearrange(A):
    """
    Rearrange array so values are alternate: one is more than next and next is vice versa
    Example: A[1] <= A[2] >= A[3] <= A[4] ...
    
    :type A: list
    :rtype: None
    """
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i % 2)


def main():
    start_time = time.time()

    #test case
    A = [234,32,13,342,456,32,564,45]
    rearrange(A)
    print(A)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()