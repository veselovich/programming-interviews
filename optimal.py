import time
from memory_profiler import profile


@profile
def reverse(x):
    """
    Reverese input without converting it to the string
    123 -> 321
    
    :type x: int
    :rtype: int
    """
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


def main():
    start_time = time.time()

    #test case
    print(reverse(123))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()