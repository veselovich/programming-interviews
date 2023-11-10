import time
from memory_profiler import profile

import math

@profile
def is_palindrome_number(x):
    """
    Check if palindrome
    2147447412 -> True, 123322 - False
    
    :type x: int
    :rtype: int
    """
    if x <= 0:
        return x == 0
    
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)
    for i in range (num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask # Remove the most significant digit of x.
        x //= 10 # Remove the least significant digit of x.
        msd_mask //= 100
    return True


def main():
    start_time = time.time()

    #test case
    print(is_palindrome_number(2147447412))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()