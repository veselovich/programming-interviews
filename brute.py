import time
from memory_profiler import profile


@profile
def swap_bits(x,i,j):
    """
    Swap bits it binary word
    Given indecies i,j = 1, 2
    [1,1,0,0] -> [1,0,1,0]
    12 -> 10
    
    :type x,i,j: int 
    :rtype: int
    """
    # extract i and j
    if (x >> i) & 1 != (x >> j) & 1:
        # create bit mask 
        bit_mask = (1 << i) | (1 << j)
        # flip with XOR
        x ^= bit_mask
    return x       


def main():
    start_time = time.time()

    #test case
    print(swap_bits(12, 1, 2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()