import time
from memory_profiler import profile

from random import randint as zero_one_random

@profile
def uniform_random(lower_bound, upper_bound):
    """
    Generate random number within bounds
    1, 10 -> 7
    
    :type lower_bound, upper_bound: int
    :rtype: int
    """
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            # zero_one_random () is the provided random number generator.
            result = (result << 1) | zero_one_random(0, 1)
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


def main():
    start_time = time.time()

    #test case
    print(uniform_random(1, 10))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()