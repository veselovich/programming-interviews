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
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2] # Stores the primes from 1 to n.
    # is_prime[i] represents (2i + 3) is prime or not.
    # Initially set each to true. Then use sieving to eliminate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # Sieving from p^2, where p^2 = (4i^2 + 12i + 9). The index in is_prime
            # is (2i^2 + 6i + 3) because is_prime[i] represents 2i + 3.
            #
            # Note that we need to use long for j because p^2 might overflow.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes


def main():
    start_time = time.time()

    #test case
    print(generate_primes(18))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()