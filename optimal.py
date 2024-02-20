import heapq
import time
from memory_profiler import profile


@profile
def online_median(sequence):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    # min_heap stores the larger half seen so far.
    min_heap = []
    # max_heap stores the smaller half seen so far.
    # values in max_heap are negative
    max_heap = []
    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        # Ensure min_heap and max_heap have equal number of elements if an even
        # number of elements is read; otherwise, min_heap must have one more
        # element than max_heap.
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0]))
                      if len(min_heap) == len(max_heap) else min_heap[0])
    return result


def main():
    start_time = time.time()

    #test case
    print(online_median([1,0,3,5,2,0,1]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()