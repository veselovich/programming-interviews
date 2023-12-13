import functools
import time
from memory_profiler import profile


@profile
def ss_decode_col_id(col):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)


def main():
    start_time = time.time()

    #test case
    print(ss_decode_col_id('AB'))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()