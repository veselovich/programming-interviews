import time
from memory_profiler import profile


@profile
def generate_pascal_triangle(n) :
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    result = [[1] *(i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            # Sets this entry to the sum of the two above adjacent entries.
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result


def main():
    start_time = time.time()

    #test case
    print(generate_pascal_triangle(4))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()