import time
from memory_profiler import profile


@profile
def longest_contained_range(A):
    # unprocessed entries records the existence of each entry in A.
    unprocessed_entries = set(A)

    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        # Finds the lower bound of the largest range containing a.
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        # Finds the upper bound of the largest range containing a.
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1
        
        max_interval_size = max(max_interval_size,
                                upper_bound - lower_bound - 1)
    return max_interval_size


def main():
    start_time = time.time()

    #test case
    print(longest_contained_range([3,-2,7,9,8,1,2,0,-1,5,8]))
    print(longest_contained_range([10,5,3,11,6,100,4]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()