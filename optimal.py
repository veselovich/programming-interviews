import collections
import time
from memory_profiler import profile

Interval = collections.namedtuple('Interval', ('left', 'right'))

@profile
def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    # Processes intervals in disjoint_ intervals which come before new_ interval.
    while (i < len(disjoint_intervals)
           and new_interval.left > disjoint_intervals[i].right):
        result.append(disjoint_intervals[i])
        i += 1

    # Processes intervals in disjoint_ intervals which overlap with new_ interval.
    while (i < len(disjoint_intervals)
           and new_interval.right >= disjoint_intervals[i].left):
        # If [a, b] and [c, d] overlap, union is [min(a, c), max (b, d)].
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right))
        i += 1
    # Processes intervals in disjoint_ intervals which come after new interval.
    return result + [new_interval] + disjoint_intervals[i:]


def main():
    start_time = time.time()

    #test case
    disjoint_intervals = [Interval(-4,-1),Interval(0,2),Interval(3,6),Interval(7,9),Interval(11,12),Interval(14,17)]
    print(add_interval(disjoint_intervals, Interval(1,8)))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()