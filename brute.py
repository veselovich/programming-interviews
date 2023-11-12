import time
from memory_profiler import profile


@profile
def plus_one(A):
    """
    Having list of digits, representing a number: increment it on 1 and return list
    Example: [1,2,3] -> [1,2,4]
    
    :type A: list
    :rtype: list
    """
    return list(map(int, str(int("".join(map(str, A))) + 1)))


def main():
    start_time = time.time()

    #test case
    A = [1,2,3]
    print(plus_one(A))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()