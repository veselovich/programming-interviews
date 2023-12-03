import time
from memory_profiler import profile
from random_sampling import random_sampling


@profile
def compute_random_permutation(n):
    """
    Generates a randon permutation
    
    :type n: int
    :rtype: list
    """
    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation


def main():
    start_time = time.time()

    #test case
    print(compute_random_permutation(6))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()