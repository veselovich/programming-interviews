import time
from memory_profiler import profile

import optimal1 # library for precomputing

# populating list
PRECOMPUTED_PARITY = [] 
for i in range(2**16):  # Assuming 16 bits in example
    PRECOMPUTED_PARITY.append(optimal1.parity(i))

@profile
def parity(x):
    """
    Computing parity of a binary word
    7 in binary is 111 -> 1+1+1 = 3 -> 3 is odd
    10 in binary is 1010 -> 1+0+1+0 = 2 -> 2 is even
    
    :type x: int
    :rtype: int
    """

    MASK_SIZE = 16
    BIT_MASK = 0xFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])


def main():
    start_time = time.time()

    #test case
    x = 7
    print(parity(x))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()