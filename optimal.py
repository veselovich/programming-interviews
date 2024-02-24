import collections
import time
from memory_profiler import profile


MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))

@profile
def find_min_max(A):
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)
    
    if len(A) <= 1:
        return MinMax(A[0], A[0])

    global_min_max = min_max(A[0], A[1])
    # Process two elements at a time.
    for i in range(2, len(A) - 1, 2):
        local_min_max = min_max(A[i], A[i + 1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest))
    # If there is odd number of elements in the array, we still need to
    # compare the last element with the existing answer.
    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1]))
    return global_min_max


def main():
    start_time = time.time()

    #test case
    print(find_min_max([3,2,5,1,2,4]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()