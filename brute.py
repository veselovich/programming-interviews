import time
from memory_profiler import profile


@profile
def func_name(x):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    #TODO
    raise NotImplemented


def main():
    start_time = time.time()

    #test case
    #TODO

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()