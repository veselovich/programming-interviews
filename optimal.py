import time
from memory_profiler import profile


@profile
def merge_two_sorted_arrays(A, m, B, n):
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1


def main():
    start_time = time.time()

    #test case
    A = [5,13,17,None,None,None,None,None]
    merge_two_sorted_arrays(A, 3, [3,7,11,19], 4)
    print(A)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()