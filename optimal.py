import time
from memory_profiler import profile


@profile
def generate_primes (n):
    """
    Given n, return all primes up to and including n.
    Example: n=18 -> [2, 3, 5, 7, 11, 13, 17]
    
    :type n: int
    :rtype: list
    """
    primes = []
    # is_prime [p] represents if p is prime or not. Initially, set each to
    # true, expecting 0 and 1. Then use sieving to eliminate nonprimes.

    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            # Sieve p's multiples.
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes


def main():
    start_time = time.time()

    #test case
    print(generate_primes(18))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()