import time
from memory_profiler import profile


@profile
def closest_int_same_bit_count(x):
    """
    Find a closest integer with the same weight
    [1,1,0] -> [1,0,1] (weight: 1+1=2)
    6 -> 5

    :type x: unsigned int
    :rtype: int
    """
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1)) # Swaps bit-i and bit-(i + 1).
            return x
    # Raise error if all bits of x are 0 or 1.
    raise ValueError ('All bits are 0 or 1')


def main():
    start_time = time.time()

    #test case
    print(closest_int_same_bit_count(47))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()