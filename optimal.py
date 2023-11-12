import time
from memory_profiler import profile


@profile
def plus_one(A):
    """
    Having list of digits, representing a number: increment it on 1 and return list
    Example: [1,2,9] -> [1,3,0]
    
    :type A: list
    :rtype: list
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # There is a carry-out, so we need one more digit to store the result.
        # A slick way to do this is to append a 0 at the end of the array,
        # and update the first entry to 1.
        A[0] = 1
        A.append(0)
    return A


def main():
    start_time = time.time()

    #test case
    A = [9,9,9]
    print(plus_one(A))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()