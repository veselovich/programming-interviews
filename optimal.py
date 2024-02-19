import heapq
import itertools
import time
from memory_profiler import profile


@profile
def sort_approximately_sorted_array(sequence, k):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    result = []
    min_heap = []
    # Adds the first k elements into min_heap. Stop if there are fewer than k
    # elements.
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    # For every new element, add it to min_heap and extract the smallest.
    for x in sequence[k:]:  # [k:]?
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # sequence is exhausted, iteratively extracts the remaining elements.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
    return result


def main():
    start_time = time.time()

    #test case
    print(sort_approximately_sorted_array([6, 5, 3, 2, 8, 10, 9], 3))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()