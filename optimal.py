import time
from memory_profiler import profile


@profile
def intersect_two_sorted_arrays(A, B):
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i]< B[j]:
            i += 1
        else: # A[i] > BIjl.
            i += 1
    return intersection_A_B


def main():
    start_time = time.time()

    #test case
    print(intersect_two_sorted_arrays([2,3,3,5,7,11], [3,3,7,15,31]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()