import time
from memory_profiler import profile


def parity(x):
    """
    Computing parity of a binary word
    7 in binary is 111 -> 1+1+1 = 3 -> 3 is odd
    10 in binary is 1010 -> 1+0+1+0 = 2 -> 2 is even
    
    :type x: int
    :rtype: int
    """

    result = 0 
    while x:
        result ^= 1 # switches each iteration between 0 and 1
        x &= x - 1 # drops lowes bit
    return result


def main():
    start_time = time.time()

    #test case
    x = 7
    print(parity(x))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()