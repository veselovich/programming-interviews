import time
from memory_profiler import profile


@profile
def power(x, y):
    """
    Calculating x power y
    2 , 3 -> 8
    
    :type x, y: int
    :rtype: int
    """
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


def main():
    start_time = time.time()

    #test case
    print(power(2, 3))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()