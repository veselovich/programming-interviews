import operator
import random
import time
from memory_profiler import profile


@profile
# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_ largest (1, A) returns 3, find_kth_largest (2, A) returns 2,
# find_ kth_largest (3, A) returns 1, and find_kth_largest (4, A) returns -1.
def find_kth_largest(k, A):
    def find_kth(comp):
    # Partition A[left: right + 1] around pivot_idx, returns the new index of
    # the pivot, new_pivot_id, after partition. After partitioning,
    # A[left: new_pivot_idx] contains elements that are greater than the
    # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
    # less than the pivot.
    #
    # Note: "less than" is defined by the comp object.
    # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx
        left, right = 0, len (A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else: # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1
    return find_kth(operator.gt)


def main():
    start_time = time.time()

    #test case
    print(find_kth_largest(3, [3,2,1,5,4,6,8,7,10,9]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()