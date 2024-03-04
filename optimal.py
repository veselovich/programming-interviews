import collections
import time
from memory_profiler import profile

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

@profile
def find_smallest_subarray_covering_set(paragraph, keywords):
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1
        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover [pl] += 1
                if keywords_to_cover [pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result


def main():
    start_time = time.time()

    #test case
    print(find_smallest_subarray_covering_set(['apple','banana','apple','apple','dog','cat','apple','dog','banana','apple','cat','dog'], {'banana','cat'}))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()