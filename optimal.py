import math
import time


def square_root(x):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    # Decides the search range according to x's value relative to 1.0.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    # Keeps searching as long as left != right.
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid
    return left


def main():
    start_time = time.time()

    #test case
    print(square_root(-1.15))
    print(square_root(-0.15))
    print(square_root(0))
    print(square_root(0.25))
    print(square_root(2.8))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()