import collections
import time


Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left.val != other.left.val:
            return self.left.val < other.left.val
        # Left endpoints are equal, so now see if one is closed and the other open
        # - closed intervals should appear first.
        return self.left.is_closed and not other.left.is_closed
    
    def __repr__(self) -> str:
        return f'Left {self.left} - Right {self.right}'
    

def union_of_intervals(intervals):
    # Empty input.
    if not intervals:
        return []
    
    # Sort intervals according to left endpoints of intervals.
    intervals.sort()
    result = [intervals[0]]
    for i in intervals:
        if intervals and (i.left.val < result[-1].right.val or
                          (i.left.val == result[-1].right.val and
                           (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or
                (i.right.val == result[-1].right.val and i.right.is_closed)):
                result[-1].right = i.right
        else:
            result.append(i)
    return result

def main():
    start_time = time.time()

    #test case
    intervals = [
        Interval(Endpoint(False, 0), Endpoint(False, 3)),
        Interval(Endpoint(True, 1), Endpoint(True, 1)),
        Interval(Endpoint(True, 2), Endpoint(True, 4)),
        Interval(Endpoint(True, 3), Endpoint(False, 4)),
        Interval(Endpoint(True, 5), Endpoint(False, 7)),
        Interval(Endpoint(True, 7), Endpoint(False, 8)),
        Interval(Endpoint(True, 8), Endpoint(False, 11)),
        Interval(Endpoint(False, 9), Endpoint(True, 11)),
        Interval(Endpoint(True, 5), Endpoint(False, 7)),
        Interval(Endpoint(True, 12), Endpoint(True, 14)),
        Interval(Endpoint(False, 12), Endpoint(True, 16)),
        Interval(Endpoint(False, 13), Endpoint(False, 15)),
        Interval(Endpoint(True, 5), Endpoint(False, 7)),
        Interval(Endpoint(False, 16), Endpoint(False, 17)),
    ]

    for i in union_of_intervals(intervals):
        print(i)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()