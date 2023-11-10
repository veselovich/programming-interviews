import time
from memory_profiler import profile


@profile
def divide (x, y) :
    """
    Given two positive integers, compute quotient without using dividing operator
    10 / 3 = 3
    
    :type x, y: int
    :rtype: int
    """
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        result += 1 << power
        x -= y_power
    return result


def main():
    start_time = time.time()

    #test case
    print(divide(10, 3))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()