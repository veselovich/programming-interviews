import time
from memory_profiler import profile


@profile
def find_nearest_repetition(paragraph):
    word_to_latest_index, nearest_repeated_distance = {}, float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance,
                                            i - latest_equal_word)
        word_to_latest_index[word] = i
    return nearest_repeated_distance if nearest_repeated_distance != float(
        'inf') else -1


def main():
    start_time = time.time()

    #test case
    print(find_nearest_repetition("All work and no play makes for no work no fun and no results".split()))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()