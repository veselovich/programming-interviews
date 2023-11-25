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
    def cyclic_permutation(start, perm, A):
        i, temp = start, A[start]
        while True:
            next_i = perm[i]
            next_temp = A[next_i]
            A[next_i] = temp
            i, temp = next_i, next_temp
            if i == start:
                break

    for i in range(len(A)):
        # Traverses the cycle to see if i is the minimum element.
        j = perm[i]
        while j != i:
            if j < i:
                break
            j = perm[j]
        else:
            cyclic_permutation(i, perm, A)

def main():
    start_time = time.time()

    #test case
    P = [2,3,0,1,5,4]
    a = ['a', 'b', 'c', 'd', 'e', 'f']
    apply_permutation(P, a)
    print(a)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()