import time
from memory_profiler import profile


@profile
def apply_permutation(perm, A):
    """
    Perform permutation of list A according to permutation array
    
    :type perm: list
    :type A: list
    :rtype: None
    """
    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtracts len (perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp
    # Restore perm.
    perm[:] = [a + len(perm) for a in perm]

def main():
    start_time = time.time()

    #test case
    P = [3,4,1,2,0,5]
    a = ['a', 'b', 'c', 'd', 'e', 'f']
    apply_permutation(P, a)
    print(a)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()