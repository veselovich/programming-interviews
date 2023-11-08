import time
from memory_profiler import profile


@profile
def parity(x):
    """
    Computing parity of a binary word
    7 in binary is 111 -> 1+1+1 = 3 -> 3 is odd
    10 in binary is 1010 -> 1+0+1+0 = 2 -> 2 is even
    
    :type x: int
    :rtype: int
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


def main():
    start_time = time.time()

    #test case
    x = 65535
    print(parity(x))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()