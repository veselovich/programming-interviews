import time
from memory_profiler import profile

from brute import PRECOMPUTED_REVERSE


@profile
def reverse_bits(x):
    """
    Reverse 64-bit word
    Example on 4-bit word:
    [1,0,1,1] -> [1,1,0,1]
    11 -> 13

    :type x: int
    :rtype: int
    """
    MASK_SIZE = 16
    BIT_MASK = 0xFFF
    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE) |
            PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) |
            PRECOMPUTED_REVERSE[(x >> (2  * MASK_SIZE)) & BIT_MASK] << MASK_SIZE |
            PRECOMPUTED_REVERSE[(x >> (3  * MASK_SIZE)) & BIT_MASK])


def main():
    start_time = time.time()

    #test case
    print(reverse_bits(11))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()