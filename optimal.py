import time
import random
from memory_profiler import profile


@profile
def random_subset(n, k):
    """
    Compute a random subset given length
    Example: n = 4, k = 2
    [0,1,2,3] -> [1,2]

    :type n, k: int
    :rtype: list
    """
    changed_elements = {}
    for i in range(k):
        # Generate a random index between i and n - 1, inclusive.
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]


def main():
    start_time = time.time()

    #test case
    n = 6
    k = 2
    print(random_subset(n, k))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()