import time
import itertools, random, bisect
from memory_profiler import profile


@profile
def nonuniform_random_number_generation(values, probabilities):
    """
    Generate number with given probability
    
    :type values: list 
    :type probabilities: list 
    :rtype: int
    """
    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    # accumulate() is cumulative sum:
    # Each element in the result is the sum of all the elements encountered so far in the original list
    # e.g.[1,2,3] -> [1, 1+2, 1+2+3] or just [1,3,6]
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
    return values[interval_idx]


def main():
    start_time = time.time()

    #test case
    values = [3,5,7,11]
    probabilities = [9/18, 6/18, 2/18, 1/18]
    print(nonuniform_random_number_generation(values, probabilities))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()