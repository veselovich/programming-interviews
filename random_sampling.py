import time
from memory_profiler import profile
import random


@profile
def random_sampling (k, A):
    """
    Sample
    Example
    
    :type x: int
    :rtype: int
    """
    for i in range(k):
    # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]


def main():
    start_time = time.time()

    #test case
    k = 3
    A = [3,7,5,11]
    random_sampling(k, A)
    print(A[:k])

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()