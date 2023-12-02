import time
import random
import itertools
from memory_profiler import profile


@profile
def online_random_sample(it, k):
    """
    Function is performing reservoir sampling,
    a technique used to obtain a random sample of k items from a stream of unknown or very large size,
    without knowing the total number of elements in advance.
    
    :type it: list
    :type k: int
    :rtype: list
    """
    # Assumption: there are at least k elements in the stream.
    
    # Stores the first k elements.
    sampling_results = list(itertools.islice(it, k))
    
    # Have read the first k elements.
    num_seen_so_far = k
    for x in it:
        num_seen_so_far += 1
        # Generate a random number in [0, num_seen_so_far - 1], and if this
        # number is in [O, k - 1], we replace that element from the sample with
        # x.
        id_to_replace = random.randrange(num_seen_so_far)
        if id_to_replace < k:
            sampling_results[id_to_replace] = x
    return sampling_results


def main():
    start_time = time.time()

    #test case
    k = 5
    stream_of_data = range(1000)
    print(online_random_sample(stream_of_data, k))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()