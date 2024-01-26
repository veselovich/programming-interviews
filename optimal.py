import collections
import time
from memory_profiler import profile


@profile
def examine_buildings_with_sunset(sequence):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    BuildingWithHeight = collections.namedtuple('BuildingWithHeight',
                                                ('id', 'height'))
    candidates = []
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [candidate.id for candidate in reversed(candidates)]


def main():
    start_time = time.time()

    #test case
    s = [150, 100, 50, 10, 120]
    print(examine_buildings_with_sunset(s))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()