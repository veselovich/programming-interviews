import time
from memory_profiler import profile


@profile
def can_reach_end(A):
    """
    Go through array. Each value in aggary is possible range to move forward
    
    :type A: list
    :rtype: int
    """
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index


def main():
    start_time = time.time()

    #test case
    A = [3,3,1,0,2,0,1]
    print(can_reach_end(A))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()