import heapq
import time
from memory_profiler import profile


@profile
def k_largest_in_binary_heap(A, k):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    if k <= 0:
        return []
    # Stores the (-value, index)-pair in candidate_ max_ heap. This heap is
    # ordered by value field. Uses the negative of value to get the effect of
    # a max heap.
    candidate_max_heap = []
    # The largest element in A is at index 0.
    candidate_max_heap.append((-A[0], 0))
    result= []
    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])
        
        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child_idx],
                                                left_child_idx))
            
        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child_idx],
                                                right_child_idx))
    return result


def main():
    start_time = time.time()

    #test case
    print(k_largest_in_binary_heap([561,314,401,28,156,359,271,11,3], 4))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()