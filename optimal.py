import time
from memory_profiler import profile

from summation import add


@profile
def multiply(x, y):
    """
    Compute multiplication without operator (only bitwise operators)
    
    :type x: int
    :rtype: int
    """
    running_sum = 0
    while x: # Examines each bit of x.
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum


def main():
    start_time = time.time()

    #test case
    print(multiply(13, 9))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()