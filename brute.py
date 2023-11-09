import time
from memory_profiler import profile

PRECOMPUTED_REVERSE = []
bits = 16

def reverse_n_bit_word(x, n=16):
    """
    Reverse 16-bit word
    Example on 4-bit word:
    [1,0,1,1] -> [1,1,0,1]
    11 -> 13

    :type x: int
    :rtype: int
    """
    reversed_value = 0
    for i in range(n):
        if (x >> i) & 1:  # Check if the i-th bit is set in x
            reversed_value |= 1 << (n - 1 - i)  # Set the bit from the opposite site
    return reversed_value


for i in range(2 ** bits):
    PRECOMPUTED_REVERSE.append(reverse_n_bit_word(i, n=bits))


def main():
    start_time = time.time()

    #test case
    print(reverse_n_bit_word(11, n=bits))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()